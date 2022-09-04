### Database Initialization

This Flask application needs a SQLite database to store data.  The database should be initialized via the Flask shell:

```
(venv) $ flask shell
>>> from project import db
>>> db.drop_all()
>>> db.create_all()
>>> quit()
(venv) $
```

### Running the Flask Application

Set the file that contains the Flask application and specify that the development environment should be used:

```sh
(venv) $ export FLASK_APP=app.py
(venv) $ export FLASK_ENV=development
```

Run development server to serve the Flask application:

```sh
(venv) $ flask run
```

Navigate to 'http://localhost:5000' in your favorite web browser to view the website!

## Key Python Modules Used

* **Flask**: micro-framework for web application development which includes the following dependencies:
  * click: package for creating command-line interfaces (CLI)
  * itsdangerous: cryptographically sign data 
  * Jinja2: templating engine
  * MarkupSafe: escapes characters so text is safe to use in HTML and XML
  * Werkzeug: set of utilities for creating a Python application that can talk to a WSGI server
* **pytest**: framework for testing Python projects
* **Flask-SQLAlchemy** - ORM (Object Relational Mapper) for Flask
* **Flask-Login** - support for user management (login/logout) in Flask
* **Flask-WTF** - simplifies forms in Flask
* **flake8** - static analysis tool

This application is written using Python 3.10.

## Testing

To run all the tests:

```sh
(venv) $ python -m pytest -v
```

To check the code coverage of the tests:

```sh
(venv) $ python -m pytest --cov-report term-missing --cov=project
```
