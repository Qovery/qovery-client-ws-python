# NodeConditionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_heartbeat_time** | **int** | Unix timestamp with millisecond precision | [optional] 
**last_transition_time** | **int** | Unix timestamp with millisecond precision | [optional] 
**message** | **str** |  | 
**reason** | **str** |  | 
**status** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from qovery-ws.models.node_condition_dto import NodeConditionDto

# TODO update the JSON string below
json = "{}"
# create an instance of NodeConditionDto from a JSON string
node_condition_dto_instance = NodeConditionDto.from_json(json)
# print the JSON string representation of the object
print NodeConditionDto.to_json()

# convert the object into a dict
node_condition_dto_dict = node_condition_dto_instance.to_dict()
# create an instance of NodeConditionDto from a dict
node_condition_dto_form_dict = node_condition_dto.from_dict(node_condition_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


