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

from qovery-ws.api.logs_api import LogsApi  # noqa: E501


class TestLogsApi(unittest.TestCase):
    """LogsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LogsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_handle_infra_logs_request(self) -> None:
        """Test case for handle_infra_logs_request

        """
        pass

    def test_handle_service_logs_request(self) -> None:
        """Test case for handle_service_logs_request

        """
        pass


if __name__ == '__main__':
    unittest.main()
