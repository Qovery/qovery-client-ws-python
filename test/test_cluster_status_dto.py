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

from qovery-ws.models.cluster_status_dto import ClusterStatusDto  # noqa: E501

class TestClusterStatusDto(unittest.TestCase):
    """ClusterStatusDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClusterStatusDto:
        """Test ClusterStatusDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClusterStatusDto`
        """
        model = ClusterStatusDto()  # noqa: E501
        if include_optional:
            return ClusterStatusDto(
                nodes = [
                    qovery-ws.models.cluster_node_dto.ClusterNodeDto(
                        addresses = [
                            qovery-ws.models.node_address_dto.NodeAddressDto(
                                address = '', 
                                type = '', )
                            ], 
                        annotations = {
                            'key' : ''
                            }, 
                        architecture = '', 
                        conditions = [
                            qovery-ws.models.node_condition_dto.NodeConditionDto(
                                last_heartbeat_time = null, 
                                last_transition_time = null, 
                                message = '', 
                                reason = '', 
                                status = '', 
                                type = '', )
                            ], 
                        kernel_version = '', 
                        kubelet_version = '', 
                        labels = {
                            'key' : ''
                            }, 
                        name = '', 
                        operating_system = '', 
                        os_image = '', 
                        pods = [
                            qovery-ws.models.node_pod_info_dto.NodePodInfoDto(
                                cpu_milli_limit = 0, 
                                cpu_milli_request = 0, 
                                environment_id = '', 
                                images_version = {
                                    'key' : ''
                                    }, 
                                memory_mib_limit = 0, 
                                memory_mib_request = 0, 
                                name = '', 
                                namespace = '', 
                                project_id = '', 
                                service_id = '', )
                            ], 
                        resources_allocatable = qovery-ws.models.node_resource_dto.NodeResourceDto(
                            cpu_milli = 0, 
                            ephemeral_storage_gib = 0, 
                            memory_mib = 0, 
                            pods = 0, ), 
                        taints = [
                            qovery-ws.models.node_taint_dto.NodeTaintDto(
                                effect = '', 
                                key = '', 
                                value = '', )
                            ], 
                        unschedulable = True, )
                    ]
            )
        else:
            return ClusterStatusDto(
                nodes = [
                    qovery-ws.models.cluster_node_dto.ClusterNodeDto(
                        addresses = [
                            qovery-ws.models.node_address_dto.NodeAddressDto(
                                address = '', 
                                type = '', )
                            ], 
                        annotations = {
                            'key' : ''
                            }, 
                        architecture = '', 
                        conditions = [
                            qovery-ws.models.node_condition_dto.NodeConditionDto(
                                last_heartbeat_time = null, 
                                last_transition_time = null, 
                                message = '', 
                                reason = '', 
                                status = '', 
                                type = '', )
                            ], 
                        kernel_version = '', 
                        kubelet_version = '', 
                        labels = {
                            'key' : ''
                            }, 
                        name = '', 
                        operating_system = '', 
                        os_image = '', 
                        pods = [
                            qovery-ws.models.node_pod_info_dto.NodePodInfoDto(
                                cpu_milli_limit = 0, 
                                cpu_milli_request = 0, 
                                environment_id = '', 
                                images_version = {
                                    'key' : ''
                                    }, 
                                memory_mib_limit = 0, 
                                memory_mib_request = 0, 
                                name = '', 
                                namespace = '', 
                                project_id = '', 
                                service_id = '', )
                            ], 
                        resources_allocatable = qovery-ws.models.node_resource_dto.NodeResourceDto(
                            cpu_milli = 0, 
                            ephemeral_storage_gib = 0, 
                            memory_mib = 0, 
                            pods = 0, ), 
                        taints = [
                            qovery-ws.models.node_taint_dto.NodeTaintDto(
                                effect = '', 
                                key = '', 
                                value = '', )
                            ], 
                        unschedulable = True, )
                    ],
        )
        """

    def testClusterStatusDto(self):
        """Test ClusterStatusDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
