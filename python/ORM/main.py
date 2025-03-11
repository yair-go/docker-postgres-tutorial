import random

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from pathlib import Path

from model import Base, Customer, Invoice


def create_instances():
    c1 = Customer("Moshe", "Cohen", "Jerusalem")
    c2 = Customer("Dan", "Ziv", "Tel Aviv")
    c3 = Customer("Moshe", "Levi", "Jerusalem")
    c4 = Customer("Josh", "Cohen", "Tel Aviv")
    c5 = Customer("David", "Cohen", "Tel Aviv")
    session.add(c1)
    session.add(c2)
    session.add(c3)
    session.add(c4)
    session.add(c5)
    session.commit()

    for i in range(10):
        c_id = random.randint(1, 6)
        invoice = Invoice(c_id)
        session.add(invoice)

    session.commit()


def create_all_tables(engine):
    Base.metadata.create_all(bind=engine)


# db_path = Path("database/mydb.db").absolute()
# engine = create_engine(rf"sqlite:///{db_path}", echo=True)

# הגדרת חיבור עם SQLAlchemy
DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"

# יצירת מנוע SQLAlchemy
engine = create_engine(DATABASE_URL)

session = Session(engine)

create_all_tables(engine)

#
# # Create instances
create_instances()


def main():
    # Queries
    results = session.query(Customer).all()
    print(results)
    print(type(results))
    
    filtered_results = session.query(Customer).filter(Customer.city == "Jerusalem")
    for customer in filtered_results:
        print(customer)
    
    print(type(filtered_results))
    
    filtered_results = filtered_results.all()
    print(filtered_results)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
