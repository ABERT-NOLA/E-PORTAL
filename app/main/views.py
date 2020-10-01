from flask import render_template, request, redirect, url_for, abort, flash
from . import main


@main.route('/')
def index():
    return render_template('index.html')
