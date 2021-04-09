import json
from typing import List

from ..MetadataItem import MetadataItem
from .ResolvedStatus import ResolvedStatus
from .ResolvedStream import ResolvedStream
from .UnresolvedStream import UnresolvedStream


class ResolvedAsset(object):
    def __init__(self, id: str = None, name: str = None, description: str = None,
                 asset_type_id: str = None, asset_type_name: str = None,
                 metadata: List[MetadataItem] = None, streams: List[ResolvedStream] = None,
                 unresolved_streams: List[UnresolvedStream] = None, status: ResolvedStatus = None):
        self.Id = id
        self.Name = name
        self.Description = description
        self.AssetTypeId = asset_type_id
        self.AssetTypeName = asset_type_name
        self.Metadata = metadata
        self.Streams = streams
        self.UnresolvedStreams = unresolved_streams
        self.Status = status

    @property
    def Id(self) -> str:
        return self.__id

    @Id.setter
    def Id(self, value: str):
        self.__id = value

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str):
        self.__name = value

    @property
    def Description(self) -> str:
        return self.__description

    @Description.setter
    def Description(self, value: str):
        self.__description = value

    @property
    def AssetTypeId(self) -> str:
        return self.__asset_type_id

    @AssetTypeId.setter
    def AssetTypeId(self, value: str):
        self.__asset_type_id = value

    @property
    def AssetTypeName(self) -> str:
        return self.__asset_type_name

    @AssetTypeName.setter
    def AssetTypeName(self, value: str):
        self.__asset_type_name = value

    @property
    def Metadata(self) -> List[MetadataItem]:
        return self.__metadata

    @Metadata.setter
    def Metadata(self, value: List[MetadataItem]):
        self.__metadata = value

    @property
    def Streams(self) -> List[ResolvedStream]:
        return self.__streams

    @Streams.setter
    def Streams(self, value: List[ResolvedStream]):
        self.__streams = value

    @property
    def UnresolvedStreams(self) -> List[UnresolvedStream]:
        return self.__unresolved_streams

    @UnresolvedStreams.setter
    def UnresolvedStreams(self, value: List[UnresolvedStream]):
        self.__unresolved_streams = value

    @property
    def Status(self) -> ResolvedStatus:
        return self.__status

    @Status.setter
    def Status(self, value: ResolvedStatus):
        self.__status = value

    def to_json(self):
        return json.dumps(self.to_dictionary())

    def to_dictionary(self):
        result = {'Id': self.Id, 'Name': self.Name, 'Description': self.Description,
                  'AssetTypeId': self.AssetTypeId, 'AssetTypeName': self.AssetTypeName,
                  'Metadata': [], 'Streams': [], 'Status': self.Status.to_dictionary()}

        if self.Metadata is not None:
            for value in self.Metadata:
                result['Metadata'].append(value.to_dictionary())

        if self.Streams is not None:
            for value in self.Streams:
                result['Streams'].append(value.to_dictionary())

        if self.UnresolvedStreams is not None:
            for value in self.UnresolvedStreams:
                result['UnresolvedStreams'].append(value.to_dictionary())

        return result

    @staticmethod
    def from_json(content):
        result = ResolvedAsset()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        if 'AssetTypeId' in content:
            result.AssetTypeId = content['AssetTypeId']

        if 'AssetTypeName' in content:
            result.AssetTypeName = content['AssetTypeName']

        if 'Metadata' in content:
            metadata = content['Metadata']
            if metadata is not None and len(metadata) > 0:
                result.Metadata = []
                for value in metadata:
                    result.Metadata.append(
                        MetadataItem.from_json(value))

        if 'Streams' in content:
            streams = content['Streams']
            if streams is not None and len(streams) > 0:
                result.Streams = []
                for value in streams:
                    result.Streams.append(
                        ResolvedStream.from_json(value))

        if 'UnresolvedStreams' in content:
            unresolved_streams = content['UnresolvedStreams']
            if unresolved_streams is not None and len(unresolved_streams) > 0:
                result.UnresolvedStreams = []
                for value in unresolved_streams:
                    result.UnresolvedStreams.append(
                        UnresolvedStream.from_json(value))

        if 'Status' in content:
            result.Status = ResolvedStatus.from_json(
                content['Status'])

        return result
