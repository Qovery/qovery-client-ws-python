# coding: utf-8

"""
    websocket-gateway

    Describe the weboscket endpoints

    The version of the OpenAPI document: 0.1.0
    Contact: erebe@erebe.eu
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from qovery-ws.models.node_condition_dto import NodeConditionDto  # noqa: E501

class TestNodeConditionDto(unittest.TestCase):
    """NodeConditionDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NodeConditionDto:
        """Test NodeConditionDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NodeConditionDto`
        """
        model = NodeConditionDto()  # noqa: E501
        if include_optional:
            return NodeConditionDto(
                last_heartbeat_time = 56,
                last_transition_time = 56,
                message = '',
                reason = '',
                status = '',
                type = ''
            )
        else:
            return NodeConditionDto(
                message = '',
                reason = '',
                status = '',
                type = '',
        )
        """

    def testNodeConditionDto(self):
        """Test NodeConditionDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
