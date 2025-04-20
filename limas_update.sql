-- This sql file creates the new version of the tables to have the order_increments functionality
-- remember to manually drop the tables that are being created
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    customer_name TEXT,
    table_number TEXT,
    order_status TEXT CHECK (order_status IN ('pending', 'completed')) NOT NULL DEFAULT 'pending',
    order_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE order_increments (
    id INTEGER PRIMARY KEY NOT NULL,
    order_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    increment_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(id)
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE order_products (
    id INTEGER PRIMARY KEY NOT NULL,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    order_increment_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    current_price INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (order_increment_id) REFERENCES order_increments(id)
);

