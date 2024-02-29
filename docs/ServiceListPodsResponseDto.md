# ServiceListPodsResponseDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pods** | [**List[PodDto]**](PodDto.md) |  | 

## Example

```python
from qovery-ws.models.service_list_pods_response_dto import ServiceListPodsResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceListPodsResponseDto from a JSON string
service_list_pods_response_dto_instance = ServiceListPodsResponseDto.from_json(json)
# print the JSON string representation of the object
print ServiceListPodsResponseDto.to_json()

# convert the object into a dict
service_list_pods_response_dto_dict = service_list_pods_response_dto_instance.to_dict()
# create an instance of ServiceListPodsResponseDto from a dict
service_list_pods_response_dto_form_dict = service_list_pods_response_dto.from_dict(service_list_pods_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


