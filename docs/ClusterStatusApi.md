# qovery-ws.ClusterStatusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_cluster_status_request**](ClusterStatusApi.md#handle_cluster_status_request) | **GET** /cluster/status | 


# **handle_cluster_status_request**
> ClusterStatusDto handle_cluster_status_request(organization, cluster)



### Example

```python
import time
import os
import qovery-ws
from qovery-ws.models.cluster_status_dto import ClusterStatusDto
from qovery-ws.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = qovery-ws.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with qovery-ws.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery-ws.ClusterStatusApi(api_client)
    organization = 'organization_example' # str | 
    cluster = 'cluster_example' # str | 

    try:
        api_response = api_instance.handle_cluster_status_request(organization, cluster)
        print("The response of ClusterStatusApi->handle_cluster_status_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterStatusApi->handle_cluster_status_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **cluster** | **str**|  | 

### Return type

[**ClusterStatusDto**](ClusterStatusDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream of cluster status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

