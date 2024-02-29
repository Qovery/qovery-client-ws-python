# coding: utf-8

"""
    websocket-gateway

    Describe the weboscket endpoints

    The version of the OpenAPI document: 0.1.0
    Contact: erebe@erebe.eu
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ServiceStateDto(str, Enum):
    """
    ServiceStateDto
    """

    """
    allowed enum values
    """
    STARTING = 'STARTING'
    RUNNING = 'RUNNING'
    ERROR = 'ERROR'
    STOPPING = 'STOPPING'
    STOPPED = 'STOPPED'
    COMPLETED = 'COMPLETED'
    WARNING = 'WARNING'

    @classmethod
    def from_json(cls, json_str: str) -> ServiceStateDto:
        """Create an instance of ServiceStateDto from a JSON string"""
        return ServiceStateDto(json.loads(json_str))

