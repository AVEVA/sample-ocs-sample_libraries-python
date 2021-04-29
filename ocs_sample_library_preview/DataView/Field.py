import json

from .FieldSource import FieldSource


class Field(object):
    """OCS Field definition"""

    def __init__(self, source: FieldSource = None, keys: list[str] = None,
                 stream_reference_names: list[str] = None, label: str = None,
                 include_uom: bool = None):
        """
        :param source: not required
        :param keys: not required
        :param stream_reference_names: not required
        :param label: not required
        :param include_uom: not required
        """
        self.Source = source
        self.Keys = keys
        self.StreamReferenceNames = stream_reference_names
        self.Label = label
        self.IncludeUom = include_uom

    @property
    def Source(self) -> FieldSource:
        """
        not required
        :return:
        """
        return self.__source

    @Source.setter
    def Source(self, value: FieldSource):
        """
        not required
        :param value:
        :return:
        """
        self.__source = value

    @property
    def Keys(self) -> list[str]:
        """
        not required
        :return:
        """
        return self.__keys

    @Keys.setter
    def Keys(self, value: list[str]):
        """
        not required
        :param value:
        :return:
        """
        self.__keys = value

    @property
    def StreamReferenceNames(self) -> list[str]:
        """
        not required
        :return:
        """
        return self.__stream_reference_names

    @StreamReferenceNames.setter
    def StreamReferenceNames(self, value: list[str]):
        """
        not required
        :param value:
        :return:
        """
        self.__stream_reference_names = value

    @property
    def Label(self) -> str:
        """
        not required
        :return:
        """
        return self.__label

    @Label.setter
    def Label(self, value: str):
        """
        not required
        :param value:
        :return:
        """
        self.__label = value

    @property
    def IncludeUom(self) -> bool:
        """
        not required
        :return:
        """
        return self.__include_uom

    @IncludeUom.setter
    def IncludeUom(self, value: bool):
        """
        not required
        :param value:
        :return:
        """
        self.__include_uom = value

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        result = {}

        # optional properties
        if self.Source is not None:
            result['Source'] = self.Source.name

        if self.Keys is not None:
            result['Keys'] = []
            for value in self.Keys:
                result['Keys'].append(value)

        if self.StreamReferenceNames is not None:
            result['StreamReferenceNames'] = []
            for value in self.StreamReferenceNames:
                result['StreamReferenceNames'].append(value)

        if self.Label is not None:
            result['Label'] = self.Label

        if self.IncludeUom is not None:
            result['IncludeUom'] = self.IncludeUom

        return result

    @staticmethod
    def fromJson(content: dict[str, str]):
        result = Field()

        if not content:
            return result

        if 'Source' in content:
            result.Source = FieldSource[content['Source']]

        if 'Keys' in content:
            keys = content['Keys']
            if keys is not None and len(keys) > 0:
                result.Keys = []
                for value in keys:
                    result.Keys.append(value)

        if 'StreamReferenceNames' in content:
            stream_reference_names = content['StreamReferenceNames']
            if stream_reference_names is not None and len(stream_reference_names) > 0:
                result.StreamReferenceNames = []
                for value in stream_reference_names:
                    result.StreamReferenceNames.append(value)

        if 'Label' in content:
            result.Label = content['Label']

        if 'IncludeUom' in content:
            result.IncludeUom = content['IncludeUom']

        return result
