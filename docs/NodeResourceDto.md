# NodeResourceDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_milli** | **int** |  | 
**ephemeral_storage_gib** | **int** |  | 
**memory_mib** | **int** |  | 
**pods** | **int** |  | 

## Example

```python
from qovery-ws.models.node_resource_dto import NodeResourceDto

# TODO update the JSON string below
json = "{}"
# create an instance of NodeResourceDto from a JSON string
node_resource_dto_instance = NodeResourceDto.from_json(json)
# print the JSON string representation of the object
print NodeResourceDto.to_json()

# convert the object into a dict
node_resource_dto_dict = node_resource_dto_instance.to_dict()
# create an instance of NodeResourceDto from a dict
node_resource_dto_form_dict = node_resource_dto.from_dict(node_resource_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


