import os
from dotenv import load_dotenv
import logging
from sqlalchemy import create_engine, text

# Load .env file
load_dotenv()

# Define connection parameters
host = os.getenv('DB_HOST')
database = os.getenv('DB_NAME')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
port = int(os.getenv('DB_PORT'))

engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}")

with engine.begin() as conn:
    # Execute queries within a transaction
    conn.execute(text("DROP TABLE products;"))
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            description TEXT,
            price DECIMAL(10, 2)
        );
    """))
    conn.execute(text("""
        INSERT INTO products (name, description, price) VALUES ('Product A', 'This is product A.', 10.01);
        INSERT INTO products (name, description, price) VALUES ('Product B', 'This is product B.', 20.02);
        INSERT INTO products (name, description, price) VALUES ('Product C', 'This is product C.', 30.03);
    """))