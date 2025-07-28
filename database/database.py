import sqlite3
import os
from cs50 import SQL
from flask import session

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db = SQL(f"sqlite:///{self.db_path}")
        def new_database():
            with open('/home/luizdomingues/Desktop/cs50x-final-project-limas/database/limas.sql', 'r') as sql_file:
                sql_script = sql_file.read()
                with sqlite3.connect(self.db_path) as con:
                    cur = con.cursor()
                    cur.executescript(sql_script)
                    con.commit()
                    print("Novo banco de dados criado com sucesso")
        if not os.path.isfile(self.db_path):
            new_database()

    # Create a order increment and add the products in the order_products table
    def add_order_products(self, order_id, increment_products):
        if len(increment_products) == 0:
            return
        order_increment_id = self.db.execute("INSERT INTO order_increments "
        "(order_id, user_id) VALUES (?, ?)", order_id, session["user_id"])
        for product in increment_products:
            price = self.db.execute("SELECT price FROM products WHERE id = ?",
                            product["id"])[0]["price"]
            self.db.execute("INSERT INTO order_products "
                    "(order_id, product_id, order_increment_id, "
                    "quantity, current_price)"
                    "VALUES (?, ?, ?, ?, ?)",
                    order_id, product["id"], order_increment_id,
                    product["quantity"], price)
        return
    # When receiving a list of orders, returns the products of those orders
    def list_products(self, orders):
        # Create a dictionary of lists of products with each key being the order id
        order_products = {}
        for order in orders:
            order_products[order["id"]] = self.db.execute(
                "SELECT * FROM "
                "(SELECT order_products.product_id AS id, "
                "SUM(quantity) AS quantity, current_price, "
                "products.product_name FROM order_products JOIN products "
                "ON order_products.product_id = products.id WHERE order_id = ? "
                "GROUP BY order_products.product_id "
                "ORDER BY products.product_type_id, price) WHERE quantity > 0",
                order["id"])
            total = 0
            for product in order_products[order["id"]]:
                total += product.get("quantity") * product.get("current_price")
            order["total"] = total
        return order_products

    def get_pending_orders(self):
        return self.db.execute("SELECT * FROM orders "
                                "WHERE order_status = 'pending' "
                                "ORDER BY id DESC")

    def get_order(self, order_id):
        return self.db.execute("SELECT * FROM orders WHERE id = ?", order_id)

    def update_order(self, order_id, customer, table):
        self.db.execute("UPDATE orders SET customer_name = ?, table_number = ? "
                    "WHERE id = ?", customer, table, order_id)

    def get_order_status(self, order_id):
        return self.db.execute("SELECT order_status FROM orders WHERE id = ?",
                        order_id)

    def delete_order_products(self, order_id):
        self.db.execute("DELETE FROM order_products WHERE order_id = ?", order_id)

    def delete_order_increments(self, order_id):
        self.db.execute("DELETE FROM order_increments WHERE order_id = ?", order_id)

    def delete_order(self, order_id):
        self.db.execute("DELETE FROM orders WHERE id = ?", order_id)

    def update_order_status(self, order_id, status):
        self.db.execute("UPDATE orders "
                    "SET order_status = ? WHERE id = ?", 
                    status, order_id)

    def get_date_since(self, date_range):
        return self.db.execute("SELECT DATE("
                                "DATETIME(current_timestamp, '-3 hours'), "
                                "'-' || ? || ' days') "
                                "AS date",
                                date_range)[0]["date"]

    def get_completed_orders_since(self, since_date):
        return self.db.execute("SELECT *, DATETIME(order_time, '-3 hours') "
                            "AS order_timef "
                            "FROM orders "
                            "WHERE order_timef >= ? "
                            "AND order_status = 'completed' "
                            "ORDER BY order_time DESC", since_date)

    def get_all_completed_orders(self):
        return self.db.execute("SELECT *, DATETIME(order_time, '-3 hours') "
                            "AS order_timef FROM orders "
                            "WHERE order_status = 'completed' "
                            "ORDER BY order_time DESC")

    def get_product_types(self):
        return self.db.execute("SELECT * FROM product_types")

    def get_products_by_type(self, type_id):
        return self.db.execute("SELECT id, product_name, "
                                "price FROM products "
                                "WHERE product_type_id = ?",
                                type_id)

    def get_user_by_username(self, username):
        return self.db.execute("SELECT * FROM users WHERE username = ?", username)

    def get_active_product_types(self):
        return self.db.execute("SELECT * FROM product_types "
                               "WHERE type_status = 'active'")

    def get_active_products_by_type(self, type_id):
        return self.db.execute("SELECT * "
                                "FROM products "
                                "WHERE product_type_id = ? "
                                "AND product_status "
                                "= 'active' "
                                "ORDER BY price",
                                type_id)

    def get_inactive_products_by_active_type(self, type_id):
        return self.db.execute("SELECT * "
                                "FROM products "
                                "WHERE product_type_id = ? "
                                "AND product_status "
                                "= 'inactive' "
                                "ORDER BY price",
                                type_id)
    
    def get_all_products_by_inactive_type(self, type_id):
        return self.db.execute("SELECT * "
                                "FROM products "
                                "WHERE product_type_id = ? "
                                "ORDER BY price",
                                type_id)

    def get_product_by_id(self, product_id):
        return self.db.execute("SELECT * FROM products "
                                "WHERE id=?",
                                product_id)

    def get_product_type_by_id(self, product_type_id):
        return self.db.execute("SELECT id FROM product_types "
                                "WHERE id = ?",
                                product_type_id)

    def update_product(self, name, price, type_id, status, product_id):
        self.db.execute("UPDATE products "
                        "SET product_name = ?, "
                        "price = ?, "
                        "product_type_id = ?, "
                        "product_status = ? "
                        "WHERE id = ?",
                        name,
                        price,
                        type_id,
                        status,
                        product_id)

    def get_full_product_type_by_id(self, product_type_id):
        return self.db.execute("SELECT * FROM product_types "
                                "WHERE id = ?",
                                product_type_id)

    def update_product_type(self, name, status, type_id):
        self.db.execute("UPDATE product_types "
                        "SET type_name = ?, "
                        "type_status = ? "
                        "WHERE id = ?",
                        name,
                        status,
                        type_id)

    def count_active_products_by_type(self, type_id):
        return self.db.execute("SELECT COUNT(id) "
                                "FROM products "
                                "WHERE product_type_id = ? "
                                "AND product_status "
                                "= 'active'",
                                type_id)

    def create_product(self, name, price, type_id):
        self.db.execute("INSERT INTO products "
                    "(product_name, price, product_type_id) "
                    "VALUES (?, ?, ?)",
                    name,
                    price,
                    type_id)

    def create_product_type(self, type_name):
        self.db.execute("INSERT INTO product_types "
                    "(type_name) "
                    "VALUES (?)",
                    type_name)

    def create_order(self, user_id, customer_name, table_number):
        return self.db.execute("INSERT INTO orders "
                            "(user_id, customer_name, table_number) "
                            "VALUES (?, ?, ?)",
                            user_id, customer_name, table_number)

    def get_order_total(self, order_id):
        return self.db.execute("SELECT SUM(current_price * quantity) "
                                "AS total FROM order_products WHERE "
                                "order_id = ?", order_id)[0].get("total")

    def get_order_username(self, order_id):
        return self.db.execute("SELECT username FROM users WHERE id "
                                "IN (SELECT user_id FROM orders "
                                "WHERE id = ?)", 
                                order_id)[0].get("username")

    def get_order_time(self, order_id):
        return self.db.execute("SELECT "
                                "DATETIME(order_time, '-3 hours') "
                                "as order_time FROM orders "
                                "WHERE id = ?", 
                                order_id)[0].get("order_time")

    def get_order_increments(self, order_id):
        return self.db.execute("SELECT order_increments.id AS id, username, "
                            "DATETIME(increment_time, '-3 hours') "
                            "AS increment_time FROM order_increments "
                            "JOIN users "
                            "ON order_increments.user_id = "
                            "users.id WHERE order_id = ? "
                            "ORDER BY increment_time DESC", 
                            order_id)

    def get_increment_products(self, increment_id, order_id):
        return self.db.execute("SELECT product_id, quantity, "
                                            "current_price, product_name "
                                            "FROM order_products "
                                            "JOIN products "
                                            "ON order_products.product_id = " 
                                            "products.id "
                                            "WHERE order_increment_id = ? " 
                                            "AND order_id = ? "
                                            "ORDER BY product_type_id, "
                                            "current_price", 
                                            increment_id, order_id)

    def get_increment_total(self, increment_id):
        return self.db.execute("SELECT "
                                        "SUM(quantity * current_price) "
                                        "AS total FROM order_products "
                                        "WHERE order_increment_id = ?",
                                        increment_id)[0].get("total")

    def create_user(self, username, password_hash):
        self.db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
                    username, password_hash)

    def get_user_id_by_username(self, username):
        return self.db.execute("SELECT id FROM users WHERE username = ?", 
                            username)[0]["id"]

db = Database("/home/luizdomingues/Desktop/cs50x-final-project-limas/database/limas.db")