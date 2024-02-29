# ClusterNodeDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**List[NodeAddressDto]**](NodeAddressDto.md) |  | 
**annotations** | **Dict[str, str]** |  | 
**architecture** | **str** |  | 
**conditions** | [**List[NodeConditionDto]**](NodeConditionDto.md) |  | 
**kernel_version** | **str** |  | 
**kubelet_version** | **str** |  | 
**labels** | **Dict[str, str]** |  | 
**name** | **str** |  | 
**operating_system** | **str** |  | 
**os_image** | **str** |  | 
**pods** | [**List[NodePodInfoDto]**](NodePodInfoDto.md) |  | 
**resources_allocatable** | [**NodeResourceDto**](NodeResourceDto.md) |  | 
**taints** | [**List[NodeTaintDto]**](NodeTaintDto.md) |  | 
**unschedulable** | **bool** |  | 

## Example

```python
from qovery-ws.models.cluster_node_dto import ClusterNodeDto

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNodeDto from a JSON string
cluster_node_dto_instance = ClusterNodeDto.from_json(json)
# print the JSON string representation of the object
print ClusterNodeDto.to_json()

# convert the object into a dict
cluster_node_dto_dict = cluster_node_dto_instance.to_dict()
# create an instance of ClusterNodeDto from a dict
cluster_node_dto_form_dict = cluster_node_dto.from_dict(cluster_node_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


