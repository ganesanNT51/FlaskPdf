from sqlalchemy import create_engine, MetaData, Table, insert, select,update,delete
from sqlalchemy.sql import and_, or_
from core import app
import json

engine = create_engine(app.config['DATABASE_URI'])


class Cust_details():
    def __init__(self):
        try:
            self.meta = MetaData()
            self.contact_table = Table("contact_table", self.meta, autoload=True, autoload_with=engine)
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

    def delete_cust(self,id):
        print('in Delete Function')
        print(id)
        stmt = self.contact_table.delete().where(self.contact_table.c.contact_id.in_([id]))
        # stmt = stmt.where(self.contact_table.c.contact_id.in_([contact_id]))
        result = engine.execute(stmt)
        return result
        # if result == '':
        #     return 'False'
        #     else:
            # return ''
        # result = engine.execute(stmt)
        # return result

    def edit_cust(self,id):
        print('in Edit Function')
        print(id)
        stmt = select([self.contact_table]).where(self.contact_table.c.contact_id.in_([id]))
        result = engine.execute(stmt)
        output = result.fetchone()
        # print(r)
        # output =  dict(r)
        # for r in result:
        #     output = r
        print(output)
        print(output.name)
        return output

    def view_cust(self,id):
        print('in Edit Function')
        print(id)
        stmt = select([self.contact_table]).where(self.contact_table.c.contact_id.in_([id]))
        result = engine.execute(stmt)
        output = result.fetchone()
        print(output)
        print(output.name)
        return output    


    def update_cust(self,id,data):
        print('in Edit post Function')
        print(id)
        print('Data to Update ')
        print(data)
        stmt = self.contact_table.update().where(self.contact_table.c.contact_id.in_([id])).values(data)
        result = engine.execute(stmt)
        return 'Success'

    def insert_signup(self,data):
        print('inside model insert cust Signup')
        result = engine.execute(self.contact_table.insert(), data)
        return result         
    