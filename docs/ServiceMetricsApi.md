# qovery-ws.ServiceMetricsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_metrics_request**](ServiceMetricsApi.md#handle_metrics_request) | **GET** /service/metrics | 


# **handle_metrics_request**
> ServiceMetricsDto handle_metrics_request(organization, cluster, project, environment, service, service_type)



### Example

```python
import time
import os
import qovery-ws
from qovery-ws.models.service_metrics_dto import ServiceMetricsDto
from qovery-ws.models.service_type import ServiceType
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
    api_instance = qovery-ws.ServiceMetricsApi(api_client)
    organization = 'organization_example' # str | 
    cluster = 'cluster_example' # str | 
    project = 'project_example' # str | 
    environment = 'environment_example' # str | 
    service = 'service_example' # str | 
    service_type = qovery-ws.ServiceType() # ServiceType | 

    try:
        api_response = api_instance.handle_metrics_request(organization, cluster, project, environment, service, service_type)
        print("The response of ServiceMetricsApi->handle_metrics_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceMetricsApi->handle_metrics_request: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **cluster** | **str**|  | 
 **project** | **str**|  | 
 **environment** | **str**|  | 
 **service** | **str**|  | 
 **service_type** | [**ServiceType**](.md)|  | 

### Return type

[**ServiceMetricsDto**](ServiceMetricsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream of services metrics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

