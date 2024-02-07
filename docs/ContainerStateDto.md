# ContainerStateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started_at** | **int** | Unix timestamp with millisecond precision | [optional] 
**state** | [**ServiceStateDto**](ServiceStateDto.md) |  | 
**state_message** | **str** |  | [optional] 
**state_reason** | **str** |  | [optional] 

## Example

```python
from qovery-ws.models.container_state_dto import ContainerStateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerStateDto from a JSON string
container_state_dto_instance = ContainerStateDto.from_json(json)
# print the JSON string representation of the object
print ContainerStateDto.to_json()

# convert the object into a dict
container_state_dto_dict = container_state_dto_instance.to_dict()
# create an instance of ContainerStateDto from a dict
container_state_dto_form_dict = container_state_dto.from_dict(container_state_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


