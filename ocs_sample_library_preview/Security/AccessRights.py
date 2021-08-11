import json

from .CommonAccessRightsEnum import CommonAccessRightsEnum


class AccessRights(object):
    """OCS access rights definition"""

    def __init__(self, access_rights: list[CommonAccessRightsEnum] = None):
        self.AccessRights = access_rights

    @property
    def AccessRights(self) -> list[CommonAccessRightsEnum]:
        return self.__access_rights

    @AccessRights.setter
    def AccessRights(self, value: list[CommonAccessRightsEnum]):
        self.__access_rights = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = []

        for value in self.AccessRights:
          result.append(value.name)

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = AccessRights()

        if not content:
            return result

        if len(content) > 0:
            result.AccessRights = []
            for i in content:
              result.AccessRights.append(CommonAccessRightsEnum[i])
        else:
            result.AccessRights = [CommonAccessRightsEnum.none]

        return result
