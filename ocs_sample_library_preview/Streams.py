import json
from typing import Any

from .BaseClient import BaseClient
from .SDS.SdsBoundaryType import SdsBoundaryType
from .SDS.SdsStreamView import SdsStreamView
from .SDS.SdsResultPage import SdsResultPage
from .SDS.SdsStream import SdsStream
from .SDS.SdsType import SdsType
from .SDS.SdsStreamViewMap import SdsStreamViewMap


class Streams(object):
    """
    Client for interacting with Streams
    """

    def __init__(self, client: BaseClient):
        """
        :param client: base client that handles auth and base routing
        """
        self.__tenant = client.tenant
        self.__uri_api = client.uri_API
        self.__base_client = client

        self.__setPathAndQueryTemplates()

    def getStreamView(self, namespace_id: str, stream_view_id: str) -> SdsStreamView:
        """
        Retrieves the streamView specified by 'stream_view_id' from Sds Service
        :param namespace_id: namespace to work against
        :param stream_view_id: streamview id to get
        :return: Stream view as SdsStreamView
        """
        if namespace_id is None:
            raise TypeError
        if stream_view_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__streamViewsPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_view_id=stream_view_id))
        self.__base_client.checkResponse(
            response, f'Failed to get SdsStreamView, {stream_view_id}.')

        result = SdsStreamView.fromJson(response.json())
        return result

    def getStreamViewMap(self, namespace_id: str, stream_view_id: str) -> SdsStreamViewMap:
        """
        Retrieves the streamView map specified by 'stream_view_id' from Sds
            Service
        :param namespace_id: namespace to work against
        :param stream_view_id:  streamview map to get
        :return:
        """
        if namespace_id is None:
            raise TypeError
        if stream_view_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__streamViewsPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_view_id=stream_view_id) + '/Map')
        self.__base_client.checkResponse(
            response, f'Failed to get SdsStreamViewMap, {stream_view_id}.')

        result = SdsStreamViewMap.fromJson(response.json())
        return result

    def getStreamViews(self, namespace_id: str, skip: int = 0,
                       count: int = 100) -> list[SdsStreamView]:
        """
        Retrieves a list of streamViews associated with the specified
            'namespace_id' under the current tenant
        :param namespace_id: namespace to work against
        :param skip: number of streamviews to skip for paging
        :param count: number streamviews in a page
        :return: array of SdsStreamviews
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__getStreamViewsPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id),
            params={'skip': skip, 'count': count})
        self.__base_client.checkResponse(
            response, 'Failed to get all SdsStreamViews.')

        content = response.json()
        results = []
        for item in content:
            results.append(SdsStreamView.fromJson(item))
        return results

    def getOrCreateStreamView(self, namespace_id: str, stream_view: SdsStreamView) -> SdsStreamView:
        """
        Tells Sds Service to create a streamView based on a local
            SdsStreamView object
        :param namespace_id: namespace to work against
        :param stream_view: Streamview object to create in OCS
        :return: created Streamview as SdsStreamview
        """
        if namespace_id is None:
            raise TypeError
        if stream_view is None or not isinstance(stream_view, SdsStreamView):
            raise TypeError

        response = self.__base_client.request(
            'post',
            self.__streamViewsPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_view_id=stream_view.Id),
            data=stream_view.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create SdsStreamView, {stream_view.Id}.')

        result = SdsStreamView.fromJson(response.json())
        return result

    def createOrUpdateStreamView(self, namespace_id: str, stream_view: SdsStreamView):
        """
        Tells Sds Service to create a streamView based on a local SdsStreamView object
        :param namespace_id: namespace to work against
        :param stream_view: Streamview object to create or update in OCS
        :return: created Streamview as SdsStream
        """
        if namespace_id is None:
            raise TypeError
        if stream_view is None or not isinstance(stream_view, SdsStreamView):
            raise TypeError

        response = self.__base_client.request(
            'put',
            self.__streamViewsPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_view_id=stream_view.Id),
            data=stream_view.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create SdsStreamView, {stream_view.Id}.')

    def deleteStreamView(self, namespace_id: str, stream_view_id: str):
        """
        Tells Sds Service to delete the streamView with the specified
            'stream_view_id'
        :param namespace_id: namespace to work against
        :param stream_view_id: id of streamview to delete
        :return:
        """
        if namespace_id is None:
            raise TypeError
        if stream_view_id is None:
            raise TypeError

        response = self.__base_client.request(
            'delete',
            self.__streamViewsPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_view_id=stream_view_id))
        self.__base_client.checkResponse(
            response, f'Failed to delete SdsStreamView, {stream_view_id}.')

    def getStream(self, namespace_id: str, stream_id: str) -> SdsStream:
        """
        Retrieves a stream specified by 'stream_id' from the Sds Service
        :param namespace_id: namespace to work against
        :param stream_id: id of the stream
        :return:the Stream as SdsStream
        """
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__streamsPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id))
        self.__base_client.checkResponse(
            response, f'Failed to get SdsStream, {stream_id}.')

        result = SdsStream.fromJson(response.json())
        return result

    def getStreamType(self, namespace_id: str, stream_id: str) -> SdsType:
        """
        Retrieves a stream specified by 'stream_id' from the Sds Service
        :param namespace_id: namespace to work against
        :param stream_id: id of the stream
        :return: the stream type as an SdsType
        """
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__streamsPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id) + '/Type')
        self.__base_client.checkResponse(
            response, f'Failed to get SdsStream type, {stream_id}.')

        result = SdsType.fromJson(response.json())
        return result

    def getStreams(self, namespace_id: str, query: str = '', skip: int = 0,
                   count: int = 100) -> list[SdsStream]:
        """
        Retrieves a list of streams associated with 'namespace_id' under the current tenant
        :param namespace_id: namespace to work against
        :param query: filtering query
        :param skip: number of streams to skip for paging
        :param count: number of streams to limit to
        :return: array of SdsStreams
        """
        if namespace_id is None:
            raise TypeError
        if query is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__getStreamsPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id),
            params={'query': query, 'skip': skip, 'count': count})
        self.__base_client.checkResponse(
            response, 'Failed to get all SdsStreams.')

        content = response.json()
        results: list[SdsStream] = []
        for item in content:
            results.append(SdsStream.fromJson(item))
        return results

    def getOrCreateStream(self, namespace_id: str, stream: SdsStream) -> SdsStream:
        """
        Tells Sds Service to create a stream based on the local 'stream' SdsStream object
        :param namespace_id: namespace to work against
        :param stream: the stream to Create or retrieve, as a SDsStream
        :return: the created Stream as an SdsStream
        """
        if namespace_id is None:
            raise TypeError
        if stream is None or not isinstance(stream, SdsStream):
            raise TypeError

        response = self.__base_client.request(
            'post',
            self.__streamsPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream.Id),
            data=stream.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create SdsStream, {stream.Id}.')

        result = SdsStream.fromJson(response.json())
        return result

    def createOrUpdateStream(self, namespace_id: str, stream: SdsStream):
        """
        Tells Sds Service to create a stream based on the local 'stream' SdsStream object
        :param namespace_id: namespace to work against
        :param stream: the stream to Create or update, as a SDsStream
        :return: the created or updated Stream as an SdsStream
        """
        if namespace_id is None:
            raise TypeError
        if stream is None or not isinstance(stream, SdsStream):
            raise TypeError

        response = self.__base_client.request(
            'put',
            self.__streamsPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream.Id),
            data=stream.toJson())
        self.__base_client.checkResponse(
            response, f'Failed to create SdsStream, {stream.Id}.')

    def updateStreamType(self, namespace_id: str, stream_id: str, stream_view_id: str):
        """
        Tells Sds Service to update a stream based on the local 'stream' SdsStream object
        :param namespace_id: namespace to work against
        :param stream_id: id of the stream to change the type of
        :param stream_view_id: if of the streamview to change the type to
        :return:
        """
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError
        if stream_view_id is None:
            raise TypeError

        response = self.__base_client.request(
            'put',
            self.__updateStreamTypePath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id),
            params={'streamViewId': stream_view_id})
        self.__base_client.checkResponse(
            response, f'Failed to update SdsStream type, {stream_id}.')

    def deleteStream(self, namespace_id: str, stream_id: str):
        """
        Tells Sds Service to delete the stream speficied by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to delete
        :return:
        """
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError

        response = self.__base_client.request(
            'delete',
            self.__streamsPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id))
        self.__base_client.checkResponse(
            response, f'Failed to delete SdsStream, {stream_id}.')

    def createOrUpdateTags(self, namespace_id: str, stream_id: str, tags: list[str]):
        """
        Tells Sds Service to create tags and associate them with the given stream_id
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to update with tags
        :param tags: tags to create or update. expected for is an array of strings
        :return:
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request(
            'put',
            self.__streamsPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id) + '/Tags',
            data=json.dumps(tags))
        self.__base_client.checkResponse(
            response, f'Failed to create tags for Stream: {stream_id}.')

    def createOrUpdateMetadata(self, namespace_id: str, stream_id: str, metadata: dict[str, str]):
        """
        Tells Sds Service to create metadata and associate them with the given stream_id
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to update with metadata
        :param metadata: metadata to create or update. expected for is an dict(string,string)
        :return:
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request(
            'put',
            self.__streamsPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id) + '/Metadata',
            data=json.dumps(metadata))
        self.__base_client.checkResponse(
            response, f'Failed to create metadata for Stream: {stream_id}.')

    def patchMetadata(self, namespace_id: str, stream_id: str, patch: list[dict, Any]):
        """
        Tells Sds Service to update metadata on the given streamId
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to update with metadata
        :param patch: a JSON patch document
        :return:
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request(
            'patch',
            self.__streamsPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id) + '/Metadata',
            data=json.dumps(patch))
        self.__base_client.checkResponse(
            response, f'Failed to update metadata for Stream: {stream_id}.')

    def getTags(self, namespace_id: str, stream_id: str) -> list[str]:
        """
        Tells Sds Service to get tags associated with the given stream_id
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the tags of
        :return: stream's tags
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__streamsPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id) + '/Tags')
        self.__base_client.checkResponse(
            response, f'Failed to get tags for Stream: {stream_id}.')

        result = response.json()
        return result

    def getMetadata(self, namespace_id: str, stream_id: str, key: str) -> Any:
        """
        Tells Sds Service to get metadata associated with the given stream_id and key
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the metadata value of
        :param key: specific metadata field to retrieve
        :return: value at the key
        """
        if namespace_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__streamsPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id) + '/Metadata/' + key)
        self.__base_client.checkResponse(
            response, f'Failed to get metadata for Stream: {stream_id}.')

        result = response.json()
        return result

    # The following section provides functionality to interact with Data
    #  We assume the value(s) passed follow the Sds object patterns
    #  supporting fromJson and toJson method

    def getValue(self, namespace_id: str, stream_id: str, index: int,
                 value_class: type = None) -> Any:
        """
        Retrieves JSON object from Sds Service for value specified by 'index' from Sds Service
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
        :param index: index at which to get a value
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson()  Default is None.
            If None returns a dynamic Python object from the data.
        :return: the value.  If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError
        if index is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__dataPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id),
            params={'index': index})
        self.__base_client.checkResponse(
            response, f'Failed to get value for SdsStream: {stream_id}.')

        result = response.json()
        if value_class is None:
            return result
        return value_class.fromJson(result)

    def getFirstValue(self, namespace_id: str, stream_id: str, value_class: type = None) -> Any:
        """
        Retrieves JSON object from Sds Service the first value to be added to
            the stream specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson()  Default is None.
            If None returns a dynamic Python object from the data.
        :return: the value.  If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__getFirstValue.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id))
        self.__base_client.checkResponse(
            response, f'Failed to get first value for SdsStream: {stream_id}.')

        result = response.json()
        if value_class is None:
            return result
        return value_class.fromJson(result)

    def getLastValue(self, namespace_id: str, stream_id: str, value_class: type = None) -> Any:
        """
        Retrieves JSON object from Sds Service the last value to be added to
            the stream specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson()  Default is None.
            If None returns a dynamic Python object from the data.
        :return: the value.  If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__getLastValue.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id))
        self.__base_client.checkResponse(
            response, f'Failed to get last value for SdsStream: {stream_id}.')

        result = response.json()
        if value_class is None:
            return result
        return value_class.fromJson(result)

    def getWindowValues(self, namespace_id: str, stream_id: str, value_class: type, start: str,
                        end: str, filter: str = '') -> list[Any]:
        """
        Retrieves JSON object representing a window of values from the stream
            specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson().
            If None returns a dynamic Python object from the data.
        :param start: Starting index
        :param end: Ending index
        :param filter: An optional filter.  By Default it is ''.
        :return: an array of values.
            If value_class is defined it is in this type.
            Otherwise it is a dynamic Python object
        """
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError
        if start is None:
            raise TypeError
        if end is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__dataPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id),
            params={'startIndex': start, 'endIndex': end, 'filter': filter})
        self.__base_client.checkResponse(
            response, f'Failed to get window values for SdsStream: {stream_id}.')

        content = response.json()
        if value_class is None:
            return content

        results = []
        for c in content:
            results.append(value_class.fromJson(c))
        return results

    def getWindowValuesPaged(self, namespace_id: str, stream_id: str, value_class: type, start: str,
                        end: str, count: int, continuation_token: str = '', filter: str = '') -> SdsResultPage:
        """
        Retrieves JSON object representing a window of values from the stream
            specified by 'stream_id' using paging
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
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
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError
        if start is None:
            raise TypeError
        if end is None:
            raise TypeError
        if count is None:
            raise TypeError
        if continuation_token is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__dataPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id),
            params={'startIndex': start, 'endIndex': end, 'filter': filter,
                    'count': count, 'continuationToken': continuation_token})
        self.__base_client.checkResponse(
            response, f'Failed to get window values for SdsStream: {stream_id}.')

        content = SdsResultPage.fromJson(response.json())

        if value_class is None:
            return content

        results = SdsResultPage(continuation_token = content.ContinuationToken)
        for r in content.Results:
            results.Results.append(value_class.fromJson(r))
        return results

    def getWindowValuesForm(self, namespace_id: str, stream_id: str, value_class: type, start: str,
                            end: str, form: str = '') -> list[Any]:
        """
        Retrieves JSON object representing a window of values from the stream
            specified by 'stream_id'.  Use this to get the data in a different
            return form
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
        :param value_class: use this to cast the value into a given type.
        Type must support .fromJson().
        If None returns a dynamic Python object from the data.
        :param start: Starting index
        :param end: Ending index
        :param form: form of the data
        :return: An array of the data in type specified if value_class
            defined.  Otherwise it is a dynamic Python object
        """
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError
        if start is None:
            raise TypeError
        if end is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__dataPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id),
            params={'startIndex': start, 'endIndex': end, 'form': form})
        self.__base_client.checkResponse(
            response, f'Failed to get window values for SdsStream, form: {stream_id}.')

        content = response.json()
        if value_class is None:
            return content

        results = []
        for c in content:
            results.append(value_class.fromJson(c))
        return results

    def getRangeValues(self, namespace_id: str, stream_id: str, value_class: type, start: str,
                       skip: int, count: int, reversed: bool, boundary_type: str,
                       stream_view_id: str = '') -> list[Any]:
        """
        Retrieves JSON object representing a range of values from the stream
            specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
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
        :param stream_view_id: streamview to map the results to
        :return: An array of the data in type specified if value_class
            is defined.  Otherwise it is a dynamic Python object
        """
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError
        if start is None:
            raise TypeError
        if skip is None:
            raise TypeError
        if count is None:
            raise TypeError
        if reversed is None or not isinstance(reversed, bool):
            raise TypeError
        if boundary_type is None:
            raise TypeError

        boundary = boundary_type
        if isinstance(boundary_type, SdsBoundaryType):
            boundary = boundary_type.value

        response = self.__base_client.request(
            'get',
            self.__transform.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id),
            params={'startIndex': start, 'skip': skip, 'count': count,
                    'reversed': reversed, 'boundary_type': boundary,
                    'stream_view_id': stream_view_id})
        self.__base_client.checkResponse(
            response, f'Failed to get range values for SdsStream: {stream_id}.')

        content = response.json()
        if value_class is None:
            return content
        results = []
        for c in content:
            results.append(value_class.fromJson(c))
        return results

    def getRangeValuesInterpolated(self, namespace_id: str, stream_id: str, value_class: type,
                                   start: str, end: str, count: int) -> list[Any]:
        """
        Retrieves JSON object representing a range of values from the stream
            specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson(). If None returns a dynamic Python
            object from the data.
        :param start: starting index
        :param end:  ending index
        :param count: number of datapoints to retrieve
        :return: An array of the data in type specified if value_class is
        defined.  Otherwise it is a dynamic Python object
        """
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError
        if start is None:
            raise TypeError
        if end is None:
            raise TypeError
        if count is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__getRangeInterpolatedQuery.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id),
            params={'startIndex': start, 'endIndex': end, 'count': count})
        self.__base_client.checkResponse(
            response, f'Failed to get range values for SdsStream: {stream_id}.')

        content = response.json()
        if value_class is None:
            return content
        results = []
        for c in content:
            results.append(value_class.fromJson(c))
        return results

    def getSampledValues(self, namespace_id: str, stream_id: str, value_class: type, start: str,
                         end: str, sample_by: str, intervals: str, filter: str = '',
                         stream_view_id: str = '') -> list[Any]:
        """
        Returns data sampled by intervals between a specified start and end index.
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
        :param value_class: use this to cast the value into a given type.
            Type must support .fromJson().
            If None returns a dynamic Python object from the data.
        :param start: starting index for intervals
        :param end:  ending index for intervals
        :param sample_by: property or properties to use when sampling
        :param intervals: number of intervals requested
        :param boundary: optional SdsBoundaryType specifies the handling of
            events at or near the startIndex and endIndex
        :param start_boundary: optional SdsBoundaryType specifies the handling
            of events at or near the startIndex
        :param end_boundary: optional SdsBoundaryType specifies the handling
            of events at or near the endIndex
        :param filter: optional filter to apply
        :param stream_view_id: optional streamview identifier
        :return: An array of the data in type specified if value_class is
            defined.  Otherwise it is a dynamic Python object
        """
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError
        if start is None:
            raise TypeError
        if end is None:
            raise TypeError
        if sample_by is None:
            raise TypeError
        if intervals is None:
            raise TypeError

        # if stream_view_id is not set, do not specify /transform/ route
        # and stream_view_id parameter
        if len(stream_view_id) == 0:
            _path = self.__getSampledValues.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id)
        else:
            _path = self.__getSampledValuesT.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id)

        response = self.__base_client.request(
            'get',
            _path,
            params={'startIndex': start,
                    'endIndex': end,
                    'sampleBy': sample_by,
                    'intervals': intervals,
                    'filter': filter,
                    'stream_view_id': stream_view_id})
        self.__base_client.checkResponse(
            response, f'Failed to get sampled values for SdsStream: {stream_id}.')

        content = response.json()
        if value_class is None:
            return content
        results = []
        for c in content:
            results.append(value_class.fromJson(c))
        return results

    def getSummaries(self, namespace_id: str, stream_id: str, value_class: type, start: str,
                     end: str, count: int, stream_view_id: str = '', filter: str = '') -> list[Any]:
        """
        Retrieves JSON object representing a summary for the stream specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get the data of
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
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError
        if start is None:
            raise TypeError
        if end is None:
            raise TypeError
        if count is None:
            raise TypeError

        # if stream_view_id is not set, do not specify /transform/ route
        # and stream_view_id parameter
        paramsToUse = {}
        if len(stream_view_id) == 0:
            _path = self.__getSummaries.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id)

            paramsToUse = {'startIndex': start,
                           'endIndex': end,
                           'count': count,
                           'filter': filter}
        else:
            _path = self.__getSummariesT.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id)

            paramsToUse = {'startIndex': start,
                           'endIndex': end,
                           'count': count,
                           'filter': filter,
                           'streamViewId': stream_view_id}

        response = self.__base_client.request(
            'get',
            _path, paramsToUse)
        self.__base_client.checkResponse(
            response, f'Failed to get summaries for SdsStream: {stream_id}.')

        content = response.json()
        if value_class is None:
            return content

        results = []
        for c in content:
            results.append(value_class.fromJson(c))
        return results

    def insertValues(self, namespace_id: str, stream_id: str, values: list[Any]):
        """
        Tells Sds Service to insert the values, defined by the list 'values',
        into the stream specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get data into
        :param values: values to sends into OCS.
            Can be string of json array of values.
            Can be an array of values of a type that has toJson defined.
        :return:
        """
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError
        if values is None:
            raise TypeError

        if callable(getattr(values[0], 'toJson', None)):
            events = []
            for value in values:
                events.append(value.toDictionary())
            payload = json.dumps(events)
        else:
            payload = values

        response = self.__base_client.request(
            'post',
            self.__insertValuesPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id),
            data=payload)
        self.__base_client.checkResponse(
            response, f'Failed to insert multiple values for SdsStream: {stream_id}.')

    def updateValues(self, namespace_id: str, stream_id: str, values: list[Any]):
        """
        Tells Sds Service to update values defined by the SdsValue list, 'values'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get data updated
        :param values: values to update in OCS.
        Can be string of json array of values.
        Can be an array of values of a type that has toJson defined.
        :return:
        """
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError
        if values is None:
            raise TypeError

        if callable(getattr(values[0], 'toJson', None)):
            events = []
            for value in values:
                events.append(value.toDictionary())
            payload = json.dumps(events)
        else:
            payload = values

        response = self.__base_client.request(
            'put',
            self.__updateValuesPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id),
            data=payload)
        self.__base_client.checkResponse(
            response, f'Failed to update all values for SdsStream: {stream_id}.')

    def replaceValues(self, namespace_id: str, stream_id: str, values: list[Any]):
        """
        Tells Sds Service to replace the values defined by the list 'values'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get data replaced
        :param values: values to replace in OCS.
            Can be string of json array of values.
            Can be an array of values of a type that has toJson defined.
        :return:
        """
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError
        if values is None:
            raise TypeError

        if callable(getattr(values[0], 'toJson', None)):
            events = []
            for value in values:
                events.append(value.toDictionary())
            payload = json.dumps(events)
        else:
            payload = values

        response = self.__base_client.request(
            'put',
            self.__replaceValuesPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id),
            data=payload)
        self.__base_client.checkResponse(
            response, f'Failed to replace values for SdsStream: {stream_id}.')

    def removeValue(self, namespace_id: str, stream_id: str, key: str):
        """
        Tells Sds Service to delete the value with a key property matching 'key'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get data removed
        :param key: the index to remove
        :return:
        """
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError
        if key is None:
            raise TypeError

        response = self.__base_client.request(
            'delete',
            self.__dataPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id),
            params={'index': key})
        self.__base_client.checkResponse(
            response, f'Failed to remove value for SdsStream: {stream_id}.')

    def removeWindowValues(self, namespace_id: str, stream_id: str, start: str, end: str):
        """
        Tells Sds Service to delete a window of values in the stream specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_id: id of the stream to get data removed
        :param start: starting index
        :param end: ending index
        :return:
        """
        if namespace_id is None:
            raise TypeError
        if stream_id is None:
            raise TypeError
        if start is None:
            raise TypeError
        if end is None:
            raise TypeError

        response = self.__base_client.request(
            'delete',
            self.__dataPath.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id,
                stream_id=stream_id),
            params={'startIndex': start, 'endIndex': end})
        self.__base_client.checkResponse(
            response, f'Failed to remove all values for  SdsStream: {stream_id}.')

    def getStreamsWindow(self, namespace_id: str, stream_ids: list[str], value_class: type,
                         start: str, end: str, join_mode: int = 1) -> list[Any]:
        """
        Retrieves JSON object representing a window of values from the stream
             specified by 'stream_id'
        :param namespace_id: id of namespace to work against
        :param stream_ids: ids of the streams to get the data of
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
        if namespace_id is None:
            raise TypeError
        if stream_ids is None:
            raise TypeError
        if not stream_ids:
            raise TypeError
        if start is None:
            raise TypeError
        if end is None:
            raise TypeError
        if join_mode is None:
            raise TypeError

        response = self.__base_client.request(
            'get',
            self.__bulkStreams.format(
                tenant_id=self.__tenant,
                namespace_id=namespace_id),
            params={'streams': ','.join(stream_ids),
                    'startIndex': start,
                    'endIndex': end,
                    'joinMode': join_mode})
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

    def __setPathAndQueryTemplates(self):
        """
        creates the urls that are used
        :return:
        """
        self.__basePath = self.__uri_api + \
            '/Tenants/{tenant_id}/Namespaces/{namespace_id}'
        self.__getStreamViewsPath = self.__basePath + '/StreamViews'
        self.__streamViewsPath = self.__getStreamViewsPath + \
            '/{stream_view_id}'
        self.__getStreamsPath = self.__basePath + '/Streams'
        self.__streamsPath = self.__getStreamsPath + '/{stream_id}'
        self.__updateStreamTypePath = self.__streamsPath + '/Type'

        self.__dataPath = self.__streamsPath + '/Data'
        self.__getFirstValue = self.__dataPath + '/First'
        self.__getLastValue = self.__dataPath + '/Last'
        self.__transform = self.__dataPath + '/Transform'
        self.__getSummaries = self.__dataPath + '/Summaries'
        self.__getSummariesT = self.__transform + '/Summaries'
        self.__getSampledValues = self.__dataPath + '/Sampled'
        self.__getSampledValuesT = self.__transform + '/Sampled'
        self.__getRangeInterpolatedQuery = self.__transform + '/Interpolated'

        self.__insertValuesPath = self.__dataPath
        self.__updateValuesPath = self.__dataPath
        self.__replaceValuesPath = self.__dataPath + '?allowCreate=false'

        self.__bulkStreams = self.__basePath + '/Bulk/Streams/Data/Joins'
