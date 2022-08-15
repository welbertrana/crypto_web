try:
    from crypto_api import app
    import json
    import unittest
except Exception as e:
    print("Some modules are Missing {}...".format(e))

class FlaskTest(unittest.TestCase):

    # Check if Index Response is 200
    def test_index(self):
        test = app.test_client(self)
        response = test.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    # Check if Global Stat Endpoint Response is 200
    def test_global_stat(self):
        test = app.test_client(self)
        response = test.get("/global_stat")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    # Check if Get All Ticker Endpoint Response is 200
    def test_get_all_ticker(self):
        test = app.test_client(self)
        response = test.get("/get_all_ticker")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    # Check if Get Top Coins Endpoint Response is 200
    def test_get_top_coins(self):
        test = app.test_client(self)
        response = test.get("/get_top_coins")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check if Get Ticker Endpoint Response is 200
    def test_get_ticker(self):
        test = app.test_client(self)
        payload = {
            "symbol": "ETH"
        }
        response = test.post("/get_ticker", data=json.dumps(payload))
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    # Check if Top Gainers Endpoint Response is 200
    def test_get_top_gainers(self):
        test = app.test_client(self)
        response = test.get("/get_top_gainers")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    # Check if Top Losers Endpoint Response is 200
    def test_get_top_losers(self):
        test = app.test_client(self)
        response = test.get("/get_top_losers")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    # Check if 7 Days Data Endpoint Response is 200
    def test_get_7d_data(self):
        test = app.test_client(self)
        payload = {
            "coinlist": ["BTC","ETH"]
        }
        response = test.post("/get_7d_data", data=json.dumps(payload))
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

if __name__ == "__main__":
    unittest.main()