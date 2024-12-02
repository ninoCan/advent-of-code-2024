include .env

YEAR := $(shell date +'%Y')
DAY := $(shell date +'%d' | sed 's/^0//')
FOLDER_PATH := src/day$(DAY)
TEST_FOLDER := tests/day$(DAY)
AOC_SESSION_COOKIE := $(<.session-cookie) 
URL_FOR_TODAY :=  "https://adventofcode.com/$(YEAR)/day/$(DAY)"
BRANCH_NAME := day$(DAY)-challenge1
DEFAULT_STEM := README

.PHONY: create-folder fetch-page generate-pyfiles convert-to-markdown commit-prompt

all: convert-to-markdown generate-pyfiles fetch-input commit-prompt

ifndef AOC_SESSION_COOKIE
	echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	echo Please store the session cookie into a AOC_SESSION_COOKIE
	echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	echo
endif

create-folder:
	mkdir -p $(FOLDER_PATH)
	mkdir -p $(TEST_FOLDER)
	touch $(FOLDER_PATH)/__init__.py $(TEST_FOLDER)/__init__.py
	@echo "Created folder: $(FOLDER_PATH)"

fetch-page: create-folder
	curl -o "$(FOLDER_PATH)/day$(DAY).html" "$(URL_FOR_TODAY)" -c .env
	@echo "Fetched page for day $(DAY) to $(FOLDER_PATH)"

convert-to-markdown: fetch-page
	pandoc -f html -t gfm -s "$(FOLDER_PATH)/day$(DAY).html" | \
		sed -n '/^##/,/\?\*$$/p' | \
		sed 's/^##/#/' \
		> $(FOLDER_PATH)/$(DEFAULT_STEM).md
	rm "$(FOLDER_PATH)/day$(DAY).html" 
	@echo "Saved fetched prompt page to $(FOLDER_PATH)/$(DEFAULT_STEM).md"

fetch-input: create-folder
	curl --cookie "session=${AOC_SESSION_COOKIE}" -o "$(FOLDER_PATH)/input.txt" "$(URL_FOR_TODAY)/input"
	@echo "Fetched input file for day $(DAY) to $(FOLDER_PATH)"

touch-files:
	touch $(FOLDER_PATH)/main.py

generate-pyfiles: convert-to-markdown touch-files
	uv run python templates/generator.py
	    @echo "Created skeletons of main and tests from templates"

commit-prompt:
	git switch -c $(BRANCH_NAME)
	git add $(FOLDER_PATH) $(TEST_FOLDER)
	git commit -m "chore: Add prompt for day $(DAY)"
	git push -u origin $(BRANCH_NAME)
