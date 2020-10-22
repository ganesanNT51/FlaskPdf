from sqlalchemy import create_engine, MetaData, Table, insert, select,update,delete
from sqlalchemy.sql import and_, or_
from core import app
import json

engine = create_engine(app.config['DATABASE_URI'])


class Signup_details():
    def __init__(self):
        try:
            self.meta = MetaData()
            self.contact_table = Table("signup_table", self.meta, autoload=True, autoload_with=engine)
        except Exception as e:
            print(e)

    def insert_cust(self,data):
        print('inside model insert cust')
        result = engine.execute(self.contact_table.insert(), data)
        return result

    def get_cust(self):
        print('in Get Function')
        stmt = select([self.contact_table])
        result = engine.execute(stmt)
        return result

    def insert_signup(self,data):
        print('inside model insert cust Signup')
        result = engine.execute(self.contact_table.insert(), data)
        return result         
    