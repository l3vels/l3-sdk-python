<a name="__pageTop"></a>
# l3vels.apis.tags.collection_api.CollectionApi

All URIs are relative to *https://api-dev.l3vels.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collection_controller_create_collection**](#collection_controller_create_collection) | **post** /v1/collection | Create a new collection inside specific game
[**count_collections_by_game_id**](#count_collections_by_game_id) | **get** /v1/collection/count/{game_id} | Count collections
[**get_collection_by_id**](#get_collection_by_id) | **get** /v1/collection/{game_id}/{id} | Retrieve collection by ID
[**get_collections**](#get_collections) | **get** /v1/collection | Retrieve collections

# **collection_controller_create_collection**
<a name="collection_controller_create_collection"></a>
> Collection collection_controller_create_collection(authorizationbody)

Create a new collection inside specific game

This API method creates collection in a specified game

### Example

```python
import l3vels
from l3vels.apis.tags import collection_api
from l3vels.model.collection import Collection
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collection_api.CollectionApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict()
    try:
        # Create a new collection inside specific game
        api_response = api_instance.collection_controller_create_collection(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling CollectionApi->collection_controller_create_collection: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

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
200 | [ApiResponseFor200](#collection_controller_create_collection.ApiResponseFor200) | The collection has been created.
400 | [ApiResponseFor400](#collection_controller_create_collection.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#collection_controller_create_collection.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#collection_controller_create_collection.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#collection_controller_create_collection.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#collection_controller_create_collection.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#collection_controller_create_collection.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#collection_controller_create_collection.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### collection_controller_create_collection.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


#### collection_controller_create_collection.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### collection_controller_create_collection.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### collection_controller_create_collection.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### collection_controller_create_collection.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### collection_controller_create_collection.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### collection_controller_create_collection.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### collection_controller_create_collection.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **count_collections_by_game_id**
<a name="count_collections_by_game_id"></a>
> int, float count_collections_by_game_id(authorizationgame_id)

Count collections

Count total collections in game.

### Example

```python
import l3vels
from l3vels.apis.tags import collection_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collection_api.CollectionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'game_id': "a44b646a-ae14-4e05-ae09-b12d5e7269bf",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Count collections
        api_response = api_instance.count_collections_by_game_id(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling CollectionApi->count_collections_by_game_id: %s\n" % e)
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
game_id | GameIdSchema | | 

# GameIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_collections_by_game_id.ApiResponseFor200) | The collections has been counted.
400 | [ApiResponseFor400](#count_collections_by_game_id.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#count_collections_by_game_id.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#count_collections_by_game_id.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#count_collections_by_game_id.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#count_collections_by_game_id.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#count_collections_by_game_id.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#count_collections_by_game_id.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### count_collections_by_game_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

#### count_collections_by_game_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_collections_by_game_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_collections_by_game_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_collections_by_game_id.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_collections_by_game_id.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_collections_by_game_id.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_collections_by_game_id.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_collection_by_id**
<a name="get_collection_by_id"></a>
> Collection get_collection_by_id(authorizationidgame_id)

Retrieve collection by ID

This API method retrieves a specific collection based on the unique identifier provided in the request.

### Example

```python
import l3vels
from l3vels.apis.tags import collection_api
from l3vels.model.collection import Collection
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collection_api.CollectionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "229fd9e0-b51f-4b20-9203-9db60995e6b1",
        'game_id': "a44b646a-ae14-4e05-ae09-b12d5e7269bf",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Retrieve collection by ID
        api_response = api_instance.get_collection_by_id(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling CollectionApi->get_collection_by_id: %s\n" % e)
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
200 | [ApiResponseFor200](#get_collection_by_id.ApiResponseFor200) | The collection has been found.
400 | [ApiResponseFor400](#get_collection_by_id.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#get_collection_by_id.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#get_collection_by_id.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#get_collection_by_id.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#get_collection_by_id.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#get_collection_by_id.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#get_collection_by_id.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### get_collection_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Collection**](../../models/Collection.md) |  | 


#### get_collection_by_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_collection_by_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_collection_by_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_collection_by_id.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_collection_by_id.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_collection_by_id.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_collection_by_id.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_collections**
<a name="get_collections"></a>
> [Collection] get_collections(authorizationgame_id)

Retrieve collections

This API method retrieves a list of collections that match the specified filter criteria. Developers can use this method to retrieve collections by name, category, status, or other properties.

### Example

```python
import l3vels
from l3vels.apis.tags import collection_api
from l3vels.model.collection import Collection
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collection_api.CollectionApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'game_id': "a44b646a-ae14-4e05-ae09-b12d5e7269bf",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Retrieve collections
        api_response = api_instance.get_collections(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling CollectionApi->get_collections: %s\n" % e)

    # example passing only optional values
    query_params = {
        'game_id': "a44b646a-ae14-4e05-ae09-b12d5e7269bf",
        'sort': "name",
        'order': "ASC",
        'search_text': "Weapons",
        'limit': 10,
        'page': 1,
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Retrieve collections
        api_response = api_instance.get_collections(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling CollectionApi->get_collections: %s\n" % e)
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

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
200 | [ApiResponseFor200](#get_collections.ApiResponseFor200) | The collections has been found
400 | [ApiResponseFor400](#get_collections.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#get_collections.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#get_collections.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#get_collections.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#get_collections.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#get_collections.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#get_collections.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### get_collections.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Collection**]({{complexTypePrefix}}Collection.md) | [**Collection**]({{complexTypePrefix}}Collection.md) | [**Collection**]({{complexTypePrefix}}Collection.md) |  | 

#### get_collections.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_collections.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_collections.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_collections.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_collections.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_collections.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_collections.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

