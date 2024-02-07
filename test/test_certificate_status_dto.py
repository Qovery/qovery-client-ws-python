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

from qovery-ws.models.certificate_status_dto import CertificateStatusDto

class TestCertificateStatusDto(unittest.TestCase):
    """CertificateStatusDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CertificateStatusDto:
        """Test CertificateStatusDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CertificateStatusDto`
        """
        model = CertificateStatusDto()
        if include_optional:
            return CertificateStatusDto(
                dns_names = [
                    ''
                    ],
                failed_issuance_attempt_count = 0,
                last_failure_issuance_time = 56,
                not_after = 56,
                not_before = 56,
                renewal_time = 56,
                state = 'STARTING',
                state_message = ''
            )
        else:
            return CertificateStatusDto(
                dns_names = [
                    ''
                    ],
                failed_issuance_attempt_count = 0,
                state = 'STARTING',
        )
        """

    def testCertificateStatusDto(self):
        """Test CertificateStatusDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
