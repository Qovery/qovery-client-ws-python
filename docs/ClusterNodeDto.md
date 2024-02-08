# ClusterNodeDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**[NodeAddressDto]**](NodeAddressDto.md) |  | 
**annotations** | **{str: (str,)}** |  | 
**architecture** | **str** |  | 
**conditions** | [**[NodeConditionDto]**](NodeConditionDto.md) |  | 
**kernel_version** | **str** |  | 
**kubelet_version** | **str** |  | 
**labels** | **{str: (str,)}** |  | 
**name** | **str** |  | 
**operating_system** | **str** |  | 
**os_image** | **str** |  | 
**pods** | [**[NodePodInfoDto]**](NodePodInfoDto.md) |  | 
**resources_allocatable** | [**NodeResourceDto**](NodeResourceDto.md) |  | 
**taints** | [**[NodeTaintDto]**](NodeTaintDto.md) |  | 
**unschedulable** | **bool** |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


