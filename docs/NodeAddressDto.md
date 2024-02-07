# NodeAddressDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from qovery-ws.models.node_address_dto import NodeAddressDto

# TODO update the JSON string below
json = "{}"
# create an instance of NodeAddressDto from a JSON string
node_address_dto_instance = NodeAddressDto.from_json(json)
# print the JSON string representation of the object
print NodeAddressDto.to_json()

# convert the object into a dict
node_address_dto_dict = node_address_dto_instance.to_dict()
# create an instance of NodeAddressDto from a dict
node_address_dto_form_dict = node_address_dto.from_dict(node_address_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


