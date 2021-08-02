"""User Resource."""
import re
import validators
from flask import Blueprint, request, jsonify
from sqlalchemy import func
from .annotations import db_session_dec
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
from api.db.dbStructure import Payment

BP = Blueprint('payment', __name__, url_prefix='/api/payment')

@BP.route('', methods=['GET'])
@db_session_dec
def payment_get(session):
    results = session.query(Payment)

    json_data = []

    for result in results:
        json_data.append({
            'id':result.idPayment,
            'idUser':result.idUser,
            'amount':result.amountPayment,
            'status':result.statePayment,
            'datetime':result.datePayment,
        })
    return jsonify(json_data)


#Neue Methode die ueber User_Id die Payments bekommt


@BP.route('/<id>', methods=['GET'])
@db_session_dec
def zahlung_by_id_get(session, id):
 
    id_zahlung = id

    try:
        if id_zahlung:
            int(id_zahlung)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400

    results = session.query(Payment)
	
    try:
        if id_zahlung:
            results = results.filter(Payment.idPayment == id_zahlung).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Transaction not found'}), 404

    json_data = {
        'id':results.idPayment,
        'idUser':results.idUser,
        'amount':results.amountPayment,
        'status':results.statePayment,
        'datetime':results.datePayment,
    }
        
    return jsonify(json_data), 200

@BP.route('', methods=['PUT'])
def zahlung_put(zahlung_inst):
    amount = request.headers.get('amountPayment', default=None)
    status = request.headers.get('statePayment', default=None)
    date = request.headers.get('datePayment', default=datetime.now())


    if None in [amount, status, date]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [amount, status, date]:
        return jsonify({'error': 'Empty parameter'}), 400 #IF-Anweisung Fehlerhaft wird nach Refactor geändert

    zahlung_inst.amountPayment = amount
    zahlung_inst.statePayment = status
    zahlung_inst.datePayment = date

    return jsonify({'status': 'changed'}), 200


@BP.route('', methods=['POST'])
@db_session_dec
def zahlung_post(session):
    user = request.headers.get('idUser',default=None)
    project = request.headers.get('idProject', default=None)
    amount = request.headers.get('amountPayment', default=None)
    status = request.headers.get('statePayment', default=None)
    date = request.headers.get('datePayment', default=datetime.now())
    

    if None in [amount, status, date]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [amount, status, date]:
        return jsonify({'error': "Empty parameter"}), 400 #IF-Anweisung Fehlerhaft wird nach Refactor geändert

    try:        
        zahlung_inst = Payment(amountPayment=amount,
                         statePayment=status,
                         datePayment=date,
                         idProject = project,
                         idUser = user)
    except (KeyError, ValueError, DecodeError):  # jwt decode errors
        return jsonify({'status': 'Invalid JWT'}), 400

    session.add(zahlung_inst)
    session.commit()
    return jsonify({'status': 'Payment POST erfolgreich'}), 201
    
