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

from qovery-ws.models.application_status_dto import ApplicationStatusDto  # noqa: E501

class TestApplicationStatusDto(unittest.TestCase):
    """ApplicationStatusDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApplicationStatusDto:
        """Test ApplicationStatusDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApplicationStatusDto`
        """
        model = ApplicationStatusDto()  # noqa: E501
        if include_optional:
            return ApplicationStatusDto(
                certificates = [
                    qovery-ws.models.certificate_status_dto.CertificateStatusDto(
                        dns_names = [
                            ''
                            ], 
                        failed_issuance_attempt_count = 0, 
                        last_failure_issuance_time = null, 
                        not_after = null, 
                        not_before = null, 
                        renewal_time = null, 
                        state = 'STARTING', 
                        state_message = '', )
                    ],
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
            return ApplicationStatusDto(
                certificates = [
                    qovery-ws.models.certificate_status_dto.CertificateStatusDto(
                        dns_names = [
                            ''
                            ], 
                        failed_issuance_attempt_count = 0, 
                        last_failure_issuance_time = null, 
                        not_after = null, 
                        not_before = null, 
                        renewal_time = null, 
                        state = 'STARTING', 
                        state_message = '', )
                    ],
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

    def testApplicationStatusDto(self):
        """Test ApplicationStatusDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
