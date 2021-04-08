import json
from typing import List

from .Status.StatusMapping import StatusMapping
from .MetadataItem import MetadataItem
from .TypeReference import TypeReference

# Alias class to avoid conflict with StatusMapping property
StatusMappingType = StatusMapping


class AssetType(object):
    """OCS Asset Type definition"""

    def __init__(self, id: str = None, name: str = None, description: str = None,
                 metadata: MetadataItem = None,
                 type_references: List[TypeReference] = None,
                 status_mapping: StatusMappingType = None):
        """
        :param id: required
        :param name: not required
        :param description: not required
        :param metadata: not required
        :param type_references: not required
        :param status_mapping: not required
        """
        self.Id = id
        self.Name = name
        self.Description = description
        self.Metadata = metadata
        self.TypeReferences = type_references
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
    def Metadata(self) -> MetadataItem:
        """
        array of MetadataItem    not required
        :return:
        """
        return self.__metadata

    @Metadata.setter
    def Metadata(self, value: MetadataItem):
        """
        array of MetadataItem    not required
        :param value:
        :return:
        """
        self.__metadata = value

    @property
    def TypeReferences(self) -> List[TypeReference]:
        """
        array of TypeReference    not required
        :return:
        """
        return self.__type_references

    @TypeReferences.setter
    def TypeReferences(self, value: List[TypeReference]):
        """
        array of TypeReference    not required
        :param value:
        :return:
        """
        self.__type_references = value

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

        if hasattr(self, 'Metadata'):
            if self.Metadata is not None:
                result['Metadata'] = []
                for value in self.Metadata:
                    result['Metadata'].append(value.toDictionary())

        if hasattr(self, 'TypeReferences'):
            if self.TypeReferences is not None:
                result['TypeReferences'] = []
                for value in self.TypeReferences:
                    result['TypeReferences'].append(value.to_dictionary())

        if hasattr(self, 'StatusMapping'):
            if self.StatusMapping is not None:
                result['StatusMapping'] = self.StatusMapping.to_dictionary()

        return result

    @staticmethod
    def from_json(content):
        result = AssetType()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        if 'Metadata' in content:
            metadata = content['Metadata']
            if metadata is not None and len(metadata) > 0:
                result.Metadata = []
                for value in metadata:
                    result.Metadata.append(MetadataItem.from_json(value))

        if 'TypeReferences' in content:
            type_references = content['TypeReferences']
            if type_references is not None and len(type_references) > 0:
                result.TypeReferences = []
                for value in type_references:
                    result.TypeReferences.append(
                        TypeReference.from_json(value))

        if 'StatusMapping' in content:
            result.StatusMapping = StatusMappingType.from_json(
                content['StatusMapping'])
