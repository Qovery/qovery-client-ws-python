"""
    websocket-gateway

    Describe the weboscket endpoints  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: erebe@erebe.eu
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.deployment_api import DeploymentApi  # noqa: E501


class TestDeploymentApi(unittest.TestCase):
    """DeploymentApi unit test stubs"""

    def setUp(self):
        self.api = DeploymentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_handle_deployment_logs_request(self):
        """Test case for handle_deployment_logs_request

        """
        pass

    def test_handle_deployment_status_request(self):
        """Test case for handle_deployment_status_request

        """
        pass


if __name__ == '__main__':
    unittest.main()
