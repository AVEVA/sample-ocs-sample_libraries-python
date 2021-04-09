import json
from typing import List

from .Status.StatusMapping import StatusMapping
from .MetadataItem import MetadataItem
from .TypeReference import TypeReference


class AssetType(object):
    """OCS Asset Type definition"""

    def __init__(self, id: str = None, name: str = None, description: str = None,
                 metadata: MetadataItem = None,
                 type_references: List[TypeReference] = None,
                 status: StatusMapping = None):
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
        self.Status = status

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
    def Metadata(self) -> List[MetadataItem]:
        """
        array of MetadataItem    not required
        :return:
        """
        return self.__metadata

    @Metadata.setter
    def Metadata(self, value: List[MetadataItem]):
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
    def Status(self) -> StatusMapping:
        """
        StatusMapping    not required
        :return:
        """
        return self.__status

    @Status.setter
    def Status(self, value: StatusMapping):
        """
        StatusMapping    not required
        :param value:
        :return:
        """
        self.__status = value

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
                    result['Metadata'].append(value.to_dictionary())

        if hasattr(self, 'TypeReferences'):
            if self.TypeReferences is not None:
                result['TypeReferences'] = []
                for value in self.TypeReferences:
                    result['TypeReferences'].append(value.to_dictionary())

        if hasattr(self, 'Status'):
            if self.Status is not None:
                result['Status'] = self.Status.to_dictionary()

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

        if 'Status' in content:
            result.Status = StatusMapping.from_json(content['Status'])

        return result
