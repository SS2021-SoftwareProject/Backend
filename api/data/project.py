import binascii
import json
import time
from base64 import b64decode

import validators
from flask import Blueprint, request, jsonify
from geopy import distance
from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound
from .annotations import db_session_dec
from api.db.dbStructure import Project


BP = Blueprint('projects', __name__, url_prefix='/api/projects')

@BP.route('', methods=['GET'])
@db_session_dec
def projects_get(session):
    results = session.query(Project)

    json_data = []

    for result in results:
        json_data.append({
            'id':result.idProject,
            'idNGO':result.idNGO,
            'idImage':result.idImage,
            'name':result.nameProject,
            'description':result.descriptionProject,
            'status':result.statusProject,
            'amount':result.amountProject,
            'shouldAmount':result.shouldAmountProject,
            'paymentInformation':result.paymentInformationProject,
            'page':result.pageProject,
            'shortDescription':result.shortdescriptionProject
        })
    return jsonify(json_data)    


@BP.route('/<id>', methods=['GET'])
@db_session_dec
def project_by_id_get(session, id):
 
    id_project = id

    try:
        if id_project:
            int(id_project)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400

    results = session.query(Project)

    try:
        if id_project:
            results = results.filter(Project.Projekt_ID == id_project).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Projekt not found'}), 404

    json_data = {
        'id':result.Projekt_ID,
        'name':result.Projekt_Name,
        'description':result.Projekt_Beschreibung,
        'status':result.Projekt_Status,
        'actualSum':result.Projekt_IstBetrag,
        'shouldSum':result.Projekt_SollBetrag,
        'paymentInformation':result.Projekt_Zahlungsinformation,
        'page':result.Projekt_Page,
        'shortDescription':result.Projekt_Kurzbeschreibung
    }
        
    return jsonify(json_data), 200

@BP.route('', methods=['POST'])
@db_session_dec
def projekt_post(session):
    name = request.headers.get('name', default=None)
    description = request.headers.get('description', default=None)
    status = request.headers.get('status', default=None)
    actualSum = request.headers.get('actualSum', default=None)
    shouldSum = request.headers.get('shouldSum', default=None)
    paymentInformation = request.headers.get('paymentInformation', default=None)
    page = request.headers.get('page', default=None)
    shortDescription = request.headers.get('shortDescription', default=None)



    if None in [name, description, status, actualSum, shouldSum, paymentInformation, page, shortDescription]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [name, description, status, actualSum, shouldSum, paymentInformation, page, shortDescription]:
        return jsonify({'error': "Empty parameter"}), 400

    """acc = WEB3.eth.account.create()"""

    projekt_inst = Project(Projekt_Name=name,
                            Projekt_Description = description,
                            Projekt_status = status,
                            Projekt_istBetrag = actualSum,
                            Projekt_sollBetrag = shouldSum,
                            Projekt_Zahlungsinformation = paymentInformation,
                            Projekt_Page = page,
                            Projekt_Kurzbeschreibung = shortDescription
                           )
        


    session.add(project_inst)
    session.commit()
    return jsonify({'status': 'Project registered'}), 201
