from typing import List

from .ResolvedProperty import ResolvedProperty


class ResolvedStream(object):
    def __init__(self, name: str = None, properties: List[ResolvedProperty] = None):
        self.Name = name
        self.Properties = properties

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str):
        self.__name = value

    @property
    def Properties(self) -> List[ResolvedProperty]:
        return self.__properties

    @Properties.setter
    def Properties(self, value: List[ResolvedProperty]):
        self.__properties = value

    @staticmethod
    def from_json(content):
        result = ResolvedStream()

        if not content:
            return result

        if 'Name' in content:
            result.Name = content['Name']

        if 'Properties' in content:
            properties = content['Properties']
            if properties is not None and len(properties) > 0:
                result.Properties = []
                for value in properties:
                    result.Properties.append(
                        ResolvedProperty.from_json(value))
