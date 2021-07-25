"""User Resource."""
import re
import validators
from flask import Blueprint, request, jsonify
from sqlalchemy import func
from db.dbStructure import Milestone
from .annotations import db_session_dec

BP = Blueprint('bild', __name__, url_prefix='/api/bild')

@BP.route('', methods=['GET'])
@db_session_dec
def bild_get(session):
    args = request.args
    id_bild = args.get('bild_id')

    results = session.query(Bild)

    if id_bild:
        results = results.filter(Bild.bild_id.contains(id_bild))
    else:
        return jsonify({'error':'missing argument'}), 400

    json_data = []

    for result in results:
        json_data.append({
            'id':result.Bild_ID,
            'picture':result.Bild_Bild,
            'description':result.Bild_Beschreibung,
            'format':result.Bild_Format
        })
    return jsonify(json_data)

@BP.route('/<id>', methods=['GET'])
@db_session_dec
def bild_by_id_get(session, id):
 
    id_bild = id

    try:
        if id_bild:
            int(id_bild)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400

    results = session.query(Bild)

    try:
        if id_bild:
            results = results.filter(Bild.bild_id == id_bild).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Picture not found'}), 404

    json_data = {
        'id':result.Bild_ID,
        'picture':result.Bild_Bild,
        'description':result.Bild_Beschreibung,
        'format':result.Bild_Format
    }
        
    return jsonify(json_data), 200

@BP.route('', methods=['PUT'])
def bild_put(bild_inst):
    picture = request.headers.get('picture', default=None)
    description = request.headers.get('description', default=None)
    format = request.headers.get('format', default=None)
    
    if None in [picture, description, format]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [picture, description, format]:
        return jsonify({'error': 'Empty parameter'}), 400

    bild_inst.Bild_Bild = picture
    bild_inst.Bild_Beschreibung = description
    bild_inst.Bild_Format = format
    
    return jsonify({'status': 'changed'}), 200


@BP.route('', methods=['POST'])
@db_session_dec
def meilenstein_post(session):
    picture = request.headers.get('picture', default=None)
    description = request.headers.get('description', default=None)
    format = request.headers.get('format', default=None)
    
    if None in [picture, description, format]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [picture, description, format]:
        return jsonify({'error': "Empty parameter"}), 400
        
    try:        
        bild_inst = Bild(Bild_Bild=picture,
                         Bild_Beschreibung=description,
                         Bild_Format=format)
    except (KeyError, ValueError, DecodeError):  # jwt decode errors
        return jsonify({'status': 'Invalid JWT'}), 400

    session.add(bild_inst)
    session.commit()
    return jsonify({'status': 'Picture registered'}), 201
    