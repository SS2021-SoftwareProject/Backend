"""User Resource."""
import re
from sqlalchemy.exc import DBAPIError
import validators
from flask import Blueprint, request, jsonify
from sqlalchemy import func
from api.db.dbStructure import Image
from sqlalchemy.orm.exc import NoResultFound
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

    results = session.query(Image)

    try:
        if id_bild:
            results = results.filter(Image.idImage == id_bild).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Picture not found'}), 404

    json_data = {
        'id':results.idImage,
        'picture':results.fileImage,
        'description':results.descriptionImage,
        'format':results.formatImage
    }
        
    return jsonify(json_data), 200

@BP.route('', methods=['POST'])
@db_session_dec
def image_post(session):
    picture = request.headers.get('fileImage', default=None)
    description = request.headers.get('descriptionImage', default=None)
    format = request.headers.get('formatImage', default=None)
    
    if None in [picture, format]: 
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [picture, format]:
        return jsonify({'error': "Empty parameter"}), 400  #beide If-Anweisungen sind noch Fehlerhaft setzte mich nach refactor dran
    
    try:        
        bild_inst = Image(fileImage=picture,
                         descriptionImage=description,
                         formatImage=format) 
    except (KeyError, ValueError, DecodeError):  # jwt decode errors
        return jsonify({'status': 'Invalid JWT'}), 400

    session.add(bild_inst)
    session.commit()
    return jsonify({'status': 'Bild POST war erfolgreich'}), 201 #hier auf status achten!
    
@BP.route('/<id>', methods=['PUT'])
@db_session_dec
def image_put(session, id):
    image_id = id

    try:
        if image_id:
            int(image_id)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400
    results = session.query(Image)

    
    try:
        old = results.filter(Image.idImage  == image_id).one()
    except NoResultFound:
        return jsonify({'error': 'Image not found'}), 404
    
    
    
    fileimage = request.headers.get('fileImage', default=old.fileImage )
    descriptionimage  = request.headers.get('descriptionImage', default=old.descriptionImage )
    formatimage   = request.headers.get('formatImage', default=old.formatImage )
    
    print(results)
    

    try:
        if image_id:
            results.filter(Image.idImage == image_id).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Image not found'}), 404

    

    
    if None in [fileimage,descriptionimage,formatimage]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [fileimage,descriptionimage,formatimage]:
        return jsonify({'error': 'Empty parameter'}), 400
    try:
        result = results.filter(Image.idImage == image_id).update({'fileImage' : fileimage, 'descriptionImage' : descriptionimage, 'formatImage' : formatimage })
    except Exception as msg:
        return jsonify({'error': repr(msg)}), 400
    session.commit()
    return jsonify({'status': 'changed'}), 200