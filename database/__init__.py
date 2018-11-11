from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_mixins import AllFeaturesMixin

from database.preprocessor import load_engine

Base = declarative_base()


class BaseModel(Base, AllFeaturesMixin):
    __abstract__ = True
    pass


from database.models import *

engine = load_engine(echo=False)
session = scoped_session(sessionmaker(bind=engine))
meta = sa.MetaData(bind=engine)

Base.metadata.create_all(engine)
BaseModel.set_session(session)
