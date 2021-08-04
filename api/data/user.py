"""User Resource."""

import re
import validators
from flask.app import Flask
from flask import Blueprint, request, jsonify
from sqlalchemy import func
from api.db.dbStructure import User
from api.db.dbStructure import Payment
from .annotations import db_session_dec,auth_user
from sqlalchemy.orm.exc import NoResultFound
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
#from api.contracts.web3 import WEB3

BP = Blueprint('user', __name__, url_prefix='/api/users')

@BP.route('', methods=['GET'])
@db_session_dec
def users_get(session):
    results = session.query(User)
    json_data = []
    for result in results:
        #balance = WEB3.eth.getBalance(result.publickeyUser)
        json_data.append({
            'id':result.idUser,
            'firstname':result.firstNameUser,
            'lastname':result.lastNameUser,
            'email':result.emailUser,
            'PasswordToken':result.passwordtokenUser,
            'Publickey':result.publickeyUser,
            'Privatekey':result.privatkeyUser,
            'RegisterDate':result.registryAtUser,
            #'balance':balance
        })
    return jsonify(json_data)

@BP.route('/<id>', methods=['GET'])
@db_session_dec
def user_by_id_get(session, id):
    id_user = id
    try:
        if id_user:
            int(id_user)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400

    results = session.query(User)

    try:
        if id_user:
            results = results.filter(User.idUser == id_user).one()
            """"balance = WEB3.eth.getBalance(results.publickeyUser)"""
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'User not found'}), 404

    json_data = {
        'id':results.idUser,
        'firstname':results.firstNameUser,
        'lastname':results.lastNameUser,
        'email':results.emailUser,
        'PasswordToken':results.passwordtokenUser,
        'Publickey':results.publickeyUser,
        'Privatekey':results.privatkeyUser,
        'RegisterDate':results.registryAtUser,
    }
        
    return jsonify(json_data), 200


@BP.route('contributions/<id>', methods=['GET'])
@db_session_dec
def contributions_by_user_id_get(session, id):
    user_id = id

    try:
        if user_id:
            int(user_id)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400

    results = session.query(Payment)


    try:
        if user_id:
            results = results.filter(Payment.idUser == user_id)
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Transaction not found'}), 404

    json_data = []

    for result in results:
        json_data.append({
            'id':result.idPayment,
            'date':result.datePayment,
            'amount':result.amountPayment,
            'project':result.idProject,
            'state':result.statePayment
        })

    return jsonify(json_data)


@BP.route('/signup', methods=['POST'])
@db_session_dec
@cross_origin()
def signup_post(session):
    email = request.values.get('email')
    password = request.values.get('password')
    firstname = request.values.get('firstname')
    lastname = request.values.get('lastname')
    results = session.query(User)
    user = results.filter(User.emailUser == email).first()
    if None in [firstname, lastname, email, password]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [firstname, lastname, email, password]:
        return jsonify({'error': "Empty parameter"}), 400

    if re.match("^[a-zA-ZäÄöÖüÜ ,.'-]+$", firstname) is None or re.match("^[a-zA-ZäÄöÖüÜ ,.'-]+$", lastname) is None:
        return jsonify({'error': 'Firstname and/or lastname must contain only alphanumeric characters'}), 400

    if user:
        return jsonify({'error': 'Invalid credentials, user already exists'}), 400
    new_user = User(emailUser = email, firstNameUser = firstname, lastNameUser = lastname, passwordtokenUser = password)
    session.add(new_user)
    session.commit()
    new_userJson = {
        'id':new_user.idUser,
        'firstname':new_user.firstNameUser,
        'lastname':new_user.lastNameUser,
        'email':new_user.emailUser,
        'PasswordToken':new_user.passwordtokenUser,
        'Publickey':new_user.publickeyUser,
        'Privatekey':new_user.privatkeyUser,
        'RegisterDate':new_user.registryAtUser
    }
    return jsonify({'success': 'User registered', 'user' : new_userJson}), 200


@BP.route('/login', methods=['POST'])
@db_session_dec
@cross_origin()
def login_post(session):
    email = request.values.get('email')
    password = request.values.get('password')

    results = session.query(User)
    user = results.filter(User.emailUser == email).first()

    if not user or not user.passwordtokenUser == password:
        return jsonify({'error': 'Invalid credentials'}), 403
    userJson = {
        'id':user.idUser,
        'firstname':user.firstNameUser,
        'lastname':user.lastNameUser,
        'email':user.emailUser,
        'PasswordToken':user.passwordtokenUser,
        'Publickey':user.publickeyUser,
        'Privatekey':user.privatkeyUser,
        'RegisterDate':user.registryAtUser
    }
    return jsonify({'success': 'User logged in', 'user' : userJson}), 200
