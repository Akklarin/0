import psycopg2 as pg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


# try:
#     conn = pg.connect(
#         host='localhost',
#         database='BHhw',
#         port=5432,
#         user='postgres',
#         password='{__MyPASSWORD__}'
#     )
#
#     cursor = conn.cursor()
#     print("Connection established.")
#
# except Exception as err:
#     print("Something went wrong.")
#     print(err)

postgres_engine = create_engine('postgresql://postgres:{__MyPASSWORD__}@localhost:5432/BHhw')
#postgres_engine = create_engine('postgresql://user:pwd@localhost/database')
PostgresSession = sessionmaker(bind=postgres_engine)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
#    address = relationship('Address', backref='users', order_by='Address.id')


Base.metadata.create_all(postgres_engine)

session = PostgresSession()
ed_user = User(name='ed')
session.add(ed_user)
session.commit()
session.close()
