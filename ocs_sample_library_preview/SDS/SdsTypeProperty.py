from enum import Enum
import json
from typing import Any

from .. import SDS
from .Enum import SdsInterpolationMode


class SdsTypeProperty(object):
    """
    Sds type property definition
    """

    def __init__(self, id: str = None, name: str = None, description: str = None, order: int = None,
                 is_key: bool = None, fixed_size: int = None, sds_type: SDS.SdsType = None,
                 value: Any = None, uom: str = None,
                 interpolation_mode: SdsInterpolationMode = None):
        """
        :param id: required
        :param name: not required
        :param description: not required
        :param order: not required
        :param is_key: required
        :param fixed_size: not required
        :param sds_type: required
        :param value: not required
        :param uom: not required
        :param interpolation_mode: not required
        """
        self.Id = id
        self.Name = name
        self.Description = description
        self.Order = order
        self.IsKey = is_key
        self.FixedSize = fixed_size
        self.SdsType = sds_type
        self.Value = value
        self.Uom = uom
        self.InterpolationMode = interpolation_mode

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
    def Name(self) -> str:
        """
        not required
        :return:
        """
        return self._name

    @Name.setter
    def Name(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self._name = value

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
    def Order(self) -> int:
        """
        not required
        :return:
        """
        return self._order

    @Order.setter
    def Order(self, value: int):
        """
        not required
        :param value:
        :return:
        """
        self._order = value

    @property
    def IsKey(self) -> bool:
        """
        required
        :return:
        """
        return self._is_key

    @IsKey.setter
    def IsKey(self, value: bool):
        """
        required
        :param value:
        :return:
        """
        self._is_key = value

    @property
    def FixedSize(self) -> int:
        """
        not required
        :return:
        """
        return self._fixed_size

    @FixedSize.setter
    def FixedSize(self, value: int):
        """
        not required
        :param value:
        :return:
        """
        self._fixed_size = value

    @property
    def SdsType(self) -> SDS.SdsType:
        """
        required
        :return:
        """
        return self._sds_type

    @SdsType.setter
    def SdsType(self, value: SDS.SdsType):
        """
        required
        :param value:
        :return:
        """
        self._sds_type = value

    @property
    def Value(self) -> Any:
        """
        not required
        :return:
        """
        return self._value

    @Value.setter
    def Value(self, value: Any):
        """
        not required
        :param value:
        :return:
        """
        self._value = value

    @property
    def Uom(self) -> str:
        """
        not required
        :return:
        """
        return self._uom

    @Uom.setter
    def Uom(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self._uom = value

    @property
    def InterpolationMode(self) -> SdsInterpolationMode:
        """
        not required
        :return:
        """
        return self._interpolation_mode

    @InterpolationMode.setter
    def InterpolationMode(self, value: SdsInterpolationMode):
        """
        not required
        :param value:
        :return:
        """
        self._interpolation_mode = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'Id': self.Id, 'IsKey': self.IsKey,
                  'SdsType': self.SdsType.toDictionary()}

        # optional properties
        if self.Name is not None:
            result['Name'] = self.Name

        if self.Description is not None:
            result['Description'] = self.Description

        if self.Order is not None:
            result['Order'] = self.Order

        if self.FixedSize is not None:
            result['FixedSize'] = self.FixedSize

        if self.Value is not None:
            if (isinstance(self.Value, Enum)):
                result['Value'] = self.Value.name
            else:
                result['Value'] = self.Value

        if self.Uom is not None:
            result['Uom'] = self.Uom

        if self.InterpolationMode is not None:
            result['InterpolationMode'] = self.InterpolationMode.name

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = SdsTypeProperty()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'Description' in content:
            result.Description = content['Description']

        if 'Order' in content:
            result.Order = content['Order']

        if 'IsKey' in content:
            result.IsKey = content['IsKey']

        if 'FixedSize' in content:
            result.FixedSize = content['FixedSize']

        if 'SdsType' in content:
            result.SdsType = SDS.SdsType.fromJson(content['SdsType'])

        if 'Value' in content:
            result.Value = content['Value']

        if 'Uom' in content:
            result.Uom = content['Uom']

        if 'InterpolationMode' in content:
            result.InterpolationMode = SdsInterpolationMode(
                content['InterpolationMode'])

        return result
