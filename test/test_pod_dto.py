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

from qovery-ws.models.pod_dto import PodDto  # noqa: E501

class TestPodDto(unittest.TestCase):
    """PodDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PodDto:
        """Test PodDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PodDto`
        """
        model = PodDto()  # noqa: E501
        if include_optional:
            return PodDto(
                name = '',
                ports = [
                    0
                    ]
            )
        else:
            return PodDto(
                name = '',
                ports = [
                    0
                    ],
        )
        """

    def testPodDto(self):
        """Test PodDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
