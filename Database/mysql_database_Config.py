from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Configuration.config import settings

Dynamic_DB_URL=f"mysql+mysqlconnector://{settings.SQL_USERNAME}:{settings.SQL_PASSWORD}@{settings.SQL_HOST_NAME}/{settings.SQL_DB_nAME}"
SQL_ALCHEMY_DATABASE_URL=Dynamic_DB_URL
engine=create_engine(SQL_ALCHEMY_DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()
def get_db():
    db=SessionLocal()
    try: 
        yield db
    finally:
        db.close()