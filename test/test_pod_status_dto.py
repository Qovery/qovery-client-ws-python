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

from qovery-ws.models.pod_status_dto import PodStatusDto  # noqa: E501

class TestPodStatusDto(unittest.TestCase):
    """PodStatusDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PodStatusDto:
        """Test PodStatusDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PodStatusDto`
        """
        model = PodStatusDto()  # noqa: E501
        if include_optional:
            return PodStatusDto(
                containers = [
                    qovery-ws.models.container_status_dto.ContainerStatusDto(
                        current_state = null, 
                        image = '', 
                        last_terminated_state = null, 
                        name = '', 
                        restart_count = 0, )
                    ],
                name = '',
                restart_count = 0,
                service_version = '',
                started_at = 56,
                state = 'STARTING',
                state_message = '',
                state_reason = ''
            )
        else:
            return PodStatusDto(
                containers = [
                    qovery-ws.models.container_status_dto.ContainerStatusDto(
                        current_state = null, 
                        image = '', 
                        last_terminated_state = null, 
                        name = '', 
                        restart_count = 0, )
                    ],
                name = '',
                restart_count = 0,
                service_version = '',
                state = 'STARTING',
                state_message = '',
                state_reason = '',
        )
        """

    def testPodStatusDto(self):
        """Test PodStatusDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
