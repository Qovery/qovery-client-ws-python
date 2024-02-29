# NodePodInfoDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_milli_limit** | **int** |  | [optional] 
**cpu_milli_request** | **int** |  | [optional] 
**environment_id** | **str** |  | [optional] 
**images_version** | **Dict[str, str]** |  | 
**memory_mib_limit** | **int** |  | [optional] 
**memory_mib_request** | **int** |  | [optional] 
**name** | **str** |  | 
**namespace** | **str** |  | 
**project_id** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 

## Example

```python
from qovery-ws.models.node_pod_info_dto import NodePodInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of NodePodInfoDto from a JSON string
node_pod_info_dto_instance = NodePodInfoDto.from_json(json)
# print the JSON string representation of the object
print NodePodInfoDto.to_json()

# convert the object into a dict
node_pod_info_dto_dict = node_pod_info_dto_instance.to_dict()
# create an instance of NodePodInfoDto from a dict
node_pod_info_dto_form_dict = node_pod_info_dto.from_dict(node_pod_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


