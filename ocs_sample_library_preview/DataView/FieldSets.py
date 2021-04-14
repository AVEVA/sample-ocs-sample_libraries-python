import json
from .FieldSet import FieldSet


class ResolvedFieldSets(object):
    """OCS Resolved Field Sets definition"""

    def __init__(self, time_of_resolution: str = None, items: list[FieldSet] = None):
        self._time_of_resolution = time_of_resolution
        self._items = items

    @property
    def TimeOfResolution(self) -> str:
        return self._time_of_resolution

    @TimeOfResolution.setter
    def TimeOfResolution(self, value: str):
        self._time_of_resolution = value

    @property
    def Items(self) -> list[FieldSet]:
        return self._items

    @Items.setter
    def Items(self, value: list[FieldSet]):
        self._items = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        result = {'TimeOfResolution': self.TimeOfResolution, 'Items': []}

        if self.Items is not None:
            for value in self.Items:
                result['Items'].append(value.toDictionary())

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = ResolvedFieldSets()

        if not content:
            return result

        if 'TimeOfResolution' in content:
            result.TimeOfResolution = content['TimeOfResolution']

        if 'Items' in content:
            items = content["Items"]
            if items is not None and len(items) > 0:
                result.Items = []
                for value in items:
                    result.Items.append(FieldSet.fromJson(value))

        return result
