from flask import Blueprint, render_template, abort


dashboard = Blueprint('dashboard', __name__, template_folder="templates")


@dashboard.route('/')
def index():
    return render_template('dashboard.html')
