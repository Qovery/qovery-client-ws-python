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
from qovery-ws.model.resource_status_dto import ResourceStatusDto
from qovery-ws.model.unit_dto import UnitDto
globals()['ResourceStatusDto'] = ResourceStatusDto
globals()['UnitDto'] = UnitDto
from qovery-ws.model.metric_dto import MetricDto


class TestMetricDto(unittest.TestCase):
    """MetricDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetricDto(self):
        """Test MetricDto"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MetricDto()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
