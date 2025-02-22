import datetime

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


FOUNDATION = 1904


def data_foudation(FOUNDATION):
    our_age = datetime.datetime.now().year - FOUNDATION
    return str(our_age)


def declination_dates(date):
    slice_one = int(date[-1:])
    slice_two = int(date[-2:])
    numbers_exclusion = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    if slice_one == 0 or slice_one > 4 or slice_two in numbers_exclusion:
        return "лет"
    elif slice_one == 1:
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
