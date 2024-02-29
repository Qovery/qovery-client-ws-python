# qovery-ws.ServiceListPodsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_service_list_pods_request**](ServiceListPodsApi.md#handle_service_list_pods_request) | **GET** /service/pods | 


# **handle_service_list_pods_request**
> ServiceListPodsResponseDto handle_service_list_pods_request(organization, cluster, project, environment, service)



### Example

```python
import time
import os
import qovery-ws
from qovery-ws.models.service_list_pods_response_dto import ServiceListPodsResponseDto
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
    api_instance = qovery-ws.ServiceListPodsApi(api_client)
    organization = 'organization_example' # str | 
    cluster = 'cluster_example' # str | 
    project = 'project_example' # str | 
    environment = 'environment_example' # str | 
    service = 'service_example' # str | 

    try:
        api_response = api_instance.handle_service_list_pods_request(organization, cluster, project, environment, service)
        print("The response of ServiceListPodsApi->handle_service_list_pods_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceListPodsApi->handle_service_list_pods_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **cluster** | **str**|  | 
 **project** | **str**|  | 
 **environment** | **str**|  | 
 **service** | **str**|  | 

### Return type

[**ServiceListPodsResponseDto**](ServiceListPodsResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List the pods of a service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

