import pyrebase
from Firebase import Firebase
# from firebase_admin import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db

fbconfig = {
    'apiKey': "AIzaSyCG9CEMR4ClQpP_X2dDkm9zOf9f2s6Q_Mk",
    'authDomain': "artini-22c83.firebaseapp.com",
    'databaseURL': "https://artini-22c83.firebaseio.com",
    'projectId': "artini-22c83",
    'storageBucket': "artini-22c83.appspot.com",
    'messagingSenderId': "850015264518",
    'appId': "1:850015264518:web:a0992497b42dec2f320887",
    'measurementId': "G-XE11DK6PDX"
}
messagesRef = Firebase('https://artini-22c83.firebaseio.com/')
firebase = firebase.FirebaseApplication("https://artini-22c83.firebaseio.com/", None)

firebase = pyrebase.initialize_app(fbconfig)
auth = firebase.auth()

ref = db.reference('server/saving-data/fireblog/posts')

cred = credentials.Certificate("/Users/thomaswasynczuk/Documents/GitHub/330/creativeproject-tw/HBaseEnv/.vscode/launch.json.json")
firebase_admin.initialize_app(cred)

# firebase-adminsdk-h1n1b@artini-22c83.iam.gserviceaccount.com

# https://ibb.co/kc3N7ZR
# https://ibb.co/g7CFR2N
# https://ibb.co/fq5bFF1