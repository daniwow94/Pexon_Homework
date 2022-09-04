"""
This file (test_users.py) contains the functional tests for the `users` blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the `users` blueprint.
"""


from flask import flash
from sqlalchemy import true


def test_login_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'Username' in response.data
    assert b'Password' in response.data
    assert b'Remember Me' in response.data
    assert b'Logout' not in response.data


def test_valid_login_logout(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/login',
                                data=dict(username='FlaskUser', password='FlaskIsAwesome'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Logout' in response.data
    assert b'Login' not in response.data
    assert b'Register' not in response.data
    assert b'Hey Pexonian, trage hier deine' in response.data
    assert b'Zertifizierung' in response.data
    assert b'Owner' in response.data

    """
    GIVEN a Flask application configured for testing
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Goodbye!' in response.data
    assert b'Logout' not in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data
    assert b'Keinen Account?' in response.data
    assert b'Hier gehts zur' in response.data
    assert b'Registrierung!' in response.data


def test_invalid_login(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = test_client.post('/login',
                                data=dict(username='FlaskUser', password='FlaskIsNotAwesome'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'ERROR! Incorrect login credentials.' in response.data
    assert b'Logout' not in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data


def test_login_already_logged_in(test_client, init_database, login_default_user):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST) when the user is already logged in
    THEN check an error message is returned to the user
    """
    response = test_client.post('/login',
                                data=dict(username='Max@Musterman.com', password='FlaskIsNotAwesome'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Already logged in!  Redirecting to your Certificate page...' in response.data
    assert b'Logout' in response.data
    assert b'Login' not in response.data
    assert b'Register' not in response.data


def test_valid_registration(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to (POST)
    THEN check the response is valid and the user is logged in
    """
    response = test_client.post('/register',
                                data=dict(email='Max1@Musterman.com', 
                                          username='FlaskUser1',
                                          first_name='Max',
                                          last_name='Musterman',
                                          password='FlaskIsGreat',
                                          confirm='FlaskIsGreat'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Thanks for registering, FlaskUser1' in response.data
    assert b'Logout' in response.data
    assert b'Login' not in response.data
    assert b'Register' not in response.data
    assert b'Hey Pexonian, hier kannst du eine Zertifizierung' in response.data
    assert b'Id' in response.data
    assert b'Owner' in response.data
    assert b'Update' in response.data
    assert b'Delete' in response.data

    """
    GIVEN a Flask application configured for testing
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Goodbye!' in response.data
    assert b'Logout' not in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data
    assert b'Username' in response.data
    assert b'Password' in response.data
    assert b'Remember Me' in response.data
    assert b'Keinen Account? Hier gehts zur' in response.data
    assert b'Registrierung!' in response.data


def test_invalid_registration(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = test_client.post('/register',
                                data=dict(email='Max2@Musterman.com', 
                                          username='FlaskUser2',
                                          first_name='Max',
                                          last_name='Musterman',
                                          password='FlaskIsGreat',
                                          confirm='FlskIsGreat'),   # Does NOT match!
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Thanks for registering, FlaskUser!' not in response.data
    assert b'[This field is required.]' not in response.data
    assert b'Logout' not in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data


def test_duplicate_registration(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to (POST) using an email address already registered
    THEN check an error message is returned to the user
    """
    # Register the new account
    test_client.post('/register',
                     data=dict(email='Max3@Musterman.com',
                                username='FlaskUser3',
                                first_name='Max',
                                last_name='Musterman',
                                password='FlaskIsTheBest',
                                confirm='FlaskIsTheBest'),
                     follow_redirects=True)
    # Try registering with the same email address
    response = test_client.post('/register',
                                data=dict(email='Max3@Musterman.com',
                                            username='FlaskUser4',
                                            first_name='Max',
                                            last_name='Musterman',
                                            password='FlaskIsStillTheBest',
                                            confirm='FlaskIsStillTheBest'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Thanks for registering, FlaskUser!' not in response.data
