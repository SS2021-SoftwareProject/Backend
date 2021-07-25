"""User Resource."""
import re
import validators
from flask import Blueprint, request, jsonify
from sqlalchemy import func
from db.dbStructure import Payment
from .annotations import db_session_dec


BP = Blueprint('zahlung', __name__, url_prefix='/api/zahlung')

@BP.route('', methods=['GET'])
@db_session_dec
def zahlung_get(session):
    args = request.args
    id_zahlung = args.get('zahlung_id')

    results = session.query(Zahlung)

    if id_zahlung:
        results = results.filter(Zahlung.zahlung_id.contains(id_zahlung))
    else:
        return jsonify({'error':'missing argument'}), 400

    json_data = []

    for result in results:
        """balance = WEB3.eth.getBalance(result.User_Publickey)"""
        json_data.append({
            'id':result.Zahlung_ID,
            'amount':result.Zahlung_Betrag,
            'status':result.Zahlung_Status,
            'date':result.Zahlung_Datum,
            'time':result.Zahlung_Uhrzeit
        })
        return jsonify(json_data)

@BP.route('/<id>', methods=['GET'])
@db_session_dec
def zahlung_by_id_get(session, id):
 
    id_zahlung = id

    try:
        if id_zahlung:
            int(id_zahlung)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400

    results = session.query(Zahlung)

    try:
        if id_zahlung:
            results = results.filter(Zahlung.zahlung_id == id_zahlung).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Transaction not found'}), 404

    json_data = {
        'id':result.Zahlung_ID,
        'amount':result.Zahlung_Betrag,
        'status':result.Zahlung_Status,
        'date':result.Zahlung_Datum,
        'time':result.Zahlung_Uhrzeit
    }
        
    return jsonify(json_data), 200

@BP.route('', methods=['PUT'])
def zahlung_put(zahlung_inst):
    amount = request.headers.get('amount', default=None)
    status = request.headers.get('status', default=None)
    date = request.headers.get('date', default=None)
    time = request.headers.get('time', default=None)

    if None in [amount, status, date, time]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [amount, status, date, time]:
        return jsonify({'error': 'Empty parameter'}), 400

    zahlung_inst.Zahlung_Betrag = amount
    zahlung_inst.Zahlung_Status = status
    zahlung_inst.Zahlung_Datum = date
    zahlung_inst.Zahlung_Uhrzeit = time

    return jsonify({'status': 'changed'}), 200


@BP.route('', methods=['POST'])
@db_session_dec
def zahlung_post(session):
    amount = request.headers.get('amount', default=None)
    status = request.headers.get('status', default=None)
    date = request.headers.get('date', default=None)
    time = request.headers.get('time', default=None)

    if None in [amount, status, date, time]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [amount, status, date, time]:
        return jsonify({'error': "Empty parameter"}), 400

    try:        
        zahlung_inst = Zahlung(Zahlung_Betrag=amount,
                         Zahlung_Status=status,
                         Zahlung_Datum=date,
                         Zahlung_Uhrzeit=time)
    except (KeyError, ValueError, DecodeError):  # jwt decode errors
        return jsonify({'status': 'Invalid JWT'}), 400

    session.add(zahlung_inst)
    session.commit()
    return jsonify({'status': 'Transaction registered'}), 201
    