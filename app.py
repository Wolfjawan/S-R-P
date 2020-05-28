from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://test:test@localhost:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# socketio = SocketIO(app)
db = SQLAlchemy(app)
CORS(app)
# @socketio.on('connect')
# def connect():
#     emit('notify', 'Connected')

# @socketio.on('disconnect')
# def disconnect():
#     print('Client disconnected')






# socket io
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)
# if __name__ == '__main__':
#     socketio.run(app)
# https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent/page/0
# https://flask-socketio.readthedocs.io/en/latest/
# end socket io


