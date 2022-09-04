import pytest
from project import create_app, db
from project.models import Certificate, User


@pytest.fixture(scope='module')
def new_user():
    user = User('Max@Musterman.com', 'FlaskIsAwesome', 'FlaskUser', 'Max', 'Musterman')
    return user

@pytest.fixture(scope='module')
def new_certificate():
    certificate = Certificate('TestCertificate', 'FlaskUser')
    return certificate


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flask_test.cfg')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert user data
    user1 = User(email='Max@Musterman.com', password_plaintext='FlaskIsAwesome', username='FlaskUser', first_name='Max', last_name='Musterman')
    user2 = User(email='Erika@Musterman.com', password_plaintext='FlaskIsAwesome2', username='FlaskUserrin', first_name='Erika', last_name='Musterman')
    db.session.add(user1)
    db.session.add(user2)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()

@pytest.fixture(scope='module')
def init_database_certificates(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert certificate data
    certificate1 = Certificate(certificate_name='Aws', owner='FlaskUser')
    certificate2 = Certificate(certificate_name='AZURE', owner='FlaskUserrin')
    db.session.add(certificate1)
    db.session.add(certificate2)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()


@pytest.fixture(scope='function')
def login_default_user(test_client):
    test_client.post('/login',
                     data=dict(username='FlaskUser', password='FlaskIsAwesome'))

    yield  # this is where the testing happens!

    test_client.get('/logout', follow_redirects=True)