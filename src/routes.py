from app import app
from flask import render_template, request, flash, redirect, url_for
from src.services.tip_service import tip_service

@app.route("/")
def render_index():
    tips = tip_service.get_visible_tips()
    return render_template("index.html", tips=tips)

@app.route("/add_tip", methods=["GET"])
def render_add_tip():
    return render_template("add_tip.html")

@app.route("/add_tip", methods=["POST"])
def add_new_tip():
    title = request.form.get("title")
    url = request.form.get("url")
    description = request.form.get("description")
    user_id = 1 #placeholder before users added

    try:
        tip_service.add_new_tip(title, url, description, user_id)
        return redirect_to_index()

    except Exception as error:
        flash(str(error))
        return redirect_to_add_tip()
    
def redirect_to_add_tip():
    return redirect(url_for("render_add_tip"))

def redirect_to_index():
    return redirect(url_for("render_index"))