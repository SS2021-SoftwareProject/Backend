"""User Resource."""
import re
import validators
from flask import Blueprint, request, jsonify
from sqlalchemy import func
from api.db.dbStructure import User
from .annotations import db_session_dec,auth_user
from api.contracts.web3 import WEB3

BP = Blueprint('user', __name__, url_prefix='/api/users')

@BP.route('', methods=['GET'])
@db_session_dec
def users_get(session):
    results = session.query(User)
    json_data = []
    for result in results:
        balance = WEB3.eth.getBalance(result.publickeyUser)
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
            results = results.filter(User.user_id == id_user).one()
            """"balance = WEB3.eth.getBalance(results.User_Publickey)"""
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'User not found'}), 404

    json_data = {
        'id':result.User_ID,
        'firstname':result.User_Vorname,
        'lastname':result.User_Nachname,
        'email':result.User_Email,
        'PasswordToken':result.User_PasswordToken,
        'Publickey':result.User_Publickey,
        'Privatekey':result.User_Privatkey,
        'RegisterDate':result.User_RegistriertAm
    }
        
    return jsonify(json_data), 200


@BP.route('', methods=['POST'])
@db_session_dec
def user_post(session):
    firstname = request.headers.get('firstname', default=None)
    lastname = request.headers.get('lastname', default=None)
    email = request.headers.get('email', default=None)
    password_Token = request.headers.get('passwordToken', default=None)

    if None in [firstname, lastname, email, password_Token]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [firstname, lastname, email, password_Token]:
        return jsonify({'error': "Empty parameter"}), 400

    if re.match("^[a-zA-ZäÄöÖüÜ ,.'-]+$", firstname) is None or re.match("^[a-zA-ZäÄöÖüÜ ,.'-]+$", lastname) is None:
        return jsonify({'error': 'Firstname and/or lastname must contain only alphanumeric characters'}), 400

    """acc = WEB3.eth.account.create()"""

    try:
        if password_Token != session.query(User).filter(User.User_passwordToken):
            return jsonify({'error': 'Invalid token.'}), 400
        
        user_inst = User(User_Vorname=firstname,
                         User_Nachname=lastname,
                         User_Email=email)
                         #User_Publickey=acc.address,
                         #User_Privatkey=acc.key)
    except (KeyError, ValueError, DecodeError):  # jwt decode errors
        return jsonify({'status': 'Invalid JWT'}), 400

    session.add(user_inst)
    session.commit()
    return jsonify({'status': 'User registered'}), 201
