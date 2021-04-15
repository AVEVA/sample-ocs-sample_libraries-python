import json

from .Enum.DataItemResourceType import DataItemResourceType
from .DataItemField import DataItemField
from .MetadataValue import MetadataValue


class DataItem(object):
    """OCS Data Item definition"""

    def __init__(self, id: str = None, name: str = None, description: str = None,
                 type_id: str = None, resource_type: DataItemResourceType = None,
                 tags: list[str] = None, metadata: list[MetadataValue] = None,
                 data_item_fields: list[DataItemField] = None,
                 ineligible_data_item_fields: list[DataItemField] = None):
        self.Id = id
        self.Name = name
        self.Description = description
        self.TypeId = type_id
        self.ResourceType = resource_type
        self.Tags = tags
        self.Metadata = metadata
        self.DataItemFields = data_item_fields
        self.IneligibleDataItemFields = ineligible_data_item_fields

    @property
    def Id(self) -> str:
        return self._id

    @Id.setter
    def Id(self, value: str):
        self._id = value

    @property
    def Name(self) -> str:
        return self._name

    @Name.setter
    def Name(self, value: str):
        self._name = value

    @property
    def Description(self) -> str:
        return self._description

    @Description.setter
    def Description(self, value: str):
        self._description = value

    @property
    def TypeId(self) -> str:
        return self._type_id

    @TypeId.setter
    def TypeId(self, value: str):
        self._type_id = value

    @property
    def ResourceType(self) -> DataItemResourceType:
        return self._resource_type

    @ResourceType.setter
    def ResourceType(self, value: DataItemResourceType):
        self._resource_type = value

    @property
    def Tags(self) -> list[str]:
        return self._tags

    @Tags.setter
    def Tags(self, value: list[str]):
        self._tags = value

    @property
    def Metadata(self) -> list[MetadataValue]:
        return self._metadata

    @Metadata.setter
    def Metadata(self, value: list[MetadataValue]):
        self._metadata = value

    @property
    def DataItemFields(self) -> list[DataItemField]:
        return self._data_item_fields

    @DataItemFields.setter
    def DataItemFields(self, value: list[DataItemField]):
        self._data_item_fields = value

    @property
    def IneligibleDataItemFields(self) -> list[DataItemField]:
        return self._ineligible_data_item_fields

    @IneligibleDataItemFields.setter
    def IneligibleDataItemFields(self, value: list[DataItemField]):
        self._ineligible_data_item_fields = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {'Id': self.Id, 'Name': self.Name, 'Description': self.Description,
                  'TypeId': self.TypeId, 'ResourceType': self.ResourceType.name, 'Tags': [],
                  'Metadata': [], 'DataItemFields': [], 'IneligibleDataItemFields': []}

        if self.Tags is not None:
            for value in self.Tags:
                result['Tags'].append(value)

        if self.Metadata is not None:
            for value in self.Metadata:
                result['Metadata'].append(value.toDictionary())

        if self.DataItemFields is not None:
            for value in self.DataItemFields:
                result['DataItemFields'].append(value.toDictionary())

        if self.IneligibleDataItemFields is not None:
            for value in self.IneligibleDataItemFields:
                result['IneligibleDataItemFields'].append(value.toDictionary())

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = DataItem()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        if 'TypeId' in content:
            result.TypeId = content['TypeId']

        if 'ResourceType' in content:
            result.ResourceType = DataItemResourceType[content['ResourceType']]

        if 'Tags' in content:
            tags = content['Tags']
            if tags is not None and len(tags) > 0:
                result.Tags = []
                for value in tags:
                    result.Tags.append(value)

        if 'Metadata' in content:
            metadata = content['Metadata']
            if metadata is not None and len(metadata) > 0:
                result.Metadata = []
                for value in metadata:
                    result.Metadata.append(MetadataValue.fromJson(value))

        if 'DataItemFields' in content:
            data_item_fields = content['DataItemFields']
            if data_item_fields is not None and len(data_item_fields) > 0:
                result.DataItemFields = []
                for value in data_item_fields:
                    result.DataItemFields.append(
                        DataItemField.fromJson(value))

        return result
