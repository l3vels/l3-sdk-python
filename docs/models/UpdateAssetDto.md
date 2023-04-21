# l3vels.model.update_asset_dto.UpdateAssetDto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**collection_id** | str,  | str,  | Collection ID to find and update the asset in. Example: Update AK-47 asset in Weapons collection. | 
**project_id** | str,  | str,  | Game/project ID to update the asset in. Example: Call of Duty | 
**name** | str,  | str,  | The name of the asset. | [optional] 
**description** | str,  | str,  | The story of asset. | [optional] 
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | Price of asset | [optional] 
**supply** | decimal.Decimal, int, float,  | decimal.Decimal,  | Supply of asset | [optional] 
**asset_url** | str,  | str,  | Asset URL | [optional] 
**[custom_props](#custom_props)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Custom props for asset. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# custom_props

Custom props for asset.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Custom props for asset. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

