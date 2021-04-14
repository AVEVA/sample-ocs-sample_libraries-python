import json


class UnresolvedStream(object):
    def __init__(self, name: str = None, reason: str = None):
        self.Name = name
        self.Reason = reason

    @property
    def Name(self) -> str:
        return self._name

    @Name.setter
    def Name(self, value: str):
        self._name = value

    @property
    def Reason(self) -> str:
        return self._reason

    @Reason.setter
    def Reason(self, value: str):
        self._reason = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return {'Name': self.Name, 'Reason': self.Reason}

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = UnresolvedStream()

        if not content:
            return result

        if 'Name' in content:
            result.Name = content['Name']

        if 'Reason' in content:
            result.Reason = content['Reason']

        return result
