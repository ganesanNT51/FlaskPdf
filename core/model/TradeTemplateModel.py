from sqlalchemy import create_engine, MetaData, Table, insert, select,update,delete,text,column,Integer
from sqlalchemy.sql import and_, or_
from core import app
import json

engine = create_engine(app.config['DATABASE_URI'])
class TradeTemplateModel():
    def __init__(self):
        try:
            self.meta = MetaData()
            self.trade_template = Table("trade_template", self.meta, autoload=True, autoload_with=engine)
        except Exception as e:
            print(e)

    
    def get_tradeTemplate(self,trade_id):
        print('in TradeTemplate Get Function')
        stmt = select([self.trade_template]).where(self.trade_template.c.trade_id.in_([trade_id]))
        result_1 = engine.execute(stmt)
        result = result_1.fetchone()
        return result