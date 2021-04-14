import json
from typing import Any


class DataErrors(object):
    def __init__(self, operation_id: str = None, error: str = None, reason: str = None,
                 child_errors: dict[str, Any] = None):
        self.OperationId = operation_id
        self.Error = error
        self.Reason = reason
        self.ChildErrors = child_errors

    @property
    def OperationId(self) -> str:
        return self._operation_id

    @OperationId.setter
    def OperationId(self, value: str):
        self._operation_id = value

    @property
    def Error(self) -> str:
        return self._error

    @Error.setter
    def Error(self, value: str):
        self._error = value

    @property
    def Reason(self) -> str:
        return self._reason

    @Reason.setter
    def Reason(self, value: str):
        self._reason = value

    @property
    def ChildErrors(self) -> dict[str, Any]:
        return self._child_errors

    @ChildErrors.setter
    def ChildErrors(self, value: dict[str, Any]):
        self._child_errors = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        return {'OperationId': self.OperationId, 'Error': self.Error, 'Reason': self.Reason,
                'ChildErrors': self.ChildErrors}

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = DataErrors()

        if not content:
            return result

        if 'OperationId' in content:
            result.OperationId = content['OperationId']

        if 'Error' in content:
            result.Error = content['Error']

        if 'Reason' in content:
            result.Reason = content['Reason']

        if 'ChildErrors' in content:
            child_errors = content['ChildErrors']
            if child_errors is not None and len(child_errors) > 0:
                result.ChildErrors = {}
                for key in child_errors:
                    result.ChildErrors[key] = child_errors[key]

        return result
