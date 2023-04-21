# l3vels.model.player_asset.PlayerAsset

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**collection_id** | str,  | str,  | The unique identifier of the collection that the Player asset is associated with. | 
**modified_on** | str, datetime,  | str,  | The date when the player was last modified. | value must conform to RFC-3339 date-time
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The amount of the specific asset that the player has. | 
**account_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | The unique identifier of the account that the Player belongs to. | 
**player_id** | str,  | str,  | The unique identifier of the player that the asset is associated with. | 
**created_on** | str, datetime,  | str,  | The date when the player was created. | value must conform to RFC-3339 date-time
**project_id** | str,  | str,  | The unique identifier of the project that the Player is associated with. This allows developers to organize their players by project and helps with tracking and reporting. | 
**modified_by** | decimal.Decimal, int, float,  | decimal.Decimal,  | The Id of the user who last modified the player. | 
**asset_id** | str,  | str,  | The unique identifier of the asset that the asset is associated with. | 
**id** | str,  | str,  | The unique identifier for the Player asset entity. | 
**created_by** | decimal.Decimal, int, float,  | decimal.Decimal,  | The Id of the user who created the player. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

