import pytest


class TestPostLogin:
    """
    Testing POST method.
    """
    resource = 'login'

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('data', [
        {'email': 'test@test', 'password': 'test'}
    ])
    def test_success(self, base_request, data):
        """
        Valid values.
        """
        response = base_request.method(method_name='POST', resource=self.resource, data=data,
                                       msg='User "{}" logged in (200)'.format(data['email']))
        assert response.status_code == 200
        assert 'token' in response.json()

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @pytest.mark.parametrize('data, error', [
        ({'email': 'test@test'}, 'Missing password'),
        ({'email': None, 'password': None}, 'Missing email or username'),
        ({'password': 'test'}, 'Missing email or username'),
    ])
    def test_failure(self, base_request, data, error):
        """
        Invalid or missing values.
        """
        response = base_request.method(method_name='POST', resource=self.resource, data=data,
                                       msg='Login has failed (400)')
        assert response.status_code == 400
        assert 'error' in response.json() and response.json()['error'] == error
