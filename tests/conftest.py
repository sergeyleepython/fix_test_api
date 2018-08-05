import urllib.parse

import pytest
import requests
from requests_toolbelt.utils import dump


@pytest.fixture()
def base_request():
    """
    
    :return: 
    """

    class BaseRequest():
        """
        
        """
        base_url = 'https://reqres.in/api/'

        headers = {
            'Content-type': 'application/json',
            'Accept': 'text/plain',
            'User-Agent': 'Mozilla/5.0'
        }

        timeout = 5

        def method(self, method_name, resource='', **kwargv):
            url = urllib.parse.urljoin(self.base_url, resource)
            response = requests.request(
                method=method_name,
                url=url,
                headers=self.headers,
                params=kwargv.get('params', None),
                json=kwargv.get('data', None),
                timeout=self.timeout
            )
            if 'msg' in kwargv:
                pytest.allure.attach(kwargv['msg'],
                                     dump.dump_all(response).decode('utf-8'))
            return response

    return BaseRequest()


def pytest_addoption(parser):
    parser.addoption('--testing-stand', action='store',
                     default=False, help="Stand on which to run tests")


@pytest.fixture
def testing_stand(request):
    return request.config.getoption("--testing-stand")
