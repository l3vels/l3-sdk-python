<a name="__pageTop"></a>
# l3vels.apis.tags.game_api.GameApi

All URIs are relative to *https://api-dev.l3vels.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_game**](#create_game) | **post** /v1/game | Create Game
[**game_controller_get_games**](#game_controller_get_games) | **get** /v1/game | Retrieve all games
[**get_game_by_id**](#get_game_by_id) | **get** /v1/game/{game_id} | Retrieve Game

# **create_game**
<a name="create_game"></a>
> Game create_game(authorizationbody)

Create Game

Create game on platform.

### Example

```python
import l3vels
from l3vels.apis.tags import game_api
from l3vels.model.game import Game
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = game_api.GameApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict()
    try:
        # Create Game
        api_response = api_instance.create_game(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling GameApi->create_game: %s\n" % e)
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
200 | [ApiResponseFor200](#create_game.ApiResponseFor200) | The Game has been found.
400 | [ApiResponseFor400](#create_game.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#create_game.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#create_game.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#create_game.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#create_game.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#create_game.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#create_game.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### create_game.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Game**](../../models/Game.md) |  | 


#### create_game.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_game.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_game.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_game.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_game.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_game.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_game.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **game_controller_get_games**
<a name="game_controller_get_games"></a>
> Game game_controller_get_games(authorizationgame_id)

Retrieve all games

Retrieve all your games/games created on the platform. You can filter games by name, description. You can sort games by field

### Example

```python
import l3vels
from l3vels.apis.tags import game_api
from l3vels.model.game import Game
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = game_api.GameApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'game_id': "a44b646a-ae14-4e05-ae09-b12d5e7269bf",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Retrieve all games
        api_response = api_instance.game_controller_get_games(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling GameApi->game_controller_get_games: %s\n" % e)

    # example passing only optional values
    query_params = {
        'sort': "ASC",
        'search_text': "Call of Duty",
        'limit': 10,
        'page': 1,
        'game_id': "a44b646a-ae14-4e05-ae09-b12d5e7269bf",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Retrieve all games
        api_response = api_instance.game_controller_get_games(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling GameApi->game_controller_get_games: %s\n" % e)
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
sort | SortSchema | | optional
search_text | SearchTextSchema | | optional
limit | LimitSchema | | optional
page | PageSchema | | optional
game_id | GameIdSchema | | 


# SortSchema

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

# GameIdSchema

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
200 | [ApiResponseFor200](#game_controller_get_games.ApiResponseFor200) | The games has been found.
400 | [ApiResponseFor400](#game_controller_get_games.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#game_controller_get_games.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#game_controller_get_games.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#game_controller_get_games.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#game_controller_get_games.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#game_controller_get_games.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#game_controller_get_games.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### game_controller_get_games.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Game**](../../models/Game.md) |  | 


#### game_controller_get_games.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### game_controller_get_games.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### game_controller_get_games.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### game_controller_get_games.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### game_controller_get_games.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### game_controller_get_games.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### game_controller_get_games.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_game_by_id**
<a name="get_game_by_id"></a>
> Game get_game_by_id(authorizationgame_id)

Retrieve Game

Get Game by ID created on the platform.

### Example

```python
import l3vels
from l3vels.apis.tags import game_api
from l3vels.model.game import Game
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = game_api.GameApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'game_id': "a44b646a-ae14-4e05-ae09-b12d5e7269bf",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Retrieve Game
        api_response = api_instance.get_game_by_id(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling GameApi->get_game_by_id: %s\n" % e)
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
200 | [ApiResponseFor200](#get_game_by_id.ApiResponseFor200) | The Game has been found.
400 | [ApiResponseFor400](#get_game_by_id.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#get_game_by_id.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#get_game_by_id.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#get_game_by_id.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#get_game_by_id.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#get_game_by_id.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#get_game_by_id.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### get_game_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Game**](../../models/Game.md) |  | 


#### get_game_by_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_game_by_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_game_by_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_game_by_id.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_game_by_id.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_game_by_id.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_game_by_id.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

