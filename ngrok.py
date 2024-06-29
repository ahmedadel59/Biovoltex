from pyngrok import ngrok
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the auth token
NGROK_AUTH = os.getenv("NGROK_AUTH")
ngrok.set_auth_token(NGROK_AUTH)

# Connect to the port
port = 8080
tunnel = ngrok.connect(port)
print("Public URL:", tunnel.public_url)
