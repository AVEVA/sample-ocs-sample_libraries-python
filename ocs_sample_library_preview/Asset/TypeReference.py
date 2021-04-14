import json


class TypeReference(object):
    """OCS Asset Type Type Reference definition"""

    def __init__(self, stream_reference_id: str = None, stream_reference_name: str = None,
                 description: str = None, type_id: str = None):
        """
        :param stream_reference_id: required
        :param stream_reference_name: required
        :param description: not required
        :param type_id: required
        """
        self.StreamReferenceId = stream_reference_id
        self.StreamReferenceName = stream_reference_name
        self.Description = description
        self.TypeId = type_id

    @property
    def StreamReferenceId(self) -> str:
        """
        required
        :return:
        """
        return self._stream_reference_id

    @StreamReferenceId.setter
    def StreamReferenceId(self, value: str):
        """"
        required
        :param value:
        :return:
        """
        self._stream_reference_id = value

    @property
    def StreamReferenceName(self) -> str:
        """
        required
        :return:
        """
        return self._stream_reference_name

    @StreamReferenceName.setter
    def StreamReferenceName(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self._stream_reference_name = value

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
    def TypeId(self) -> str:
        """
        required
        :return:
        """
        return self._type_id

    @TypeId.setter
    def TypeId(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self._type_id = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {
            'StreamReferenceId': self.StreamReferenceId,
            'StreamReferenceName': self.StreamReferenceName,
            'TypeId': self.TypeId
        }

        # optional properties
        if self.Description is not None:
            result['Description'] = self.Description

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = TypeReference()

        if not content:
            return result

        if 'StreamReferenceId' in content:
            result.StreamReferenceId = content['StreamReferenceId']

        if 'StreamReferenceName' in content:
            result.StreamReferenceName = content['StreamReferenceName']

        if 'Description' in content:
            result.Description = content['Description']

        if 'TypeId' in content:
            result.TypeId = content['TypeId']

        return result
