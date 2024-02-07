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

from qovery-ws.models.database_status_dto import DatabaseStatusDto

class TestDatabaseStatusDto(unittest.TestCase):
    """DatabaseStatusDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatabaseStatusDto:
        """Test DatabaseStatusDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatabaseStatusDto`
        """
        model = DatabaseStatusDto()
        if include_optional:
            return DatabaseStatusDto(
                id = '',
                pods = [
                    qovery-ws.models.pod_status_dto.PodStatusDto(
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
                        started_at = null, 
                        state = 'STARTING', 
                        state_message = '', 
                        state_reason = '', )
                    ],
                state = 'STARTING'
            )
        else:
            return DatabaseStatusDto(
                id = '',
                pods = [
                    qovery-ws.models.pod_status_dto.PodStatusDto(
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
                        started_at = null, 
                        state = 'STARTING', 
                        state_message = '', 
                        state_reason = '', )
                    ],
                state = 'STARTING',
        )
        """

    def testDatabaseStatusDto(self):
        """Test DatabaseStatusDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
