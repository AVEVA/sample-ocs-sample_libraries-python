import json

from .SdsStreamView import SdsStreamView


class SdsStreamViewProperty(object):
    """Sds StreamView Property definition"""
    @property
    def SourceId(self) -> str:
        """
        required
        :return:
        """
        return self.__source_id

    @SourceId.setter
    def SourceId(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self.__source_id = value

    @property
    def TargetId(self) -> str:
        """
        required
        :return:
        """
        return self.__target_id

    @TargetId.setter
    def TargetId(self, value: str):
        """
        required
        :param value:
        :return:
        """
        self.__target_id = value

    @property
    def SdsStreamView(self) -> SdsStreamView:
        """
        not required
        :return:
        """
        return self.__sds_stream_view

    @SdsStreamView.setter
    def SdsStreamView(self, value: SdsStreamView):
        """
        not required
        :param value:
        :return:
        """
        self.__sds_stream_view = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {'SourceId': self.SourceId, 'TargetId': self.TargetId}

        if self.SdsStreamView is not None:
            result['SdsStreamView'] = self.SdsStreamView.toDictionary()

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = SdsStreamViewProperty()

        if not content:
            return result

        if 'SourceId' in content:
            result.SourceId = content['SourceId']

        if 'TargetId' in content:
            result.TargetId = content['TargetId']

        if 'SdsStreamView' in content:
            result.SdsStreamView = SdsStreamView.fromJson(
                content['SdsStreamView'])

        return result
