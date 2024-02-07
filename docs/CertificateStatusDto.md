# CertificateStatusDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_names** | **List[str]** |  | 
**failed_issuance_attempt_count** | **int** |  | 
**last_failure_issuance_time** | **int** | Unix timestamp with millisecond precision | [optional] 
**not_after** | **int** | Unix timestamp with millisecond precision | [optional] 
**not_before** | **int** | Unix timestamp with millisecond precision | [optional] 
**renewal_time** | **int** | Unix timestamp with millisecond precision | [optional] 
**state** | [**ServiceStateDto**](ServiceStateDto.md) |  | 
**state_message** | **str** |  | [optional] 

## Example

```python
from qovery-ws.models.certificate_status_dto import CertificateStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateStatusDto from a JSON string
certificate_status_dto_instance = CertificateStatusDto.from_json(json)
# print the JSON string representation of the object
print CertificateStatusDto.to_json()

# convert the object into a dict
certificate_status_dto_dict = certificate_status_dto_instance.to_dict()
# create an instance of CertificateStatusDto from a dict
certificate_status_dto_form_dict = certificate_status_dto.from_dict(certificate_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


