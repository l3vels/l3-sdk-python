# l3vels.model.asset.Asset

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**modified_on** | str, datetime,  | str,  | The date when the collection was last modified. | value must conform to RFC-3339 date-time
**minted_amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The minted amount of the asset. | 
**description** | str,  | str,  | The description of the asset. | 
**asset_url** | str,  | str,  | The asset URL. | 
**created_by** | decimal.Decimal, int, float,  | decimal.Decimal,  | The Id of the user who created the collection. | 
**supply** | decimal.Decimal, int, float,  | decimal.Decimal,  | The supply of the asset. | 
**collection_id** | str,  | str,  | The unique identifier of the collection that the asset is associated with. This allows developers to organize their collections by project and helps with tracking and reporting. | 
**[medias](#medias)** | list, tuple,  | tuple,  | Additional images associated with the asset, such as screenshots or promotional images. | 
**account_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | The unique identifier of the account that the Collection belongs to. | 
**token_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | The token id of the asset. | 
**created_on** | str, datetime,  | str,  | The date when the collection was created. | value must conform to RFC-3339 date-time
**project_id** | str,  | str,  | The unique identifier of the project that the asset is associated with. This allows developers to organize their assets by project and helps with tracking and reporting. | 
**parent_id** | str,  | str,  | ID of the parent asset. | 
**price** | decimal.Decimal, int, float,  | decimal.Decimal,  | The price of the asset. | 
**asset_type** | str,  | str,  | The asset type. Can be main or nested. | 
**modified_by** | decimal.Decimal, int, float,  | decimal.Decimal,  | The Id of the user who last modified the collection. | 
**name** | str,  | str,  | The name of the asset. | 
**main_media** | str,  | str,  | The main or featured image associated with the asset. You can set it from the Dashboard as main image. | 
**[attributes](#attributes)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Custom attributes of the asset. | 
**id** | str,  | str,  | The unique identifier for the asset entity. | 
**[properties](#properties)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Custom properties of the asset. | 
**status** | str,  | str,  | The status of the asset. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# properties

Custom properties of the asset.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Custom properties of the asset. | 

# attributes

Custom attributes of the asset.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Custom attributes of the asset. | 

# medias

Additional images associated with the asset, such as screenshots or promotional images.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Additional images associated with the asset, such as screenshots or promotional images. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

