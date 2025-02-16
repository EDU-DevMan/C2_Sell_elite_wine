import datetime

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


DATE_FOUNDATION = 2015

our_age = datetime.datetime.now().year - DATE_FOUNDATION


def declination_dates(foundation):
    if foundation[-1:] == str(1):
        return "год"
    elif foundation[-1:] == str(0) or foundation[-1:] > str(4):
        return "лет"
    else:
        return "года"


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(
    our_age=our_age,
    declin_dates=declination_dates(str(our_age)),
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
