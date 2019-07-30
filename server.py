from flask import Flask
from flask_cors import CORS, cross_origin
from flask_api import status
from flask import request, jsonify
import atexit
import sys
import json
from sqlalchemy import create_engine, Column, Integer, String

from model.user import Users
from app import app, db
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
from controlers.save_users import *

CORS(app)
variables={
    "m1speed":0,
    "m2speed":0,
    "runMotors1":False,
    "runMotors2":False,
    "runMotors3":False,
    "runMotors4":False,
    }
user_status = False

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

def turnOffM2():
    print("turnOffM2")
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)


def m1goForward():
    print("m1 Forward")
    myMotor1.run(Adafruit_MotorHAT.FORWARD)
    myMotor1.setSpeed(variables["m1speed"])

def m1goBackward():
    print("m1 Backward")
    myMotor1.run(Adafruit_MotorHAT.BACKWARD)
    myMotor1.setSpeed(variables["m1speed"])

def m2goForward():
    print("m2 Forward")
    myMotor2.run(Adafruit_MotorHAT.FORWARD)
    myMotor2.setSpeed(variables["m2speed"])

def m2goBackward():
    print("m2 Backward")
    myMotor2.run(Adafruit_MotorHAT.BACKWARD)
    myMotor2.setSpeed(variables["m2speed"])

@app.route('/move-control',methods=['post'])
def moveControl():
    if request.method == "POST":
        req_data = request.get_json()
#move control
        if req_data['moveType']:
            if req_data['moveType'] == 'forward':
                variables["m1speed"]=req_data['speed']
                m1goForward()
            if req_data['moveType'] == 'backward':
                variables["m1speed"]=req_data['speed']
                m1goBackward()
            if req_data['moveType'] == 'stop':
                variables["m1speed"]=req_data['speed']
                turnOffMotors()

# tern control
            if req_data['ternType'] == 'ternLeft':
                m2goForward()
                variables["m2speed"]=req_data['ternSpeed']
            if req_data['ternType'] == 'ternRight':
                m2goBackward()
                variables["m2speed"]=req_data['ternSpeed']
            if req_data['ternType'] == 'turnOffM2':
                variables["m2speed"]=req_data['ternSpeed']
                turnOffM2()
        return ""





@app.route("/")
def hello():
    return "Hello there this is mohsen's python server"


# @app.route('/login',methods=['post'])
# def login():
#     if request.method == "POST":
#         req_data = request.get_json()
#         name = req_data['user_name']
#         password = req_data['password']

#         #if user["user_name"]==user_name and user["password"]==password:
#             #user_status = True
#             #print(user_status)
#             #return "true"

#         content = "user name or password are wrong"
#         return content, status.HTTP_404_NOT_FOUND




# @app.route('/check_api',methods=['post'])
# def check_api():
#     if request.method == "POST":
#         return "true"



# @app.route('/get-users',methods=['get'])
# def get_users():
#     users = db.session.query(Users).all()
#     users_json = []
#     for user in users:
#         single_user_json = {
#             'id': user.id,
#             'name': user.name,
#             'email':user.email,
#             'password':user.password
#         }
#         users_json.append(single_user_json)

#     return jsonify(users_json)
