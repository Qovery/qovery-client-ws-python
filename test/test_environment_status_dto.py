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
from qovery.model.application_status_dto import ApplicationStatusDto
from qovery.model.database_status_dto import DatabaseStatusDto
from qovery.model.service_state_dto import ServiceStateDto
globals()['ApplicationStatusDto'] = ApplicationStatusDto
globals()['DatabaseStatusDto'] = DatabaseStatusDto
globals()['ServiceStateDto'] = ServiceStateDto
from qovery.model.environment_status_dto import EnvironmentStatusDto


class TestEnvironmentStatusDto(unittest.TestCase):
    """EnvironmentStatusDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEnvironmentStatusDto(self):
        """Test EnvironmentStatusDto"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EnvironmentStatusDto()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()