<a name="__pageTop"></a>
# l3vels.apis.tags.transaction_api.TransactionApi

All URIs are relative to *https://api-dev.l3vels.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction_by_id**](#get_transaction_by_id) | **get** /v1/transaction/{game_id}/{id} | Retrieve Transaction by ID
[**get_transactions**](#get_transactions) | **get** /v1/transaction | Retrieve transactions

# **get_transaction_by_id**
<a name="get_transaction_by_id"></a>
> Transaction get_transaction_by_id(authorizationidgame_id)

Retrieve Transaction by ID

Retrieve transaction by ID

### Example

```python
import l3vels
from l3vels.apis.tags import transaction_api
from l3vels.model.transaction import Transaction
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transaction_api.TransactionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
        'game_id': "game_id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Retrieve Transaction by ID
        api_response = api_instance.get_transaction_by_id(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling TransactionApi->get_transaction_by_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 
game_id | GameIdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GameIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_transaction_by_id.ApiResponseFor200) | The transaction has been found.
400 | [ApiResponseFor400](#get_transaction_by_id.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#get_transaction_by_id.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#get_transaction_by_id.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#get_transaction_by_id.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#get_transaction_by_id.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#get_transaction_by_id.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#get_transaction_by_id.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### get_transaction_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Transaction**](../../models/Transaction.md) |  | 


#### get_transaction_by_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_transaction_by_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_transaction_by_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_transaction_by_id.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_transaction_by_id.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_transaction_by_id.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_transaction_by_id.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_transactions**
<a name="get_transactions"></a>
> Transaction get_transactions(authorizationgame_id)

Retrieve transactions

Retrieve all transactions.

### Example

```python
import l3vels
from l3vels.apis.tags import transaction_api
from l3vels.model.transaction import Transaction
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = transaction_api.TransactionApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'game_id': "a44b646a-ae14-4e05-ae09-b12d5e7269bf",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Retrieve transactions
        api_response = api_instance.get_transactions(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling TransactionApi->get_transactions: %s\n" % e)

    # example passing only optional values
    query_params = {
        'game_id': "a44b646a-ae14-4e05-ae09-b12d5e7269bf",
        'collection_id': "a44b646a-ae14-4e05-ae09-b12d5e7269bf",
        'player_id': "a44b646a-ae14-4e05-ae09-b12d5e7269bf",
        'sort': "name",
        'order': "ASC",
        'search_text': "Hammer",
        'limit': 10,
        'page': 1,
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Retrieve transactions
        api_response = api_instance.get_transactions(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling TransactionApi->get_transactions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
game_id | GameIdSchema | | 
collection_id | CollectionIdSchema | | optional
player_id | PlayerIdSchema | | optional
sort | SortSchema | | optional
order | OrderSchema | | optional
search_text | SearchTextSchema | | optional
limit | LimitSchema | | optional
page | PageSchema | | optional


# GameIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CollectionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PlayerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["ASC", "DESC", ] 

# SearchTextSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

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
200 | [ApiResponseFor200](#get_transactions.ApiResponseFor200) | The transactions has been found.
400 | [ApiResponseFor400](#get_transactions.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#get_transactions.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#get_transactions.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#get_transactions.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#get_transactions.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#get_transactions.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#get_transactions.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### get_transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Transaction**](../../models/Transaction.md) |  | 


#### get_transactions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_transactions.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_transactions.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_transactions.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_transactions.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_transactions.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_transactions.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

