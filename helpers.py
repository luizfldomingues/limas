from flask import redirect, render_template, session, flash
from functools import wraps
from database.database import db
from werkzeug.security import check_password_hash

def apology(message, code="400"):
    return render_template("apology.html", message=message, code=code)

class Constants:
    """Definitiosn of contansts used accross the code"""
    roles = ("staff", "manager")

class Filters:
    """ Definitions of filters, mainly used my jinja """
    @staticmethod
    def brl(value):
        """Format value from BRL cents to BRL"""
        if type(value) is not int:
            value = 0
        return f"R${value / 100:,.2f}".replace(".", ";").replace(",", ".").replace(";", ",")

    @staticmethod
    def translate(word):
        translations = {
            'staff': 'colaborador',
            'manager': 'gerente',
        }
        try:
            return translations[word]
        except KeyError:
            return word

def update_user_session(user_id):
    """ Updates user session id so that all current sessions get loged out """
    user = db.get_user_by_id(user_id)
    if not user:
        return None
    return db.change_user_session_id(user_id=user_id, new_id=(user["session_id"] + 1))

def login_session(session, password, user_id=None, username=None):
    """ Logs the user in 
        Return None if failed to log in 
        Return 1 if success """

    if user_id is not None:
        user = db.get_user_by_id(user_id)
    elif username is not None:
        try:
            user = db.get_user_by_username(username)[0]
            print(user)
        except IndexError:
            return None
    else:
        return None

    if not user:
        return None

    if not check_password_hash(pwhash=user["hash"], password=password):
        return None

    session["user_id"] = user["id"]
    session["user_role"] = user["role"]
    session["session_id"] = user["session_id"]
    flash(f"Logado com sucesso como {user["username"]}.")
    return 1


def login_required(f):
    """ Decorate routes to require login. """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            flash("Área exclusiva para usuários registrados.")
            return redirect("/login")
        user = db.get_user_by_id(session.get("user_id"))
        if not user:
            return apology("Usuário não encontrado no banco de dados")
        if not user["session_id"] == session.get("session_id"):
            flash("Todas as suas sessões foram desconectadas. Por favor, entre novamente.")
            session.clear()
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function

def manager_only(f):
    """ Decorate routes to only allow managers to visit 
        Assumes the route also requires login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_role") != "manager":
            flash("Área exclusiva para gerentes.")
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function


