"""User Resource."""
import re
import validators
from flask import Blueprint, request, jsonify
from sqlalchemy import func
from api.db.dbStructure import Milestone
from sqlalchemy.orm.exc import NoResultFound
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
            'titel':result.nameMilestone,
            'betrag':result.amountMilestone,
            'beschreibung':result.descriptionMilestone,
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

    results = session.query(Milestone)

    try:
        if id_meilenstein:
            results = results.filter(Milestone.idMilestone == id_meilenstein).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Milestone not found'}), 404

    json_data = {
        'id':results.idMilestone,
        'titel':results.nameMilestone,
        'betrag':results.amountMilestone,
        'beschreibung':results.descriptionMilestone,
        'idImage':results.idImage,
        'idProject':results.idProject
    }
        
    return jsonify(json_data), 200

@BP.route('/byprojectid/<id>', methods=['GET'])
@db_session_dec
def meilenstein_by_project_id_get(session, id):
    project_id = id
    try:
        if project_id:
            int(project_id)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400
    results = session.query(Milestone)
    try:
        if project_id:
            results = results.filter(Milestone.idProject == project_id)
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Milestones not found'}), 404
    
    json_data = []

    for result in results:
        json_data.append({
            'name':result.nameMilestone,
            'amount':result.amountMilestone,
            'description':result.descriptionMilestone
        })

    return jsonify(json_data)

@BP.route('/byprojectidfull/<id>', methods=['GET'])
@db_session_dec
def full_meilenstein_by_project_id_get(session, id):
    project_id = id
    try:
        if project_id:
            int(project_id)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400
    results = session.query(Milestone)
    try:
        if project_id:
            results = results.filter(Milestone.idProject == project_id)
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Milestones not found'}), 404
    
    json_data = []

    for result in results:
        json_data.append({
            'id':result.idMilestone,
            'image':result.idImage,
            'name':result.nameMilestone,
            'amount':result.amountMilestone,
            'description':result.descriptionMilestone
        })

    return jsonify(json_data)

@BP.route('', methods=['POST'])
@db_session_dec
def meilenstein_post(session):
    name = request.headers.get('nameMilestone', default=None)
    amount = request.headers.get('amountMilestone', default=None)
    description = request.headers.get('descriptionMilestone', default=None)
    imageID = request.headers.get('idImage', default=None)
    projectID = request.headers.get('idProject',default=None)
    

    if None in [name, amount, description]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [name, amount, description]:
        return jsonify({'error': "Empty parameter"}), 400
        
    if re.match("^[a-zA-Z???????????? ,.'-]+$", name) is None:
        return jsonify({'error': 'name must contain only alphanumeric characters'}), 400 #Auch hier noch fehlerhafte IF-Anweisungen setze mich nach dem Refactoring daran

    try:        
        meilenstein_inst = Milestone(nameMilestone=name,
                         amountMilestone=amount,
                         descriptionMilestone=description,
                         idImage=imageID,
                         idProject=projectID)
    except (KeyError, ValueError, DecodeError):  # jwt decode errors
        return jsonify({'status': 'Invalid JWT'}), 400

    session.add(meilenstein_inst)
    session.commit()
    return jsonify({'status': 'Milestone registered'}), 201
    
@BP.route('/<id>', methods=['PUT'])
@db_session_dec
def milestone_put(session, id):
    milestone_id = id

    try:
        if milestone_id:
            int(milestone_id)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400
    results = session.query(Milestone)

    
    try:
        old = results.filter(Milestone.idMilestone == milestone_id).one()
    except NoResultFound:
        return jsonify({'error': 'Milestone not found'}), 404
    
    idimage = request.headers.get('idImage', default=old.idImage)
    idproject = request.headers.get('idProject', default=old.idProject )
    namemilestone= request.headers.get('nameMilestone', default=old.nameMilestone)
    amountmilestone= request.headers.get('amountMilestone', default=old.amountMilestone)
    descriptionmilestone = request.headers.get('descriptionMilestone', default=old.descriptionMilestone)
    

    try:
        if milestone_id:
            results.filter(Milestone.idMilestone == milestone_id).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Milestone not found'}), 404
    if None in [idimage, idproject, namemilestone, amountmilestone, descriptionmilestone]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [idimage,idproject,namemilestone ,amountmilestone, descriptionmilestone]:
        return jsonify({'error': 'Empty parameter'}), 400
    
    try:
        result = results.filter(Milestone.idMilestone == milestone_id).update({'idImage' : idimage , 'idProject' : idproject, 'nameMilestone' : namemilestone, 'amountMilestone' : amountmilestone , 'descriptionMilestone' : descriptionmilestone})
    except Exception as msg:
        return jsonify({'error': repr(msg)}), 400
    
    session.commit()
    return jsonify({'status': 'changed'}), 200