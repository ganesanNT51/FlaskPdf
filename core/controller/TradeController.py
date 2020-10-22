from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from core.model.tradeModel import Trade_details
from core.model.tradeMediaModel import TradeMedia_details
import json

app = Blueprint('trade', __name__)

# displaying the mos personalia info..
@app.route('/viewtrade/<int:id>' ,methods = ["GET","POST"])
def ViewTrade(id):
    print('In Trade View  Form')
    print(id)
    id = int(id)
    t = Trade_details()
    output = t.get_trade_All(id)
    tm = TradeMedia_details()
    output_tm = tm.get_trade_medias_by_trade(id)
    media_type = 'jpeg'
    output_tm_image = tm.get_trade_images_by_trade(id,media_type)
    # json_data = json.dumps([dict(r) for r in output_tm_image])
    # print('Images data only ...')
    # print(json_data) 
    # row_as_dict = dict(row)
    # print('hello sqlalchemy  result into dict to calculate length of row')    
    # print(row_as_dict)
    return render_template('view_trade.html',trade_data = output, trade_view = output_tm,trade_images = output_tm_image ,id = id)

@app.route('/trade_index')
def TredeIndex():
    print('ín Index')
    c = Trade_details()
    output = c.get_trade() 
    print(output)
    # return all rows as a JSON array of objects
    json_data = json.dumps([dict(r) for r in output])
    print('Return data to Android ..')
    print(json_data)        
    # return json_data
    #print(output.json())
    # return output.json()
    # xlen = len(json_data)
    # print(xlen)
    return render_template('trade_index.html',trade_data=output)    