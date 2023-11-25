from sqlalchemy import Column, Integer, String, create_engine, Boolean
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
    # item = Column(String(250), nullable=False)
    # quantity = Column(Integer(250), nullable=False)
    # is_available = Column(Boolean, nullable=False),
    # inventory = Column(String(250), nullable=False)
    rice = Column(Integer, nullable=False)
    flour = Column(Integer, nullable=False)
    sugar = Column(Integer, nullable=False)
    powdered_milk = Column(Integer, nullable=False)
    canned_goods = Column(Integer, nullable=False)
    cooking_oil = Column(Integer, nullable=False)
    blankets = Column(Integer, nullable=False)
    clothing = Column(Integer, nullable=False)
    tents = Column(Integer, nullable=False)
    water = Column(Integer, nullable=False)
    hygiene_kits = Column(Integer, nullable=False)


engine = create_engine('sqlite:///reports.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)