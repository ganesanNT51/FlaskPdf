from sqlalchemy import create_engine, MetaData, Table, insert, select,update,delete,text,column,Integer
from sqlalchemy.sql import and_, or_
from core import app
import json

engine = create_engine(app.config['DATABASE_URI'])
class Trade_details():
    def __init__(self):
        try:
            self.meta = MetaData()
            self.trades = Table("trades", self.meta, autoload=True, autoload_with=engine)
            self.trade_media = Table("trade_media", self.meta, autoload=True, autoload_with=engine)
        except Exception as e:
            print(e)

    def insert_cust(self,data):
        print('inside model insert cust')
        result = engine.execute(self.trades.insert(), data)
        return result

    def get_trade(self):
        print('in Trade Get Function')
        stmt = select([self.trades])
        result = engine.execute(stmt)
        return result

    def get_trade_All(self,id):
        print('in Trade All Get Function')
        stmt = select([self.trades.c.trade_id,self.trades.c.trade_name,self.trades.c.trade_desc]).where(self.trades.c.trade_id.in_([id]))
        result_1 = engine.execute(stmt)
        result = result_1.fetchone()
        return result    


    def view_trade(self,id):
        print('in Trade View Function')
        print(id)
        stmt = self.trades.join(self.trade_media, self.trade_media.c.trade_id == self.trades.c.trade_id)
        print(stmt)
        stmt = select([self.trades,self.trade_media.c.media_link,self.trade_media.c.media_type]).select_from(stmt).where(
            self.trades.c.trade_id.in_([id])
            )
        print(stmt)
        result = engine.execute(stmt)
        # output =  dict(result)
        # output = result.fetchone()
        print(result)
        # print(output.trade_name)
        return result  