<a name="__pageTop"></a>
# l3vels.apis.tags.default_api.DefaultApi

All URIs are relative to *https://api-dev.l3vels.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat_controller_webhook**](#chat_controller_webhook) | **post** /v1/chat/webhook | 

# **chat_controller_webhook**
<a name="chat_controller_webhook"></a>
> chat_controller_webhook()



### Example

```python
import l3vels
from l3vels.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.chat_controller_webhook()
    except l3vels.ApiException as e:
        print("Exception when calling DefaultApi->chat_controller_webhook: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#chat_controller_webhook.ApiResponseFor200) | 

#### chat_controller_webhook.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

