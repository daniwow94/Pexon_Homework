import os



DEV_DB = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')

pg_user = 'admin'
#Need to be hide
pg_password = 'bad_password'
pg_db = 'Homework'
pg_host = 'db'
pg_port = 5432


PROD_DB = f'postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}'