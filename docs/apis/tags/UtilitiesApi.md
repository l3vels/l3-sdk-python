<a name="__pageTop"></a>
# l3vels.apis.tags.utilities_api.UtilitiesApi

All URIs are relative to *https://api-dev.l3vels.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**utility_controller_health**](#utility_controller_health) | **get** /v1/utilities/health | 

# **utility_controller_health**
<a name="utility_controller_health"></a>
> utility_controller_health()



### Example

```python
import l3vels
from l3vels.apis.tags import utilities_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = utilities_api.UtilitiesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.utility_controller_health()
    except l3vels.ApiException as e:
        print("Exception when calling UtilitiesApi->utility_controller_health: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#utility_controller_health.ApiResponseFor200) | 
400 | [ApiResponseFor400](#utility_controller_health.ApiResponseFor400) | Account or User was not found.
403 | [ApiResponseFor403](#utility_controller_health.ApiResponseFor403) | Forbidden. Session is closed  or expired 

#### utility_controller_health.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### utility_controller_health.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### utility_controller_health.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

