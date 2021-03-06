import re
import validators
from flask import Blueprint, request, jsonify
from sqlalchemy import func
from api.db.dbStructure import Image
from api.db.dbStructure import Solution
from api.db.dbStructure import Summary
from api.db.dbStructure import Problem
from sqlalchemy.orm.exc import NoResultFound
from .annotations import db_session_dec

BP = Blueprint('description', __name__, url_prefix='/api/description')

@BP.route('/summary', methods=['GET'])
@db_session_dec
def description_summary_get(session):
    results = session.query(Summary)

    json_data = []

    for result in results:
        json_data.append({
            'id':result.idSummary,
            'image':result.idImage,
            'description':result.descriptionSummary
        })
    return jsonify(json_data)


@BP.route('/solution', methods=['GET'])
@db_session_dec
def description_solution_get(session):
    results = session.query(Solution)

    json_data = []

    for result in results:
        json_data.append({
            'id':result.idSolution,
            'image':result.idImage,
            'description':result.descriptionSolution
        })
    return jsonify(json_data)

@BP.route('/problem', methods=['GET'])
@db_session_dec
def description_problem_get(session):
    results = session.query(Problem)

    json_data = []

    for result in results:
        json_data.append({
            'id':result.idProblem,
            'image':result.idImage,
            'description':result.descriptionProblem
        })
    return jsonify(json_data)


@BP.route('/summary/<id>', methods=['GET'])
@db_session_dec
def description_summary_by_id_get(session, id):
    id_desc = id
    try:
        if id_desc:
            int(id_desc)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400

    results = session.query(Summary)

    try:
        if id_desc:
            results = results.filter(Summary.idSummary == id_desc).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Summary not found'}), 404
    
    json_data = {
        'image':results.idImage,
        'description':results.descriptionSummary
    }
        
    return jsonify(json_data), 200


@BP.route('/solution/<id>', methods=['GET'])
@db_session_dec
def description_Solution_by_id_get(session, id):
    id_desc = id
    try:
        if id_desc:
            int(id_desc)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400

    results = session.query(Solution)

    try:
        if id_desc:
            results = results.filter(Solution.idSolution == id_desc).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Solution not found'}), 404
    
    json_data = {
        'image':results.idImage,
        'description':results.descriptionSolution
    }
        
    return jsonify(json_data), 200


@BP.route('/problem/<id>', methods=['GET'])
@db_session_dec
def description_Problem_by_id_get(session, id):
    id_desc = id
    try:
        if id_desc:
            int(id_desc)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400

    results = session.query(Problem)

    try:
        if id_desc:
            results = results.filter(Problem.idProblem == id_desc).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Problem not found'}), 404
    
    json_data = {
        'image':results.idImage,
        'description':results.descriptionProblem
    }
        
    return jsonify(json_data), 200


@BP.route('/summary', methods=['POST'])
@db_session_dec
def summary_post(session):
    image = request.headers.get('idImage', default=None)
    description = request.headers.get('descriptionSummary',default=None)

    if None in [image, description]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [image, description]:
        return jsonify({'error': "Empty parameter"}), 400

    try:        
        desc_inst = Summary(idImage=image,
                         descriptionSummary=description)
    except (KeyError, ValueError, DecodeError):  # jwt decode errors
        return jsonify({'status': 'Invalid JWT'}), 400

    session.add(desc_inst)
    session.commit()
    return jsonify({'status': 'Summary POST erfogreich'}), 201


@BP.route('/solution', methods=['POST'])
@db_session_dec
def solution_post(session):
    image = request.headers.get('idImage', default=None)
    description = request.headers.get('descriptionSolution',default=None)

    if None in [image, description]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [image, description]:
        return jsonify({'error': "Empty parameter"}), 400

    try:        
        desc_inst = Solution(idImage=image,
                         descriptionSolution=description)
    except (KeyError, ValueError, DecodeError):  # jwt decode errors
        return jsonify({'status': 'Invalid JWT'}), 400

    session.add(desc_inst)
    session.commit()
    return jsonify({'status': 'Solution POST erfogreich'}), 201


