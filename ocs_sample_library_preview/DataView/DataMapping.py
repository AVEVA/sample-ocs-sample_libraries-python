import json
from ocs_sample_library_preview.DataView.SummaryDirection import SummaryDirection

from ..SDS.SdsTypeCode import SdsTypeCode
from ..SDS.SdsSummaryType import SdsSummaryType
from .SummaryDirection import SummaryDirection

# Alias class to avoid conflict with SummaryDirection property
SummaryDirectionType = SummaryDirection


class DataMapping(object):
    """OCS Data Mapping definition"""

    def __init__(self, target_id: str = None, target_stream_reference_name: str = None,
                 target_field_key: str = None, type_code: SdsTypeCode = None, uom: str = None,
                 summary_type: SdsSummaryType = None, summary_direction: SummaryDirectionType = None,
                 field_set_index: int = None, field_index: int = None):
        self._target_id = target_id
        self._target_stream_reference_name = target_stream_reference_name
        self._target_field_key = target_field_key
        self._type_code = type_code
        self._uom = uom
        self._summary_type = summary_type
        self._summary_direction = summary_direction
        self._field_set_index = field_set_index
        self._field_index = field_index

    @property
    def TargetId(self) -> str:
        return self._target_id

    @TargetId.setter
    def TargetId(self, value: str):
        self._target_id = value

    @property
    def TargetStreamReferenceName(self) -> str:
        return self._target_stream_reference_name

    @TargetStreamReferenceName.setter
    def TargetStreamReferenceName(self, value: str):
        self._target_stream_reference_name = value

    @property
    def TargetFieldKey(self) -> str:
        return self._target_field_key

    @TargetFieldKey.setter
    def TargetFieldKey(self, value: str):
        self._target_field_key = value

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
    def SummaryDirection(self) -> SummaryDirectionType:
        return self._summary_direction

    @SummaryDirection.setter
    def SummaryDirection(self, value: SummaryDirectionType):
        self._summary_direction = value

    @property
    def FieldSetIndex(self) -> int:
        return self._field_set_index

    @FieldSetIndex.setter
    def FieldSetIndex(self, value: int):
        self._field_set_index = value

    @property
    def FieldIndex(self) -> int:
        return self._field_index

    @FieldIndex.setter
    def FieldIndex(self, value: int):
        self._field_index = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {'TargetId': self.TargetId,
                  'TargetStreamReferenceName': self.TargetStreamReferenceName,
                  'TargetFieldKey': self.TargetFieldKey, 'TypeCode': self.TypeCode.value,
                  'Uom': self.Uom, 'SummaryType': self.SummaryType.value}

        if self.SummaryDirection is not None:
            result['SummaryDirection'] = self.SummaryDirection.value

        if self.FieldSetIndex is not None:
            result['FieldSetIndex'] = self.FieldSetIndex

        if self.FieldIndex is not None:
            result['FieldIndex'] = self.FieldIndex

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = DataMapping()

        if not content:
            return result

        if 'TargetId' in content:
            result.TargetId = content['TargetId']

        if 'TargetStreamReferenceName' in content:
            result.TargetStreamReferenceName = content['TargetStreamReferenceName']

        if 'TargetFieldKey' in content:
            result.TargetFieldKey = content['TargetFieldKey']

        if 'TypeCode' in content:
            result.TypeCode = SdsTypeCode[content['TypeCode']]

        if 'Uom' in content:
            result.Uom = content['Uom']

        if 'SummaryType' in content:
            result.SummaryType = SdsSummaryType[content['SummaryType']]

        if 'SummaryDirection' in content:
            result.SummaryDirection = SummaryDirectionType[content['SummaryDirection']]

        if 'FieldSetIndex' in content:
            result.FieldSetIndex = content['FieldSetIndex']

        if 'FieldIndex' in content:
            result.FieldIndex = content['FieldIndex']

        return result
