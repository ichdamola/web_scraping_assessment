# SQLAlchemy Imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Third Party Imports
from databases import Database

# Own Imports
from backend.config.settings import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

DB_ENGINE = create_engine(SQLALCHEMY_DATABASE_URL)

# Construct a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=DB_ENGINE)

# Construct a base class for declarative class definitions.
Base = declarative_base()
Base.metadata.create_all(DB_ENGINE)

# Construct a db connector to connect, shutdown database
db_connect = Database(SQLALCHEMY_DATABASE_URL)
