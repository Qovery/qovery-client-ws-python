# qovery.ServiceStatusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_service_status_request**](ServiceStatusApi.md#handle_service_status_request) | **GET** /service/status | 


# **handle_service_status_request**
> ServiceStatusDto handle_service_status_request(organization, cluster, project, environment)



### Example


```python
import time
import qovery
from qovery.api import service_status_api
from qovery.model.service_status_dto import ServiceStatusDto
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = qovery.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with qovery.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = service_status_api.ServiceStatusApi(api_client)
    organization = "organization_example" # str | 
    cluster = "cluster_example" # str | 
    project = "project_example" # str, none_type | 
    environment = "environment_example" # str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.handle_service_status_request(organization, cluster, project, environment)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ServiceStatusApi->handle_service_status_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  |
 **cluster** | **str**|  |
 **project** | **str, none_type**|  |
 **environment** | **str, none_type**|  |

### Return type

[**ServiceStatusDto**](ServiceStatusDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream of services status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

