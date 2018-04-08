import pyrebase
import config

firebase = pyrebase.initialize_app(config.FirebaseConfig().config)
db = firebase.database()


def get():
    return db.child("playlist").get().each()


def pop(name):
    db.child("playlist").child(name).remove()
