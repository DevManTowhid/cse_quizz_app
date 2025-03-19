import firebase_admin
from firebase_admin import credentials, firestore, db
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read credentials from environment variable
firebase_credentials = json.loads(os.getenv("FIREBASE_CREDENTIALS"))

# Initialize Firebase
cred = credentials.Certificate(firebase_credentials)
firebase_admin.initialize_app(cred, {
    'databaseURL': os.getenv("FIREBASE_DATABASE_URL")
})

# Initialize Firestore & Realtime Database
firestore_db = firestore.client()
rtdb = db.reference("/")
