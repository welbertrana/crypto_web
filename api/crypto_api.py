from flask import Flask, jsonify, request
import mysql.connector
import json
import configparser
import os

os.chdir(os.path.dirname(__file__))

config = configparser.ConfigParser()

# Read Config Files
config.read('config/dev_config.ini')

def connect_to_db():
    db = mysql.connector.connect(
    host= config['DATABASE']['HOST'],
    user=config['DATABASE']['USER'],
    password=config['DATABASE']['PASSWORD'],
    database=config['DATABASE']['DB'],
    auth_plugin=config['DATABASE']['AUTH_PLUGIN']
    )
    cursor = db.cursor()

    return db, cursor

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return 'Welcome to Crypto API'

@app.route('/global_stat', methods=['GET'])
def global_stat():
    db, cursor = connect_to_db()
    query = """
        SELECT `coins_count`,
        `active_markets`,
        `total_mcap`,
        `total_volume`,
        `btc_d`,
        `eth_d`,
        `mcap_change`,
        `volume_change`,
        `avg_change_percent`,
        `volume_ath`,
        `mcap_ath`,
        `date`
        FROM {}""".format(config['MATERIALIZED']['DAILY_GLOBAL'])
    cursor.execute(query)
    sql_resp = cursor.fetchall()
    cursor_des = cursor.description
    columns = list(map(lambda x: x[0],cursor_des))
    dict_result = dict(zip(columns, sql_resp[0]))
    dict_result["date"] = str(dict_result["date"])
    result = json.dumps(dict_result)

    db.close()
    return result

@app.route('/get_all_ticker', methods=['GET'])
def get_all_ticker():
    result = []
    db, cursor = connect_to_db()
    query = """
        SELECT id, symbol, `name`, nameid, `rank`, price_usd, percent_change_24h, 
        percent_change_1h, percent_change_7d, price_btc, market_cap_usd, volume24, volume24a, 
        csupply, tsupply, msupply, coins_num, `time`
        FROM {}""".format(config['MATERIALIZED']['DAILY_ALL_COINS'])
    cursor.execute(query)
    sql_resp = cursor.fetchall()
    cursor_des = cursor.description
    columns = list(map(lambda x: x[0],cursor_des))
    
    for resp in sql_resp:
        dict_result = dict(zip(columns, resp))
        result.append(dict_result)
    
    result = json.dumps(result)
    db.close()
    return result

@app.route('/get_top_coins', methods=['GET'])
def get_top_coins():
    top = 9
    result = []
    db, cursor = connect_to_db()
    query = """
        SELECT id, symbol, `name`, nameid, `rank`, price_usd, percent_change_24h, 
        percent_change_1h, percent_change_7d, price_btc, market_cap_usd, volume24, volume24a, 
        csupply, tsupply, msupply, coins_num, `time`
        FROM {} ORDER BY cast(`rank` as unsigned) ASC LIMIT {}""".format(config['MATERIALIZED']['DAILY_ALL_COINS'], top)
    cursor.execute(query)
    sql_resp = cursor.fetchall()
    cursor_des = cursor.description
    columns = list(map(lambda x: x[0],cursor_des))
    
    for resp in sql_resp:
        dict_result = dict(zip(columns, resp))
        result.append(dict_result)
    
    result = json.dumps(result)
    db.close()
    return result

@app.route('/get_ticker', methods=['POST'])
def get_ticker():
    db, cursor = connect_to_db()
    body = request.data.decode('utf8')
    json_body = json.loads(body)
    coin = json_body["symbol"] if json_body["symbol"] else "BTC" # Default value to BTC
    query = """
        SELECT id, symbol, `name`, nameid, `rank`, price_usd, percent_change_24h, 
        percent_change_1h, percent_change_7d, price_btc, market_cap_usd, volume24, volume24a, 
        csupply, tsupply, msupply, coins_num, `time`
        FROM {} WHERE symbol='{}'""".format(config['MATERIALIZED']['DAILY_ALL_COINS'],coin)
    cursor.execute(query)
    sql_resp = cursor.fetchall()
    cursor_des = cursor.description
    columns = list(map(lambda x: x[0],cursor_des))
    dict_result = dict(zip(columns, sql_resp[0]))
    result = json.dumps(dict_result)

    db.close()
    return result

@app.route('/get_top_gainers', methods=['GET'])
def get_top_gainers():
    top = 6
    result = []
    db, cursor = connect_to_db()
    query = """
        SELECT id, symbol, `name`, nameid, `rank`, price_usd, percent_change_24h, 
        percent_change_1h, percent_change_7d, price_btc, market_cap_usd, volume24, volume24a, 
        csupply, tsupply, msupply, coins_num, `time`
        FROM {} ORDER BY cast(percent_change_7d as decimal) DESC LIMIT {}""".format(config['MATERIALIZED']['DAILY_ALL_COINS'], top)
    cursor.execute(query)
    sql_resp = cursor.fetchall()
    cursor_des = cursor.description
    columns = list(map(lambda x: x[0],cursor_des))
    
    for resp in sql_resp:
        dict_result = dict(zip(columns, resp))
        result.append(dict_result)
    
    result = json.dumps(result)
    db.close()
    return result


@app.route('/get_top_losers', methods=['GET'])
def get_top_losers():
    top = 6
    result = []
    db, cursor = connect_to_db()
    query = """
        SELECT id, symbol, `name`, nameid, `rank`, price_usd, percent_change_24h, 
        percent_change_1h, percent_change_7d, price_btc, market_cap_usd, volume24, volume24a, 
        csupply, tsupply, msupply, coins_num, `time`
        FROM {} ORDER BY cast(percent_change_7d as decimal) ASC LIMIT {}""".format(config['MATERIALIZED']['DAILY_ALL_COINS'], top)
    cursor.execute(query)
    sql_resp = cursor.fetchall()
    cursor_des = cursor.description
    columns = list(map(lambda x: x[0],cursor_des))
    
    for resp in sql_resp:
        dict_result = dict(zip(columns, resp))
        result.append(dict_result)
    
    result = json.dumps(result)
    db.close()
    return result


@app.route('/get_7d_data', methods=['POST'])
def get_7d_data():
    body = request.data.decode('utf8')
    json_body = json.loads(body)
    values = ["'"+str(col)+"'" for col in list(json_body["coinlist"])]
    str_values = ','.join(list(values))
    result = []
    db, cursor = connect_to_db()
    query = """
        SELECT * 
        FROM {} 
        WHERE symbol IN ({})""".format(config['MATERIALIZED']['DAILY_7D_TICKER'], str_values)
    cursor.execute(query)
    sql_resp = cursor.fetchall()
    cursor_des = cursor.description
    columns = list(map(lambda x: x[0],cursor_des))
    
    for resp in sql_resp:
        dict_result = dict(zip(columns, resp))
        result.append(dict_result)
    
    result = json.dumps(result)
    db.close()
    return result

if __name__ == '__main__':
    app.run(port = config['APP']['PORT'])