@BP.route('/problem', methods=['POST'])
@db_session_dec
def problem_post(session):
    image = request.headers.get('idImage', default=None)
    description = request.headers.get('descriptionProblem',default=None)

    if None in [image, description]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [image, description]:
        return jsonify({'error': "Empty parameter"}), 400

    try:        
        desc_inst = Problem(idImage=image,
                         descriptionProblem=description)
    except (KeyError, ValueError, DecodeError):  # jwt decode errors
        return jsonify({'status': 'Invalid JWT'}), 400

    session.add(desc_inst)
    session.commit()
    return jsonify({'status': 'Problem POST erfogreich'}), 201


@BP.route('/summary/<id>', methods=['PUT'])
@db_session_dec
def summary_put(session, id):
    summary_id = id

    try:
        if summary_id:
            int(summary_id)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400
    results = session.query(Summary)
    
    try:
        old = results.filter(Summary.idSummary == summary_id).one()
    except NoResultFound:
        return jsonify({'error': 'Summary not found'}), 404

    image = request.headers.get('idImage', default=old.idImage)
    desc = request.headers.get('descriptionSummary', default=old.descriptionSummary)

    

    try:
        if summary_id:
            results.filter(Summary.idSummary == summary_id).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Summary not found'}), 404

    

    if None in [image, desc]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [image]:
        return jsonify({'error': 'Empty parameter'}), 400
        
    try:
        result = results.filter(Summary.idSummary == summary_id).update({'idImage' : image, 'descriptionSummary' : desc})
    except Exception as msg:
        return jsonify({'error': repr(msg)}), 400
    
    session.commit()
    return jsonify({'status': 'changed'}), 200

@BP.route('/solution/<id>', methods=['PUT'])
@db_session_dec
def solution_put(session, id):
    solution_id = id

    try:
        if solution_id:
            int(solution_id)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400
    results = session.query(Solution)
    
    try:
        old = results.filter(Solution.idSolution == solution_id).one()
    except NoResultFound:
        return jsonify({'error': 'Solution not found'}), 404

    image = request.headers.get('idImage', default=old.idImage)
    desc = request.headers.get('descriptionSolution', default=old.descriptionSolution)

    

    try:
        if solution_id:
            results.filter(Solution.idSolution == solution_id).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Solution not found'}), 404

    

    if None in [image, desc]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [image]:
        return jsonify({'error': 'Empty parameter'}), 400
        
    try:
        result = results.filter(Solution.idSolution == solution_id).update({'idImage' : image, 'descriptionSolution' : desc})
    except Exception as msg:
        return jsonify({'error': repr(msg)}), 400
    
    session.commit()
    return jsonify({'status': 'changed'}), 200



@BP.route('/problem/<id>', methods=['PUT'])
@db_session_dec
def problem_put(session, id):
    problem_id = id

    try:
        if problem_id:
            int(problem_id)
    except ValueError:
        return jsonify({'error': 'bad argument'}), 400
    results = session.query(Problem)
    
    try:
        old = results.filter(Problem.idProblem == problem_id).one()
    except NoResultFound:
        return jsonify({'error': 'Problem not found'}), 404

    image = request.headers.get('idImage', default=old.idImage)
    desc = request.headers.get('descriptionProblem', default=old.descriptionProblem)

    

    try:
        if problem_id:
            results.filter(Problem.idProblem == problem_id).one()
        else:
            return jsonify({'error':'missing argument'}), 400
    except NoResultFound:
        return jsonify({'error': 'Problem not found'}), 404

    

    if None in [image, desc]:
        return jsonify({'error': 'Missing parameter'}), 400

    if "" in [image]:
        return jsonify({'error': 'Empty parameter'}), 400
        
    try:
        result = results.filter(Problem.idProblem == problem_id).update({'idImage' : image, 'descriptionProblem' : desc})
    except Exception as msg:
        return jsonify({'error': repr(msg)}), 400
    
    session.commit()
    return jsonify({'status': 'changed'}), 200