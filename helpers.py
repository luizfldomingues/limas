from flask import redirect, render_template, session, flash
from functools import wraps

def apology(message, code="400"):
    return render_template("apology.html", message=message, code=code)

class Filters:
    """ Definitions of filters, mainly used my jinja """
    @staticmethod
    def brl(value):
        """Format value from BRL cents to BRL"""
        if type(value) is not int:
            value = 0
        return f"R${value / 100:,.2f}".replace(".", ";").replace(",", ".").replace(";", ",")

def placeholders(n=0):
    return ", ".join(['?']*n)

# TODO: Understand how this works
def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function

def manager_only(f):
    """ Decorate routes to only allow managers to visit """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_role") != "manager":
            flash("Área exclusiva para gerentes")
            return redirect("/")
        return f(*args, **kwargs)

    return decorated_function


