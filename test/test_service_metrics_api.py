"""
    websocket-gateway

    Describe the weboscket endpoints  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: erebe@erebe.eu
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.service_metrics_api import ServiceMetricsApi  # noqa: E501


class TestServiceMetricsApi(unittest.TestCase):
    """ServiceMetricsApi unit test stubs"""

    def setUp(self):
        self.api = ServiceMetricsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_handle_metrics_request(self):
        """Test case for handle_metrics_request

        """
        pass


if __name__ == '__main__':
    unittest.main()
