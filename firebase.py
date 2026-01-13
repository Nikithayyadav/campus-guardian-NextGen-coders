import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("firebase_key.json")

firebase_admin.initialize_app(cred, {
    "databaseURL": "https://YOUR_DATABASE_URL.firebaseio.com"
})

ref = db.reference("sos_alerts")
