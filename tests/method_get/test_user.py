import pytest


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
class TestGetUser:
    """
    Testing GET method.
    """
    resource = 'users'

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('page', [-1, 1, 4])
    def test_list_found(self, base_request, page):
        """
        Valid page values.
        """
        response = base_request.method(method_name='GET', resource=self.resource, params={'page': page},
                                       msg='{} is found (200)'.format(self.resource))
        assert response.status_code == 200
        assert response.json()['page'] == page
        assert len(response.json()['data'])

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_list_page_without_page_param(self, base_request):
        """
        If you don't pass page param, the system implicitly assign page = 1.
        """
        response = base_request.method(method_name='GET', resource=self.resource,
                                       msg='{} is found (200)'.format(self.resource))
        assert response.status_code == 200
        assert response.json()['page'] == 1
        assert len(response.json()['data'])

    @pytest.mark.parametrize('page', [0, 'foo'])
    def test_list_page_ignored(self, base_request, page):
        """
        Page values of zero, None and string are substituted with 1.
        """
        response = base_request.method(method_name='GET', resource=self.resource, params={'page': page},
                                       msg='{} is found (200)'.format(self.resource))
        assert response.status_code == 200
        assert response.json()['page'] == 1
        assert len(response.json()['data'])

    @pytest.mark.parametrize('page', [5])
    def test_list_not_found(self, base_request, page):
        """
        The value is above valid boundary value.
        """
        response = base_request.method(method_name='GET', resource=self.resource, params={'page': page},
                                       msg='{} is found (200)'.format(self.resource))
        assert response.status_code == 200
        assert response.json()['page'] == page
        assert not len(response.json()['data'])

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('resource_id', [1, 12])
    def test_found(self, base_request, resource_id):
        """
        Valid values.
        """
        resource = '/'.join([self.resource, str(resource_id)])
        response = base_request.method(method_name='GET', resource=resource,
                                       msg='{} is found (200)'.format(resource))
        assert response.status_code == 200
        assert response.json()['data']['id'] == resource_id

    @pytest.mark.parametrize('resource_id', [-1, 0, 13])
    def test_not_found_for_digit(self, base_request, resource_id):
        """
        Values are out of scope of the valid values.
        """
        resource = '/'.join([self.resource, str(resource_id)])
        response = base_request.method(method_name='GET', resource=resource,
                                       msg='{} not found (404)'.format(resource))
        assert response.status_code == 404

    @pytest.mark.parametrize('resource_id', ['foo'])
    def test_not_found_for_letters(self, base_request, resource_id):
        """
        Non-digit value is not valid.
        """
        resource = '/'.join([self.resource, str(resource_id)])
        response = base_request.method(method_name='GET', resource=resource,
                                       msg='{} not found (404)'.format(resource))
        assert response.status_code == 404
