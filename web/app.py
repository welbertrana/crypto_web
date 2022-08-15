from flask import Flask, render_template
import app_module as module
import configparser

config = configparser.ConfigParser()

# Read Config Files
config.read('config/dev_config.ini')

app = Flask(__name__)

@app.route('/')
def index():
    # Get Data from API Endpoints
    global_stat = module.load_global_stats()
    top_coins = module.get_top_coins()
    top_gainers = module.get_top_gains()
    top_losers = module.get_top_losers()

    # Extract list of Coin Symbols from data
    top_list = [data["symbol"] for data in top_gainers]
    loser_list = [data["symbol"] for data in top_losers]

    # Get and Create Chart Data for plotting
    top_chartdata = module.get_7d_data(top_list)
    loser_chartdata = module.get_7d_data(loser_list)

    return render_template('index.html',
                        stat = global_stat, 
                        top = top_coins,
                        gainer = top_gainers,
                        losers = top_losers,
                        top_chart = top_chartdata,
                        loser_chart = loser_chartdata)

if __name__ == "__main__":
    app.run(debug=True, port = config['APP']['PORT'])
    