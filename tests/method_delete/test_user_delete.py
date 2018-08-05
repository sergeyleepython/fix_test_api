import pytest


class TestDeleteUser:
    """
    Testing DELETE method.
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
        response = base_request.method(method_name='DELETE', resource=self.resource, data=data,
                                       msg='User is deleted (204)')
        assert response.status_code == 204
