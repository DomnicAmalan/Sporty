
from flask import Blueprint, render_template, flash, request
import requests

client = Blueprint('client', __name__, template_folder="templates/client")

@client.route('/')
def display_books():
    return render_template("client/index.html")

@client.route('/signup')
def signup():
    return render_template("client/signup.html")

@client.route('/login')
def login():
    return render_template("client/login.html")

@client.route('/create-password')
def create_password_page(email):
    return render_template("client/create-password.html", email=email)

@client.route('/dashboard')
def dashboard():
    return render_template("client/dashboard.html")
