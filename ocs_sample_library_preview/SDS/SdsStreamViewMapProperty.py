import json

from .. import SDS
from .Enum import SdsStreamViewMode


class SdsStreamViewMapProperty(object):
    """Sds StreamViewMap Property definition"""
    @property
    def SourceId(self) -> str:
        """
        required
        :return:
        """
        return self._source_id

    @SourceId.setter
    def SourceId(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self._source_id = value

    @property
    def TargetId(self) -> str:
        """
        required
        :return:
        """
        return self._target_id

    @TargetId.setter
    def TargetId(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self._target_id = value

    @property
    def Mode(self) -> SdsStreamViewMode:
        """
        not required
        :return:
        """
        return self._mode

    @Mode.setter
    def Mode(self, value: SdsStreamViewMode):
        """
        not required
        :param value:
        :return:
        """
        self._mode = value

    @property
    def SdsStreamViewMap(self) -> SDS.SdsStreamViewMap:
        """
        not required
        :return:
        """
        return self._sds_stream_view_map

    @SdsStreamViewMap.setter
    def SdsStreamViewMap(self, value: SDS.SdsStreamViewMap):
        """
        not required
        :param value:
        :return:
        """
        self._sds_stream_view_map = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'SourceId': self.SourceId, 'TargetId': self.TargetId}

        if self.Mode is not None:
            result['Mode'] = self.Mode.name

        if self.SdsStreamViewMap is not None:
            result['SdsStreamViewMap'] = self.SdsStreamViewMap.toDictionary()

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = SdsStreamViewMapProperty()

        if not content:
            return result

        if 'SourceId' in content:
            result.SourceId = content['SourceId']

        if 'TargetId' in content:
            result.TargetId = content['TargetId']

        if 'Mode' in content:
            result.Mode = SdsStreamViewMode[content['Mode']]

        if 'SdsStreamViewMap' in content:
            result.SdsStreamViewMap = SDS.SdsStreamView.fromJson(
                content['SdsStreamViewMap'])

        return result
