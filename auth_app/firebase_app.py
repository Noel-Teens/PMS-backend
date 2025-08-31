import os
import firebase_admin
from firebase_admin import credentials
from django.conf import settings

def initialize_firebase():
    # Avoid double-initialization in autoreload / multiple workers
    if not firebase_admin._apps:
        cred_path = settings.FIREBASE_CREDENTIALS_FILE
        if not cred_path or not os.path.exists(cred_path):
            raise RuntimeError("FIREBASE_CREDENTIALS_FILE not set or file not found")
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)

# Initialize at import
initialize_firebase()