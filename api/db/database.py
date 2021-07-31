import click
from flask.cli import with_appcontext
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from .dbStructure import BASE

DB_URI = "mariadb+mariadbconnector://rootApi:thiel@127.0.0.1:3306/backend"
ENGINE = create_engine(DB_URI)

DB_SESSION: scoped_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=ENGINE))


def close_db(_):
    """
    Close the database session.
    :return: -
    """
    DB_SESSION()


def init_db():
    """
    Initiates the database from the ORM model.
    :return: -
    """
    BASE.metadata.drop_all(ENGINE)
    BASE.metadata.create_all(ENGINE)
    #add_sample_data(DB_SESSION)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """
    Defines the flask command for initializing the database.
    :return: -
    """
    init_db()
    click.echo('Initialized and cleared the database.')


def init_app(app):
    """
    Adds the commands and close context to the given app.
    :param app: the app the commands should registered to
    :return: -
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

if __name__=="__main__":
    init_db()