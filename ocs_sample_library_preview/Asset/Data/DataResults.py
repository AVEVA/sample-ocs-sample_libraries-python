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

    @staticmethod
    def from_json(content):
        result = DataResults()

        if not content:
            return result

        if 'Results' in content:
            result.Results = content['Results']

        if 'Errors' in content:
            result.Errors = DataErrors.from_json(content['Errors'])
