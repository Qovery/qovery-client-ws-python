# ServiceLogResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_name** | **str** |  | 
**created_at** | **int** | Unix timestamp with millisecond precision | 
**message** | **str** |  | 
**pod_name** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from qovery-ws.models.service_log_response_dto import ServiceLogResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLogResponseDto from a JSON string
service_log_response_dto_instance = ServiceLogResponseDto.from_json(json)
# print the JSON string representation of the object
print ServiceLogResponseDto.to_json()

# convert the object into a dict
service_log_response_dto_dict = service_log_response_dto_instance.to_dict()
# create an instance of ServiceLogResponseDto from a dict
service_log_response_dto_form_dict = service_log_response_dto.from_dict(service_log_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


