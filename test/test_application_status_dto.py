"""
    websocket-gateway

    Describe the weboscket endpoints  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: erebe@erebe.eu
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import qovery
from qovery.model.certificate_status_dto import CertificateStatusDto
from qovery.model.pod_status_dto import PodStatusDto
from qovery.model.service_state_dto import ServiceStateDto
globals()['CertificateStatusDto'] = CertificateStatusDto
globals()['PodStatusDto'] = PodStatusDto
globals()['ServiceStateDto'] = ServiceStateDto
from qovery.model.application_status_dto import ApplicationStatusDto


class TestApplicationStatusDto(unittest.TestCase):
    """ApplicationStatusDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApplicationStatusDto(self):
        """Test ApplicationStatusDto"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApplicationStatusDto()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()