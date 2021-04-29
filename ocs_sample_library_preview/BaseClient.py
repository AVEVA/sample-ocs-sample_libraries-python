import requests

from .Authentication import Authentication
from .SdsError import SdsError


class BaseClient(object):
    """Handles communication with Sds Service.  Internal Use"""

    def __init__(self, api_version: str, tenant: str, url: str, client_id: str = None,
                 client_secret: str = None, accept_verbosity: bool = False):
        self.__api_version = api_version
        self.__tenant = tenant
        self.__url = url  # if resource.endswith("/")  else resource + "/"
        self.__accept_verbosity = accept_verbosity
        self.__request_timeout = None
        if (client_id is not None):
            self.__auth_object = Authentication(
                tenant, url, client_id, client_secret)
            self.__auth_object.getToken()
        else:
            self.__auth_object = None

        self.__uri_api = url + '/api/' + api_version

    @property
    def uri(self) -> str:
        """
        Gets the base url
        :return:
        """
        return self.__url

    @property
    def uri_API(self) -> str:
        """
        Returns the base URL plus api versioning information
        :return:
        """
        return self.__uri_api

    @property
    def api_version(self) -> str:
        """
        Returns just the base api versioning information
        :return:
        """
        return self.__api_version

    @property
    def tenant(self) -> str:
        """
        Returns the tenant ID
        :return:
        """
        return self.__tenant

    @property
    def AcceptVerbosity(self) -> bool:
        return self.__accept_verbosity

    @AcceptVerbosity.setter
    def AcceptVerbosity(self, value: bool):
        self.__accept_verbosity = value

    @property
    def RequestTimeout(self) -> int:
        return self.__request_timeout

    @RequestTimeout.setter
    def RequestTimeout(self, value: int):
        self.__request_timeout = value

    def _getToken(self) -> str:
        """
        Gets the bearer token
        :return:
        """
        return self.__auth_object.getToken()

    def sdsHeaders(self) -> dict[str, str]:
        """
        Gets the base headers needed for SDS call
        :return:
        """
        headers = {'Content-type': 'application/json',
                   'Accept': 'application/json'}
        if (self.__auth_object is not None):
            headers['Authorization'] = 'Bearer %s' % self._getToken()
        if (self.__accept_verbosity):
            headers['Accept-Verbosity'] = 'verbose'
        if self.__request_timeout is not None:
            headers['Request-Timeout'] = str(self.__request_timeout)

        return headers

    def checkResponse(self, response, main_message: str):
        if response.status_code < 200 or response.status_code >= 300:
            status = response.status_code
            reason = response.text
            url = response.url

            if 'Operation-Id' in response.headers:
                opId = response.headers['Operation-Id']
                error = f'  {status}:{reason}.  URL {url}  OperationId {opId}'
            else:
                error = f'  {status}:{reason}.  URL {url}'

            response.close()

            message = main_message + error
            raise SdsError(message)

        # this happens on a collection return that is partially successful
        if response.status_code == 207:
            status = response.status_code
            error = response.json['Error']
            reason = response.json['Reason']
            errors = str(response.json['ChildErrors'])
            url = response.url

            if 'Operation-Id' in response.headers:
                opId = response.headers['Operation-Id']
                errorToWrite = f'  {status}:{error}:{reason}. \n\n{errors}\n\n  URL {url}  OperationId {opId}'
            else:
                errorToWrite = f'  {status}:{error}:{reason}. \n\n{errors}\n\n  URL {url}'

            response.close()

            message = main_message + errorToWrite
            raise SdsError(message)

    def request(self, method: str, url: str, params=None, data=None, headers=None, **kwargs):
        if not headers:
            headers = self.sdsHeaders()
        return requests.request(method, url, params=params, data=data, headers=headers, **kwargs)
