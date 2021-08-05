import binascii
import json
import time
from base64 import b64decode
from sqlalchemy.exc import DBAPIError

import validators
from flask import Blueprint, request, jsonify
from geopy import distance
from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound
from .annotations import db_session_dec
from api.db.dbStructure import Project
from api.db.dbStructure import Summary
from api.db.dbStructure import Problem
from api.db.dbStructure import Solution
from api.db.dbStructure import Image



BP = Blueprint('projects', __name__, url_prefix='/api/projects')

@BP.route('', methods=['GET'])
@db_session_dec
def projects_get(session):
    results = session.query(Project)
    sumRes = session.query(Summary)
    imageRes = session.query(Image)
    probRes = session.query(Problem)
    solRes = session.query(Solution)
    sumImage = ""
    probImage = ""
    solImage = ""
    image = ""

    json_data = []
    for result in results:

        try:
            if result.idImage:
                image = imageRes.filter(Image.idImage == result.idImage).one()
            else:
                return jsonify({'error':'missing argument in Image'}), 400
        except NoResultFound:
            return jsonify({'error': 'Image not found'}), 404

        try:
            if result.idSolution:
                solImage = solRes.filter(Solution.idSolution == result.idSolution).one()
            else:
                return jsonify({'error':'missing argument in Image'}), 400
        except NoResultFound:
            return jsonify({'error': 'Image not found'}), 404
        
        try:
            if result.idSolution:
                sumImage = sumRes.filter(Summary.idSummary == result.idSummary).one()
            else:
                return jsonify({'error':'missing argument in Image'}), 400
        except NoResultFound:
            return jsonify({'error': 'Image not found'}), 404

        try:
            if result.idSolution:
                probImage = probRes.filter(Problem.idProblem == result.idProblem).one()
            else:
                return jsonify({'error':'missing argument in Image'}), 400
        except NoResultFound:
            return jsonify({'error': 'Image not found'}), 404

        json_data.append({
            'id':result.idProject,
            'idNGO':result.idNGO,
            'bild':image.fileImage,
            'beschreibung':result.shortDescription,
            'descSolution':solImage.descriptionSolution,
            'descSummary':sumImage.descriptionSummary,
            'descProblem':probImage.descriptionProblem,
            'name':result.nameProject,
            'status':result.statusProject,
            'istBetrag':result.amountProject,
            'sollBetrag':result.shouldAmountProject,
            'paymentInformation':result.paymentInformationProject,
            'page':result.pageProject
        })
    return jsonify(json_data)    


@BP.route('/<id>', methods=['GET'])
@db_session_dec
def project_by_id_get(session, id):
 
    id_project = id
    imageRes = session.query(Image)
    try:
        if id_project:
            int(id_project)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400

    results = session.query(Project)

    try:
        if id_project:
            results = results.filter(Project.idProject == id_project).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Projekt not found'}), 404

    try:
        if results.idImage:
            imageRes = imageRes.filter(Image.idImage == results.idImage).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Projekt not found'}), 404


    json_data = {
        'id':results.idProject,
        'idNGO':results.idNGO,
        'bild':imageRes.fileImage,
        'beschreibung':results.shortDescription,
        'descSolution':results.idSolution,
        'descSummary':results.idSummary,
        'descProblem':results.idProblem,
        'name':results.nameProject,
        'status':results.statusProject,
        'istBetrag':results.amountProject,
        'sollBetrag':results.shouldAmountProject,
        'paymentInformation':results.paymentInformationProject,
        'page':results.pageProject
    }
        
    return jsonify(json_data), 200

@BP.route('/descriptions/<id>', methods=['GET'])
@db_session_dec
def description_by_project_id_get(session, id):
    id_project = id

    try:
        if id_project:
            int(id_project)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400

    results = session.query(Project)
    sumRes = session.query(Summary)
    imageRes = session.query(Image)
    probRes = session.query(Problem)
    solRes = session.query(Solution)
    sumImage = ""
    probImage = ""
    solImage = ""

    try:
        if id_project:
            results = results.filter(Project.idProject == id_project).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Projekt not found'}), 404


    try:
        if results.idImage:
            sumImage = imageRes.filter(Image.idImage == results.idSummary).one()
            probImage = imageRes.filter(Image.idImage == results.idProblem).one()
            solImage = imageRes.filter(Image.idImage == results.idSolution).one()
        else:
            return jsonify({'error':'missing argument in Image'}), 400
    except NoResultFound:
        return jsonify({'error': 'Image not found'}), 404


    try:
        if results.idSummary:
            sumRes = sumRes.filter(Summary.idSummary == results.idSummary).one()
        else:
            return jsonify({'error':'missing argument in Summary'}), 400
    except NoResultFound:
        return jsonify({'error': 'Summary not found'}), 404

    try:
        if results.idProblem:
            probRes = probRes.filter(Problem.idProblem == results.idProblem).one()
        else:
            return jsonify({'error':'missing argument in Problem'}), 400
    except NoResultFound:
        return jsonify({'error': 'Problem not found'}), 404
    
    try:
        if results.idSolution:
            solRes = solRes.filter(Solution.idSolution == results.idSolution).one()
        else:
            return jsonify({'error':'missing argument in Solution'}), 400
    except NoResultFound:
        return jsonify({'error': 'Solution not found'}), 404




    json_data = {
        'summary':sumRes.descriptionSummary,
        'problems':probRes.descriptionProblem,
        'solution':solRes.descriptionSolution,
        'imageSum':sumImage.fileImage,
        'imageProb':probImage.fileImage,
        'imageSol':solImage.fileImage
    }

    return jsonify(json_data), 200

