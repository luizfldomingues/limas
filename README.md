Final Project CS50x 2024/2025
=============================

## Purpose

This project aims to be an efficient order manager for dine-in establishment, e.g., restaurants, icecream shops etc.

## How to run

After downloading the project files, make sure you have all dependencies installed. Read further for more informations about dependencies.

To start running the application, execute:
```bash
flask run
```

That is going to, by default, deploy your application locally on address 127.0.0.1:5000. You can access it on your local browser and start using.

You can also add the flag --host=0.0.0.0 to run it on all addresses, including your local network, so it can be accessed locally using different devices.

## How to use

The project design's goal is to be the most intuitive as possible. Currently, all the app interface is written in Portuguese.

# TODO: explain how the pages work

By default, anyone that can access your app can create a new account. In order to change that, you can change the value of the variable allow_new_users in preferences.py.

## Dependencies

The project depends on some python packages, including cs50, flask, flask_session, werkzeug.security etc.

In order to make it easier for you to execute the program, there's a requirements.txt file that can help you manage the python dependencies. The recommended way to use it is in a python venv.

To create a python venv, activate it and install the dependencies, follow the steps bellow.

Create the python venv and activate it (in the project root folder):
```console
python -m venv .venv
```

Then activate it:
```console
source .venv/bin/activate
```

Now, you can install the dependencies in a python virtual environment from the requirements.txt file:
```console
pip install -r requirements.txt
```

This way, you should have all python dependencies installed.

If you want to run the program again later, in another bash section, just active the virtual environment as shown above, and all dependencies are meant to still be in that environment.
