import json

from .Field import Field


class FieldSet(object):
    """OCS Field Set definition"""

    def __init__(self, query_id: str = None, data_fields: list[Field] = None,
                 identifying_field: Field = None):
        """
        :param query_id: required
        :param data_fields: not required
        :param identifying_field: not required
        """
        self._query_id = query_id
        self._data_fields = data_fields
        self._identifying_field = identifying_field

    @property
    def QueryId(self) -> str:
        """
        required
        :return:
        """
        return self._query_id

    @QueryId.setter
    def QueryId(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self._query_id = value

    @property
    def DataFields(self) -> list[Field]:
        """
        not required
        :return:
        """
        return self._data_fields

    @DataFields.setter
    def DataFields(self, value: list[Field]):
        """
        not required
        :param value:
        :return:
        """
        self._data_fields = value

    @property
    def IdentifyingField(self) -> Field:
        """
        not required
        :return:
        """
        return self._identifying_field

    @IdentifyingField.setter
    def IdentifyingField(self, value: Field):
        """
        not required
        :param value:
        :return:
        """
        self._identifying_field = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'QueryId': self.QueryId}

        # optional properties
        if self.DataFields is not None:
            result['DataFields'] = []
            for value in self.DataFields:
                result['DataFields'].append(value.toDictionary())

        if self.IdentifyingField is not None:
            result['IdentifyingField'] = self.IdentifyingField.toDictionary()

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = FieldSet()

        if not content:
            return result

        if 'QueryId' in content:
            result.QueryId = content['QueryId']

        if 'DataFields' in content:
            data_fields = content['DataFields']
            if data_fields is not None and len(data_fields) > 0:
                result.DataFields = []
                for value in data_fields:
                    result.DataFields.append(Field.fromJson(value))

        if 'IdentifyingField' in content:
            result.IdentifyingField = Field.fromJson(
                content['IdentifyingField'])

        return result
