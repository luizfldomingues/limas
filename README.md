Lima's - A simple order and sales manager for dine-in establishments.
=============================

## Purpose

This project aims to be an efficient order manager for dine-in establishment, e.g., restaurants, icecream shops etc.
I.e. it makes the life of establishment owners easier by handling the orders and sales management for them.

## How to run

After downloading the project files, make sure you have all dependencies installed. Read the dependency section for more informations.

To start running the application, execute in the project root folder:
```bash
flask run
```
Alternatively:
```bash
python3 -m flask run
```

That is going to, by default, deploy your application locally on address 127.0.0.1:5000 (localhost:5000). You can access it via http on your local browser and start using.

You can also add the flag --host=0.0.0.0 to run it on all addresses, including your local network, so it can be accessed by other devices in your local network.

## Dependencies

The project depends on some python packages, including cs50, flask, flask_session, werkzeug.security, matplotlib etc.

In order to make it easier for you to execute the program, there's a requirements.txt file that can help you manage the python dependencies. The recommended way to use it is in a python venv.

To create a python venv, activate it and install the dependencies, follow the steps bellow.

Create the python venv and activate it (in the project root folder):
```bash
python -m venv .venv
```

Then activate it:
```bash
source .venv/bin/activate
```

Now, you can install the dependencies in a python virtual environment from the requirements.txt file:
```bash
pip install -r requirements.txt
```

This way, you should have all python dependencies installed.

If you want to run the program again later, in another bash section, just active the virtual environment as shown above, and all dependencies will be as you left them in that environment, without affecting your other python sessions.

## How to use

The project design's goal is to be the most intuitive as possible. Currently, all the app interface is written in Portuguese, because of the context it is originally meant to be used.

When acessing the app for the first time via browser, you will be redirected to a registration page. The first account registered is always an admin of the system.

If you are logged in, you can see the active orders in the main page (to go to the main page just click on lima's logo on the header from any page you are). To create a new order, you can click the link in the main page or on the header, shown as "novo pedido". You will be asked about the table number, customer name and the products of that order. After creating the new order, they will appear in the main page, where you can increment, edit, complete or see more details about the order (including deleting it).

There is a section for consulting the order history. You can access it from the header on "histórico". You will be asked for how long you want to see the history and then all the completed orders in that period will be shown. If you click to see an order details, you can also reopen it.

Specially, if you are a manager, you will have acess to the products page, where you can edit the products and their types, the reports page, where you can generate reports of your sales for a specified time period, and the users page, where you can manage the users of the system.

By default, anyone that can access your app can create a new account. In order to change that, you can change the value of the variable allow_new_users in preferences.py to False.

## Showcase

Here is a video presentation of the project

