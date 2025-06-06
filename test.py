import os
from dotenv import load_dotenv 

load_dotenv('var.env')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
print(BEARER_TOKEN)
