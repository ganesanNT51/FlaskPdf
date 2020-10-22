from sqlalchemy import create_engine, MetaData, Table, insert, select,update,delete
from sqlalchemy.sql import and_, or_
from core import app
import json

engine = create_engine(app.config['DATABASE_URI'])
class TradeMedia_details():
    def __init__(self):
        try:
            self.meta = MetaData()
            self.trade_media = Table("trade_media", self.meta, autoload=True, autoload_with=engine)
        except Exception as e:
            print(e)

    def get_trade_medias_by_trade(self,trade_id):
        print('in Trade Media View Function')
        print(trade_id)
        stmt = select([self.trade_media]).where(self.trade_media.c.trade_id.in_([trade_id]))
        print(stmt)
        result = engine.execute(stmt)
        # output = result.fetchone()
        return result   

    def get_trade_images_by_trade(self,trade_id,media_type):
        print('in Trade Media View Function')
        print(trade_id)
        stmt = select([self.trade_media]).where(self.trade_media.c.trade_id.in_([trade_id]))
        stmt = stmt.where(self.trade_media.c.media_type.in_([media_type]))    
        print(stmt)
        result = engine.execute(stmt)
        # output = result.fetchone()
        return result        