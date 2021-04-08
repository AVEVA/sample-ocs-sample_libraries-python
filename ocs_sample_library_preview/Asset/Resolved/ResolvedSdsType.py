from typing import List

from ...SDS.SdsTypeCode import SdsTypeCode
from ..Resolved.ResolvedSource import ResolvedSource

# Alias class to avoid conflict with SdsTypeCode property
SdsTypeCodeType = SdsTypeCode


class ResolvedSdsType(object):
    def __init__(self, sds_type_code: SdsTypeCodeType = None, properties: List[ResolvedSource] = None):
        self.SdsTypeCode = sds_type_code
        self.Properties = properties

    @property
    def SdsTypeCode(self) -> SdsTypeCodeType:
        return self.__sds_type_code

    @SdsTypeCode.setter
    def SdsTypeCode(self, value: SdsTypeCodeType):
        self.__sds_type_code = value

    @property
    def Properties(self) -> List[ResolvedSource]:
        return self.__properties

    @Properties.setter
    def Properties(self, value: List[ResolvedSource]):
        self.__properties = value

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
                        ResolvedSource.from_json(value))
