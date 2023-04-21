<a name="__pageTop"></a>
# l3vels.apis.tags.player_api.PlayerApi

All URIs are relative to *https://api-dev.l3vels.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_players_by_game_id**](#count_players_by_game_id) | **get** /v1/player/count/{project_id} | Count players
[**create_player**](#create_player) | **post** /v1/player | Create new player
[**get_player_by_id**](#get_player_by_id) | **get** /v1/player/{project_id}/{id} | Retrieve player by ID
[**get_players**](#get_players) | **get** /v1/player | Retrieve players
[**player_asset_controller_player_asset_by_id**](#player_asset_controller_player_asset_by_id) | **get** /v1/player-asset/{project_id}/{id} | Retrieve player asset by ID
[**player_asset_controller_player_assets**](#player_asset_controller_player_assets) | **get** /v1/player-asset | Retrieve player assets
[**update_player**](#update_player) | **put** /v1/player | Update an existing Player

# **count_players_by_game_id**
<a name="count_players_by_game_id"></a>
> int, float count_players_by_game_id(authorizationproject_id)

Count players

Count players in game. Example: count players in game Call of Duty.

### Example

```python
import l3vels
from l3vels.apis.tags import player_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = player_api.PlayerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'project_id': "1",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Count players
        api_response = api_instance.count_players_by_game_id(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling PlayerApi->count_players_by_game_id: %s\n" % e)
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
project_id | ProjectIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count_players_by_game_id.ApiResponseFor200) | The players has been found.
400 | [ApiResponseFor400](#count_players_by_game_id.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#count_players_by_game_id.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#count_players_by_game_id.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#count_players_by_game_id.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#count_players_by_game_id.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#count_players_by_game_id.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#count_players_by_game_id.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### count_players_by_game_id.ApiResponseFor200
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

#### count_players_by_game_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_players_by_game_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_players_by_game_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_players_by_game_id.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_players_by_game_id.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_players_by_game_id.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count_players_by_game_id.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_player**
<a name="create_player"></a>
> Player create_player(authorizationcreate_player_dto)

Create new player

Create new player for game/project. Example: Create new player Jack in game Call of Duty.

### Example

```python
import l3vels
from l3vels.apis.tags import player_api
from l3vels.model.player import Player
from l3vels.model.create_player_dto import CreatePlayerDto
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = player_api.PlayerApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = CreatePlayerDto(
        unique_id="f811b994a31",
        name="Jack",
        username="jack",
        email="jack@gmail.com",
        avatar="https://example.com/avatar.png",
        project_id="353c69f6-76a6-4baa-b68b-852c1c531953",
        is_create_wallet=True,
        custom_props=[{"prop_name":"VIP","prop_type":"Boolean","prop_value":"true"}],
    )
    try:
        # Create new player
        api_response = api_instance.create_player(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling PlayerApi->create_player: %s\n" % e)
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
Type | Description  | Notes
------------- | ------------- | -------------
[**CreatePlayerDto**](../../models/CreatePlayerDto.md) |  | 


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
200 | [ApiResponseFor200](#create_player.ApiResponseFor200) | The players has successfully created.
400 | [ApiResponseFor400](#create_player.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#create_player.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#create_player.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#create_player.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#create_player.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#create_player.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#create_player.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### create_player.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Player**](../../models/Player.md) |  | 


#### create_player.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_player.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_player.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_player.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_player.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_player.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_player.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_player_by_id**
<a name="get_player_by_id"></a>
> Player get_player_by_id(authorizationidproject_id)

Retrieve player by ID

Retrieves a specific player by ID associated with game/project. Example: retrieve player Jack from game Call of Duty.

### Example

```python
import l3vels
from l3vels.apis.tags import player_api
from l3vels.model.player import Player
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = player_api.PlayerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "9abd57ce-b11c-4828-ab6a-19f568a8081a",
        'project_id': "556a2843-b302-4b9d-916c-cefcb5d66053",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Retrieve player by ID
        api_response = api_instance.get_player_by_id(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling PlayerApi->get_player_by_id: %s\n" % e)
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
project_id | ProjectIdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_player_by_id.ApiResponseFor200) | The player has been found.
400 | [ApiResponseFor400](#get_player_by_id.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#get_player_by_id.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#get_player_by_id.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#get_player_by_id.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#get_player_by_id.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#get_player_by_id.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#get_player_by_id.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### get_player_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Player**](../../models/Player.md) |  | 


#### get_player_by_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_player_by_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_player_by_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_player_by_id.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_player_by_id.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_player_by_id.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_player_by_id.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_players**
<a name="get_players"></a>
> [Player] get_players(authorizationproject_id)

Retrieve players

Retrieve a list of players that match the specified filter criteria. Developers can use this method to retrieve players by name, category, status, or other properties. Example: Retrieve players from game Call of Duty.

### Example

```python
import l3vels
from l3vels.apis.tags import player_api
from l3vels.model.player import Player
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = player_api.PlayerApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'project_id': "a44b646a-ae14-4e05-ae09-b12d5e7269bf",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Retrieve players
        api_response = api_instance.get_players(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling PlayerApi->get_players: %s\n" % e)

    # example passing only optional values
    query_params = {
        'project_id': "a44b646a-ae14-4e05-ae09-b12d5e7269bf",
        'sort': "name",
        'order': "ASC",
        'search_text': "Jack",
        'limit': 10,
        'page': 1,
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Retrieve players
        api_response = api_instance.get_players(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling PlayerApi->get_players: %s\n" % e)
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
project_id | ProjectIdSchema | | 
sort | SortSchema | | optional
order | OrderSchema | | optional
search_text | SearchTextSchema | | optional
limit | LimitSchema | | optional
page | PageSchema | | optional


# ProjectIdSchema

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
200 | [ApiResponseFor200](#get_players.ApiResponseFor200) | The players has been found
400 | [ApiResponseFor400](#get_players.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#get_players.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#get_players.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#get_players.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#get_players.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#get_players.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#get_players.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### get_players.ApiResponseFor200
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
[**Player**]({{complexTypePrefix}}Player.md) | [**Player**]({{complexTypePrefix}}Player.md) | [**Player**]({{complexTypePrefix}}Player.md) |  | 

#### get_players.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_players.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_players.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_players.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_players.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_players.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_players.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **player_asset_controller_player_asset_by_id**
<a name="player_asset_controller_player_asset_by_id"></a>
> PlayerAsset player_asset_controller_player_asset_by_id(authorizationidproject_id)

Retrieve player asset by ID

Retrieve player asset by ID. Player asset represents a single asset that a player owns. It has amount field that represents how many of this asset player owns.

### Example

```python
import l3vels
from l3vels.apis.tags import player_api
from l3vels.model.player_asset import PlayerAsset
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = player_api.PlayerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
        'project_id': "project_id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Retrieve player asset by ID
        api_response = api_instance.player_asset_controller_player_asset_by_id(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling PlayerApi->player_asset_controller_player_asset_by_id: %s\n" % e)
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
project_id | ProjectIdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#player_asset_controller_player_asset_by_id.ApiResponseFor200) | The player asset has been found.
400 | [ApiResponseFor400](#player_asset_controller_player_asset_by_id.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#player_asset_controller_player_asset_by_id.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#player_asset_controller_player_asset_by_id.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#player_asset_controller_player_asset_by_id.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#player_asset_controller_player_asset_by_id.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#player_asset_controller_player_asset_by_id.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#player_asset_controller_player_asset_by_id.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### player_asset_controller_player_asset_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PlayerAsset**](../../models/PlayerAsset.md) |  | 


#### player_asset_controller_player_asset_by_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### player_asset_controller_player_asset_by_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### player_asset_controller_player_asset_by_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### player_asset_controller_player_asset_by_id.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### player_asset_controller_player_asset_by_id.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### player_asset_controller_player_asset_by_id.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### player_asset_controller_player_asset_by_id.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **player_asset_controller_player_assets**
<a name="player_asset_controller_player_assets"></a>
> [PlayerAsset] player_asset_controller_player_assets(authorizationproject_id)

Retrieve player assets

This API method retrieves a list of Player assets that match the specified filter criteria. Developers can use this method to retrieve Player assets by player, game/project or other properties.

### Example

```python
import l3vels
from l3vels.apis.tags import player_api
from l3vels.model.player_asset import PlayerAsset
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = player_api.PlayerApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'project_id': "a44b646a-ae14-4e05-ae09-b12d5e7269bf",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Retrieve player assets
        api_response = api_instance.player_asset_controller_player_assets(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling PlayerApi->player_asset_controller_player_assets: %s\n" % e)

    # example passing only optional values
    query_params = {
        'project_id': "a44b646a-ae14-4e05-ae09-b12d5e7269bf",
        'asset_id': "a44b646a-ae14-4e05-ae09-b12d5e7269bf",
        'player_id': "a44b646a-ae14-4e05-ae09-b12d5e7269bf",
        'sort': "name",
        'order': "ASC",
        'limit': 10,
        'page': 1,
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Retrieve player assets
        api_response = api_instance.player_asset_controller_player_assets(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling PlayerApi->player_asset_controller_player_assets: %s\n" % e)
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
project_id | ProjectIdSchema | | 
asset_id | AssetIdSchema | | optional
player_id | PlayerIdSchema | | optional
sort | SortSchema | | optional
order | OrderSchema | | optional
limit | LimitSchema | | optional
page | PageSchema | | optional


# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssetIdSchema

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
200 | [ApiResponseFor200](#player_asset_controller_player_assets.ApiResponseFor200) | The player assets has been found
400 | [ApiResponseFor400](#player_asset_controller_player_assets.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#player_asset_controller_player_assets.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#player_asset_controller_player_assets.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#player_asset_controller_player_assets.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#player_asset_controller_player_assets.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#player_asset_controller_player_assets.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#player_asset_controller_player_assets.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### player_asset_controller_player_assets.ApiResponseFor200
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
[**PlayerAsset**]({{complexTypePrefix}}PlayerAsset.md) | [**PlayerAsset**]({{complexTypePrefix}}PlayerAsset.md) | [**PlayerAsset**]({{complexTypePrefix}}PlayerAsset.md) |  | 

#### player_asset_controller_player_assets.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### player_asset_controller_player_assets.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### player_asset_controller_player_assets.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### player_asset_controller_player_assets.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### player_asset_controller_player_assets.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### player_asset_controller_player_assets.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### player_asset_controller_player_assets.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_player**
<a name="update_player"></a>
> Player update_player(authorization)

Update an existing Player

This API method allows developers to update an existing Player by providing the ID of the Player and the updated properties and associated assets.

### Example

```python
import l3vels
from l3vels.apis.tags import player_api
from l3vels.model.player import Player
from pprint import pprint
# Defining the host is optional and defaults to https://api-dev.l3vels.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = l3vels.Configuration(
    host = "https://api-dev.l3vels.xyz"
)

# Enter a context with an instance of the API client
with l3vels.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = player_api.PlayerApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Update an existing Player
        api_response = api_instance.update_player(
            header_params=header_params,
        )
        pprint(api_response)
    except l3vels.ApiException as e:
        print("Exception when calling PlayerApi->update_player: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_player.ApiResponseFor200) | The players has successful updated.
400 | [ApiResponseFor400](#update_player.ApiResponseFor400) | Bad Request, The request was unacceptable, often due to missing a required parameter.
401 | [ApiResponseFor401](#update_player.ApiResponseFor401) | Unauthorized, No valid API key provided.
404 | [ApiResponseFor404](#update_player.ApiResponseFor404) | Not Found, The requested resource doesn&#x27;t exist.
409 | [ApiResponseFor409](#update_player.ApiResponseFor409) | Conflict, The request conflicts with another request (perhaps due to using the same idempotent key).
429 | [ApiResponseFor429](#update_player.ApiResponseFor429) | Too Many Requests, Too many requests hit the API too quickly. We recommend an exponential backoff of your requests.
500 | [ApiResponseFor500](#update_player.ApiResponseFor500) | Server Errors, Something went wrong on L3vels&#x27;s end.
504 | [ApiResponseFor504](#update_player.ApiResponseFor504) | Gateway Timeout, Your request took too long.

#### update_player.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Player**](../../models/Player.md) |  | 


#### update_player.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_player.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_player.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_player.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_player.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_player.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_player.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

