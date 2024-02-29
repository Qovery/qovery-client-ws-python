# PodStatusDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containers** | [**List[ContainerStatusDto]**](ContainerStatusDto.md) |  | 
**name** | **str** |  | 
**restart_count** | **int** |  | 
**service_version** | **str** |  | 
**started_at** | **int** | Unix timestamp with millisecond precision | [optional] 
**state** | [**ServiceStateDto**](ServiceStateDto.md) |  | 
**state_message** | **str** |  | 
**state_reason** | **str** |  | 

## Example

```python
from qovery-ws.models.pod_status_dto import PodStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of PodStatusDto from a JSON string
pod_status_dto_instance = PodStatusDto.from_json(json)
# print the JSON string representation of the object
print PodStatusDto.to_json()

# convert the object into a dict
pod_status_dto_dict = pod_status_dto_instance.to_dict()
# create an instance of PodStatusDto from a dict
pod_status_dto_form_dict = pod_status_dto.from_dict(pod_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


