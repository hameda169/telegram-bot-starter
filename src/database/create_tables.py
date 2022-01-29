from src.database.engine import database_engine
from src.database.models.__base__ import Base

# this should be here to declare the model classes
import src.database.models.__index__

if __name__ == '__main__':
    Base.metadata.create_all(database_engine)
