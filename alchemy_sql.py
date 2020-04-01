from sqlalchemy import create_engine, Column, String,NUMERIC,VARCHAR,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://user:pass@localhost/data_sql')
engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Computer(Base):

    __tablename__ = 'Computers'
    id = Column(Integer, primary_key= True)
    name = Column(String)
    hard_drive = Column(VARCHAR)
    processor = Column(VARCHAR)
    ram_amount = Column(NUMERIC)
    maximum_ram = Column(NUMERIC)
    hard_drive_space = Column(String)
    form_factor = Column(VARCHAR)

    def __init__(self, name, hard_drive, processor, ram_amount, maximum_ram, hard_drive_space, form_factor):
        self.name = name
        self.hard_drive = hard_drive
        self.processor = processor
        self.ram_amount = ram_amount
        self.maximum_ram = maximum_ram
        self.hard_drive_space = hard_drive_space
        self.form_factor = form_factor

    def save_computer(self):
        session.add(self)
        session.commit()

Computer1 = Computer("Dell","Dell 500GB 7,200 RPM SATA 2.5in Hard Drive","Intel Core i9 processor",8,8,"512GB","18.3 cm (7.2 in)")
session.add(Computer1)
session.commit()