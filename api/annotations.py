from functools import wraps
from typing import List

from flask import request, abort
from jwt import DecodeError
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from backend.blockstack_auth import BlockstackAuth
from backend.db.dbStructure import DB_SESSION

def db_session_dec(func):
    """
    Decorator for resources that need a DB-Session.
    :param func: function to decorate
    :return:
    """

    @wraps(func)
    def decorated_function(*args, **kws):
        sess: Session = None
        try:
            sess = DB_SESSION()
            return func(sess, *args, **kws)
        finally:
            if sess:
                sess.rollback()
                sess.close()

    return decorated_function
