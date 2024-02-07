# ContainerStateTerminatedDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exit_code** | **int** |  | 
**exit_code_message** | **str** |  | 
**finished_at** | **int** | Unix timestamp with millisecond precision | [optional] 
**message** | **str** |  | 
**reason** | **str** |  | 
**signal** | **int** |  | 
**started_at** | **int** | Unix timestamp with millisecond precision | [optional] 

## Example

```python
from qovery-ws.models.container_state_terminated_dto import ContainerStateTerminatedDto

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerStateTerminatedDto from a JSON string
container_state_terminated_dto_instance = ContainerStateTerminatedDto.from_json(json)
# print the JSON string representation of the object
print ContainerStateTerminatedDto.to_json()

# convert the object into a dict
container_state_terminated_dto_dict = container_state_terminated_dto_instance.to_dict()
# create an instance of ContainerStateTerminatedDto from a dict
container_state_terminated_dto_form_dict = container_state_terminated_dto.from_dict(container_state_terminated_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


