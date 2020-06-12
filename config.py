# import os

# basedir = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_ECHO = False
# SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_DATABASE_URI = "postgresql://user:pass@localhost/data_sql"

connect_to_database = psycopg2.connect(database="data_sql",user="user",password="pass", host="localhost",port=5432)
os_path = os.path.abspath(os.path.dirname(__file__))
connect_to_postgres = 'postgresql:///' + os.path.join(basedir, 'postgresql')
connect_to_engine = 'postgresql+psycopg2://user:pass@localhost:5432/data_sql'
