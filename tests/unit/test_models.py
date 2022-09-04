"""
This file (test_models.py) contains the unit tests for the models.py file.
"""
from project.models import User, Certificate


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, password_hashed, authenticated, and active fields are defined correctly
    """
    user = User('Max@Musterman.com', 'FlaskIsAwesome', 'FlaskUser', 'Max', 'Musterman')
    assert user.email == 'Max@Musterman.com'
    assert user.password_hashed != 'FlaskIsAwesome'
    assert user.__repr__() == '<User: Max@Musterman.com>'
    assert user.is_authenticated
    assert user.is_active
    assert not user.is_anonymous


def test_new_user_with_fixture(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email and password_hashed fields are defined correctly
    """
    assert new_user.email == 'Max@Musterman.com'
    assert new_user.password_hashed != 'FlaskIsAwesome'


def test_setting_password(new_user):
    """
    GIVEN an existing User
    WHEN the password for the user is set
    THEN check the password is stored correctly and not as plaintext
    """
    new_user.set_password('MyNewPassword')
    assert new_user.password_hashed != 'MyNewPassword'
    assert new_user.is_password_correct('MyNewPassword')
    assert not new_user.is_password_correct('MyNewPassword2')
    assert not new_user.is_password_correct('FlaskIsAwesome')


def test_user_id(new_user):
    """
    GIVEN an existing User
    WHEN the ID of the user is defined to a value
    THEN check the user ID returns a string (and not an integer) as needed by Flask-WTF
    """
    new_user.id = 17
    assert isinstance(new_user.get_id(), str)
    assert not isinstance(new_user.get_id(), int)
    assert new_user.get_id() == '17'


def test_new_certificate():
    """
    GIVEN a Certificate model
    WHEN a new Certificate is created
    THEN check the certificate_name and owner fields are defined correctly
    """
    certificate = Certificate('TestCertificate', 'FlaskUser')
    assert certificate.certificate_name == 'TestCertificate'
    assert certificate.owner == 'FlaskUser'
    assert certificate.__repr__() == '<Certificate: TestCertificate>'
    

def test_new_certificate_with_fixture(new_certificate):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email and password_hashed fields are defined correctly
    """
    assert new_certificate.certificate_name == 'TestCertificate'
    assert new_certificate.owner == 'FlaskUser'