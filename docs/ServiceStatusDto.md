# ServiceStatusDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environments** | [**List[EnvironmentStatusDto]**](EnvironmentStatusDto.md) |  | 

## Example

```python
from qovery-ws.models.service_status_dto import ServiceStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStatusDto from a JSON string
service_status_dto_instance = ServiceStatusDto.from_json(json)
# print the JSON string representation of the object
print ServiceStatusDto.to_json()

# convert the object into a dict
service_status_dto_dict = service_status_dto_instance.to_dict()
# create an instance of ServiceStatusDto from a dict
service_status_dto_form_dict = service_status_dto.from_dict(service_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


