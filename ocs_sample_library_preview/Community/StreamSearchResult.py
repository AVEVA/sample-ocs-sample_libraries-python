import json


class StreamSearchResult(object):
    """OCS stream search result definition"""

    def __init__(self, id: str = None, name: str = None, type_id: str = None,
                 description: str = None, self_link: str = None):
        self.Id = id
        self.Name = name
        self.TypeId = type_id
        self.Description = description
        self.Self = self_link

    @property
    def Id(self) -> str:
        return self.__id

    @Id.setter
    def Id(self, value: str):
        self.__id = value

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, value: str):
        self.__name = value

    @property
    def TypeId(self) -> str:
        return self.__type_id

    @TypeId.setter
    def TypeId(self, value: str):
        self.__type_id = value

    @property
    def Description(self) -> str:
        return self.__description

    @Description.setter
    def Description(self, value: str):
        self.__description = value

    @property
    def Self(self) -> str:
        return self.__self

    @Self.setter
    def Self(self, value: str):
        self.__self = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return {'Id': self.Id, 'Name': self.Name, 'TypeId': self.TypeId,
                'Description': self.Description, 'Self': self.Self}

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = StreamSearchResult()

        if not content:
            return result

        if 'Id' in content:
            result.Id = content['Id']

        if 'Name' in content:
            result.Name = content['Name']

        if 'TypeId' in content:
            result.TypeId = content['TypeId']

        if 'Description' in content:
            result.Description = content['Description']

        if 'Self' in content:
            result.Self = content['Self']

        return result
