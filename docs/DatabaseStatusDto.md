# DatabaseStatusDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**pods** | [**List[PodStatusDto]**](PodStatusDto.md) |  | 
**state** | [**ServiceStateDto**](ServiceStateDto.md) |  | 

## Example

```python
from qovery-ws.models.database_status_dto import DatabaseStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseStatusDto from a JSON string
database_status_dto_instance = DatabaseStatusDto.from_json(json)
# print the JSON string representation of the object
print DatabaseStatusDto.to_json()

# convert the object into a dict
database_status_dto_dict = database_status_dto_instance.to_dict()
# create an instance of DatabaseStatusDto from a dict
database_status_dto_form_dict = database_status_dto.from_dict(database_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


