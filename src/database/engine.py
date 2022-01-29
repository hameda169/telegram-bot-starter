from os import environ

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

database_engine = create_engine(environ.get('DB_URL'))
