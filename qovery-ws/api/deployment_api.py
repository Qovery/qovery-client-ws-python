"""
    websocket-gateway

    Describe the weboscket endpoints  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: erebe@erebe.eu
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from qovery-ws.api_client import ApiClient, Endpoint as _Endpoint
from qovery-ws.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)


class DeploymentApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.handle_deployment_logs_request_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [],
                'endpoint_path': '/deployment/logs',
                'operation_id': 'handle_deployment_logs_request',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'organization',
                    'cluster',
                    'project',
                    'environment',
                    'version',
                ],
                'required': [
                    'organization',
                    'cluster',
                    'project',
                    'environment',
                    'version',
                ],
                'nullable': [
                    'cluster',
                    'version',
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'organization':
                        (str,),
                    'cluster':
                        (str, none_type,),
                    'project':
                        (str,),
                    'environment':
                        (str,),
                    'version':
                        (str, none_type,),
                },
                'attribute_map': {
                    'organization': 'organization',
                    'cluster': 'cluster',
                    'project': 'project',
                    'environment': 'environment',
                    'version': 'version',
                },
                'location_map': {
                    'organization': 'path',
                    'cluster': 'path',
                    'project': 'path',
                    'environment': 'path',
                    'version': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.handle_deployment_status_request_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [],
                'endpoint_path': '/deployment/status',
                'operation_id': 'handle_deployment_status_request',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'organization',
                    'cluster',
                    'project',
                    'environment',
                    'version',
                ],
                'required': [
                    'organization',
                    'cluster',
                    'project',
                    'environment',
                    'version',
                ],
                'nullable': [
                    'cluster',
                    'environment',
                    'version',
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'organization':
                        (str,),
                    'cluster':
                        (str, none_type,),
                    'project':
                        (str,),
                    'environment':
                        (str, none_type,),
                    'version':
                        (str, none_type,),
                },
                'attribute_map': {
                    'organization': 'organization',
                    'cluster': 'cluster',
                    'project': 'project',
                    'environment': 'environment',
                    'version': 'version',
                },
                'location_map': {
                    'organization': 'path',
                    'cluster': 'path',
                    'project': 'path',
                    'environment': 'path',
                    'version': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def handle_deployment_logs_request(
        self,
        organization,
        cluster,
        project,
        environment,
        version,
        **kwargs
    ):
        """handle_deployment_logs_request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.handle_deployment_logs_request(organization, cluster, project, environment, version, async_req=True)
        >>> result = thread.get()

        Args:
            organization (str):
            cluster (str, none_type):
            project (str):
            environment (str):
            version (str, none_type):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            str
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['organization'] = \
            organization
        kwargs['cluster'] = \
            cluster
        kwargs['project'] = \
            project
        kwargs['environment'] = \
            environment
        kwargs['version'] = \
            version
        return self.handle_deployment_logs_request_endpoint.call_with_http_info(**kwargs)

    def handle_deployment_status_request(
        self,
        organization,
        cluster,
        project,
        environment,
        version,
        **kwargs
    ):
        """handle_deployment_status_request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.handle_deployment_status_request(organization, cluster, project, environment, version, async_req=True)
        >>> result = thread.get()

        Args:
            organization (str):
            cluster (str, none_type):
            project (str):
            environment (str, none_type):
            version (str, none_type):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            str
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['organization'] = \
            organization
        kwargs['cluster'] = \
            cluster
        kwargs['project'] = \
            project
        kwargs['environment'] = \
            environment
        kwargs['version'] = \
            version
        return self.handle_deployment_status_request_endpoint.call_with_http_info(**kwargs)

