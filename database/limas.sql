CREATE TABLE product_types (
    id INTEGER PRIMARY KEY NOT NULL,
    type_name TEXT NOT NULL UNIQUE,
    type_status TEXT CHECK (type_status IN ('active', 'inactive')) NOT NULL DEFAULT 'active'
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY NOT NULL,
    product_name TEXT NOT NULL UNIQUE,
    product_type_id INTEGER NOT NULL,
    price INTEGER NOT NULL,
    product_status TEXT CHECK (product_status IN ('active', 'inactive')) NOT NULL DEFAULT 'active',
    FOREIGN KEY (product_type_id) REFERENCES product_types(id)
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    role TEXT CHECK (role IN ('manager', 'staff')) NOT NULL DEFAULT 'staff',
    hash TEXT NOT NULL,
    user_status TEXT CHECK (user_status IN ('active', 'inactive')) NOT NULL DEFAULT 'active'
);

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
    FOREIGN KEY (order_id) REFERENCES orders(id),
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

--TODO: Add indexes on tables
