from app import app
from flask import render_template, request, flash, redirect, url_for
from services.tip_service import tip_service
from services.user_service import user_service

@app.route("/", methods=["GET"])
def render_index():
    tips = tip_service.get_visible_tips()
    return render_template("index.html", tips=tips)

@app.route("/", methods=["POST"])
def delete_tip():
    id_to_delete = request.form["delete"]
    delete = tip_service.delete_tip(id_to_delete)
    if delete:
        flash("Poisto onnistui")
    else:
        flash("Poisto ei onnistunut")
    return redirect_to_index()

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

@app.route("/register", methods=["GET"])
def render_register():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register_new_user():
    name = request.form.get("name")
    username = request.form.get("username")
    password = request.form.get("password")
    password_confirmation = request.form.get("password_confirmation")

    try:
        user_service.create_user(name, username, password, password_confirmation)
        flash(str("Käyttäjätunnus on rekisteröity."))
        return redirect_to_index()
    except Exception as error:
        flash(str(error))
        return redirect_to_register()

def redirect_to_add_tip():
    return redirect(url_for("render_add_tip"))

def redirect_to_index():
    return redirect(url_for("render_index"))

def redirect_to_register():
    return redirect(url_for("render_register"))