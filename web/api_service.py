import http.client
import json
import configparser

config = configparser.ConfigParser()

# Read Config Files
config.read('config/dev_config.ini')

api_url = "{}:{}".format(config['CRYPTO_API']['HOST'], config['CRYPTO_API']['PORT'])

client = http.client.HTTPConnection(api_url)
# Header used for Http Request
headers = {}

# Helper function to parse http response to json format
def parse_response(data):
    g_data = data.getresponse()
    r_data = g_data.read()
    d_data = r_data.decode("utf-8")
    return json.loads(d_data)

# Start of Http Requests to Crypto API Service
def get_global_stats():
    client.request("GET", "/global_stat", headers=headers)
    return parse_response(client)

def get_all_ticker():
    client.request("GET", "/get_all_ticker", headers=headers)
    return parse_response(client)

def get_top_coins():
    client.request("GET", "/get_top_coins", headers=headers)
    return parse_response(client)

def get_ticker(payload):
    client.request("POST", "/get_ticker", headers=headers, body=json.dumps(payload))
    return parse_response(client)

def get_top_gains():
    client.request("GET", "/get_top_gainers", headers=headers)
    return parse_response(client)

def get_top_losers():
    client.request("GET", "/get_top_losers", headers=headers)
    return parse_response(client)
    
def get_7d_data(payload):
    client.request("POST", "/get_7d_data", headers=headers, body=json.dumps(payload))
    return parse_response(client)
# End of Http Requests to Crypto API Service