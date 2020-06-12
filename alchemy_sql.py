from sqlalchemy import create_engine, Column, String,NUMERIC,VARCHAR,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import connect_to_engine

engine = create_engine('connect_to_engine')
engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

Base = session_base

class Computer(Base):

    __tablename__ = 'computers'
    id = Column(Integer, primary_key= True)
    computer_name = Column(String)
    hard_drive = Column(VARCHAR)
    processor = Column(VARCHAR)
    ram_amount = Column(NUMERIC)
    maximum_ram = Column(NUMERIC)
    hard_drive_space = Column(String)
    form_factor = Column(VARCHAR)

    def __init__(self, computer_name, hard_drive, processor, ram_amount, maximum_ram, hard_drive_space, form_factor):
        self.computer_name = computer_name
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
Computer2 = Computer("LG","HDD","Intell Pentium II 350Hz",60,512,"2000GB","63.5 cm(max)")
Computer3 = Computer("Acer","Solid State Drive (SSD)","Intel i5",4,64,"30GB","SFF(small form factor)")
session.add(Computer1)
session.add(Computer2)
session.add(Computer3)
session.commit()
