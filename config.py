from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access variables using os.getenv
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

print("Email:", email)
print("Password:", password)