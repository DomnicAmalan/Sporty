
from flask import Blueprint, render_template, flash

client = Blueprint('client', __name__, template_folder="templates/client")

@client.route('/')
def display_books():
    return render_template("client/index.html")