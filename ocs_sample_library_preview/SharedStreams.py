from typing import Any

from .BaseClient import BaseClient
from .SDS.SdsResultPage import SdsResultPage
from .SDS.SdsStream import SdsStream
from .SDS.SdsType import SdsType
from .PatchableSecurable import PatchableSecurable

from .Streams import Streams

class SharedStreams(PatchableSecurable, object):
    """
    Client for interacting with Streams shared in a Community
    """

    def __init__(self, client: BaseClient):
        """
        :param client: base client that handles auth and base routing
        """
        super().__init__(client=client, collection='Streams')

        self.__uri_api = client.uri_API
        self.__base_client = client

        # Streams client used to handle requests
        self.__streams = Streams(self.__base_client)

        self.__setPathAndQueryTemplates()

    def getStream(self, tenant_id: str, namespace_id: str, community_id: str, stream_id: str) -> SdsStream:
        """
        Retrieves a stream specified by 'stream_id' in a community specified by 'community_id' from the Sds Service
        :param tenant_id: tenant to work against
        :param namespace_id: namespace to work against
        :param community_id: community to work against
        :param stream_id: id of the stream
        :return:the Stream as SdsStream
        """
        self.__validateParameters(tenant_id, namespace_id, community_id, stream_id)
        headers = self.__base_client.getCommunityRequestHeaders(community_id=community_id)

        response = self.__base_client.request(
            'get',
            self.__stream_path.format(
                tenant_id=tenant_id,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream_id)),
            headers=headers)
        self.__base_client.checkResponse(
            response, f'Failed to get SdsStream, {stream_id}.')

        result = SdsStream.fromJson(response.json())
        return result

    def getStreamType(self, tenant_id: str, namespace_id: str, community_id: str, stream_id: str) -> SdsType:
        """
        Retrieves a stream specified by 'stream_id' in a community specified by 'community_id' from the Sds Service
        :param tenant_id: tenant to work against
        :param namespace_id: namespace to work against
        :param community_id: community to work against
        :param stream_id: id of the stream
        :return: the stream type as an SdsType
        """
        self.__validateParameters(tenant_id, namespace_id, community_id, stream_id)
        headers = self.__base_client.getCommunityRequestHeaders(community_id=community_id)

        response = self.__base_client.request(
            'get',
            self.__stream_path.format(
                tenant_id=tenant_id,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream_id)) + '/Type',
            headers=headers)
        self.__base_client.checkResponse(
            response, f'Failed to get SdsStream type, {stream_id}.')

        result = SdsType.fromJson(response.json())
        return result

    def getStreams(self, tenant_id: str, namespace_id: str, community_id: str, stream_id: str, query: str = '', skip: int = 0,
                   count: int = 100) -> list[SdsStream]:
        """
        Retrieves a list of streams associated with 'namespace_id' under the specified tenant and community
        :param tenant_id: tenant to work against
        :param namespace_id: namespace to work against
        :param community_id: community to work against
        :param stream_id: id of the stream
        :param query: filtering query
        :param skip: number of streams to skip for paging
        :param count: number of streams to limit to
        :return: array of SdsStreams
        """
        self.__validateParameters(tenant_id, namespace_id, community_id, stream_id)
        headers = self.__base_client.getCommunityRequestHeaders(community_id=community_id)

        response = self.__base_client.request(
            'get',
            self.__streams_path.format(
                tenant_id=tenant_id,
                namespace_id=namespace_id),
            params={'query': query, 'skip': skip, 'count': count},
            headers=headers)
        self.__base_client.checkResponse(
            response, 'Failed to get all SdsStreams.')
        
        content = response.json()
        results: list[SdsStream] = []
        for item in content:
            results.append(SdsStream.fromJson(item))
        return results

    # The following section provides functionality to interact with Data
    #  We assume the value(s) passed follow the Sds object patterns
    #  supporting fromJson and toJson method

    def getValue(self, tenant_id: str, namespace_id: str, community_id: str, stream_id: str, index: int, value_class: type = None) -> Any:
        """
        Retrieves JSON object from Sds Service for value specified by 'index' from Sds Service
        :param tenant_id: tenant to work against
        :param namespace_id: namespace to work against
        :param community_id: community to work against
        :param stream_id: id of the stream
        :param index: index at which to get a value
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson()  Default is None.
            If None returns a dynamic Python object from the data.
        :return: the value.  If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        self.__validateParameters(tenant_id, namespace_id, community_id, stream_id, index)
        headers = self.__base_client.getCommunityRequestHeaders(community_id=community_id)
        url=self.__stream_path.format(
                namespace_id=namespace_id,
                tenant_id=tenant_id,
                stream_id=self.__base_client.encode(stream_id))

        return self.__streams.getValueUrl(url, index, value_class, headers)

    def getFirstValue(self, tenant_id: str, namespace_id: str, community_id: str, stream_id: str, value_class: type = None) -> Any:
        """
        Retrieves JSON object from Sds Service the first value to be added to
            the stream specified by 'stream_id'
        :param tenant_id: tenant to work against
        :param namespace_id: namespace to work against
        :param community_id: community to work against
        :param stream_id: id of the stream
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson()  Default is None.
            If None returns a dynamic Python object from the data.
        :return: the value.  If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        self.__validateParameters(tenant_id, namespace_id, community_id, stream_id)
        headers = self.__base_client.getCommunityRequestHeaders(community_id=community_id)
        url=self.__stream_path.format(
                tenant_id=tenant_id,
                namespace_id=namespace_id,
                community_id=community_id,
                stream_id=self.__base_client.encode(stream_id))

        return self.__streams.getFirstValueUrl(url, value_class, headers)

    def getLastValue(self, tenant_id: str, namespace_id: str, community_id: str, stream_id: str, value_class: type = None) -> Any:
        """
        Retrieves JSON object from Sds Service the last value to be added to
            the stream specified by 'stream_id'
        :param tenant_id: tenant to work against
        :param namespace_id: namespace to work against
        :param community_id: community to work against
        :param stream_id: id of the stream
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson()  Default is None.
            If None returns a dynamic Python object from the data.
        :return: the value.  If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        self.__validateParameters(tenant_id, namespace_id, community_id, stream_id)
        headers = self.__base_client.getCommunityRequestHeaders(community_id=community_id)
        url = self.__stream_path.format(
            tenant_id=tenant_id,
            namespace_id=namespace_id,
            stream_id=self.__base_client.encode(stream_id))

        return self.__streams.getLastValueUrl(url, value_class, headers=headers)

    def getWindowValues(self, tenant_id: str, namespace_id: str, community_id: str, stream_id: str, start: str, end: str, value_class: type, filter: str = '') -> list[Any]:
        """
        Retrieves JSON object representing a window of values from the stream
            specified by 'stream_id'
        :param tenant_id: tenant to work against
        :param namespace_id: namespace to work against
        :param community_id: community to work against
        :param stream_id: id of the stream
        :param start: Starting index
        :param end: Ending index
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson().
            If None returns a dynamic Python object from the data.
        :param filter: An optional filter.  By Default it is ''.
        :return: an array of values.
            If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        self.__validateParameters(tenant_id, namespace_id, community_id, stream_id)
        headers = self.__base_client.getCommunityRequestHeaders(community_id=community_id)
        url = self.__stream_path.format(
            tenant_id=tenant_id,
            namespace_id=namespace_id,
            stream_id=self.__base_client.encode(stream_id))

        return self.__streams.getWindowValuesUrl(url, value_class, start, end, filter, headers)

    def getWindowValuesPaged(self, tenant_id: str, namespace_id: str, community_id: str, stream_id: str, value_class: type, start: str,
                                end: str, count: int, continuation_token: str = '', filter: str = '') -> SdsResultPage:
        """
        Retrieves JSON object representing a window of values from the stream
            specified by 'stream_id' using paging
        :param tenant_id: tenant to work against
        :param namespace_id: namespace to work against
        :param community_id: community to work against
        :param stream_id: id of the stream
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson().
            If None returns a dynamic Python object from the data.
        :param start: Starting index
        :param end: Ending index
        :param count: maximum number of events to return.
        :param continuationToken: token used to retrieve the next page of data.
        :param filter: An optional filter.  By Default it is ''.
        :return: an SdsResultPage containing the results and the next continuation token.
            If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        self.__validateParameters(tenant_id, namespace_id, community_id, stream_id, start, end, count)
        headers = self.__base_client.getCommunityRequestHeaders(community_id=community_id)
        url = self.__stream_path.format(
            tenant_id=tenant_id,
            namespace_id=namespace_id,
            stream_id=self.__base_client.encode(stream_id))

        return self.__streams.getWindowValuesPagedUrl(url, value_class, start, end, count, continuation_token, filter, headers)

    def getWindowValuesForm(self, tenant_id:str, namespace_id: str, community_id: str, stream_id: str, value_class: type, start: str,
                               end: str, form: str = '') -> list[Any]:
        """
        Retrieves JSON object representing a window of values from the stream
            specified by 'stream_id'.  Use this to get the data in a different
            return form
        :param tenant_id: tenant to work against
        :param namespace_id: namespace to work against
        :param community_id: community to work against
        :param stream_id: id of the stream
        :param value_class: use this to cast the value into a given type.
        Type must support .fromJson().
        If None returns a dynamic Python object from the data.
        :param start: Starting index
        :param end: Ending index
        :param form: form of the data
        :return: An array of the data in type specified if value_class
            defined.  Otherwise it is a dynamic Python object
        """
        self.__validateParameters(tenant_id, namespace_id, community_id, stream_id, start, end)
        headers = self.__base_client.getCommunityRequestHeaders(community_id=community_id)
        url = self.__stream_path.format(
            tenant_id=tenant_id,
            namespace_id=namespace_id,
            stream_id=self.__base_client.encode(stream_id))

        return self.__streams.getWindowValuesFormUrl(url, value_class, start, end, form, headers)

    def getRangeValues(self, tenant_id: str, namespace_id: str, community_id: str, stream_id: str, value_class: type, start: str,
                          skip: int, count: int, reversed: bool, boundary_type: str,
                          filter: str = '', stream_view_id: str = '') -> list[Any]:
        """
        Retrieves JSON object representing a range of values from the stream
            specified by 'stream_id'
        :param tenant_id: tenant to work against
        :param namespace_id: namespace to work against
        :param community_id: community to work against
        :param stream_id: id of the stream
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson(). If None returns a dynamic Python
            object from the data.
        :param start: Starting index
        :param skip: number of values to skip after start index.
            Important in paging
        :param count: number of values to return
        :param reversed: which direction to go when getting values
        :param boundary_type: the boundary condition to use.
            Can be an SdsBoundaryType or the integer value
        :param filter: An optional filter.  By Default it is ''.
        :param stream_view_id: streamview to map the results to
        :return: An array of the data in type specified if value_class
            is defined.  Otherwise it is a dynamic Python object
        """
        self.__validateParameters(tenant_id, namespace_id, community_id, start, skip, count, reversed, boundary_type)
        headers = self.__base_client.getCommunityRequestHeaders(community_id=community_id)
        url = self.__stream_path.format(
                        tenant_id=tenant_id,
                        namespace_id=namespace_id,
                        stream_id=self.__base_client.encode(stream_id))

        return self.__streams.getRangeValuesUrl(url, value_class, start, skip, count, reversed, boundary_type, filter, stream_view_id, headers)

    def getRangeValuesInterpolated(self, tenant_id: str, namespace_id: str, community_id: str, stream_id: str, value_class: type,
                                      start: str, end: str, count: int, filter: str = '') -> list[Any]:
        """
        Retrieves JSON object representing a range of values from the stream
            specified by 'stream_id'
        :param tenant_id: tenant to work against
        :param namespace_id: namespace to work against
        :param community_id: community to work against
        :param stream_id: id of the stream
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson(). If None returns a dynamic Python
            object from the data.
        :param start: starting index
        :param end:  ending index
        :param count: number of datapoints to retrieve
        :param filter: An optional filter.  By Default it is ''.
        :return: An array of the data in type specified if value_class is
        defined.  Otherwise it is a dynamic Python object
        """
        self.__validateParameters(tenant_id, namespace_id, community_id, stream_id, start, end, count)
        headers = self.__base_client.getCommunityRequestHeaders(community_id=community_id)
        url = self.__stream_path.format(
                tenant_id=tenant_id if tenant_id != '' else tenant_id,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream_id))

        return self.__streams.getRangeValuesInterpolatedUrl(url, value_class, start, end, count, filter, headers)

    def getIndexCollectionValues(self, tenant_id: str, namespace_id: str, community_id: str, stream_id: str, value_class: type,
                                      index: list[str]) -> list[Any]:
        """
        Retrieves JSON object representing values at specific indexes from the stream
            specified by 'stream_id'
        :param tenant_id: tenant to work against
        :param namespace_id: namespace to work against
        :param community_id: community to work against
        :param stream_id: id of the stream
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson(). If None returns a dynamic Python
            object from the data.
        :param index: One or more indexes to retrieve events at
        :return: An array of the data in type specified if value_class is
        defined.  Otherwise it is a dynamic Python object
        """
        self.__validateParameters(tenant_id, namespace_id, community_id, stream_id, index)
        headers = self.__base_client.getCommunityRequestHeaders(community_id=community_id)
        url = self.__stream_path.format(
                tenant_id=tenant_id,
                namespace_id=namespace_id,
                stream_id=self.__base_client.encode(stream_id))

        return self.__streams.getIndexCollectionValuesUrl(url, value_class, index, headers)

    def getSampledValues(self, tenant_id: str, namespace_id: str, community_id: str, stream_id: str, value_class: type, start: str,
                            end: str, sample_by: str, intervals: str, filter: str = '', stream_view_id: str = '') -> list[Any]:
        """
        Returns data sampled by intervals between a specified start and end index.
        :param tenant_id: tenant to work against
        :param namespace_id: namespace to work against
        :param community_id: community to work against
        :param stream_id: id of the stream
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson().
            If None returns a dynamic Python object from the data.
        :param start: starting index for intervals
        :param end:  ending index for intervals
        :param sample_by: property or properties to use when sampling
        :param intervals: number of intervals requested
        :param filter: optional filter to apply
        :param stream_view_id: optional streamview identifier
        :return: An array of the data in type specified if value_class is
            defined.  Otherwise it is a dynamic Python object
        """
        self.__validateParameters(tenant_id, namespace_id, community_id, stream_id)
        headers = self.__base_client.getCommunityRequestHeaders(community_id=community_id)
        url = self.__stream_path.format(
            tenant_id=tenant_id,
            namespace_id=namespace_id,
            stream_id=self.__base_client.encode(stream_id))

        return self.__streams.getSampledValuesUrl(url, value_class, start, end, sample_by, intervals, filter, stream_view_id, headers)

    def getSummaries(self, tenant_id: str, namespace_id: str, community_id: str, stream_id: str, value_class: type, start: str,
                        end: str, count: int, stream_view_id: str = '', filter: str = '') -> list[Any]:
        """
        Retrieves JSON object representing a summary for the stream specified by 'stream_id'
        :param tenant_id: tenant to work against
        :param namespace_id: namespace to work against
        :param community_id: community to work against
        :param stream_id: id of the stream
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson().
            If None returns a dynamic Python object from the data.
        Note- for this function the default return json string is not a
            JSON array of the value, so the same type definition won't work.
        :param start: starting index
        :param end:  ending index
        :param count: number of datapoints in summary
        :param stream_view_id: streamview to tranform the data into
        :param filter: filter to apply
        :return: An array of the data summary in type specified if value_class
            is defined.  Otherwise it is a dynamic Python object
        """
        self.__validateParameters(tenant_id, namespace_id, community_id, stream_id)
        headers = self.__base_client.getCommunityRequestHeaders(community_id=community_id)
        url = self.__stream_path.format(
            tenant_id=tenant_id,
            namespace_id=namespace_id,
            stream_id=self.__base_client.encode(stream_id))

        return self.__streams.getSummariesUrl(url, value_class, start, end, count, stream_view_id, filter, headers)

    def getStreamsWindow(self, tenant_id: str, namespace_id: str, community_id: str, stream_ids: list[str], value_class: type,
                         start: str, end: str, join_mode: int = 1) -> list[Any]:
        """
        Retrieves JSON object representing a window of values from the stream
             specified by 'stream_id'
        :param tenant_id: tenant to work against
        :param namespace_id: namespace to work against
        :param community_id: community to work against
        :param stream_id: id of the stream
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson(). If None returns a dynamic Python
            object from the data.
        :param start: Starting index
        :param end: Ending index
        :param joinMode: Join mode, supports numbers or strings.
            Defaults to outer
        :return: an array of values.
            If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        self.__validateParameters(namespace_id, stream_ids, start, end)
        headers = self.__base_client.getCommunityRequestHeaders(community_id=community_id)
            
        response = self.__base_client.request(
            'get',
            self.__bulk_join_path.format(
                tenant_id=tenant_id,
                namespace_id=namespace_id),
            params={'streams': ','.join(stream_ids),
                    'startIndex': start,
                    'endIndex': end,
                    'joinMode': join_mode},
            headers=headers)
        self.__base_client.checkResponse(
            response, f'Failed to get bulk values for SdsStream: {stream_ids}.')

        content = response.json()
        if value_class is None:
            return content

        values = []
        for valueArray in content:
            valuesInside = []
            for value in valueArray:
                valuesInside.append(value_class.fromJson(value))
            values.append(valuesInside)
        return values

    # private methods

    def __validateParameters(*args):
        for arg in args:
            if arg is None:
                raise TypeError
            if type(arg) is list and not arg:
                raise TypeError

    def __setPathAndQueryTemplates(self):
        """
        creates the urls that are used
        :return:
        """
        self.__base_path = self.__uri_api + \
            '/Tenants/{tenant_id}/Namespaces/{namespace_id}'
        self.__streams_path = self.__base_path + '/Streams'
        self.__stream_path = self.__streams_path + '/{stream_id}'
        self.__bulk_join_path = self.__base_path + '/Bulk/Streams/Data/Joins'