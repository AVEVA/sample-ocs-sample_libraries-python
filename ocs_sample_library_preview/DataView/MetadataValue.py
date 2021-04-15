import json
from typing import Any

from ..SDS import SdsTypeCode


class MetadataValue(object):
    """OCS Metadata Value definition"""

    def __init__(self, name: str = None, value: Any = None, description: str = None,
                 type_code: SdsTypeCode = None, uom: str = None):
        self.Name = name
        self.Value = value
        self.Description = description
        self.TypeCode = type_code
        self.Uom = uom

    @property
    def Name(self) -> str:
        return self._name

    @Name.setter
    def Name(self, value: str):
        self._name = value

    @property
    def Value(self) -> Any:
        return self._value

    @Value.setter
    def Value(self, value: Any):
        self._value = value

    @property
    def Description(self) -> str:
        return self._description

    @Description.setter
    def Description(self, value: str):
        self._description = value

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

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return {'Name': self.Name, 'Value': self.Value, 'Description': self.Description,
                'TypeCode': self.TypeCode.name, 'Uom': self.Uom}

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = MetadataValue()

        if not content:
            return result

        if 'Name' in content:
            result.Name = content['Name']

        if 'Value' in content:
            result.Value = content['Value']

        if 'Description' in content:
            result.Description = content['Description']

        if 'TypeCode' in content:
            result.TypeCode = SdsTypeCode[content['TypeCode']]

        if 'Uom' in content:
            result.Uom = content['Uom']

        return result
