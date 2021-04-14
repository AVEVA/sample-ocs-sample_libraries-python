import json

from .Status.StatusMapping import StatusMapping
from .MetadataItem import MetadataItem
from .TypeReference import TypeReference


class AssetType(object):
    """OCS Asset Type definition"""

    def __init__(self, id: str = None, name: str = None, description: str = None,
                 metadata: MetadataItem = None,
                 type_references: list[TypeReference] = None,
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
        return self._id

    @Id.setter
    def Id(self, value: str):
        """"
        required
        :param value:
        :return:
        """
        self._id = value

    @property
    def Name(self) -> str:
        """
        not required
        :return:
        """
        return self._name

    @Name.setter
    def Name(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self._name = value

    @property
    def Description(self) -> str:
        """
        not required
        :return:
        """
        return self._description

    @Description.setter
    def Description(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self._description = value

    @property
    def Metadata(self) -> list[MetadataItem]:
        """
        list of MetadataItem    not required
        :return:
        """
        return self._metadata

    @Metadata.setter
    def Metadata(self, value: list[MetadataItem]):
        """
        list of MetadataItem    not required
        :param value:
        :return:
        """
        self._metadata = value

    @property
    def TypeReferences(self) -> list[TypeReference]:
        """
        list of TypeReference    not required
        :return:
        """
        return self._type_references

    @TypeReferences.setter
    def TypeReferences(self, value: list[TypeReference]):
        """
        list of TypeReference    not required
        :param value:
        :return:
        """
        self._type_references = value

    @property
    def Status(self) -> StatusMapping:
        """
        StatusMapping    not required
        :return:
        """
        return self._status

    @Status.setter
    def Status(self, value: StatusMapping):
        """
        StatusMapping    not required
        :param value:
        :return:
        """
        self._status = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'Id': self.Id}

        # optional properties
        if self.Name is not None:
            result['Name'] = self.Name

        if self.Description is not None:
            result['Description'] = self.Description

        if self.Metadata is not None:
            result['Metadata'] = []
            for value in self.Metadata:
                result['Metadata'].append(value.toDictionary())

        if self.TypeReferences is not None:
            result['TypeReferences'] = []
            for value in self.TypeReferences:
                result['TypeReferences'].append(value.toDictionary())

        if self.Status is not None:
            result['Status'] = self.Status.toDictionary()

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
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
                    result.Metadata.append(MetadataItem.fromJson(value))

        if 'TypeReferences' in content:
            type_references = content['TypeReferences']
            if type_references is not None and len(type_references) > 0:
                result.TypeReferences = []
                for value in type_references:
                    result.TypeReferences.append(
                        TypeReference.fromJson(value))

        if 'Status' in content:
            result.Status = StatusMapping.fromJson(content['Status'])

        return result
