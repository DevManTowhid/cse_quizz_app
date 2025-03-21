import firebase_admin
from firebase_admin import credentials, firestore, db
import os
import json
from dotenv import load_dotenv

load_dotenv()
# Read credentials from environment variable
firebase_credentials = json.loads(os.getenv("FIREBASE_CREDENTIALS"))



  # Load variables from .env

firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")

if firebase_credentials is None:
    raise ValueError("FIREBASE_CREDENTIALS is not set in the environment")

firebase_credentials = json.loads(firebase_credentials)  # Convert string to JSON
# Initialize Firebase
cred = credentials.Certificate(firebase_credentials)
firebase_admin.initialize_app(cred, {
    'databaseURL': os.getenv("FIREBASE_DATABASE_URL")
})

# Initialize Firestore & Realtime Database
firestore_db = firestore.client()
rtdb = db.reference("/")