'''
@BP.route('/descriptions/<id>', methods=['GET'])
@db_session_dec
def project_by_id_get(session, id):
    id_project = id

    try:
        if id_project:
            int(id_project)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400

    results = session.query(Project)
    sumRes = session.query(Summary)
    probRes = session.querry(Problem)
    solRes = session.querry(Solution)

    try:
        if id_project:
            results = results.filter(Project.idProject == id_project).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Projekt not found'}), 404

    try:
        if results.idSummary:
            sumRes = sumRes.filter(Summary.idSummary == results.idSummary).one()
        else:
            return jsonify({'error':'missing argument in Summary'}), 400
    except NoResultFound:
        return jsonify({'error': 'Summary not found'}), 404

    try:
        if results.idProblem:
            probRes = probRes.filter(Problem.idProblem == results.idProblem).one()
        else:
            return jsonify({'error':'missing argument in Problem'}), 400
    except NoResultFound:
        return jsonify({'error': 'Problem not found'}), 404
    
    try:
        if results.idSolution:
            solRes = solRes.filter(Solution.idSolution == results.idSolution).one()
        else:
            return jsonify({'error':'missing argument in Solution'}), 400
    except NoResultFound:
        return jsonify({'error': 'Solution not found'}), 404

    json_data = {
        'summary':sumRes.descriptionSummary,
        'problems':probRes.descriptionProblem,
        'solution':solRes.descriptionSolution,
        'idImageSum':sumRes.idImage,
        'idImageProb':probRes.idImage,
        'idImageSol':solRes.idImage
    }

    return jsonify(json_data), 200
'''

@BP.route('', methods=['POST'])
@db_session_dec
def projekt_post(session):
    name = request.headers.get('nameProject', default=None)
    ngo = request.headers.get('idNGO', default=None)
    image = request.headers.get('idImage', default=None)
    status = request.headers.get('statusProject', default=None)
    actualSum = request.headers.get('amountProject', default=None)
    shouldSum = request.headers.get('shouldAmountProject', default=None)
    paymentInformation = request.headers.get('paymentInformationProject', default=None)
    page = request.headers.get('pageProject', default=None)
    sumID = request.headers.get('idSummary', default=None)
    probID = request.headers.get('idProblem', default=None)
    solID = request.headers.get('idSolution', default=None)
    shortDesc = request.headers.get('shortDescription', default=None)

    if None in [name, status, actualSum, shouldSum, paymentInformation, shortDesc ,page]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [name, status, actualSum, shouldSum, paymentInformation, page]:
        return jsonify({'error': "Empty parameter"}), 400

    """acc = WEB3.eth.account.create()"""
    try:
        projekt_inst = Project(nameProject=name,
                            idImage = image,
                            statusProject = status,
                            amountProject = actualSum,
                            shouldAmountProject = shouldSum,
                            paymentInformationProject = paymentInformation,
                            shortDescription = shortDesc,
                            pageProject = page,
                            idSolution = solID,
                            idSummary = sumID,
                            idProblem = probID,
                            idNGO = ngo
                           )
    except (KeyError, ValueError, DecodeError):  # jwt decode errors
        return jsonify({'status': 'Invalid JWT'}), 400



    session.add(projekt_inst)
    session.commit()
    return jsonify({'status': 'Project POST erfolgreich'}), 201


@BP.route('/<id>', methods=['PUT'])
@db_session_dec
def Project_put(session, id):
    project_id = id

    try:
        if project_id:
            int(project_id)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400
    results = session.query(Project)
    try:
        old = results.filter(Project.idProject == project_id).one()
    except NoResultFound:
        return jsonify({'error': 'Projekt not found'}), 404

    ngo = request.args.get('idNGO', default=old.idNGO)
    image = request.args.get('idImage', default=old.idImage)
    shortDesc = request.args.get('shortDescription ', default=old.shortDescription )
    solution = request.args.get('idSolution', default=old.idSolution)
    summary = request.args.get('idSummary', default=old.idSummary)
    problem = request.args.get('idProblem', default=old.idProblem)
    name = request.args.get('nameProject', default=old.nameProject)
    status = request.args.get('statusProject', default=old.statusProject)
    amount = request.args.get('amountProject', default=old.amountProject)
    souldAmaunt = request.args.get('shouldAmountProject', default=old.shouldAmountProject)
    payment = request.args.get('paymentInformationProject', default=old.paymentInformationProject)
    page = request.args.get('pageProject', default=old.pageProject)

    print(f"args : {request.args}")
    print(f"form : {request.form}")
    print(f"data : {request.data}")
    print(f"headers : {request.headers}")

    try:
        if project_id:
            results.filter(Project.idProject == project_id).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'NGO not found'}), 404

    
    if None in [solution, summary, problem, image, shortDesc, name, status, amount, souldAmaunt, payment, page]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [solution, summary, problem, image, name, status, amount, souldAmaunt, payment, page]:
        return jsonify({'error': "Empty parameter"}), 400 #IF-Anweisung Fehlerhaft wird nach Refactor geändert
        

    try:
        result = results.filter(Project.idProject == project_id).update({'idNGO' : ngo, 'idImage' : image, 'shortDescription' : shortDesc, 'idSolution' : solution, 'idSummary' : summary,
     'idProblem' : problem, 'nameProject' : name, 'statusProject' : status, 'amountProject' : amount, 'shouldAmountProject' : souldAmaunt, 'paymentInformationProject' : payment, 'pageProject' : page})
    except Exception as msg:
        return jsonify({'error': repr(msg)}), 400
    session.commit()
    return jsonify({'status': 'changed'}), 200