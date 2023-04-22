# l3vels.model.collection.Collection

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**modified_on** | str, datetime,  | str,  | The date when the collection was last modified. | value must conform to RFC-3339 date-time
**unique_id** | str,  | str,  | The unique identifier that can be provided by game studio. | 
**[custom_property_props](#custom_property_props)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Custom properties that are unique to the collection and defined by the developer to categorize and filter them. | 
**[social_links](#social_links)** | list, tuple,  | tuple,  | Additional social links associated with the collection | 
**description** | str,  | str,  | A brief description of the collection. | 
**logo_image** | str,  | str,  | An image representing the collection&#x27;s logo. | 
**web_link** | str,  | str,  | A URL link to the collection&#x27;s webpage. | 
**created_by** | str,  | str,  | The Id of the user who created the collection. | 
**supply** | decimal.Decimal, int, float,  | decimal.Decimal,  | The supply represents the number of assets that are available within the Collection. | 
**url** | str,  | str,  | A unique URL for the collection on the L3vels platform. | 
**[medias](#medias)** | list, tuple,  | tuple,  | Additional images associated with the collection, such as screenshots or promotional images. | 
**account_id** | str,  | str,  | The unique identifier of the account that the Collection belongs to. | 
**created_on** | str, datetime,  | str,  | The date when the collection was created. | value must conform to RFC-3339 date-time
**modified_by** | str,  | str,  | The Id of the user who last modified the collection. | 
**name** | str,  | str,  | The name of the collection. | 
**main_media** | str,  | str,  | The main or featured image associated with the game. You can set it from the dashboard as main image. | 
**[custom_asset_props](#custom_asset_props)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Custom assets fields associated with the collection. | 
**[categories](#categories)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The category or categories that the collection belongs to. | 
**id** | str,  | str,  | The unique identifier for the collection entity. | 
**game_id** | str,  | str,  | The unique identifier of the game that the collection is associated with. This allows developers to organize their collections by game and helps with tracking and reporting. | 
**status** | str,  | str,  | The current status of the collection. Possible values are: Draft, Active | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# medias

Additional images associated with the collection, such as screenshots or promotional images.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Additional images associated with the collection, such as screenshots or promotional images. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# custom_property_props

Custom properties that are unique to the collection and defined by the developer to categorize and filter them.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Custom properties that are unique to the collection and defined by the developer to categorize and filter them. | 

# social_links

Additional social links associated with the collection

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Additional social links associated with the collection | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# custom_asset_props

Custom assets fields associated with the collection.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Custom assets fields associated with the collection. | 

# categories

The category or categories that the collection belongs to.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The category or categories that the collection belongs to. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

