from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Reports(Base):
    __tablename__ = 'all_reports'

    id = Column(Integer, primary_key=True, autoincrement=True)
    evacuation_site = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)
    time = Column(String(250), nullable=False)
    situation = Column(String(500), nullable=False)
    affected_pop = Column(String(500), nullable=False)
    displaced = Column(String(500), nullable=False)
    response = Column(String(500), nullable=False)
    preparer = Column(String(250), nullable=False)
    releaser = Column(String(250), nullable=False)


engine = create_engine('sqlite:///reports.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
