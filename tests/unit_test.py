import unittest
import requests
import sys
sys.path.append('.')
from config import GitConfig


class UnitTest(unittest.TestCase):

    def test_github_config(self):
        """this function is created to test github configuration e.g. github api server (url) is up and running,
        header is correct, access token is valid and correct etc."""
        header = {'Accept': GitConfig.GIT_DEV_VERSION, 'Authorization': "Token " + GitConfig.GIT_API_TOKEN}
        request_url = f"{GitConfig.GIT_API_URL}"
        request_result = requests.get(request_url, headers=header)
        self.assertEqual(request_result.status_code, 200)


if __name__ == '__main__':
    # todo: more tests can be added for star info in dataframe and graph, csv created in csv_downloads or not,
    #  flask api responses etc.
    unittest.main()