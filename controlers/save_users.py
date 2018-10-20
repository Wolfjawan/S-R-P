from model.user import Users
from app import app, db
from flask import request, jsonify

@app.route('/save-data',methods=['post'])
def save_data():
    print(request.method)
    if request.method == 'POST':
        req_data = request.get_json()
        name = req_data['user_name']
        password = req_data['password']
        email = req_data['email']
        user = Users(name, email, password)
        db.session.add(user)
        db.session.commit()
        print(user)
        return "cool"