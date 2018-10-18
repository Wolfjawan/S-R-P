from flask import Flask
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
from flask_cors import CORS, cross_origin
from flask_api import status
from flask import request, jsonify
from model.user import Users
from app import app, db
import atexit
import sys
import json
store={"speed":100}
user_status = False

#from sqlalchemy.ext.declarative import declarative_base

#Base = declarative_base()

from sqlalchemy import create_engine, Column, Integer, String
# db_string="postgres://test:test@localhost:5432/test"
# db = create_engine(db_string, echo=True)

#app = Flask(__name__)
CORS(app)

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
myMotor1 = mh.getMotor(1)
myMotor2 = mh.getMotor(2)
myMotor3 = mh.getMotor(3)
myMotor4 = mh.getMotor(4)

# hey 
def turnOffMotors():
    print("stop")
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
    
atexit.register(turnOffMotors)

from controlers import *

def increase_speed():
    print(store["speed"])
    store["speed"]=store["speed"]+10
    
  
def m1goForward():
    print("moto1")  
    myMotor1.run(Adafruit_MotorHAT.FORWARD)
    myMotor1.setSpeed(store["speed"])
    print(store["speed"])
    


@app.route("/")
def hello():
    return "Hello World!"
    
@app.route('/save',methods=['post'])
def save():
    if request.method == "POST":
        req_data = request.get_json()
        name = req_data['name']
        if name == 4:
            m1goForward()
            return "moto1"
        if name == 6:
            turnOffMotors()
            return "stop"
        if name == 10:
            increase_speed()
            return "speed"
        if name == 20:
            # db.execute("INSERT INTO admins (name, password) values ('mohsen','11111')")
            user_1 = User('Mohsen3', 'mohmon@gmail.com')
            db.session.add(user_1)
            db.session.commit()
            return "cool"


        

@app.route('/login',methods=['post'])
def login():
    if request.method == "POST":
        req_data = request.get_json()
        name = req_data['user_name']
        password = req_data['password']
        
        #if user["user_name"]==user_name and user["password"]==password:
            #user_status = True
            #print(user_status)
            #return "true"
        
        content = "user name or password are wrong"
        return content, status.HTTP_404_NOT_FOUND




@app.route('/check_api',methods=['post'])
def check_api():
    if request.method == "POST":
        return "true"
    
    

@app.route('/get-users',methods=['get'])
def get_users():
    users = db.session.query(Users)
    users_json = []
    for user in users:
        single_user_json = {
            'name': user.name,
        }
        users_json.append(single_user_json)
        
    return jsonify(users_json)
     
#FLASK_APP=server.py FLASK_ENV=development flask run --host=0.0.0.0 --port=8000
