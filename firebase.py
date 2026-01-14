import firebase_admin
from firebase_admin import credentials, db
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

cred = credentials.Certificate(
    os.path.join(BASE_DIR, "firebase_key.json")
)

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://campus-guardian-1b2e3-default-rtdb.firebaseio.com"
})

ref = db.reference("/sos_alerts")
