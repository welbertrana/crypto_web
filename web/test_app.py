try:
    from app import app
    import unittest
except Exception as e:
    print("Some modules are Missing {}...".format(e))

class FlaskTest(unittest.TestCase):

    # Check if Website fully loads
    def test_index(self):
        test = app.test_client(self)
        response = test.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


if __name__ == "__main__":
    unittest.main()