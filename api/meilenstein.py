"""User Resource."""
import re
import validators
from flask import Blueprint, request, jsonify
from sqlalchemy import func
from backend.db.dbStructure.py import Meilenstein


BP = Blueprint('meilenstein', __name__, url_prefix='/api/meilenstein')

@BP.route('', methods=['GET'])
@db_session_doc
def meilenstein_get(session):
    args = request.args
    id_meilenstein = args.get('meilenstein_id')

    results = session.query(Meilenstein)

    if id_meilenstein:
        results = results.filter(Meilenstein.meilenstein_id.contains(id_meilenstein))
    else:
        return jsonify({'error':'missing argument'}), 400

    json_data = []

    for result in results:
        json_data.append({
            'id':result.Meilenstein_ID,
            'name':result.Meilenstein_Name,
            'amount':result.Meilenstein_Betrag,
            'description':result.Meilenstein_Beschreibung
        })
        return jsonify(json_data)

@BP.route('/<id>', methods=['GET'])
@db_session_doc
def meilenstein_by_id_get(session, id):
 
    id_meilenstein = id

    try:
        if id_meilenstein:
            int(id_meilenstein)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400

    results = session.query(Meilenstein)

    try:
        if id_meilenstein:
            results = results.filter(Meilenstein.meilenstein_id == id_meilenstein).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Milestone not found'}), 404

    json_data = {
        'id':result.Meilenstein_ID,
        'name':result.Meilenstein_Name,
        'amount':result.Meilenstein_Betrag,
        'description':result.Meilenstein_Beschreibung
    }
        
    return jsonify(json_data), 200

@BP.route('', methods=['PUT'])
def meilenstein_put(meilenstein_inst):
    name = request.headers.get('name', default=None)
    amount = request.headers.get('amount', default=None)
    description = request.headers.get('description', default=None)
    
    if None in [name, amount, description]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [name, amount, description]:
        return jsonify({'error': 'Empty parameter'}), 400
        
    if re.match("^[a-zA-ZäÄöÖüÜ ,.'-]+$", name) is None:
        return jsonify({'error': 'name must contain only alphanumeric characters'}), 400

    meilenstein_inst.Meilenstein_Name = name
    meilenstein_inst.Meilenstein_Betrag = amount
    meilenstein_inst.Meilenstein_Beschreibung = description
    
    return jsonify({'status': 'changed'}), 200


@BP.route('', methods=['POST'])
@db_session_dec
def meilenstein_post(session):
    name = request.headers.get('name', default=None)
    amount = request.headers.get('amount', default=None)
    description = request.headers.get('description', default=None)
    
    if None in [name, amount, description]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [name, amount, description]:
        return jsonify({'error': "Empty parameter"}), 400
        
    if re.match("^[a-zA-ZäÄöÖüÜ ,.'-]+$", name) is None:
        return jsonify({'error': 'name must contain only alphanumeric characters'}), 400

    try:        
        meilenstein_inst = Meilenstein(Meilenstein_Name=name,
                         Meilenstein_Betrag=amount,
                         Meilenstein_Beschreibung=description)
    except (KeyError, ValueError, DecodeError):  # jwt decode errors
        return jsonify({'status': 'Invalid JWT'}), 400

    session.add(meilenstein_inst)
    session.commit()
    return jsonify({'status': 'Milestone registered'}), 201
    