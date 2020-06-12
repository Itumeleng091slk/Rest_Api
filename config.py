# import os

# basedir = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_ECHO = False
# SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_DATABASE_URI = "postgresql://user:pass@localhost/data_sql"

connect_to_database = psycopg2.connect(database="data_sql",user="user",password="pass", host="localhost",port=5432)
