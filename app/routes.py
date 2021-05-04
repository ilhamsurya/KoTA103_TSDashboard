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


# 404 Error handler
@app.errorhandler(404)
def resource_not_found(e):
    return render_template("auth/404.html"), 404
