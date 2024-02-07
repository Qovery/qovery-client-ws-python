# ContainerStatusDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_state** | [**ContainerStateDto**](ContainerStateDto.md) |  | [optional] 
**image** | **str** |  | 
**last_terminated_state** | [**ContainerStateTerminatedDto**](ContainerStateTerminatedDto.md) |  | [optional] 
**name** | **str** |  | 
**restart_count** | **int** |  | 

## Example

```python
from qovery-ws.models.container_status_dto import ContainerStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerStatusDto from a JSON string
container_status_dto_instance = ContainerStatusDto.from_json(json)
# print the JSON string representation of the object
print ContainerStatusDto.to_json()

# convert the object into a dict
container_status_dto_dict = container_status_dto_instance.to_dict()
# create an instance of ContainerStatusDto from a dict
container_status_dto_form_dict = container_status_dto.from_dict(container_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


