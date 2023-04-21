<a name="__pageTop"></a>
# l3vels.apis.tags.contract_api.ContractApi

All URIs are relative to *https://api-dev.l3vels.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contract_controller_collection_size**](#contract_controller_collection_size) | **get** /v1/contract/collection-size | Collection size
[**contract_controller_contract_uri**](#contract_controller_contract_uri) | **get** /v1/contract/contract-uri | Get Contract URI
[**contract_controller_set_contract_uri**](#contract_controller_set_contract_uri) | **put** /v1/contract/contract-uri | Update Contract URI
[**contract_controller_set_sale_status**](#contract_controller_set_sale_status) | **put** /v1/contract/sale-status | Update Sale status

# **contract_controller_collection_size**
<a name="contract_controller_collection_size"></a>
> contract_controller_collection_size(authorizationcollection_idproject_id)

Collection size

Get size of collection

### Example

```python
import l3vels
from l3vels.apis.tags import contract_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = contract_api.ContractApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'collection_id': "collection_id_example",
        'project_id': "project_id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Collection size
        api_response = api_instance.contract_controller_collection_size(
            query_params=query_params,
            header_params=header_params,
        )
    except l3vels.ApiException as e:
        print("Exception when calling ContractApi->contract_controller_collection_size: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
collection_id | CollectionIdSchema | | 
project_id | ProjectIdSchema | | 


# CollectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | 

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#contract_controller_collection_size.ApiResponseFor200) | Collection size
400 | [ApiResponseFor400](#contract_controller_collection_size.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#contract_controller_collection_size.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#contract_controller_collection_size.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#contract_controller_collection_size.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#contract_controller_collection_size.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#contract_controller_collection_size.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#contract_controller_collection_size.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### contract_controller_collection_size.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_collection_size.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_collection_size.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_collection_size.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_collection_size.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_collection_size.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_collection_size.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_collection_size.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **contract_controller_contract_uri**
<a name="contract_controller_contract_uri"></a>
> contract_controller_contract_uri(authorizationcollection_idproject_id)

Get Contract URI

Gets contract uri of contract

### Example

```python
import l3vels
from l3vels.apis.tags import contract_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = contract_api.ContractApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'collection_id': "collection_id_example",
        'project_id': "project_id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Get Contract URI
        api_response = api_instance.contract_controller_contract_uri(
            query_params=query_params,
            header_params=header_params,
        )
    except l3vels.ApiException as e:
        print("Exception when calling ContractApi->contract_controller_contract_uri: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
collection_id | CollectionIdSchema | | 
project_id | ProjectIdSchema | | 


# CollectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | 

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#contract_controller_contract_uri.ApiResponseFor200) | Contract URI
400 | [ApiResponseFor400](#contract_controller_contract_uri.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#contract_controller_contract_uri.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#contract_controller_contract_uri.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#contract_controller_contract_uri.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#contract_controller_contract_uri.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#contract_controller_contract_uri.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#contract_controller_contract_uri.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### contract_controller_contract_uri.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_contract_uri.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_contract_uri.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_contract_uri.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_contract_uri.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_contract_uri.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_contract_uri.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_contract_uri.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **contract_controller_set_contract_uri**
<a name="contract_controller_set_contract_uri"></a>
> contract_controller_set_contract_uri(authorizationset_contract_uri_dto)

Update Contract URI

Update Contract URI

### Example

```python
import l3vels
from l3vels.apis.tags import contract_api
from l3vels.model.set_contract_uri_dto import SetContractUriDto
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = contract_api.ContractApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = SetContractUriDto(
        project_id="a44b646a-ae14-4e05-ae09-b12d5e7269bf",
        collection_id="a44b646a-ae14-4e05-ae09-b12d5e7269bf",
        contract_uri="https://api.example.com/contract/{contractAddress}",
    )
    try:
        # Update Contract URI
        api_response = api_instance.contract_controller_set_contract_uri(
            header_params=header_params,
            body=body,
        )
    except l3vels.ApiException as e:
        print("Exception when calling ContractApi->contract_controller_set_contract_uri: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SetContractUriDto**](../../models/SetContractUriDto.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | 

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#contract_controller_set_contract_uri.ApiResponseFor200) | Contract URI Updated
400 | [ApiResponseFor400](#contract_controller_set_contract_uri.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#contract_controller_set_contract_uri.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#contract_controller_set_contract_uri.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#contract_controller_set_contract_uri.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#contract_controller_set_contract_uri.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#contract_controller_set_contract_uri.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#contract_controller_set_contract_uri.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### contract_controller_set_contract_uri.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_set_contract_uri.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_set_contract_uri.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_set_contract_uri.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_set_contract_uri.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_set_contract_uri.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_set_contract_uri.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_set_contract_uri.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **contract_controller_set_sale_status**
<a name="contract_controller_set_sale_status"></a>
> contract_controller_set_sale_status(authorizationset_sale_status_dto)

Update Sale status

Update Sale status to PAUSED, PRE_SALE or PUBLIC

### Example

```python
import l3vels
from l3vels.apis.tags import contract_api
from l3vels.model.set_sale_status_dto import SetSaleStatusDto
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = contract_api.ContractApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = SetSaleStatusDto(
        project_id="a44b646a-ae14-4e05-ae09-b12d5e7269bf",
        collection_id="a44b646a-ae14-4e05-ae09-b12d5e7269bf",
        sale_status=dict(),
    )
    try:
        # Update Sale status
        api_response = api_instance.contract_controller_set_sale_status(
            header_params=header_params,
            body=body,
        )
    except l3vels.ApiException as e:
        print("Exception when calling ContractApi->contract_controller_set_sale_status: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SetSaleStatusDto**](../../models/SetSaleStatusDto.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | 

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#contract_controller_set_sale_status.ApiResponseFor200) | Sale status updated
400 | [ApiResponseFor400](#contract_controller_set_sale_status.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#contract_controller_set_sale_status.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#contract_controller_set_sale_status.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#contract_controller_set_sale_status.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#contract_controller_set_sale_status.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#contract_controller_set_sale_status.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#contract_controller_set_sale_status.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### contract_controller_set_sale_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_set_sale_status.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_set_sale_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_set_sale_status.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_set_sale_status.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_set_sale_status.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_set_sale_status.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### contract_controller_set_sale_status.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

