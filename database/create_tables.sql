CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255),
    phone VARCHAR(50),
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    age INT,
    signup_date DATE,
    loyalty_level VARCHAR(20)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(100),
    supplier VARCHAR(255),
    cost NUMERIC(10,2),
    price NUMERIC(10,2),
    stock_quantity INT,
    created_at DATE
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    store_id INT,
    order_date DATE,
    status VARCHAR(30),
    payment_method VARCHAR(50),
    sales_channel VARCHAR(50)
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    unit_cost NUMERIC(10,2),
    unit_price NUMERIC(10,2),
    line_total NUMERIC(10,2)
);