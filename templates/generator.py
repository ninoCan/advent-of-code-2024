import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def main() -> None:
    environment = Environment(loader=FileSystemLoader("templates"))
    params = {
        "year": datetime.datetime.now().year,
        "day": datetime.date.today().day,
    }

    main_path = (
        f"""src/day{params["day"]}/main.py"""
    )
    test_path = f"""tests/day{params["day"]}/test_main.py"""

    for file in Path(__file__).parent.glob('*.jinja'):
        template = environment.get_template(file.name)
        dest = test_path if "test" in file.name else main_path

        with open(dest, "w") as destination:
            destination.write(template.render(**params))


if __name__ == "__main__":
    main()
