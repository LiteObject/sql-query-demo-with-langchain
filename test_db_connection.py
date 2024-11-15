from langchain_community.utilities import SQLDatabase

# Define your connection parameters
host = 'localhost'
database = 'mydatabase'
username = 'myuser'
password = 'mypassword'
port = 5431  # specify a different port for your application

try:
    # Establish a connection to the database
    db = SQLDatabase.from_uri(f"postgresql://{username}:{password}@{host}:{port}/{database}")
    print("Connected to the database!")

    # Execute a query
    result = db.run("SELECT NOW();")
    print("Query result:", result)

except Exception as e:
    print(f"Error connecting to the database: {e}")
