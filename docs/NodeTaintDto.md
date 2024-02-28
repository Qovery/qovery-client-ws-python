# NodeTaintDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** |  | 
**key** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from qovery-ws.models.node_taint_dto import NodeTaintDto

# TODO update the JSON string below
json = "{}"
# create an instance of NodeTaintDto from a JSON string
node_taint_dto_instance = NodeTaintDto.from_json(json)
# print the JSON string representation of the object
print NodeTaintDto.to_json()

# convert the object into a dict
node_taint_dto_dict = node_taint_dto_instance.to_dict()
# create an instance of NodeTaintDto from a dict
node_taint_dto_form_dict = node_taint_dto.from_dict(node_taint_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


