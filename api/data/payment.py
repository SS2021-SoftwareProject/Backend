"""User Resource."""
import re
import validators
import requests
from flask import Blueprint, request, jsonify
from sqlalchemy import func
from .annotations import db_session_dec
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
from api.db.dbStructure import User
from api.db.dbStructure import Project

from api.db.dbStructure import Payment
from api.data.contract_calls import project_constructor
from api.data.contract_calls import project_donate
from web3 import Web3

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
            'idProject':result.idProject,
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
        'idProject':results.idProject,
        'idUser':results.idUser,
        'amount':results.amountPayment,
        'status':results.statePayment,
        'datetime':results.datePayment,
    }
        
    return jsonify(json_data), 200


@BP.route('', methods=['POST'])
@db_session_dec
def zahlung_post(session):

    user = request.args.get('idUser', default=None)
    project = request.args.get('idProject', default=None)
    amount = request.args.get('amount', default=None)
    status = request.args.get('status', default="complete")
    date = request.args.get('date', default=datetime.now())

    myUser = session.query(User)
    projects = session.query(Project)

    try:
        if user:
            myUser = myUser.filter(User.idUser == user).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Payment not found'}), 404


    gwei = (int(amount) * 363841)
    wei = (int(gwei) * 1000000000)


    theProject = projects.filter(Project.idProject == project).one()
    project_donate(theProject, myUser, wei)

    # ----------------------------------------------------------------------------------------------------
    # Append to Blockchain
    # ----------------------------------------------------------------------------------------------------
    
    

    try:
        projects.filter(Project.idProject == project).update
    except NoResultFound:
        return jsonify({'error': 'Payment not found'}), 404

    # DONT CHANGE!------------------------------------------------
    #url = 'http://127.0.0.1:6000/new_block'
    #data= {'transaction': project,
    #        'amount' : amount,
    #        'customerID': user}


    #requests.post(url, data = data)
    # DONT CHANGE!------------------------------------------------



    if None in [user, project, amount]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [user, project, amount]:
        return jsonify({'error': "Empty parameter"}), 400 #IF-Anweisung Fehlerhaft wird nach Refactor ge??ndert
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
    
@BP.route('/<id>', methods=['PUT'])
@db_session_dec
def payment_put(session, id):
    payment_id = id

    try:
        if payment_id:
            int(payment_id)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400
    results = session.query(Payment)

    
    try:
        old = results.filter(Payment.idPayment == payment_id).one()
    except NoResultFound:
        return jsonify({'error': 'Payment not found'}), 404
    
    iduser   = request.headers.get('idUser', default=old.idUser)
    idproject = request.headers.get('idProject', default=old.idProject )
    amountpayment= request.headers.get('amountPayment', default=old.amountPayment)
    statepayment= request.headers.get('statePayment', default=old.statePayment)
    datepayment= request.headers.get('datePayment', default=old.datePayment)
    
    
    try:
        if payment_id:
            results.filter(Payment.idPayment == payment_id).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Payment not found'}), 404
    if None in [iduser,idproject, amountpayment,statepayment ,datepayment ]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [iduser,idproject, amountpayment,statepayment ,datepayment]:
        return jsonify({'error': 'Empty parameter'}), 400
    
    try:
        result = results.filter(Payment.idPayment == payment_id).update({'idUser' : iduser , 'idProject' : idproject, 'amountPayment' : amountpayment , 'statePayment' : statepayment, 'datePayment' : datepayment })
    except Exception as msg:
        return jsonify({'error': repr(msg)}), 400
    
    session.commit()
    return jsonify({'status': 'changed'}), 200
