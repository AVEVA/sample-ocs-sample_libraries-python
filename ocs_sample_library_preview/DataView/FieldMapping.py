import json

from ..SDS import SdsSummaryType, SdsTypeCode
from . import Enum
from .DataMapping import DataMapping


class FieldMapping(object):
    """OCS Field Mapping definition"""

    def __init__(self, id: str = None, label: str = None, field_kind: Enum.FieldKind = None,
                 data_mappings: list[DataMapping] = None, type_code: SdsTypeCode = None,
                 uom: str = None, summary_type: SdsSummaryType = None,
                 summary_direction: Enum.SummaryDirection = None):
        self.Id = id
        self.Label = label
        self.FieldKind = field_kind
        self.DataMappings = data_mappings
        self.TypeCode = type_code
        self.Uom = uom
        self.SummaryType = summary_type
        self.SummaryDirection = summary_direction

    @property
    def Id(self) -> str:
        return self._id

    @Id.setter
    def Id(self, value: str):
        self._id = value

    @property
    def Label(self) -> str:
        return self._label

    @Label.setter
    def Label(self, value: str):
        self._label = value

    @property
    def FieldKind(self) -> Enum.FieldKind:
        return self._field_kind

    @FieldKind.setter
    def FieldKind(self, value: Enum.FieldKind):
        self._field_kind = value

    @property
    def DataMappings(self) -> list[DataMapping]:
        return self._data_mappings

    @DataMappings.setter
    def DataMappings(self, value: list[DataMapping]):
        self._data_mappings = value

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
    def SummaryType(self) -> SdsSummaryType:
        return self._summary_type

    @SummaryType.setter
    def SummaryType(self, value: SdsSummaryType):
        self._summary_type = value

    @property
    def SummaryDirection(self) -> Enum.SummaryDirection:
        return self._summary_direction

    @SummaryDirection.setter
    def SummaryDirection(self, value: Enum.SummaryDirection):
        self._summary_direction = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {}

        # optional properties
        if self.Id is not None:
            result['Id'] = self.Id

        if self.Label is not None:
            result['Label'] = self.Label

        if self.FieldKind is not None:
            result['FieldKind'] = self.FieldKind.name

        if self.DataMappings is not None:
            result['DataMappings'] = []
            for value in self.DataMappings:
                result['DataMappings'].append(value.toDictionary())

        if self.TypeCode is not None:
            result['TypeCode'] = self.TypeCode.name

        if self.Uom is not None:
            result['Uom'] = self.Uom

        if self.SummaryType is not None:
            result['SummaryType'] = self.SummaryType.name

        if self.SummaryDirection is not None:
            result['SummaryDirection'] = self.SummaryDirection.name

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = FieldMapping()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Label' in content:
            result.Label = content['Label']

        if 'FieldKind' in content:
            result.FieldKind = Enum.FieldKind[content['FieldKind']]

        if 'DataMappings' in content:
            data_mappings = content['DataMappings']
            if data_mappings is not None and len(data_mappings) > 0:
                result.DataMappings = []
                for value in data_mappings:
                    result.DataMappings.append(DataMapping.fromJson(value))

        if 'TypeCode' in content:
            result.TypeCode = SdsTypeCode[content['TypeCode']]

        if 'Uom' in content:
            result.Uom = content['Uom']

        if 'SummaryType' in content:
            result.SummaryType = SdsSummaryType[content['SummaryType']]

        if 'SummaryDirection' in content:
            result.SummaryDirection = Enum.SummaryDirection[content['SummaryDirection']]

        return result
