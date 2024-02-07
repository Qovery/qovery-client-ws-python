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

from qovery-ws.models.container_state_terminated_dto import ContainerStateTerminatedDto

class TestContainerStateTerminatedDto(unittest.TestCase):
    """ContainerStateTerminatedDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContainerStateTerminatedDto:
        """Test ContainerStateTerminatedDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContainerStateTerminatedDto`
        """
        model = ContainerStateTerminatedDto()
        if include_optional:
            return ContainerStateTerminatedDto(
                exit_code = 56,
                exit_code_message = '',
                finished_at = 56,
                message = '',
                reason = '',
                signal = 56,
                started_at = 56
            )
        else:
            return ContainerStateTerminatedDto(
                exit_code = 56,
                exit_code_message = '',
                message = '',
                reason = '',
                signal = 56,
        )
        """

    def testContainerStateTerminatedDto(self):
        """Test ContainerStateTerminatedDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
