# l3vels.model.create_player_dto.CreatePlayerDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**project_id** | str,  | str,  | Game/project ID to create the player for. Example: Create player Jack for game Fortnite. | 
**name** | str,  | str,  | The name of the player. | 
**unique_id** | str,  | str,  | You can send your generated unique ID for player if it&#x27;s handy for game. If field is empty, we will generate unique ID. | [optional] 
**username** | str,  | str,  | The username of the player. | [optional] 
**email** | str,  | str,  | The email of the player. | [optional] 
**avatar** | str,  | str,  | The image URL of the player avatar. | [optional] 
**is_create_wallet** | bool,  | BoolClass,  | Should create wallet for player or not. | [optional] 
**[custom_props](#custom_props)** | list, tuple,  | tuple,  | Custom props for player. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# custom_props

Custom props for player.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Custom props for player. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

