import json

from ..SDS.SdsTypeCode import SdsTypeCode

# Alias class to avoid conflict with SdsTypeCode property
SdsTypeCodeType = SdsTypeCode


class MetadataItem(object):
    """OCS Asset Metadata Item definition"""

    def __init__(self, id: str = None, name: str = None, description: str = None,
                 sds_type_code: SdsTypeCodeType = None, uom: str = None, value: str = None):
        """
        :param id: required
        :param name: required
        :param description: not required
        :param sds_type_code: required
        :param uom: not required
        :param value: not required
        """
        self.Id = id
        self.Name = name
        self.Description = description
        self.SdsTypeCode = sds_type_code
        self.Uom = uom
        self.Value = value

    @property
    def Id(self) -> str:
        """
        required
        :return:
        """
        return self.__id

    @Id.setter
    def Id(self, value: str):
        """"
        required
        :param value:
        :return:
        """
        self.__id = value

    @property
    def Name(self) -> str:
        """
        required
        :return:
        """
        return self.__name

    @Name.setter
    def Name(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self.__name = value

    @property
    def Description(self) -> str:
        """
        not required
        :return:
        """
        return self.__description

    @Description.setter
    def Description(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__description = value

    @property
    def SdsTypeCode(self) -> SdsTypeCodeType:
        """
        SdsTypeCode required
        :return:
        """
        return self.__sds_type_code

    @SdsTypeCode.setter
    def SdsTypeCode(self, value: SdsTypeCodeType):
        """
        SdsTypeCode    required
        :param value:
        :return:
        """
        self.__sds_type_code = value

    @property
    def Uom(self) -> str:
        """
        not required
        :return:
        """
        return self.__uom

    @Uom.setter
    def Uom(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__uom = value

    @property
    def Value(self) -> str:
        """
        not required
        :return:
        """
        return self.__value

    @Value.setter
    def Value(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__value = value

    def to_json(self):
        return json.dumps(self.to_dictionary())

    def to_dictionary(self):
        # required properties
        result = {'Id': self.Id, 'Name': self.Name,
                  'SdsTypeCode': self.SdsTypeCode.value}

        # optional properties
        if hasattr(self, 'Description'):
            result['Description'] = self.Description

        if hasattr(self, 'Uom'):
            result['Uom'] = self.Uom

        if hasattr(self, 'Value'):
            result['Value'] = self.Value

        return result

    @staticmethod
    def from_json(content):
        result = MetadataItem()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        if 'SdsTypeCode' in content:
            result.SdsTypeCode = SdsTypeCode(content['SdsTypeCode'])

        if 'Uom' in content:
            result.Uom = content['Uom']

        if 'Value' in content:
            result.Value = content['Value']
