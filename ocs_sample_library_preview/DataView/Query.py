import json

from .DataItemResourceType import DataItemResourceType


class Query(object):
    """OCS Query definition"""

    def __init__(self, id: str = None, kind: DataItemResourceType = None, value: str = None):
        """
        :param id: required
        :param kind: not required
        :param value: not required
        """
        self._id = id
        self._kind = kind
        self._value = value

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
    def Kind(self) -> DataItemResourceType:
        """
        not required
        :return:
        """
        return self._kind

    @Kind.setter
    def Kind(self, value: DataItemResourceType):
        """
        not required
        :param value:
        :return:
        """
        self._kind = value

    @property
    def Value(self) -> str:
        """
        not required
        :return:
        """
        return self._value

    @Value.setter
    def Value(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self._value = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'Id': self.Id}

        # optional properties
        if self.Kind is not None:
            result['Kind'] = self.Kind.value

        if self.Value is not None:
            result['Value'] = self.Value

        return result

    @staticmethod
    def fromJson(jsonObj):
        return Query.fromDictionary(jsonObj)

    @staticmethod
    def fromDictionary(content):
        query = Query()

        if not content:
            return query

        if 'Id' in content:
            query.Id = content['Id']

        if 'Kind' in content:
            query.Kind = DataItemResourceType[content['Kind']]

        if 'Value' in content:
            query.Value = content['Value']

        return query
