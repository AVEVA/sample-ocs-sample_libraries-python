import json

from .BaseClient import BaseClient
from .OMF.Topic import Topic
from .Securable import Securable


class Topics(Securable, object):
    """
    Client for interacting with OCS Topic
    """

    def __init__(self, client: BaseClient):
        """
        Initializes the Topics client
        :param client: This is the base client that is used to make REST calls
        """
        super().__init__(client=client, collection='Topics')

        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def getTopicById(self, namespace_id: str, topic_id: str) -> Topic:
        """
        Returns the specified Topic
        :param namespace_id: The namespace identifier
        :param topic_id: The topic identifier
        """
        if namespace_id is None:
            raise TypeError
        if topic_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__topic_path.format(
            namespace_id=namespace_id, topic_id=topic_id))
        self.__base_client.checkResponse(
            response, f'Failed to get Topic, {topic_id}.')

        result = Topic.fromJson(response.json())
        return result

    def getTopics(self, namespace_id: str, query: str = '', skip: int = 0, count: int = 100,
                  ) -> list[Topic]:
        """
        Returns a list of Topics
        :param namespace_id: The namespace identifier
        :param query: An optional query string to search for matching topics.
        :param skip: An optional parameter representing the zero-based offset of the first topic to
        retrieve. If not specified, a default value of 0 is used.
        :param count: An optional parameter, between 1 and 1000 (inclusive), that represents the
        maximum number of retrieved Topics. If not specified, the default is 100.
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request('get', self.__topics_path.format(
            namespace_id=namespace_id), params={'skip': skip, 'count': count, 'query': query})
        self.__base_client.checkResponse(response, f'Failed to get Topics.')

        results = []
        for i in response.json():
            results.append(Topic.fromJson(i))
        return results

    # private methods

    def __setPathAndQueryTemplates(self):
        """
        Creates URLs that are used by the client
        :return:
        """
        self.__base_path = self.__base_client.uri_API + '/Tenants/' + \
            self.__base_client.tenant + '/Namespaces/{namespace_id}'
        self.__topics_path = self.__base_path + '/topics'
        self.__topic_path = self.__topics_path + '/{topic_id}'
