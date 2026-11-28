import os

from dotenv import load_dotenv

print(os.environ)
load_dotenv()  # Load environment variables from .env file
print(os.getenv("DB_PASSWORD"))  # Print the value of DB_PASSWORD to verify it's loaded correctly