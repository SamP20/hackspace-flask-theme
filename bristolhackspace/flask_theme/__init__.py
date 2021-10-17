from flask import Blueprint
import jinja2

theme_blueprint = Blueprint('theme', __name__, template_folder="templates", static_folder="static")

theme_blueprint.jinja_loader = jinja2.ChoiceLoader([
    theme_blueprint.jinja_loader,
    jinja2.PackageLoader(__name__) # in the same folder will search the 'templates' folder
])