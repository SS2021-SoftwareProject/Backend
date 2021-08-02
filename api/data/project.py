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
from api.db.dbStructure import Summary
from api.db.dbStructure import Problem
from api.db.dbStructure import Solution
from api.db.dbStructure import Image



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
            'descSolution':result.idSolution,
            'descSummary':result.idSummary,
            'descProblem':result.idProblem,
            'name':result.nameProject,
            'status':result.statusProject,
            'amount':result.amountProject,
            'shouldAmount':result.shouldAmountProject,
            'paymentInformation':result.paymentInformationProject,
            'page':result.pageProject
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
            results = results.filter(Project.idProject == id_project).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Projekt not found'}), 404

    json_data = {
        'id':results.idProject,
        'idNGO':results.idNGO,
        'idImage':results.idImage,
        'descSolution':results.idSolution,
        'descSummary':results.idSummary,
        'descProblem':results.idProblem,
        'name':results.nameProject,
        'status':results.statusProject,
        'amount':results.amountProject,
        'shouldAmount':results.shouldAmountProject,
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
    probRes = session.querry(Problem)
    solRes = session.querry(Solution)
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
        'imageSumFormat':sumImage.formatImage,
        'imageProb':probImage.fileImage,
        'imageProbFormat':probImage.formatImage,
        'imageSol':solImage.fileImage,
        'imageSolFormat':solImage.formatImage
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
    ngo = request.headers.get('idImage', default=None)
    image = request.headers.get('idImage', default=None)
    status = request.headers.get('statusProject', default=None)
    actualSum = request.headers.get('amountProject', default=None)
    shouldSum = request.headers.get('shouldAmountProject', default=None)
    paymentInformation = request.headers.get('paymentInformationProject', default=None)
    page = request.headers.get('pageProject', default=None)
    sumID = request.headers.get('idSummary', default=None)
    probID = request.headers.get('idProblem', default=None)
    solID = request.headers.get('idSolution', default=None)


    if None in [name, status, actualSum, shouldSum, paymentInformation, page]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [name, status, actualSum, shouldSum, paymentInformation, page]:
        return jsonify({'error': "Empty parameter"}), 400

    """acc = WEB3.eth.account.create()"""
    try:
        projekt_inst = Project(nameProject=name,
                            statusProject = status,
                            amountProject = actualSum,
                            shouldAmountProject = shouldSum,
                            paymentInformationProject = paymentInformation,
                            pageProject = page,
                            idSolution = solID,
                            idSummary = sumID,
                            idProblem = probID,
                            idNGO = ngo,
                            idImage = image
                           )
    except (KeyError, ValueError, DecodeError):  # jwt decode errors
        return jsonify({'status': 'Invalid JWT'}), 400



    session.add(projekt_inst)
    session.commit()
    return jsonify({'status': 'Project POST erfolgreich'}), 201
