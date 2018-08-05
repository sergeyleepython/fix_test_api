import pytest


class TestPostUser:
    """
    Testing POST method.
    """
    resource = 'users'

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('data', [
        {'name': 'morpheus', 'job': 'leader'}
    ])
    def test_create(self, base_request, data):
        """
        Valid values.
        """
        response = base_request.method(method_name='POST', resource=self.resource, data=data,
                                       msg='User "{}" is created (201)'.format(data['name']))
        assert response.status_code == 201
        assert int(response.json()['id']) > 0 and response.json()['name'] == data['name']
