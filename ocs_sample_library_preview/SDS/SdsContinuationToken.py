class SdsContinuationToken(object):
    """
    definition of SdsContinuationToken
    """

    def __init__(self, token: str = ''):
        self.token = token

    @property
    def token(self) -> str:
        return self.__token

    @token.setter
    def token(self, value: str):
        self.__token = value

    def continuing(self):
      if self.token == None:
        return False
      return True