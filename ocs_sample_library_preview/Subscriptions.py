import json

from .BaseClient import BaseClient
from .OMF.Subscription import Subscription
from .Securable import Securable


class Subscriptions(Securable, object):
    """
    Client for interacting with OCS Subscription
    """

    def __init__(self, client: BaseClient):
        """
        Initializes the Subscriptions client
        :param client: This is the base client that is used to make REST calls
        """
        super().__init__(client=client, collection='Subscriptions')

        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def getSubscriptionById(self, namespace_id: str, subscription_id: str) -> Subscription:
        """
        Returns the specified Subscription
        :param namespace_id: The namespace identifier
        :param subscription_id: The subscription identifier
        """
        if namespace_id is None:
            raise TypeError
        if subscription_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__subscription_path.format(
            namespace_id=namespace_id, subscription_id=subscription_id))
        self.__base_client.checkResponse(
            response, f'Failed to get Subscription, {subscription_id}.')

        result = Subscription.fromJson(response.json())
        return result

    def getSubscriptions(self, namespace_id: str, query: str = '', skip: int = 0, count: int = 100,
                  ) -> list[Subscription]:
        """
        Returns a list of Subscriptions
        :param namespace_id: The namespace identifier
        :param query: An optional query string to search for matching subscriptions.
        :param skip: An optional parameter representing the zero-based offset of the first subscription to
        retrieve. If not specified, a default value of 0 is used.
        :param count: An optional parameter, between 1 and 1000 (inclusive), that represents the
        maximum number of retrieved Subscriptions. If not specified, the default is 100.
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__subscriptions_path.format(
            namespace_id=namespace_id), params={'skip': skip, 'count': count, 'query': query})
        self.__base_client.checkResponse(response, f'Failed to get Subscriptions.')

        results = []
        for i in response.json():
            results.append(Subscription.fromJson(i))
        return results

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        Creates URLs that are used by the client
        :return:
        """
        self.__base_path = self.__base_client.uri_API + '/Tenants/' + \
            self.__base_client.tenant + '/Namespaces/{namespace_id}'
        self.__subscriptions_path = self.__base_path + '/subscriptions'
        self.__subscription_path = self.__subscriptions_path + '/{subscription_id}'
