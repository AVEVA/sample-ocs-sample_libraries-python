import json
from ocs_sample_library_preview.Asset import Data

from ..SDS.SdsTypeCode import SdsTypeCode
from .Field import Field
from .FieldSet import FieldSet
from .DataViewShape import DataViewShape
from .Query import Query


class DataView(object):
    """OCS Data View definition"""

    def __init__(self, id: str = None, name: str = None, description: str = None,
                 index_field: Field = None, queries: list[Query] = None,
                 data_field_sets: list[FieldSet] = None, grouping_fields: list[Field] = None,
                 default_start_index: str = None, default_end_index: str = None,
                 default_interval: str = None, index_type_code: SdsTypeCode = None,
                 shape: DataViewShape = None):
        """
        :param id: required
        :param name: not required
        :param description: not required
        :param index_field: not required
        :param queries: not required
        :param data_field_sets: not required
        :param grouping_fields: not required
        :param default_start_index: not required
        :param default_end_index: not required
        :param default_interval: not required
        :param index_type_code: not required
        :param shape: not required
        """
        self._id = id
        self._name = name
        self._description = description
        self._index_field = index_field
        self._queries = queries
        self._data_field_sets = data_field_sets
        self._grouping_fields = grouping_fields
        self._default_start_index = default_start_index
        self._default_end_index = default_end_index
        self._default_interval = default_interval
        self._index_type_code = index_type_code
        self._shape = shape

    @property
    def Id(self) -> str:
        """
        required
        :return:
        """
        return self._id

    @Id.setter
    def Id(self, value: str):
        """
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
    def IndexField(self) -> Field:
        """
        Field    not required
        :return:
        """
        return self._index_field

    @IndexField.setter
    def IndexField(self, value: Field):
        """
        Field    not required
        :param value:
        :return:
        """
        self._index_field = value

    @property
    def Queries(self) -> list[Query]:
        """
        list of Query    not required
        :return:
        """
        return self._queries

    @Queries.setter
    def Queries(self, value: list[Query]):
        """
        list of Query    not required
        :param value:
        :return:
        """
        self._queries = value

    @property
    def DataFieldSets(self) -> list[FieldSet]:
        """
        list of FieldSet    not required
        :return:
        """
        return self._data_field_sets

    @DataFieldSets.setter
    def DataFieldSets(self, value: list[FieldSet]):
        """
        list of FieldSet    not required
        :param value:
        :return:
        """
        self._data_field_sets = value

    @property
    def GroupingFields(self) -> list[Field]:
        """
        list of Field    not required
        :return:
        """
        return self._grouping_fields

    @GroupingFields.setter
    def GroupingFields(self, value: list[Field]):
        """
        list of Field    not required
        :param value:
        :return:
        """
        self._grouping_fields = value

    @property
    def DefaultStartIndex(self) -> str:
        """
        not required
        :return:
        """
        return self._default_start_index

    @DefaultStartIndex.setter
    def DefaultStartIndex(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self._default_start_index = value

    @property
    def DefaultEndIndex(self) -> str:
        """
        not required
        :return:
        """
        return self._default_end_index

    @DefaultEndIndex.setter
    def DefaultEndIndex(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self._default_end_index = value

    @property
    def DefaultInterval(self) -> str:
        """
        not required
        :return:
        """
        return self._default_interval

    @DefaultInterval.setter
    def DefaultInterval(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self._default_interval = value

    @property
    def IndexTypeCode(self) -> SdsTypeCode:
        """
        not required
        :return:
        """
        return self._index_type_code

    @IndexTypeCode.setter
    def IndexTypeCode(self, value: SdsTypeCode):
        """
        not required
        :param value:
        :return:
        """
        self._index_type_code = value

    @property
    def Shape(self) -> DataViewShape:
        """
        not required
        :return:
        """
        return self._shape

    @Shape.setter
    def Shape(self, value: DataViewShape):
        """
        not required
        :param value:
        :return:
        """
        self._shape = value

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

        if self.IndexField is not None:
            result['IndexField'] = self.IndexField.toDictionary()

        if self.Queries is not None:
            result['Queries'] = []
            for value in self.Queries:
                result['Queries'].append(value.toDictionary())

        if self.DataFieldSets is not None:
            result['DataFieldSets'] = []
            for value in self.DataFieldSets:
                result['DataFieldSets'].append(value.toDictionary())

        if self.GroupingFields is not None:
            result['GroupingFields'] = []
            for value in self.GroupingFields:
                result['GroupingFields'].append(value.toDictionary())

        if self.DefaultStartIndex is not None:
            result['DefaultStartIndex'] = self.DefaultStartIndex

        if self.DefaultEndIndex is not None:
            result['DefaultEndIndex'] = self.DefaultEndIndex

        if self.DefaultInterval is not None:
            result['DefaultInterval'] = self.DefaultInterval

        if self.IndexTypeCode is not None:
            result['IndexTypeCode'] = self.IndexTypeCode.name

        if self.Shape is not None:
            result['Shape'] = self.Shape.name

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = DataView()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        if 'IndexField' in content:
            result.IndexField = Field.fromJson(content['IndexField'])

        if 'Queries' in content:
            queries = content['Queries']
            if queries is not None and len(queries) > 0:
                result.Queries = []
                for value in queries:
                    result.Queries.append(Query.fromJson(value))

        if 'DataFieldSets' in content:
            data_field_sets = content['DataFieldSets']
            if data_field_sets is not None and len(data_field_sets) > 0:
                result.DataFieldSets = []
                for value in data_field_sets:
                    result.DataFieldSets.append(FieldSet.fromJson(value))

        if 'GroupingFields' in content:
            grouping_fields = content['GroupingFields']
            if grouping_fields is not None and len(grouping_fields) > 0:
                result.GroupingFields = []
                for value in grouping_fields:
                    result.GroupingFields.append(Field.fromJson(value))

        if 'DefaultStartIndex' in content:
            result.DefaultStartIndex = content['DefaultStartIndex']

        if 'DefaultEndIndex' in content:
            result.DefaultEndIndex = content['DefaultEndIndex']

        if 'DefaultInterval' in content:
            result.DefaultInterval = content['DefaultInterval']

        if 'IndexTypeCode' in content:
            result.IndexTypeCode = SdsTypeCode[content['IndexTypeCode']]

        if 'Shape' in content:
            result.Shape = DataViewShape[content['Shape']]

        return result
