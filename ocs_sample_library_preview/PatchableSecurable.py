from jsonpatch import JsonPatch

from .BaseClient import BaseClient
from .Securable import Securable

class PatchableSecurable(Securable, object):
    """
    Client for interacting with the access control of a collection that is patchable
    """

    def __init__(self, client: BaseClient, collection: str):
        """
        :param client: base client that handles auth and base routing
        :param acl_path: The access control path of the object
        """
        super().__init__(client=client, collection=collection)

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
