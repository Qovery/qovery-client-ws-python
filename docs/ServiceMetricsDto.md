# ServiceMetricsDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**MetricDto**](MetricDto.md) |  | 
**memory** | [**MetricDto**](MetricDto.md) |  | 
**pod_name** | **str** |  | 
**storages** | [**List[MetricDto]**](MetricDto.md) |  | 

## Example

```python
from qovery-ws.models.service_metrics_dto import ServiceMetricsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceMetricsDto from a JSON string
service_metrics_dto_instance = ServiceMetricsDto.from_json(json)
# print the JSON string representation of the object
print ServiceMetricsDto.to_json()

# convert the object into a dict
service_metrics_dto_dict = service_metrics_dto_instance.to_dict()
# create an instance of ServiceMetricsDto from a dict
service_metrics_dto_form_dict = service_metrics_dto.from_dict(service_metrics_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


