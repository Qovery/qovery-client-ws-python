# qovery-ws.DeploymentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_deployment_logs_request**](DeploymentApi.md#handle_deployment_logs_request) | **GET** /deployment/logs | 
[**handle_deployment_status_request**](DeploymentApi.md#handle_deployment_status_request) | **GET** /deployment/status | 


# **handle_deployment_logs_request**
> str handle_deployment_logs_request(organization, cluster, project, environment, version)



### Example


```python
import time
import qovery-ws
from qovery-ws.api import deployment_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = qovery-ws.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with qovery-ws.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = deployment_api.DeploymentApi(api_client)
    organization = "organization_example" # str | 
    cluster = "cluster_example" # str, none_type | 
    project = "project_example" # str | 
    environment = "environment_example" # str | 
    version = "version_example" # str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.handle_deployment_logs_request(organization, cluster, project, environment, version)
        pprint(api_response)
    except qovery-ws.ApiException as e:
        print("Exception when calling DeploymentApi->handle_deployment_logs_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  |
 **cluster** | **str, none_type**|  |
 **project** | **str**|  |
 **environment** | **str**|  |
 **version** | **str, none_type**|  |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream of deployment logs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_deployment_status_request**
> str handle_deployment_status_request(organization, cluster, project, environment, version)



### Example


```python
import time
import qovery-ws
from qovery-ws.api import deployment_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = qovery-ws.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with qovery-ws.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = deployment_api.DeploymentApi(api_client)
    organization = "organization_example" # str | 
    cluster = "cluster_example" # str, none_type | 
    project = "project_example" # str | 
    environment = "environment_example" # str | 
    version = "version_example" # str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.handle_deployment_status_request(organization, cluster, project, environment, version)
        pprint(api_response)
    except qovery-ws.ApiException as e:
        print("Exception when calling DeploymentApi->handle_deployment_status_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  |
 **cluster** | **str, none_type**|  |
 **project** | **str**|  |
 **environment** | **str**|  |
 **version** | **str, none_type**|  |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream of deployment status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

