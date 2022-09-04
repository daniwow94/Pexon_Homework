"""
This file (test_recipes.py) contains the functional tests for the `recipes` blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the `recipes` blueprint.
"""

from project import create_app


def test_home_page(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    #Logging in -> "/"  has the decorator @login_required
    response = test_client.post('/login',
                                data=dict(username='FlaskUser', password='FlaskIsAwesome'),
                                follow_redirects=True)

    
    response = test_client.get('/', follow_redirects=True)
    assert response.status_code == 200
    assert b'Hey Pexonian, trage hier deine' in response.data
    assert b'Zertifizierung' in response.data
    assert b'Owner' in response.data

def test_home_page_post(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is is posted to (POST)
    THEN check that the response is valid
    """
    #Logging in -> "/"  has the decorator @login_required
    response = test_client.post('/login',
                                data=dict(username='FlaskUser', password='FlaskIsAwesome'),
                                follow_redirects=True)

    

    
    response = test_client.post('/', 
                                data=dict(certificate_name='Aws'), 
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Hey Pexonian, trage hier deine' in response.data
    assert b'Zertifizierung' in response.data
    assert b'Owner' in response.data
    assert b'Aws' in response.data

def test_certificate_page(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/certificate' page is requested (GET)
    THEN check that the response is valid
    """
    #Logging in -> "/"  has the decorator @login_required
    response = test_client.post('/login',
                                data=dict(username='FlaskUser', password='FlaskIsAwesome'),
                                follow_redirects=True)

    
    response = test_client.get('/certificate', follow_redirects=True)
    assert response.status_code == 200
    assert b'Hey Pexonian, hier kannst du eine Zertifizierung' in response.data
    assert b'Zertifizierung' in response.data
    assert b'Owner' in response.data

def test_certificate_page_post(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/certificate' page is is posted to (POST)
    THEN check that the response is valid
    """
    #Logging in -> "/"  has the decorator @login_required
    response = test_client.post('/login',
                                data=dict(username='FlaskUser', password='FlaskIsAwesome'),
                                follow_redirects=True)

    

    
    response = test_client.post('/certificate', 
                                data=dict(certificate_name='Azure'), 
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Hey Pexonian, hier kannst du eine Zertifizierung' in response.data
    assert b'Zertifizierung' in response.data
    assert b'Owner' in response.data
    assert b'Azure' in response.data

