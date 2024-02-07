# ServiceInfraLogResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** | Unix timestamp with millisecond precision | 
**message** | **str** |  | 

## Example

```python
from qovery-ws.models.service_infra_log_response_dto import ServiceInfraLogResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceInfraLogResponseDto from a JSON string
service_infra_log_response_dto_instance = ServiceInfraLogResponseDto.from_json(json)
# print the JSON string representation of the object
print ServiceInfraLogResponseDto.to_json()

# convert the object into a dict
service_infra_log_response_dto_dict = service_infra_log_response_dto_instance.to_dict()
# create an instance of ServiceInfraLogResponseDto from a dict
service_infra_log_response_dto_form_dict = service_infra_log_response_dto.from_dict(service_infra_log_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


