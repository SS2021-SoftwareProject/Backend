"""User Resource."""
import re
import validators
from flask import Blueprint, request, jsonify
from sqlalchemy import func
from db.dbStructure import NGO
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
            results = results.filter(NGO.ngo_id == id_ngo).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'NGO not found'}), 404

    json_data = {
        'id':result.NGO_ID,
        'name':result.NGO_Name,
        'email':result.NGO_Email
    }
        
    return jsonify(json_data), 200

@BP.route('', methods=['PUT'])
def ngo_put(ngo_inst):
    name = request.headers.get('name', default=None)
    email = request.headers.get('email', default=None)
    
    if email is not None and not validators.email(email):
        return jsonify({'error': 'email is not valid'}), 400

    if None in [name, email]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [name, email]:
        return jsonify({'error': 'Empty parameter'}), 400
        
    if re.match("^[a-zA-ZäÄöÖüÜ ,.'-]+$", name) is None:
        return jsonify({'error': 'name must contain only alphanumeric characters'}), 400

    ngo_inst.NGO_Name = name
    ngo_inst.NGO_Email = email
    
    return jsonify({'status': 'changed'}), 200


@BP.route('', methods=['POST'])
@db_session_dec
def ngo_post(session):
    name = request.headers.get('name', default=None)
    email = request.headers.get('enail', default=None)
    
    if email is not None and not validators.email(email):
        return jsonify({'error': 'email is not valid'}), 400
        
    if None in [name, email]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [name, email]:
        return jsonify({'error': "Empty parameter"}), 400
        
    if re.match("^[a-zA-ZäÄöÖüÜ ,.'-]+$", name) is None:
        return jsonify({'error': 'name must contain only alphanumeric characters'}), 400

    try:        
        ngo_inst = NGO(NGO_Name=name,
                         NGO_Email=email)
    except (KeyError, ValueError, DecodeError):  # jwt decode errors
        return jsonify({'status': 'Invalid JWT'}), 400

    session.add(ngo_inst)
    session.commit()
    return jsonify({'status': 'NGO registered'}), 201
    