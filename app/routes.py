import os, sys
import datetime as dt
from flask import (
    render_template,
    url_for,
    redirect,
    request,
    make_response,
    abort,
    jsonify,
    session,
    flash,
)
from app import app
# from flask_mysqldb import MySQL
# from conn.py import conn

# Home route
@app.route("/")
def index():
    return render_template("landingpage.html")


# User registration route
@app.route("/register")
def register():
    return render_template("auth/register.html")


# User login route
@app.route("/login")
def login():
    return render_template("auth/login.html")


# User Dashboard roaute
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard/dashboard.html")


# User Dashboard roaute
@app.route("/forecasting")
def forecasting():
    return render_template("dashboard/forecasting.html")


# User Dashboard roaute
@app.route("/map")
def heatmap():
    return render_template("dashboard/map.html")

# testing show data 
# @app.route('/kat')
# def kategori():
#     cursor = conn.cursor()
#     hasil = cursor.execute("SELECT * FROM kategori")
#     if hasil > 0 :
#         result = cursor.fetchall()
#         return render_template('templates/testing.html', result = result)


# 404 Error handler
@app.errorhandler(404)
def resource_not_found(e):
    return render_template("auth/404.html"), 404
