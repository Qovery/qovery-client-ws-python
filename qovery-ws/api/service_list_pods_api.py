# coding: utf-8

"""
    websocket-gateway

    Describe the weboscket endpoints

    The version of the OpenAPI document: 0.1.0
    Contact: erebe@erebe.eu
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from pydantic import StrictStr

from qovery-ws.models.service_list_pods_response_dto import ServiceListPodsResponseDto

from qovery-ws.api_client import ApiClient
from qovery-ws.api_response import ApiResponse
from qovery-ws.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ServiceListPodsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def handle_service_list_pods_request(self, organization : StrictStr, cluster : StrictStr, project : StrictStr, environment : StrictStr, service : StrictStr, **kwargs) -> ServiceListPodsResponseDto:  # noqa: E501
        """handle_service_list_pods_request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.handle_service_list_pods_request(organization, cluster, project, environment, service, async_req=True)
        >>> result = thread.get()

        :param organization: (required)
        :type organization: str
        :param cluster: (required)
        :type cluster: str
        :param project: (required)
        :type project: str
        :param environment: (required)
        :type environment: str
        :param service: (required)
        :type service: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ServiceListPodsResponseDto
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the handle_service_list_pods_request_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.handle_service_list_pods_request_with_http_info(organization, cluster, project, environment, service, **kwargs)  # noqa: E501

    @validate_arguments
    def handle_service_list_pods_request_with_http_info(self, organization : StrictStr, cluster : StrictStr, project : StrictStr, environment : StrictStr, service : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """handle_service_list_pods_request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.handle_service_list_pods_request_with_http_info(organization, cluster, project, environment, service, async_req=True)
        >>> result = thread.get()

        :param organization: (required)
        :type organization: str
        :param cluster: (required)
        :type cluster: str
        :param project: (required)
        :type project: str
        :param environment: (required)
        :type environment: str
        :param service: (required)
        :type service: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ServiceListPodsResponseDto, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'organization',
            'cluster',
            'project',
            'environment',
            'service'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method handle_service_list_pods_request" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['organization']:
            _path_params['organization'] = _params['organization']

        if _params['cluster']:
            _path_params['cluster'] = _params['cluster']

        if _params['project']:
            _path_params['project'] = _params['project']

        if _params['environment']:
            _path_params['environment'] = _params['environment']

        if _params['service']:
            _path_params['service'] = _params['service']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "ServiceListPodsResponseDto",
        }

        return self.api_client.call_api(
            '/service/pods', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
