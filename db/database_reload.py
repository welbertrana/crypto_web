import mysql.connector
import coin_api
import pandas as pd
import configparser
import os

os.chdir(os.path.dirname(__file__))

config = configparser.ConfigParser()

# Read Config Files
config.read('config/dev_config.ini')

db = mysql.connector.connect(
  host= config['DATABASE']['HOST'],
  user=config['DATABASE']['USER'],
  password=config['DATABASE']['PASSWORD'],
  database=config['DATABASE']['DB'],
  auth_plugin=config['DATABASE']['AUTH_PLUGIN']
)
cursor = db.cursor()

def reload_global_stats():
    global_stats = coin_api.get_global_stats()
    df = pd.DataFrame(global_stats)
    insert_query = "INSERT INTO {}({}) VALUES({})"
    cols = ','.join(list(df.columns))
    values = [str(df.at[0, col]) for col in list(df.columns)]
    str_values = ','.join(list(values))
    try:
        cursor.execute(insert_query.format(config['TABLES']['DAILY_GLOBAL'],cols, str_values))
        print("Inserted {} records to daily_global...".format(cursor.rowcount))
        db.commit()
    except:
        print("Error occurred on inserting...")

def reload_all_coins_ticker(start, limit):
    counter = 0
    global_stats = coin_api.get_all_coins_ticker(start, limit)
    data_df = global_stats["data"]
    info = global_stats["info"]
    df = pd.DataFrame(data_df)
    df["coins_num"] = info["coins_num"]
    df["time"] = info["time"]
    for i in df.index:
        insert_query = "INSERT INTO {}({}) VALUES({})"
        cols = ','.join(list(df.columns))
        values = ["'"+str(df.at[i, col])+"'" for col in list(df.columns)]
        str_values = ','.join(list(values))
        try:
            cursor.execute(insert_query.format(config['TABLES']['DAILY_ALL_COINS'],cols, str_values).replace('rank', '`rank`'))
            db.commit()
            counter = counter + 1
        except mysql.connector.Error as err:
            print("Error occurred on inserting...", err)

    print("Inserted {} records to daily_all_coins_ticker...".format(counter))

def refresh_global_stats():
    try:
        cursor.callproc(config['STORED_PROCEDURE']['DAILY_GLOBAL'])
        db.commit()
        print("Successfully loaded data into {}...".format(config['MATERIALIZED']['DAILY_GLOBAL']))
    except mysql.connector.Error as err:
        print("Error occurred on inserting...", err)
    return

def refresh_all_coins_ticker():
    try:
        cursor.callproc(config['STORED_PROCEDURE']['DAILY_ALL_COINS'])
        db.commit()
        print("Successfully loaded data into {}...".format(config['MATERIALIZED']['DAILY_ALL_COINS']))
    except mysql.connector.Error as err:
        print("Error occurred on inserting...", err)
    return

def refresh_7d_coins_ticker():
    try:
        cursor.callproc(config['STORED_PROCEDURE']['DAILY_7D_TICKER'])
        db.commit()
        print("Successfully loaded data into {}...".format(config['MATERIALIZED']['DAILY_7D_TICKER']))
    except mysql.connector.Error as err:
        print("Error occurred on inserting...", err)
    return

# Reload MySQL Database
reload_global_stats()
reload_all_coins_ticker(0, 100)

# Load Latest data to Materialized Views
refresh_global_stats()
refresh_all_coins_ticker()
refresh_7d_coins_ticker()

db.close()