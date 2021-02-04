from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

FlaskBP = Blueprint("FlaskBP", __name__,
                    template_folder='templates')

@FlaskBP.route("/home")
def helloNow():
    return "<h1>Hello</h1>"