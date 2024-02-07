# EnvironmentStatusDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | [**List[ApplicationStatusDto]**](ApplicationStatusDto.md) |  | 
**containers** | [**List[ApplicationStatusDto]**](ApplicationStatusDto.md) |  | 
**databases** | [**List[DatabaseStatusDto]**](DatabaseStatusDto.md) |  | 
**helms** | [**List[ApplicationStatusDto]**](ApplicationStatusDto.md) |  | 
**id** | **str** |  | 
**jobs** | [**List[ApplicationStatusDto]**](ApplicationStatusDto.md) |  | 
**project_id** | **str** |  | 
**state** | [**ServiceStateDto**](ServiceStateDto.md) |  | 

## Example

```python
from qovery-ws.models.environment_status_dto import EnvironmentStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentStatusDto from a JSON string
environment_status_dto_instance = EnvironmentStatusDto.from_json(json)
# print the JSON string representation of the object
print EnvironmentStatusDto.to_json()

# convert the object into a dict
environment_status_dto_dict = environment_status_dto_instance.to_dict()
# create an instance of EnvironmentStatusDto from a dict
environment_status_dto_form_dict = environment_status_dto.from_dict(environment_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


