from flask import Flask
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
from flask_cors import CORS, cross_origin
from flask_api import status
from flask import request
import atexit
import sys
import json
store={"speed":100}
user_status = False

from sqlalchemy import create_engine
db_string="postgres://test:test@localhost:5432/test"
db = create_engine(db_string)


# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
myMotor1 = mh.getMotor(1)
myMotor2 = mh.getMotor(2)
myMotor3 = mh.getMotor(3)
myMotor4 = mh.getMotor(4)

def turnOffMotors():
    print("stop")
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
    
atexit.register(turnOffMotors)

def increase_speed():
    print(store["speed"])
    store["speed"]=store["speed"]+10
    
  
def m1goForward():
    print("moto1")  
    myMotor1.run(Adafruit_MotorHAT.FORWARD)
    myMotor1.setSpeed(store["speed"])
    print(store["speed"])
    

app = Flask(__name__)
CORS(app)
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
            db.execute("INSERT INTO admins (name, password) values ('mohsen','11111')")
            return "cool"
        
user={
    "user_name":"mohsen",
    "password":"111111"
    }


@app.route('/login',methods=['post'])
def login():
    if request.method == "POST":
        req_data = request.get_json()
        user_name = req_data['user_name']
        password = req_data['password']
        if user["user_name"]==user_name and user["password"]==password:
            user_status = True
            print(user_status)
            return "true"
        
        content = "user name or password are wrong"
        return content, status.HTTP_404_NOT_FOUND

@app.route('/check_api',methods=['post'])
def check_api():
    if request.method == "POST":
        return "true"
