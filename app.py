import alpaca_trade_api as tradeapi
import time

from chalice import Chalice

app = Chalice(app_name='buyv2')

key = "PKIY2IKI7V4ZM2YSWGN3"
sec = "8QzTRw4ysw/60xWe9jG8He2T1WxAHZTsI2bF1N/O"

#API endpoint URL
url = "https://paper-api.alpaca.markets"

#api_version v2 refers to the version that we'll use
#very important for the documentation
api = tradeapi.REST(key, sec, url, api_version='v2')

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/buyv2', methods=['POST'])
def buyv2():
    request = app.current_request
    webhook_message = request.json_body
    
    data = api.submit_order(symbol=webhook_message['ticker'],
                            qty="1",
                            side="buy",
                            type="market",
                            time_in_force="gtc")
    
    return {
        'webhook_message': webhook_message
    }