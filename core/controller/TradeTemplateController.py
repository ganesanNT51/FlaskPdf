from flask import Blueprint, render_template,render_template_string, request, redirect, url_for, flash, jsonify
# from core.model.tradeModel import Trade_details
from core.model.TradeTemplateModel import TradeTemplateModel
from core.model.tradeModel import Trade_details
from core.model.tradeMediaModel import TradeMedia_details
import json

app = Blueprint('tradeTemplate', __name__)

# displaying the mos personalia info..

@app.route('/trade_template')
def TredeTemplate():
    print('ín Trade Template')
    trade_id = 2
    trade_id = int(trade_id)
    c = TradeTemplateModel()
    temp = c.get_tradeTemplate(trade_id) 
    # print(output)
    # return all rows as a JSON array of objects
    # json_data = json.dumps([dict(r) for r in output])
    print('Return data to Android ..')
    # print(output.html_data)        
    # return json_data
    #print(output.json())
    # return output.json()
    # xlen = len(json_data)
    # print(xlen)
    # return render_template('trade_blank.html',trade_data=output) 

    print('In Trade View  Form')
    id = 2
    print(id)
    id = int(id)
    t = Trade_details()
    output = t.get_trade_All(id)
    tm = TradeMedia_details()
    output_tm = tm.get_trade_medias_by_trade(id)
    media_type = 'jpeg'
    output_tm_image = tm.get_trade_images_by_trade(id,media_type)
    return render_template_string(temp.html_data,trade_data = output, trade_view = output_tm,trade_images = output_tm_image ,id = id)