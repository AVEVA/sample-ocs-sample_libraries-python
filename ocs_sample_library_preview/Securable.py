from jsonpatch import JsonPatch
from typing import Any

from .BaseClient import BaseClient
from .Security.AccessControlList import AccessControlList
from .Security.Owner import Owner

class Securable(object):
    """
    Client for interacting with the access control of a collection
    """

    def __init__(self, client: BaseClient, collection: str):
        """
        :param client: base client that handles auth and base routing
        :param acl_path: The access control path of the object
        """
        self.__tenant = client.tenant
        self.__uri_api = client.uri_API
        self.__base_client = client
        self.__collection = collection

        self.__setPathAndQueryTemplates()

    def getDefaultAccessControl(self, namespace_id: str) -> AccessControlList:
        """
        Get a collection's default access control list
        """
        response = self.__base_client.request(
            'get', self.__default_collection_acl_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id))
        self.__base_client.checkResponse(
            response, f'Failed to get collection access control, {self.__collection}.')
        result = AccessControlList.fromJson(response.json())
        return result

    def updateDefaultAccessControl(self, namespace_id: str, access_control: AccessControlList):
        """
        Update a collection's default access control list
        :param access_control: The access control list
        """
        if access_control is None:
            raise TypeError

        response = self.__base_client.request(
            'put', self.__default_collection_acl_path(
                tenant_id=self.__tenant,
                namespace_id=namespace_id),
            data=access_control.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to update collection access control, {self.__collection}.')

    def patchDefaultAccessControl(self, namespace_id: str, patch: JsonPatch):
        """
        Patch a collection's default access control list
        :param patch: A JSON Patch document describing the patch operations
        """
        if patch is None:
            raise TypeError

        response = self.__base_client.request(
            'patch', self.__default_collection_acl_path(
                tenant_id=self.__tenant,
                namespace_id=namespace_id),
            data=patch.to_string())
        self.__base_client.checkResponse(
            response, f'Failed to patch collection access control, {self.__collection}.')

    def getAccessControl(self, namespace_id: str, item_id: str) -> AccessControlList:
        """
        Get an item's access control list
        :param item_id: The item identifier
        """
        if item_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get', self.__item_acl_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                item_id=item_id))
        self.__base_client.checkResponse(
            response, f'Failed to get access control, {item_id} in collection {self.__collection}.')

        result = AccessControlList.fromJson(response.json())
        return result

    def updateAccessControl(self, namespace_id: str, item_id: str, access_control: AccessControlList):
        """
        Update an item's access control list
        :param item_id: The item identifier
        :param access_control: The access control list
        """
        if item_id is None:
            raise TypeError
        if access_control is None:
            raise TypeError

        response = self.__base_client.request(
            'put', self.__item_acl_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                item_id=item_id),
            data=access_control.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to update access control, {item_id} in collection {self.__collection}.')

    def patchAccessControl(self, namespace_id: str, item_id: str, patch: JsonPatch):
        """
        Patch an item's access control list
        :param item_id: The item identifier
        :param patch: A JSON Patch document describing the patch operations
        """
        if item_id is None:
            raise TypeError
        if patch is None:
            raise TypeError

        response = self.__base_client.request(
            'patch', self.__item_acl_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                item_id=item_id),
            data=patch.to_string())
        self.__base_client.checkResponse(
            response, f'Failed to patch access control, {item_id} in collection {self.__collection}.')

    def getOwner(self, namespace_id: str, item_id: str) -> Owner:
        """
        Get an item's owner
        :param item_id: The item identifier
        """
        if item_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get', self.__item_owner_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                item_id=item_id))
        self.__base_client.checkResponse(
            response, f'Failed to get owner, {item_id} in collection {self.__collection}.')

        result = Owner.fromJson(response.json())
        return result

    def updateOwner(self, namespace_id: str, item_id: str, owner: Owner):
        """
        Update an item's access control list
        :param item_id: The item identifier
        :param owner: The owner
        """
        if item_id is None:
            raise TypeError
        if owner is None:
            raise TypeError

        response = self.__base_client.request(
            'put', self.__item_owner_path.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                item_id=item_id),
            data=owner.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to update access control, {item_id} in collection {self.__collection}.')

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        creates the urls that are used
        :return:
        """
        if self.__collection == 'Namespaces':
          self.__base_path = self.__uri_api + \
              '/Tenants/{tenant_id}'
        else:
          self.__base_path = self.__uri_api + \
              '/Tenants/{tenant_id}/Namespaces/{namespace_id}'

        self.__default_collection_acl_path = self.__base_path + \
            '/AccessControl/' + self.__collection
        
        self.__collection_path = self.__base_path + '/' + self.__collection

        self.__item_path = self.__collection_path + '/{item_id}'
        self.__item_acl_path = self.__item_path + '/AccessControl'
        self.__item_owner_path = self.__item_path + '/Owner'
