import pytest


class TestPutUser:
    """
    Testing PUT method.
    """
    resource = 'users'

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('data', [
        {'name': 'neo', 'job': 'worker'}
    ])
    @pytest.mark.parametrize('resource_id', [1])
    def test_update(self, base_request, data, resource_id):
        """
        Valid values.
        """
        response = base_request.method(method_name='PUT', resource=self.resource, data=data,
                                       msg='User is replaced (200)')
        assert response.status_code == 200
        assert response.json()['job'] == data['job'] and 'updatedAt' in response.json()
