
import api_service as api
import math
import datetime
from datetime import datetime
import random 

# Return Random Hex Color every execution
def getRandomColor():
    letters = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = '#'
    x = 0
    while x < 6:
        color += letters[random.randint(0,len(letters)-1)]
        x = x + 1
  
    return color

# Converts Number digits into worded format
def millify(n):
    millnames = ['',' Thousand',' Million',' Billion',' Trillion']
    try:
        n = float(n)
        millidx = max(0,min(len(millnames)-1,
                            int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
        if millidx == 1:
            millidx = 0 # Dont convert Thousand
        return '{:.3f}{}'.format(n / 10**(3 * millidx), millnames[millidx])
    except:
        return ''
        
# Change date to proper formatting
def fix_date(date):
    datetime_obj=datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    return datetime_obj.strftime("%B %d, %Y %I:%M:%S %p")

# Fix Data Formatting for each fields
def clean_values(data):
    percent_fields = ["btc_d", "eth_d", "mcap_change", "volume_change","avg_change_percent","percent_change_24h", "percent_change_1h", "percent_change_7d"]
    int_fields = ["coins_count", "active_markets", "rank", "price_usd", "id", "price_btc", "coins_num"]
    text_fields = ["symbol", "name", "nameid"]
    for key in data:
        if (key in percent_fields):
            data[key] = str(data[key])+'%'
        elif (key in int_fields):
            data[key] = data[key]
        elif (key in text_fields):
            data[key] = str(data[key])
        elif (key == "date"):
            data[key] = fix_date(data[key])
        elif (key == "time"):
            data[key] = data[key]
        else:
            if (data[key]):
                data[key] = millify(data[key])   

    return data

# Helper function for formatting Chart Data
def create_chart_mapping(data):
    tmp_name = ''
    tmp_dict = {}
    tmp_change = []
    tmp_time = []
    datasets = []
    labels = []
    counter = 0
    for items in data:
        if tmp_name == '':
            tmp_name = items['name']

        if items['name'] != tmp_name:
            color = getRandomColor()
            tmp_dict = {
                'label': tmp_name,
                'data': tmp_change,
                'backgroundColor': color,
                'borderColor': color,
                'lineTension': 0.1
            }
            labels = tmp_time
            datasets.append(tmp_dict)

            tmp_change = []
            tmp_time = []
            tmp_name = items['name']

        if items['name'] == tmp_name:
            tmp_change.append(items['percent_change_7d'])
            dtime_format = datetime.fromtimestamp(int(items['time']))
            dtime_str = dtime_format.strftime("%m-%d-%Y %I:%M %p")
            tmp_time.append(dtime_str)
        
        if (counter == len(data) - 1):
            color = getRandomColor()
            tmp_dict = {
                'label': tmp_name,
                'data': tmp_change,
                'backgroundColor': color,
                'borderColor': color,
                'lineTension': 0.1
            }
            labels = tmp_time
            datasets.append(tmp_dict)
        counter += 1


    chartData = {
        'labels': labels,
        'datasets': datasets
    }

    return chartData

# Start of Functions to call API Service
def load_global_stats():
    global_stat = api.get_global_stats()
    global_stat = clean_values(global_stat)
    return global_stat

def get_top_coins():
    top_coin = api.get_top_coins()
    result = []
    for coin in top_coin:
        result.append(clean_values(coin))
    return result

def get_top_gains():
    top_gains = api.get_top_gains()
    result = []
    for coin in top_gains:
        result.append(clean_values(coin))
    return result

def get_top_losers():
    top_losers = api.get_top_losers()
    result = []
    for coin in top_losers:
        result.append(clean_values(coin))
    return result

def get_7d_data(list):
    payload = {
        "coinlist": list
    }
    data_7d = api.get_7d_data(payload)
    chart_data = create_chart_mapping(data_7d)
    return chart_data
# End of Functions to call API Service