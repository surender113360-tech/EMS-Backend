import os
# env file variable can be access by python
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

load_dotenv()
database_url=os.getenv("DATABASE_URL")
# print(database_url)
engine = create_engine(database_url)
session = sessionmaker(bind = engine,autocommit = False,autoflush = False)
base = declarative_base()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def create_table():
  base.metadata.create_all(bind=engine)
