import datetime
import pandas
import argparse

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from collections import defaultdict

from decouple import config


FOUNDATION = 1920
NUMBERS_EXCLUSION = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
EXCLUSION_ZERO = 0
EXCLUSION_ONE = 1
EXCLUSION_FOUR = 4


def calculation_date(FOUNDATION):
    our_age = datetime.datetime.now().year - FOUNDATION
    return str(our_age)


def declension_dates(date):
    slice_one = int(date[-1:])
    slice_two = int(date[-2:])

    if (slice_one == EXCLUSION_ZERO or
            slice_one > EXCLUSION_FOUR or
            slice_two in NUMBERS_EXCLUSION):
        return "лет"
    elif slice_one == EXCLUSION_ONE:
        return "год"
    else:
        return "года"


def reading_wine_file(xlsx):
    excel_data_df = pandas.read_excel(xlsx,
                                      na_values=['N/A', 'NA'],
                                      keep_default_na=False)
    data = excel_data_df.to_dict(orient='records')

    categories_wines = defaultdict(list)
    for x in sorted(data, key=lambda x: x['Категория']):
        categories_wines[x['Категория']].append(x)

    return categories_wines


def main():
    parser = argparse.ArgumentParser(description='Demo-сайт Винный Магазин')
    parser.add_argument('--your_path',
                        default=config('FILE_PATH'),
                        help='Формат ввода --your_path my_path/MY_FILE.xlsx')
    args = parser.parse_args()

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    found_date = calculation_date(FOUNDATION)
    rendered_page = template.render(
        our_age=found_date,
        declin_dates=declension_dates(found_date),
        wines_file=reading_wine_file(args.your_path),
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
