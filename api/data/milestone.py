"""User Resource."""
import re
import validators
from flask import Blueprint, request, jsonify
from sqlalchemy import func
from api.db.dbStructure import Milestone
from .annotations import db_session_dec

BP = Blueprint('milestone', __name__, url_prefix='/api/milestone')

@BP.route('', methods=['GET'])
@db_session_dec
def meilenstein_get(session):
    results = session.query(Milestone)
    json_data = []

    for result in results:
        json_data.append({
            'id':result.idMilestone,
            'name':result.nameMilestone,
            'amount':result.amountMilestone,
            'description':result.descriptionMilestone,
            'idImage':result.idImage,
            'idProject':result.idProject
        })
    return jsonify(json_data)

@BP.route('/<id>', methods=['GET'])
@db_session_dec
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
    