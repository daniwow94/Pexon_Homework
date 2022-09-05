from enum import unique

from flask import flash
from project import db
from datetime import datetime
from wtforms.validators import ValidationError
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """
    Class that represents a user of the application

    The following attributes of a user are stored in this table:
        * email - email address of the user
        * hashed password - hashed password (using werkzeug.security)
        * registered_on - date & time that the user registered

    REMEMBER: Never store the plaintext password in a database!
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20),nullable=False)
    password_hashed = db.Column(db.String(128), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=True)

    def __init__(self, email: str, password_plaintext: str, username: str, first_name: str, last_name: str):
        """
        Create a new User object using the email address, username, first_name, last_name and hashing the
        plaintext password using Werkzeug.Security.
        """
        self.email = email
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password_hashed = self._generate_password_hash(password_plaintext)
        self.registered_on = datetime.now()

    def is_password_correct(self, password_plaintext: str):
        return check_password_hash(self.password_hashed, password_plaintext)

    def set_password(self, password_plaintext: str):
        self.password_hashed = self._generate_password_hash(password_plaintext)

    @staticmethod
    def _generate_password_hash(password_plaintext):
        return generate_password_hash(password_plaintext)

    def __repr__(self):
        return f'<User: {self.email}>'
        

    @property
    def is_authenticated(self):
        """Return True if the user has been successfully registered."""
        return True

    @property
    def is_active(self):
        """Always True, as all users are active."""
        return True

    @property
    def is_anonymous(self):
        """Always False, as anonymous users aren't supported."""
        return False

    def get_id(self):
        """Return the user ID as a unicode string (`str`)."""
        return str(self.id)

class Certificate(db.Model):
    """
    Class that represents a Certificate of the application
    The following attributes of a user are stored in this table:
        * certificate_name - name of the certificate
        * owner - the owner of the certificate (first_name of the user)
        * registered_on - date & time that the certificate was added
    """

    __tablename__ = 'certificates'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    registered_on = db.Column(db.DateTime, nullable=True)
    certificate_name = db.Column(db.String, nullable=False)
    owner = db.Column(db.String, nullable=False)

    def __init__(self, certificate_name: str, owner: str):
        """Create a new Certificate object using the certificate_name an the owner."""
        self.certificate_name = certificate_name
        self.owner = owner
        self.registered_on = datetime.now()

    def __repr__(self):
        return f'<Certificate: {self.certificate_name}>'
