import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="postgres"
)
cur = conn.cursor()

# Önceki çalıştırmalardan / diğer projelerden kalan tabloları temizle
cur.execute("DROP TABLE IF EXISTS customers, products, orders CASCADE;")

cur.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    country VARCHAR(50),
    signup_date DATE
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    price NUMERIC(8,2),
    stock_quantity INTEGER
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    order_date DATE,
    total_amount NUMERIC(10,2)
);
""")

cur.execute("""
INSERT INTO customers (customer_name, email, country, signup_date) VALUES
('Ali Veli', 'ali.veli@example.com', 'Turkey', '2022-01-10'),
('Ayşe Yılmaz', 'ayse.yilmaz@example.com', 'Turkey', '2021-05-03'),
('John Doe', 'john.doe@example.com', 'USA', '2020-11-15'),
('Emma Brown', 'emma.b@example.co.uk', 'UK', '2023-02-21'),
('Carlos Mendez', 'carlos.m@example.com', 'Mexico', '2022-07-12'),
('Merve Demir', 'merve.d@example.com', 'Turkey', '2021-09-30');
""")

cur.execute("""
INSERT INTO products (product_name, price, stock_quantity) VALUES
('Wireless Mouse', 199.90, 30),
('Gaming Keyboard', 499.99, 15),
('USB-C Cable', 49.95, 100),
('27" Monitor', 1899.00, 8),
('Laptop Stand', 329.50, 20),
('Noise-Cancelling Headphones', 1250.75, 5);
""")

cur.execute("""
INSERT INTO orders (customer_id, order_date, total_amount) VALUES
(1, '2022-01-15', 249.90),
(2, '2022-06-10', 499.99),
(3, '2023-01-05', 1250.75),
(1, '2023-03-12', 199.90),
(4, '2023-05-01', 329.50),
(5, '2023-06-18', 1899.00),
(6, '2021-10-10', 49.95);
""")

conn.commit()
cur.close()
conn.close()