"""User Resource."""
import re
import validators
from flask import Blueprint, request, jsonify
from sqlalchemy import func
from db.dbStructure import User
from .annotations import db_session_dec,auth_user


BP = Blueprint('user', __name__, url_prefix='/api/users')

@BP.route('', methods=['GET'])
@db_session_dec
def users_get(session):
    args = request.args
    id_user = args.get('user_id')

    results = session.query(User)

    if id_user:
        results = results.filter(User.user_id.contains(id_user))
    else:
        return jsonify({'error':'missing argument'}), 400

    json_data = []

    for result in results:
        """balance = WEB3.eth.getBalance(result.User_Publickey)"""
        json_data.append({
            'id':result.User_ID,
            'firstname':result.User_Vorname,
            'lastname':result.User_Nachname,
            'email':result.User_Email,
            'PasswordToken':result.User_PasswordToken,
            'Publickey':result.User_Publickey,
            'Privatekey':result.User_Privatkey,
            'RegisterDate':result.User_RegistriertAm
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

@BP.route('', methods=['PUT'])
@auth_user
def user_put(user_inst):
    firstname = request.headers.get('firstname', default=None)
    lastname = request.headers.get('lastname', default=None)
    email = request.headers.get('email', default=None)

    if email is not None and not validators.email(email):
        return jsonify({'error': 'email is not valid'}), 400

    if None in [firstname, lastname, email]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [firstname, lastname, email]:
        return jsonify({'error': 'Empty parameter'}), 400

    if re.match("^[a-zA-ZäÄöÖüÜ ,.'-]+$", firstname) is None or re.match("^[a-zA-ZäÄöÖüÜ ,.'-]+$", lastname) is None:
        return jsonify({'error': 'Firstname and/or lastname must contain only alphanumeric characters'}), 400

    user_inst.User_Vorname = firstname
    user_inst.User_Nachname = lastname
    user_inst.User_Email = email

    return jsonify({'status': 'changed'}), 200


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
