# ClusterStatusDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[ClusterNodeDto]**](ClusterNodeDto.md) |  | 

## Example

```python
from qovery-ws.models.cluster_status_dto import ClusterStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterStatusDto from a JSON string
cluster_status_dto_instance = ClusterStatusDto.from_json(json)
# print the JSON string representation of the object
print ClusterStatusDto.to_json()

# convert the object into a dict
cluster_status_dto_dict = cluster_status_dto_instance.to_dict()
# create an instance of ClusterStatusDto from a dict
cluster_status_dto_form_dict = cluster_status_dto.from_dict(cluster_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


