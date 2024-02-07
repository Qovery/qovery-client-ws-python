# qovery-ws.LogsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_infra_logs_request**](LogsApi.md#handle_infra_logs_request) | **GET** /infra/logs | 
[**handle_service_logs_request**](LogsApi.md#handle_service_logs_request) | **GET** /service/logs | 


# **handle_infra_logs_request**
> ServiceInfraLogResponseDto handle_infra_logs_request(organization, cluster, project, environment, service, infra_component_type)



### Example


```python
import time
import os
import qovery-ws
from qovery-ws.models.service_infra_log_response_dto import ServiceInfraLogResponseDto
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
    api_instance = qovery-ws.LogsApi(api_client)
    organization = 'organization_example' # str | 
    cluster = 'cluster_example' # str | 
    project = 'project_example' # str | 
    environment = 'environment_example' # str | 
    service = 'service_example' # str | 
    infra_component_type = 'infra_component_type_example' # str | 

    try:
        api_response = api_instance.handle_infra_logs_request(organization, cluster, project, environment, service, infra_component_type)
        print("The response of LogsApi->handle_infra_logs_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogsApi->handle_infra_logs_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **cluster** | **str**|  | 
 **project** | **str**|  | 
 **environment** | **str**|  | 
 **service** | **str**|  | 
 **infra_component_type** | **str**|  | 

### Return type

[**ServiceInfraLogResponseDto**](ServiceInfraLogResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream of infra logs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_service_logs_request**
> ServiceLogResponseDto handle_service_logs_request(organization, cluster, project, environment, service)



### Example


```python
import time
import os
import qovery-ws
from qovery-ws.models.service_log_response_dto import ServiceLogResponseDto
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
    api_instance = qovery-ws.LogsApi(api_client)
    organization = 'organization_example' # str | 
    cluster = 'cluster_example' # str | 
    project = 'project_example' # str | 
    environment = 'environment_example' # str | 
    service = 'service_example' # str | 

    try:
        api_response = api_instance.handle_service_logs_request(organization, cluster, project, environment, service)
        print("The response of LogsApi->handle_service_logs_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogsApi->handle_service_logs_request: %s\n" % e)
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

[**ServiceLogResponseDto**](ServiceLogResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream of services logs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

