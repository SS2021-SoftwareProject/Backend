"""User Resource."""
import re
import validators
from flask import Blueprint, request, jsonify
from sqlalchemy import func
from api.db.dbStructure import User
from .annotations import db_session_dec,auth_user
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
            'balance':balance
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
        'id':result.idUser,
        'firstname':result.firstNameUser,
        'lastname':result.lastNameUser,
        'email':result.emailUser,
        'PasswordToken':result.passwordtokenUser,
        'Publickey':result.publickeyUser,
        'Privatekey':result.privatkeyUser,
        'RegisterDate':result.registryAtUser
    }
        
    return jsonify(json_data), 200


@BP.route('/signup', methods=['POST'])
@db_session_dec
def signup_post(session):
    email = request.headers.get('email')
    password = request.headers.get('password')
    firstname = request.headers.get('firstname')
    lastname = request.headers.get('lastname')
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
    return jsonify({'success': 'User has been created'}), 200


@BP.route('/login', methods=['POST'])
@db_session_dec
def login_post(session):
    email = request.form.get('email')
    password = request.form.get('password')

    results = session.query(User)
    user = results.filter(emailUser=email).first()
    if not user or not user.passwordtokenUser == password:
        return jsonify({'error': 'Invalid credentials'}), 403
    return jsonify({'success': 'User logged in'}), 200