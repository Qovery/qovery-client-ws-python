"""
    websocket-gateway

    Describe the weboscket endpoints  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: erebe@erebe.eu
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import qovery-ws
from qovery-ws.model.container_status_dto import ContainerStatusDto
from qovery-ws.model.service_state_dto import ServiceStateDto
globals()['ContainerStatusDto'] = ContainerStatusDto
globals()['ServiceStateDto'] = ServiceStateDto
from qovery-ws.model.pod_status_dto import PodStatusDto


class TestPodStatusDto(unittest.TestCase):
    """PodStatusDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPodStatusDto(self):
        """Test PodStatusDto"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PodStatusDto()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
