import datetime

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


FOUNDATION = 1920
NUMBERS_EXCLUSION = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
EXCLUSION_ZERO = 0
EXCLUSION_ONE = 1
EXCLUSION_FOUR = 4


def data_foudation(FOUNDATION):
    our_age = datetime.datetime.now().year - FOUNDATION
    return str(our_age)


def declination_dates(date):
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


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(
    our_age=data_foudation(FOUNDATION),
    declin_dates=declination_dates(data_foudation(FOUNDATION)),
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
