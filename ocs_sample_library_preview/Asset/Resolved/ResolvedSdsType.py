import json
from typing import List

from ...SDS.SdsTypeCode import SdsTypeCode
from .ResolvedEnum import ResolvedEnum

# Alias class to avoid conflict with SdsTypeCode property
SdsTypeCodeType = SdsTypeCode


class ResolvedSdsType(object):
    def __init__(self, sds_type_code: SdsTypeCodeType = None, properties: List[ResolvedEnum] = None):
        self.SdsTypeCode = sds_type_code
        self.Properties = properties

    @property
    def SdsTypeCode(self) -> SdsTypeCodeType:
        return self.__sds_type_code

    @SdsTypeCode.setter
    def SdsTypeCode(self, value: SdsTypeCodeType):
        self.__sds_type_code = value

    @property
    def Properties(self) -> List[ResolvedEnum]:
        return self.__properties

    @Properties.setter
    def Properties(self, value: List[ResolvedEnum]):
        self.__properties = value

    def to_json(self):
        return json.dumps(self.to_dictionary())

    def to_dictionary(self):
        result = {'SdsTypeCode': self.SdsTypeCode.value, 'Properties': []}

        if self.Properties is not None:
            for value in self.Properties:
                result['Properties'].append(value.to_dictionary())

        return result

    @staticmethod
    def from_json(content):
        result = ResolvedSdsType()

        if not content:
            return result

        if 'SdsTypeCode' in content:
            result.SdsTypeCode = SdsTypeCode[content['SdsTypeCode']]

        if 'Properties' in content:
            properties = content['Properties']
            if properties is not None and len(properties) > 0:
                result.Properties = []
                for value in properties:
                    result.Properties.append(
                        ResolvedEnum.from_json(value))

        return result
