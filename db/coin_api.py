import http.client
import json

client = http.client.HTTPSConnection("coinlore-cryptocurrency.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "coinlore-cryptocurrency.p.rapidapi.com",
    'x-rapidapi-key': "b927bed714msh218da26504f8499p168b9cjsnd4f730dc89ba"
}

def parse_response(data):
    g_data = data.getresponse()
    r_data = g_data.read()
    d_data = r_data.decode("utf-8")
    return json.loads(d_data)

def get_global_stats():
    client.request("GET", "/api/global/", headers=headers)
    return parse_response(client)

def get_all_coins_ticker(start, limit):
    client.request("GET", f"/api/tickers/?start={start}&limit={limit}", headers=headers)
    return parse_response(client)

def get_coin_ticker(id):
    client.request("GET", f"/api/ticker/?id={id}", headers=headers)
    return parse_response(client)

def get_exchanges():
    client.request("GET", "/api/exchanges/", headers=headers)
    return parse_response(client)

def get_markets_of_coin(id):
    client.request("GET", f"/api/coin/markets/?id={id}", headers=headers)
    return parse_response(client)

def get_exchange_pairs(id):
    client.request("GET", f"/api/exchange/?id={id}", headers=headers)
    return parse_response(client)

