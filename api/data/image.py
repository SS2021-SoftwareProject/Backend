"""User Resource."""
import re
import validators
from flask import Blueprint, request, jsonify
from sqlalchemy import func
from api.db.dbStructure import Image
from .annotations import db_session_dec

BP = Blueprint('image', __name__, url_prefix='/api/image')

@BP.route('', methods=['GET'])
@db_session_dec
def Image_get(session):
    results = session.query(Image)
    json_data = []
    for result in results:
        json_data.append({
            'id':result.idImage,
            'picture':result.fileImage,
            'description':result.descriptionImage,
            'format':result.formatImage
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
    