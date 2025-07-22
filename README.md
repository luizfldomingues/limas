Final Project CS50x 2024/2025
=============================

## Purpose

This project aims to be an efficient order manager for dine-in establishment, e.g., restaurants, icecream shops etc.

## How to run

After downloading the project files, make sure you have all dependencies installed, then go to database folder and run:
```console
sqlite3 limas.db
```
Then, in sqlite program, run:
```sqlite3
.read limas.sql
```
By default, new users can be registered. In order to change that, you can change the value of the variable allow_new_users in preferences.py.

After that, your application is ready to run. To do so, go to the project root folder and run:
```bash
flask run
```
That is going to, by default, deploy your application locally on adress 127.0.0.1:5000. You can access it on your local browser and start using.

You can also add the flag --host=0.0.0.0 to run it on all adresses, including your local network (don't worry, flask is going to tell you your local ip), so it can be acessed from anyone using the same router as you

## How to use

The project design's goal is to be the most intuitive as possible. Currently, all the app interface is 

## Dependencies

The project depends on some python packages, including cs50, flask, flask_session, werkzeug.security etc.


In order to make it easier for you to execute the program, there's a requirements.txt file that can help you manage the python dependencies. The recomended way to use it is in a python venv.

To create a python venv, activate it and install the dependencies, follow:

Create the python venv and activate it (in the project root folder):
```console
python -m venv .venv
```

Then activate it:
```console
source .venv/bin/activate
```

Now, you can install the dependencies in a python virtual enviroment from the requirements.txt file:
```console
pip install -r requirements.txt
```

This way, you should have all python dependencies installed.

If you want to run the program again later, in another bash section, just active the virtual environment as shown above, and all dependencies are meant to still be in that enviroment.
