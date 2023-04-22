# l3vels.model.game.Game

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**modified_on** | str, datetime,  | str,  | The date and time that the Game entity was last modified. | value must conform to RFC-3339 date-time
**contact_phone** | str,  | str,  |  A phone number for contacting the Game&#x27;s developers or support team. | 
**[social_links](#social_links)** | list, tuple,  | tuple,  | Additional social links associated with the collection | 
**description** | str,  | str,  | A brief description of the Game. | 
**instagram** | str,  | str,  | The link to the Game&#x27;s official Instagram account. | 
**logo_image** | str,  | str,  | The logo or icon associated with the Game. | 
**web_link** | str,  | str,  | The URL for the Game&#x27;s website or landing page. | 
**created_by** | str,  | str,  | The user or system that created the Game entity. | 
**url** | str,  | str,  | A unique URL for the game on the L3vels platform. | 
**contact_email** | str,  | str,  | An email address for contacting the Game&#x27;s developers or support team. | 
**[medias](#medias)** | list, tuple,  | tuple,  | Additional images associated with the collection, such as screenshots or promotional images. | 
**twitter** | str,  | str,  | The link to the Game&#x27;s official Twitter account. | 
**account_id** | str,  | str,  |  The unique identifier of the account that the Game belongs to. This allows developers to manage multiple Games across multiple accounts. | 
**discord** | str,  | str,  | The link to the Game&#x27;s Discord server. | 
**created_on** | str, datetime,  | str,  | The date and time that the Game entity was created. | value must conform to RFC-3339 date-time
**modified_by** | str,  | str,  | The user or system that last modified the Game entity. | 
**name** | str,  | str,  | The name of the Game. | 
**main_media** | str,  | str,  | The main or featured image associated with the Game. You can set it from the Dashboard as main image. | 
**id** | str,  | str,  | The unique identifier for the Game entity. | 
**category** | str,  | str,  | The category or genre of the Game. | 
**status** | str,  | str,  | The current status of the Game, such as \&quot;Draft\&quot;, \&quot;Active\&quot;, or \&quot;Inactive\&quot;. | 
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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

