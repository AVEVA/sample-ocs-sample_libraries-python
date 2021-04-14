import json

from ..SDS.SdsTypeCode import SdsTypeCode


class DataItemField(object):
    """OCS Data Item Field definition"""

    def __init__(self, id: str = None, name: str = None, type_code: SdsTypeCode = None,
                 uom: str = None, is_key: bool = None, stream_reference_name: str = None):
        self._id = id
        self._name = name
        self._type_code = type_code
        self._uom = uom
        self._is_key = is_key
        self._stream_reference_name = stream_reference_name

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
    def TypeCode(self) -> SdsTypeCode:
        return self._type_code

    @TypeCode.setter
    def TypeCode(self, value: SdsTypeCode):
        self._type_code = value

    @property
    def Uom(self) -> str:
        return self._uom

    @Uom.setter
    def Uom(self, value: str):
        self._uom = value

    @property
    def IsKey(self) -> bool:
        return self._is_key

    @IsKey.setter
    def IsKey(self, value: bool):
        self._is_key = value

    @property
    def StreamReferenceName(self) -> str:
        return self._stream_reference_name

    @StreamReferenceName.setter
    def StreamReferenceName(self, value: str):
        self._stream_reference_name = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return {'Id': self.Id, 'Name': self.Name, 'TypeCode': self.TypeCode.value, 'Uom': self.Uom,
                'IsKey': self.IsKey, 'StreamReferenceName': self.StreamReferenceName}

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = DataItemField()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'TypeCode' in content:
            result.TypeCode = SdsTypeCode[content['TypeCode']]

        if 'Uom' in content:
            result.Uom = content['Uom']

        if 'IsKey' in content:
            result.IsKey = content['IsKey']

        if 'StreamReferenceName' in content:
            result.StreamReferenceName = content['StreamReferenceName']

        return result
