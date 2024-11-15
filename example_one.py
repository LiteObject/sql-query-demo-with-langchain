import os
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_ollama.llms import OllamaLLM
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Define your connection parameters
host = os.getenv('DB_HOST')
database = os.getenv('DB_NAME')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
port = int(os.getenv('DB_PORT'))

db = SQLDatabase.from_uri(f"postgresql://{username}:{password}@{host}:{port}/{database}")
# print(db.dialect)
# print(db.get_usable_table_names())
result = db.run("""
SELECT SUM(price) FROM products
""")
print("Query result:", result)

llm = OllamaLLM(model="llama3.2", temperature=0)
chain = create_sql_query_chain(llm, db)
# response = chain.invoke({"question": "How many products are there"})
response = chain.invoke({"question": "What is the total price of all products?"})
print("Answer:", response)

# Print the prompt
# chain.get_prompts()[0].pretty_print()