from app import app, db
from flask_api import status
from flask import request, jsonify
import atexit
import sys
import json
from sqlalchemy import create_engine, Column, Integer, String
from model.user import Users
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
from controlers.save_users import *
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
    return "<div style='display: flex;flex-wrap: wrap;justify-content: space-around;'><span style='text-align: center;margin-top: 50px; width: 80%;border: 2px solid #a75353;height: fit-content;padding: 40px;background-color: #c7c2c2;box-shadow: 2px 5px 10px rgba(0,0,0,.25);border-radius: 10px;font-weight: bold;font-size: 50px;'>HELLO THERE, WELCOME TO MY PYTHON SERVER</span><span style='width: 80%;margin-top: 50px; display: flex;flex-wrap: wrap;justify-content: space-around;'><img style='text-align: center;width: fit-content;border: 2px solid #a75353;height: fit-content;background-color: #c7c2c2;box-shadow: 2px 5px 10px rgba(0,0,0,.25);border-radius: 50%;' src='https://avatars3.githubusercontent.com/u/30389896?s=400&u=ca31770f8782515d9a6c4749848796e649f0635e&v=4'/></span></div>"


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


@app.route('/get-users',methods=['get'])
def get_users():
    users = db.session.query(Users).all()
    # print(users)
    users_json = []
    for user in users:
        print(user)
        single_user_json = {
            'id': user.id,
            'email':user.email,
            'name': user.name,
            'password':user.password
        }
        users_json.append(single_user_json)
    return jsonify(users_json)
# @app.route('/get-users',methods=['get'])
# def get_users():
#     users = db.session.query(Users).all()
#     print(users.get_json())
#     return jsonify(users:users)