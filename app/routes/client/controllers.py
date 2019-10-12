
from flask import Blueprint, render_template, flash, request
import requests

client = Blueprint('client', __name__, template_folder="templates/client")

@client.route('/')
def display_books():
    return render_template("client/index.html")

@client.route('/signup')
def signup():
    return render_template("client/signup.html")
