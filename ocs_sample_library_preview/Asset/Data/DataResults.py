import json
from typing import Any, List

from .DataErrors import DataErrors


class DataResults(object):
    def __init__(self, results: dict[str, List[Any]] = None, errors: DataErrors = None):
        self.Results = results
        self.Errors = errors

    @property
    def Results(self) -> dict[str, List[Any]]:
        return self.__results

    @Results.setter
    def Results(self, value: dict[str, List[Any]]):
        self.__results = value

    @property
    def Errors(self) -> DataErrors:
        return self.__errors

    @Errors.setter
    def Errors(self, value: DataErrors):
        self.__errors = value

    def to_json(self):
        return json.dumps(self.to_dictionary())

    def to_dictionary(self):
        result = {'Results': self.Results}

        if self.Errors is not None:
            result['Errors'] = self.Errors.to_dictionary()

        return result

    @staticmethod
    def from_json(content):
        result = DataResults()

        if not content:
            return result

        if 'Results' in content:
            results = content['Results']
            if results is not None and len(results) > 0:
                result.Results = {}
                for key in results:
                    result.Results[key] = results[key]

        if 'Errors' in content:
            result.Errors = DataErrors.from_json(content['Errors'])

        return result
