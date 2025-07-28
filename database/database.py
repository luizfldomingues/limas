import sqlite3
import os
from flask import session

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        if not os.path.isfile(self.db_path):
            self._init_database()

    def _get_db_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_database(self):
        with open('/home/luizdomingues/Desktop/cs50x-final-project-limas/database/limas.sql', 'r') as sql_file:
            sql_script = sql_file.read()
        with self._get_db_connection() as conn:
            conn.executescript(sql_script)
            conn.commit()
            print("Novo banco de dados criado com sucesso")

    def _execute_query(self, query, params=(), fetchone=False, lastrowid=False):
        with self._get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            if lastrowid:
                result = cursor.lastrowid
            elif fetchone:
                result = cursor.fetchone()
            else:
                result = cursor.fetchall()
            conn.commit()
            return result

    def add_order_products(self, order_id, increment_products):
        if not increment_products:
            return
        order_increment_id = self._execute_query(
            "INSERT INTO order_increments (order_id, user_id) VALUES (?, ?)",
            (order_id, session["user_id"]),
            lastrowid=True
        )
        for product in increment_products:
            price_row = self._execute_query(
                "SELECT price FROM products WHERE id = ?",
                (product["id"],),
                fetchone=True
            )
            if price_row:
                price = price_row["price"]
                self._execute_query(
                    "INSERT INTO order_products (order_id, product_id, order_increment_id, quantity, current_price) VALUES (?, ?, ?, ?, ?)",
                    (order_id, product["id"], order_increment_id, product["quantity"], price)
                )

    def list_products(self, orders):
        order_products = {}
        for order in orders:
            products = self._execute_query(
                "SELECT * FROM (SELECT op.product_id AS id, SUM(op.quantity) AS quantity, op.current_price, p.product_name "
                "FROM order_products op JOIN products p ON op.product_id = p.id WHERE op.order_id = ? "
                "GROUP BY op.product_id ORDER BY p.product_type_id, p.price) WHERE quantity > 0",
                (order["id"],)
            )
            order_products[order["id"]] = [dict(row) for row in products]
            total = sum(p["quantity"] * p["current_price"] for p in order_products[order["id"]])
            order["total"] = total
        return order_products

    def get_pending_orders(self):
        rows = self._execute_query("SELECT * FROM orders WHERE order_status = 'pending' ORDER BY id DESC")
        return [dict(row) for row in rows]

    def get_order(self, order_id):
        rows = self._execute_query("SELECT * FROM orders WHERE id = ?", (order_id,))
        return [dict(row) for row in rows]

    def update_order(self, order_id, customer, table):
        self._execute_query("UPDATE orders SET customer_name = ?, table_number = ? WHERE id = ?", (customer, table, order_id))

    def get_order_status(self, order_id):
        rows = self._execute_query("SELECT order_status FROM orders WHERE id = ?", (order_id,))
        return [dict(row) for row in rows]

    def delete_order_products(self, order_id):
        self._execute_query("DELETE FROM order_products WHERE order_id = ?", (order_id,))

    def delete_order_increments(self, order_id):
        self._execute_query("DELETE FROM order_increments WHERE order_id = ?", (order_id,))

    def delete_order(self, order_id):
        self._execute_query("DELETE FROM orders WHERE id = ?", (order_id,))

    def update_order_status(self, order_id, status):
        self._execute_query("UPDATE orders SET order_status = ? WHERE id = ?", (status, order_id))

    def get_date_since(self, date_range):
        row = self._execute_query("SELECT DATE(DATETIME(current_timestamp, '-3 hours'), '-' || ? || ' days') AS date", (date_range,), fetchone=True)
        return row['date'] if row else None

    def get_completed_orders_since(self, since_date):
        rows = self._execute_query(
            "SELECT *, DATETIME(order_time, '-3 hours') AS order_timef FROM orders "
            "WHERE order_timef >= ? AND order_status = 'completed' ORDER BY order_time DESC",
            (since_date,)
        )
        return [dict(row) for row in rows]

    def get_all_completed_orders(self):
        rows = self._execute_query(
            "SELECT *, DATETIME(order_time, '-3 hours') AS order_timef FROM orders "
            "WHERE order_status = 'completed' ORDER BY order_time DESC"
        )
        return [dict(row) for row in rows]

    def get_product_types(self):
        rows = self._execute_query("SELECT * FROM product_types")
        return [dict(row) for row in rows]

    def get_products_by_type(self, type_id):
        rows = self._execute_query("SELECT id, product_name, price FROM products WHERE product_type_id = ?", (type_id,))
        return [dict(row) for row in rows]

    def get_user_by_username(self, username):
        rows = self._execute_query("SELECT * FROM users WHERE username = ?", (username,))
        return [dict(row) for row in rows]

    def get_active_product_types(self):
        rows = self._execute_query("SELECT * FROM product_types WHERE type_status = 'active'")
        return [dict(row) for row in rows]

    def get_active_products_by_type(self, type_id):
        rows = self._execute_query(
            "SELECT * FROM products WHERE product_type_id = ? AND product_status = 'active' ORDER BY price",
            (type_id,)
        )
        return [dict(row) for row in rows]

    def get_inactive_products_by_active_type(self, type_id):
        rows = self._execute_query(
            "SELECT * FROM products WHERE product_type_id = ? AND product_status = 'inactive' ORDER BY price",
            (type_id,)
        )
        return [dict(row) for row in rows]

    def get_all_products_by_inactive_type(self, type_id):
        rows = self._execute_query("SELECT * FROM products WHERE product_type_id = ? ORDER BY price", (type_id,))
        return [dict(row) for row in rows]

    def get_product_by_id(self, product_id):
        rows = self._execute_query("SELECT * FROM products WHERE id=?", (product_id,))
        return [dict(row) for row in rows]

    def get_product_type_by_id(self, product_type_id):
        rows = self._execute_query("SELECT id FROM product_types WHERE id = ?", (product_type_id,))
        return [dict(row) for row in rows]

    def update_product(self, name, price, type_id, status, product_id):
        self._execute_query(
            "UPDATE products SET product_name = ?, price = ?, product_type_id = ?, product_status = ? WHERE id = ?",
            (name, price, type_id, status, product_id)
        )

    def get_full_product_type_by_id(self, product_type_id):
        rows = self._execute_query("SELECT * FROM product_types WHERE id = ?", (product_type_id,))
        return [dict(row) for row in rows]

    def update_product_type(self, name, status, type_id):
        self._execute_query("UPDATE product_types SET type_name = ?, type_status = ? WHERE id = ?", (name, status, type_id))

    def count_active_products_by_type(self, type_id):
        row = self._execute_query(
            "SELECT COUNT(id) as count FROM products WHERE product_type_id = ? AND product_status = 'active'",
            (type_id,),
            fetchone=True
        )
        return row['count'] if row else 0

    def create_product(self, name, price, type_id):
        self._execute_query("INSERT INTO products (product_name, price, product_type_id) VALUES (?, ?, ?)", (name, price, type_id))

    def create_product_type(self, type_name):
        self._execute_query("INSERT INTO product_types (type_name) VALUES (?)", (type_name,))

    def create_order(self, user_id, customer_name, table_number):
        return self._execute_query(
            "INSERT INTO orders (user_id, customer_name, table_number) VALUES (?, ?, ?)",
            (user_id, customer_name, table_number),
            lastrowid=True
        )

    def get_order_total(self, order_id):
        row = self._execute_query("SELECT SUM(current_price * quantity) AS total FROM order_products WHERE order_id = ?", (order_id,), fetchone=True)
        return row['total'] if row else 0

    def get_order_username(self, order_id):
        row = self._execute_query("SELECT username FROM users WHERE id IN (SELECT user_id FROM orders WHERE id = ?)", (order_id,), fetchone=True)
        return row['username'] if row else None

    def get_order_time(self, order_id):
        row = self._execute_query("SELECT DATETIME(order_time, '-3 hours') as order_time FROM orders WHERE id = ?", (order_id,), fetchone=True)
        return row['order_time'] if row else None

    def get_order_increments(self, order_id):
        rows = self._execute_query(
            "SELECT oi.id AS id, u.username, DATETIME(oi.increment_time, '-3 hours') AS increment_time "
            "FROM order_increments oi JOIN users u ON oi.user_id = u.id WHERE oi.order_id = ? "
            "ORDER BY oi.increment_time DESC",
            (order_id,)
        )
        return [dict(row) for row in rows]

    def get_increment_products(self, increment_id, order_id):
        rows = self._execute_query(
            "SELECT op.product_id, op.quantity, op.current_price, p.product_name "
            "FROM order_products op JOIN products p ON op.product_id = p.id "
            "WHERE op.order_increment_id = ? AND op.order_id = ? "
            "ORDER BY p.product_type_id, op.current_price",
            (increment_id, order_id)
        )
        return [dict(row) for row in rows]

    def get_increment_total(self, increment_id):
        row = self._execute_query("SELECT SUM(quantity * current_price) AS total FROM order_products WHERE order_increment_id = ?", (increment_id,), fetchone=True)
        return row['total'] if row else 0

    def create_user(self, username, password_hash):
        self._execute_query("INSERT INTO users (username, hash) VALUES (?, ?)", (username, password_hash))

    def get_user_id_by_username(self, username):
        row = self._execute_query("SELECT id FROM users WHERE username = ?", (username,), fetchone=True)
        return row['id'] if row else None

db = Database("database/limas.db")
