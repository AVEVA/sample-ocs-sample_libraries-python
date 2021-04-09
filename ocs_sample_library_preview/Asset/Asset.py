import json
from typing import List

from .Status.StatusMapping import StatusMapping
from .MetadataItem import MetadataItem
from .StreamReference import StreamReference

# Alias class to avoid conflict with StatusMapping property
StatusMappingType = StatusMapping


class Asset(object):
    """OCS Asset definition"""

    def __init__(self, id: str = None, name: str = None, description: str = None,
                 asset_type_id: str = None, metadata: List[MetadataItem] = None,
                 stream_references: List[StreamReference] = None,
                 status_mapping: StatusMappingType = None):
        """
        :param id: required
        :param name: not required
        :param description: not required
        :param asset_type_id: not required
        :param metadata: not required
        :param stream_references: not required
        :param status_mapping: not required
        """
        self.Id = id
        self.Name = name
        self.Description = description
        self.AssetTypeId = asset_type_id
        self.Metadata = metadata
        self.StreamReferences = stream_references
        self.StatusMapping = status_mapping

    @property
    def Id(self) -> str:
        """
        required
        :return:
        """
        return self.__id

    @Id.setter
    def Id(self, value: str):
        """"
        required
        :param value:
        :return:
        """
        self.__id = value

    @property
    def Name(self) -> str:
        """
        not required
        :return:
        """
        return self.__name

    @Name.setter
    def Name(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__name = value

    @property
    def Description(self) -> str:
        """
        not required
        :return:
        """
        return self.__description

    @Description.setter
    def Description(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__description = value

    @property
    def AssetTypeId(self) -> str:
        """
        not required
        :return:
        """
        return self.__asset_type_id

    @AssetTypeId.setter
    def AssetTypeId(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__asset_type_id = value

    @property
    def Metadata(self) -> List[MetadataItem]:
        """
        list of MetadataItem    not required
        :return:
        """
        return self.__metadata

    @Metadata.setter
    def Metadata(self, value: List[MetadataItem]):
        """
        list of MetadataItem    not required
        :param value:
        :return:
        """
        self.__metadata = value

    @property
    def StreamReferences(self) -> List[StreamReference]:
        """
        list of StreamReference    not required
        :return:
        """
        return self.__stream_references

    @StreamReferences.setter
    def StreamReferences(self, value: List[StreamReference]):
        """
        list of StreamReference    not required
        :param value:
        :return:
        """
        self.__stream_references = value

    @property
    def StatusMapping(self) -> StatusMappingType:
        """
        StatusMapping    not required
        :return:
        """
        return self.__status_mapping

    @StatusMapping.setter
    def StatusMapping(self, value: StatusMappingType):
        """
        StatusMapping    not required
        :param value:
        :return:
        """
        self.__status_mapping = value

    def to_json(self):
        return json.dumps(self.to_dictionary())

    def to_dictionary(self):
        # required properties
        result = {'Id': self.Id}

        # optional properties
        if hasattr(self, 'Name'):
            result['Name'] = self.Name

        if hasattr(self, 'Description'):
            result['Description'] = self.Description

        if hasattr(self, 'AssetTypeId'):
            result['AssetTypeId'] = self.AssetTypeId

        if hasattr(self, 'Metadata'):
            if self.Metadata is not None:
                result['Metadata'] = []
                for value in self.Metadata:
                    result['Metadata'].append(value.to_dictionary())

        if hasattr(self, 'StreamReferences'):
            if self.StreamReferences is not None:
                result['StreamReferences'] = []
                for value in self.StreamReferences:
                    result['StreamReferences'].append(
                        value.to_dictionary())

        if hasattr(self, 'StatusMapping'):
            if self.StatusMapping is not None:
                result['StatusMapping'] = self.StatusMapping.to_dictionary()

        return result

    @staticmethod
    def from_json(content):
        result = Asset()

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

        if 'Metadata' in content:
            metadata = content['Metadata']
            if metadata is not None and len(metadata) > 0:
                result.Metadata = []
                for value in metadata:
                    result.Metadata.append(
                        MetadataItem.from_json(value))

        if 'StreamReferences' in content:
            streamReferences = content['StreamReferences']
            if streamReferences is not None and len(streamReferences) > 0:
                result.StreamReferences = []
                for value in streamReferences:
                    result.StreamReferences.append(
                        StreamReference.from_json(value))

        if 'StatusMapping' in content:
            result.StatusMapping = StatusMappingType.from_json(
                content['StatusMapping'])

        return result
