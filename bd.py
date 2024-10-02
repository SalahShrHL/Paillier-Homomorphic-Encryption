import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
x=0

db= firestore.client()

# Add a new doc in collection 'persons' with an auto generated ID 
def addPatient(data):
    db.collection('Patient').document().set(data)

def addDoctor(data):
    db.collection('Doctor').document().set(data)


def getPartientInfo(data):
    docs = db.collection('Patient').where("email", "==", data).get()
    return docs

def getDoctorInfo(data):
    docs = db.collection('Doctor').where("email", "==", data).get()
    return docs

def getDoctors():
    docs = db.collection('Doctor').get()
    return docs

def addSpec(data):
    db.collection('Spec').document(data).set({'name': data})

def getspeci():
    docs = db.collection('Spec').get()
    return docs
