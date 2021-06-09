from .BaseClient import BaseClient
from .Security.Role import Role


class Roles(object):
    """
    Client for interacting with OCS Roles
    """

    def __init__(self, client: BaseClient):
        """
        Initializes the Roles client
        :param client: This is the base client that is used to make REST calls
        """
        self.__base_client = client
        self.__setPathAndQueryTemplates()

    def getRoleById(self, role_id: str) -> Role:
        """
        Returns the specified role
        :param role_id: The role identifier
        """
        if role_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get', self.__role_path.format(role_id=role_id))
        self.__base_client.checkResponse(
            response, f'Failed to get role, {role_id}.')

        result = Role.fromJson(response.json())
        return result

    def getRoles(self, skip: int = 0, count: int = 100) -> list[Role]:
        """
        Returns a list of roles
        :param skip: An optional parameter representing the zero-based offset of the first role to
        retrieve. If not specified, a default value of 0 is used.
        :param count: An optional parameter, between 1 and 1000 (inclusive), that represents the
        maximum number of retrieved roles. If not specified, the default is 100.
        """
        response = self.__base_client.request('get', self.__roles_path, params={
                                              'skip': skip, 'count': count})
        self.__base_client.checkResponse(response, f'Failed to get roles.')

        results = []
        for i in response.json():
            results.append(Role.fromJson(i))
        return results

    def createRole(self, role: Role) -> Role:
        """
        Creates a new tenant role
        :param role: A role object
        """
        if role is None or not isinstance(role, Role):
            raise TypeError

        response = self.__base_client.request(
            'post', self.__roles_path, data=role.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create role')

        result = Role.fromJson(response.json())
        return result

    def updateRole(self, role: Role) -> Role:
        """
        Updates a tenant role with a specified Id
        :param role: A role object
        """
        if role is None or not isinstance(role, Role):
            raise TypeError

        response = self.__base_client.request(
            'put', self.__role_path.format(role_id=role.Id), data=role.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to update role, {role.Id}')

        result = Role.fromJson(response.json())
        return result

    def deleteRole(self, role_id: str):
        """
        Deletes a tenant, non built-in role
        :param role_id: The role identifier
        """
        if role_id is None:
            raise TypeError

        response = self.__base_client.request(
            'delete', self.__role_path.format(role_id=role_id))
        self.__base_client.checkResponse(
            response, f'Failed to delete role, {role_id}.')

    def __setPathAndQueryTemplates(self):
        """
        Creates URLs that are used by the client
        : return:
        """
        self.__roles_path = self.__base_client.uri_API + '/Tenants/' + \
            self.__base_client.tenant + '/Roles'
        self.__role_path = self.__roles_path + '/{role_id}'
