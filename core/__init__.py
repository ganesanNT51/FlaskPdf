from flask import Flask 
app = Flask(__name__)


app.config.from_object('core.config.SECRET_KEY')
app.config.from_object('core.config.ProductionConfig')

config = app.config

#from core import routes
from core.controller.custcontroller import app as cust

app.register_blueprint(cust, url_prefix='')

from core.controller.signupController import app as signup

app.register_blueprint(signup, url_prefix='')

from core.controller.TradeController import app as trade

app.register_blueprint(trade, url_prefix='')

from core.controller.TradeMediaController import app as tradeMedia

app.register_blueprint(tradeMedia, url_prefix='')


from core.controller.TradeTemplateController import app as tradeTemplate

app.register_blueprint(tradeTemplate, url_prefix='')