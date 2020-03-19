##############################################################################
# Copyright (c) 2020 China Mobile Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################
'''
a common http_handler
'''
import urllib.request
import json
import ssl
from http.client import HTTPException
from urllib.error import HTTPError, URLError
# pylint: disable=E0611
from log_utils import LOGGER
from errors import ERROR_CODE

# pylint: disable=W0212
ssl._create_default_https_context = ssl._create_unverified_context

HEADERS = {
    'Connection': 'keep-alive',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
}

TIME_OUT = 3000


class UrllibHttpHandler:
    """
    http handler based on urllib of python2.7
    """

    def __init__(self):
        self.__header = HEADERS

    def get(self, url):
        """
        run the get request
        """
        try:
            req = urllib.request.Request(url, headers=self.__header)
            res = urllib.request.urlopen(req, timeout=TIME_OUT)
        except HTTPException as http_exp:
            LOGGER.error(http_exp)
            LOGGER.error(u"%s %s", ERROR_CODE['E100001'], url)
        except HTTPError as http_err:
            LOGGER.error(http_err)
            LOGGER.error(u"%s %s", ERROR_CODE['E100001'], url)
            LOGGER.error(u"%s %s", ERROR_CODE['E600001'], url)
        else:
            return res

    def post(self, url, parameter=None):
        """
        run the post request, parameter must to encode to bytes
        """
        try:
            data = json.dumps(parameter).encode(encoding="utf-8")
            LOGGER.debug("data is %s", data)
            req = urllib.request.Request(url, data=data, headers=self.__header)
            req.add_header("Content-Type", "application/json")
            res = urllib.request.urlopen(req, timeout=TIME_OUT)
        except HTTPException as http_exp:
            LOGGER.error(http_exp)
            LOGGER.error(u"%s %s", ERROR_CODE['E100001'], url)
        except TimeoutError as timeout_error:
            LOGGER.error(timeout_error)
            LOGGER.error(u"%s", ERROR_CODE['E100003'])
        except HTTPError as http_err:
            LOGGER.error(http_err)
            LOGGER.error(u"%s %s", ERROR_CODE['E100001'], url)
            LOGGER.error(u"%s %s", ERROR_CODE['E600001'], url)
        except URLError as url_err:
            LOGGER.error(url_err)
            LOGGER.error(u"%s %s", ERROR_CODE['E100001'], url)
        else:
            return res

    def put(self, url, parameter=None):
        """
        run the put request, parameter must to encode to bytes
        """
#         parameter_data = urllib.parse.urlencode(parameter) #??
        data = json.dumps(parameter).encode(encoding="utf-8")
        LOGGER.debug("data is %s", data)
        req = urllib.request.Request(url, data=data, headers=self.__header)
        req.get_method = lambda: 'PUT'
        res = urllib.request.urlopen(req)
        return res

    def patch(self, url, parameter=None, etag=None):
        """
        run the patch request, parameter must to encode to bytes
        """
        data = json.dumps(parameter).encode(encoding="utf-8")
        LOGGER.debug("data is %s", data)
        req = urllib.request.Request(url, data=data, headers=self.__header)
        req.add_header("Content-Type", "application/json")
        req.add_header("If-Match", etag)
        req.get_method = lambda: 'PATCH'
        res = None
        try:
            res = urllib.request.urlopen(req, timeout=TIME_OUT)
        except HTTPException as http_exp:
            LOGGER.error(http_exp)
            LOGGER.error(u"%s %s", ERROR_CODE['E100001'], url)
        except HTTPError as http_err:
            LOGGER.error(http_err)
            LOGGER.error(u"%s %s", ERROR_CODE['E100001'], url)
            LOGGER.error(u"%s %s", ERROR_CODE['E600001'], url)
        except TypeError as type_err:
            LOGGER.error(type_err)
            LOGGER.error(u"%s %s", ERROR_CODE['E100001'], url)
        return res

    def delete(self, url):
        '''
        run the delete request,
        '''
        req = urllib.request.Request(url, headers=self.__header)
        req.get_method = lambda: 'DELETE'
        res = urllib.request.urlopen(req)
        return res
