# MetricDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **int** |  | 
**current_percent** | **int** |  | 
**limit** | **int** |  | 
**name** | **str** |  | [optional] 
**status** | [**ResourceStatusDto**](ResourceStatusDto.md) |  | 
**unit** | [**UnitDto**](UnitDto.md) |  | 

## Example

```python
from qovery-ws.models.metric_dto import MetricDto

# TODO update the JSON string below
json = "{}"
# create an instance of MetricDto from a JSON string
metric_dto_instance = MetricDto.from_json(json)
# print the JSON string representation of the object
print MetricDto.to_json()

# convert the object into a dict
metric_dto_dict = metric_dto_instance.to_dict()
# create an instance of MetricDto from a dict
metric_dto_form_dict = metric_dto.from_dict(metric_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


