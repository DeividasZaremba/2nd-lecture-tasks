from datetime import date
from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


# engine = create_engine('sqlite:///darbuotojai1.db')
Base = declarative_base()

class Darbuotojai(Base):
    __tablename__ = 'Darbuotoju sarasas'
    id = Column(Integer, primary_key=True)
    fname = Column("Vardas", String)
    lname = Column("Pavarde", String)
    dob = Column("Gimimo data", String)
    position = Column("Pareigos", String)
    salary = Column("Atlyginimas", Integer)
    worksfrom = Column("Nuo kada dirba", Date, default=date.today)

    def __init__(self, fname, lname, dob, position, salary):
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f'{self.id} {self.fname} {self.lname} {self.dob} - {self.position} {self.salary} {self.worksfrom}'

# Base.metadata.create_all(engine)

engine = create_engine("sqlite:///darbuotojai1.db")
Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = int(input("""Pasirinkite veiksma darbuotoju sarasui: 
    1 - Irasyti
    2 - Perziureti
    3 - Istrinti
    4 - Atnaujinti
    Pasirinkite: """))

    if pasirinkimas == 1:
        fname = input("Iveskite darbuotojo varda: ")
        lname = input("Iveskite darbuotojo pavarde: ")
        dob = input("Iveskite darbuotojo gimimo data (YYYY-MM-DD): ")
        position = input("Iveskite darbuotojo pareigas: ")
        salary = int(input("Iveskite darbuotojo atlyginima: "))
        darbuotojas = Darbuotojai(fname, lname, dob, position, salary)
        session.add(darbuotojas)
        session.commit()
    if pasirinkimas == 2:
        darbuotojai = session.query(Darbuotojai).all()
        print("------------------------")
        for a in darbuotojai:
            print(a)
        print("------------------------")
    if pasirinkimas == 3:
        darbuotojai = session.query(Darbuotojai).all()
        print("------------------------")
        for a in darbuotojai:
            print(a)
        print("------------------------")
        rem_id = int(input("Pasirinkite darbuotojo ID (skaiciu) kuri norite istrinti: "))
        trinamas_darb = session.query(Darbuotojai).get(rem_id)
        session.delete(trinamas_darb)
        session.commit()
    if pasirinkimas == 4:
        darbuotojai = session.query(Darbuotojai).all()
        print("------------------------")
        for b in darbuotojai:
            print(b)
        print("------------------------")
        darb_id = int(input("Pasirinkite darbuotojo ID (skaiciu) kuri norite pakeisti: "))
        pakeitimas = int(input("""Pasirinkite ka norite keisti: 
        1 - Varda
        2 - Pavarde
        3 - Gimimo data
        4 - Pareigas
        5 - Atlyginima
        Pasirinkite: """))
        keiciamas_darb = session.query(Darbuotojai).get(darb_id)
        if pakeitimas == 1:
            keiciamas_darb.fname = input('Iveskite nauja darbuotojo varda: ')
        if pakeitimas == 2:
            keiciamas_darb.lname = input('Iveskite nauja darbuotojo pavarde: ')
        if pakeitimas == 3:
            keiciamas_darb.dob = input('Iveskite nauja darbuotojo gimimo data: ')
        if pakeitimas == 4:
            keiciamas_darb.position = input('Iveskite naujas darbuotojo pareigas: ')
        if pakeitimas == 5:
            keiciamas_darb.salary = int(input('Iveskite nauja darbuotojo atlyginima: '))
        session.commit()