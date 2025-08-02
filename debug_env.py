import os
from dotenv import load_dotenv

load_dotenv()
print("HF_TOKEN: ", os.getenv('HF_TOKEN')[:10] + "..." if os.getenv('HF_TOKEN') else "Not set")
print("XAI_API_KEY: ", os.getenv('XAI_API_KEY')[:10] + "..." if os.getenv('XAI_API_KEY') else "Not set")
print("SERPAPI_API_KEY: ", os.getenv('SERPAPI_API_KEY')[:10] + "..." if os.getenv('SERPAPI_API_KEY') else "Not set")
