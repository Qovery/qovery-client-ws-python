# qovery-ws.InfraStatusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_infra_status_request**](InfraStatusApi.md#handle_infra_status_request) | **GET** /infra/status | 


# **handle_infra_status_request**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} handle_infra_status_request(organization, cluster)



### Example


```python
import time
import qovery-ws
from qovery-ws.api import infra_status_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = qovery-ws.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with qovery-ws.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = infra_status_api.InfraStatusApi(api_client)
    organization = "organization_example" # str | 
    cluster = "cluster_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.handle_infra_status_request(organization, cluster)
        pprint(api_response)
    except qovery-ws.ApiException as e:
        print("Exception when calling InfraStatusApi->handle_infra_status_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  |
 **cluster** | **str**|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream of infra status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

