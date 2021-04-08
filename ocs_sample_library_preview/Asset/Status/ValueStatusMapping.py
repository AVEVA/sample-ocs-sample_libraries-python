import json
from typing import Any

from .StatusEnum import StatusEnum


class ValueStatusMapping(object):
    """OCS Asset Value Status Mapping definition"""

    def __init__(self, value: Any = None, status: StatusEnum = None, display_name: str = None):
        """
        :param value: required
        :param status: required
        :param display_name: not required
        """
        self.Value = value
        self.Status = status
        self.DisplayName = display_name

    @property
    def Value(self) -> Any:
        """
        required
        :return:
        """
        return self.__value

    @Value.setter
    def Value(self, value: Any):
        """
        required
        :param value:
        :return:
        """
        self.__value = value

    @property
    def Status(self) -> StatusEnum:
        """
        StatusEnum    required
        :return:
        """
        return self.__status

    @Status.setter
    def Status(self, value: StatusEnum):
        """
        StatusEnum    required
        :param value:
        :return:
        """
        self.__status = value

    @property
    def DisplayName(self) -> str:
        """
        not required
        :return:
        """
        return self.__display_name

    @DisplayName.setter
    def DisplayName(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__display_name = value

    def to_json(self):
        return json.dumps(self.to_dictionary())

    def to_dictionary(self):
        # required properties
        result = {'Value': self.Value, 'Status': self.Status.value}

        # optional properties
        if hasattr(self, 'DisplayName'):
            result['DisplayName'] = self.DisplayName

        return result

    @staticmethod
    def from_json(content):
        result = ValueStatusMapping()

        if not content:
            return result

        if 'Value' in content:
            result.Value = content['Value']

        if 'Status' in content:
            result.Status = StatusEnum(content['Status'])

        if 'DisplayName' in content:
            result.DisplayName = content['DisplayName']
