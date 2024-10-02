from flask import Flask, render_template, redirect, request
from bd import addPatient, getPartientInfo, addDoctor, getDoctorInfo, getspeci, getDoctors
from flask import jsonify , make_response
import datetime
from pailler import CryptHomomr , DecryptHomomr
from phe import paillier
import math

#######################################
############ Génération des clés ######

public_key, private_key = paillier.generate_paillier_keypair()

#######################################

app = Flask(__name__)
current_user = None
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin')
def signin():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/dashboard/<string:user_id>')
def dashboard(user_id):
    d=getDoctors()
    l=[]
    for h in d:
        l.append(h.to_dict())
    print(l)
    dict = {
        'uid': user_id,
        'l': l
    }
    return render_template('dashboard.html', dict=dict)

@app.route('/registerDoctor')
def registerDoctor():
    return render_template('registerDoctor.html')

@app.route('/register_check', methods=["POST"])
def register_check():
    if(request.method == 'POST'):
        global current_user
        req = request.form
        current_user= req['name']
        d = getPartientInfo(req['email'])
        if(d== []):
            data={
                'name': req['name'],
                'age': req['age'],
                'sexe': req['sexe'],
                'bg': req['blood'],
                'email': req['email'],
                'pwd':req['pwd']
            }
            addPatient(data)
            return redirect('/dashboard/'+str(current_user))
    return render_template('register.html', x=0, message="User already registred")

@app.route('/register_checkD', methods=["POST"])
def register_checkD():
    if(request.method == 'POST'):
        global current_user
        req = request.form
        current_user= req['name']
        d = getDoctorInfo(req['email'])
        if(d== []):
            data={
                'name': req['name'],
                'email': req['email'],
                'spec': req['spec'],
                'sexe': req['sexe'],
                'date': datetime.datetime.now().strftime('%A %d-%m-%Y, %H:%M:%S'),
                'pwd':req['pwd']
            }
            addDoctor(data)
            return redirect('/dashboard/'+str(current_user))
    return render_template('register.html', x=0, message="User already registred")

@app.route('/login_check', methods=["POST"])
def login_check():
    if(request.method == 'POST'):
       global current_user
       req = request.form
       d=getPartientInfo(req['email'])
       print(d[0].to_dict())
       if(d == []):
        return render_template('login.html', x=0, message="User not registred")
       elif (d[0].to_dict()['pwd']!= req['pwd']):
        return render_template('login.html', x=0, message="Incorrect password")
       else:
        current_user = d[0].to_dict()['name']
        return redirect('/dashboard/'+str(current_user))

@app.route('/api/spec', methods=['GET'])
def getspec():
    docs=getspeci()
    l=[]
    for doc in docs:
        l.append(doc.to_dict())
    return l


@app.route('/PatientForm/<string:user_id>')
def patient_form(user_id):
    d=getDoctors()
    l=[]
    for h in d:
        l.append(h.to_dict())
    print(l)
    dict = {
        'uid': user_id,
        'l': l
    }
    return render_template('patient_form.html', dict=dict)

@app.route('/resultat_conslt/<string:user_id>')
def resultat_conslt(user_id):
    d=getDoctors()
    l=[]
    for h in d:
        l.append(h.to_dict())
    print(l)
    dict = {
        'uid': user_id,
        'l': l
    }
    return render_template('Resultat.html', dict=dict)


getspec()
if __name__== "__main__":
    app.run(debug=True , port=5000)