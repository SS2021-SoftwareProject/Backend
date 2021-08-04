"""User Resource."""
import re
import requests
from requests.sessions import session
from sqlalchemy.exc import DBAPIError
import validators
from flask import Blueprint, request, jsonify
from sqlalchemy import func
from api.db.dbStructure import NGO
from sqlalchemy.orm.exc import NoResultFound
from .annotations import db_session_dec


BP = Blueprint('ngo', __name__, url_prefix='/api/ngo')

@BP.route('', methods=['GET'])
@db_session_dec
def ngo_get(session):
   
    results = session.query(NGO)

    json_data = []

    for result in results:
        """balance = WEB3.eth.getBalance(result.User_Publickey)"""
        json_data.append({
            'id':result.idNGO,
            'name':result.nameNGO,
            'email':result.emailNGO
        })
    return jsonify(json_data)

@BP.route('/<id>', methods=['GET'])
@db_session_dec
def ngo_by_id_get(session, id):
 
    id_ngo = id

    try:
        if id_ngo:
            int(id_ngo)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400

    results = session.query(NGO)
    try:
        if id_ngo:
            results = results.filter(NGO.idNGO == id_ngo).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'NGO not found'}), 404

    json_data = {
        'id':results.idNGO,
        'name':results.nameNGO,
        'email':results.emailNGO
    }
        
    return jsonify(json_data), 200

@BP.route('/<id>', methods=['PUT'])
@db_session_dec
def ngo_put(session, id):
    ngo_id = id

    try:
        if ngo_id:
            int(ngo_id)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400
    results = session.query(NGO)
    
    try:
        old = results.filter(NGO.idNGO == ngo_id).one()
    except NoResultFound:
        return jsonify({'error': 'NGO not found'}), 404

    name = request.headers.get('nameNGO', default=old.nameNGO)
    email = request.headers.get('emailNGO', default=old.emailNGO)

    

    try:
        if ngo_id:
            results.filter(NGO.idNGO == ngo_id).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'NGO not found'}), 404

    

    if email is not None and not validators.email(email):
        return jsonify({'error': 'email is not valid'}), 400

    if None in [email, name]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [email, name]:
        return jsonify({'error': 'Empty parameter'}), 400
        
    if re.match("^[a-zA-ZäÄöÖüÜ ,.'-]+$", name) is None:
        return jsonify({'error': 'name must contain only alphanumeric characters'}), 400
    try:
        result = results.filter(NGO.idNGO == ngo_id).update({'nameNGO' : name, 'emailNGO' : email})
    except Exception as msg:
        return jsonify({'error': repr(msg)}), 400
    
    session.commit()
    return jsonify({'status': 'changed'}), 200

'''
@BP.route('', methods=['PUT'])
def ngo_put(ngo_inst):
    name = request.headers.get('nameNGO', default=None)
    email = request.headers.get('emailNGO', default=None)
    
    if email is not None and not validators.email(email):
        return jsonify({'error': 'email is not valid'}), 400

    if None in [email, name]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [email, name]:
        return jsonify({'error': 'Empty parameter'}), 400
        
    if re.match("^[a-zA-ZäÄöÖüÜ ,.'-]+$", name) is None:
        return jsonify({'error': 'name must contain only alphanumeric characters'}), 400

    ngo_inst.nameNGO = name
    ngo_inst.emailNGO = email
    
    return jsonify({'status': 'changed'}), 200
'''


@BP.route('', methods=['POST'])
@db_session_dec
def ngo_post(session):
    name = request.headers.get('nameNGO', default=None)
    email = request.headers.get('emailNGO', default=None)
    
    if email is not None and not validators.email(email):
        return jsonify({'error': 'email is not valid'}), 400
        
    if None in [name, email]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [name, email]:
        return jsonify({'error': "Empty parameter"}), 400
        
    if re.match("^[a-zA-ZäÄöÖüÜ ,.'-]+$", name) is None:
        return jsonify({'error': 'name must contain only alphanumeric characters'}), 400

    try:        
        ngo_inst = NGO(nameNGO=name,
                         emailNGO=email)
    except (KeyError, ValueError, DecodeError):  # jwt decode errors
        return jsonify({'status': 'Invalid JWT'}), 400

    session.add(ngo_inst)
    session.commit()
    return jsonify({'status': 'NGO POST erfogreich'}), 201
    
