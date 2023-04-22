# l3vels.model.transaction.Transaction

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**modified_on** | str, datetime,  | str,  | The date when the collection was last modified. | value must conform to RFC-3339 date-time
**chain_id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Chain ID: 1 for Ethereum, 5 for Goerli, 80001 for Polygon Mumbai, etc. | 
**method** | str,  | str,  | Function method name that was called in smart contract | 
**contract_id** | str,  | str,  | Contract ID the transaction is associated with. | 
**block_number** | decimal.Decimal, int, float,  | decimal.Decimal,  | Unique block number in the blockchain. | 
**contract_address** | str,  | str,  | Contract address where the transaction happened. | 
**type** | str,  | str,  | Transaction type: Mint, Transfer, Award, Airdrop, etc. | 
**created_by** | str,  | str,  | The Id of the user who created the collection. | 
**collection_id** | str,  | str,  | The unique identifier of the collection that the transaction is associated with. This allows developers to organize their transactions by game and helps with tracking and reporting. | 
**environment** | str,  | str,  | Chain environment: Testnet, Mainnet, etc. | 
**account_id** | str,  | str,  | The unique identifier of the account that the transaction belongs to. | 
**blockchain** | str,  | str,  | Main blockchain identifier: Ethereum, Polygon, etc. | 
**created_on** | str, datetime,  | str,  | The date when the collection was created. | value must conform to RFC-3339 date-time
**modified_by** | str,  | str,  | The Id of the user who last modified the collection. | 
**from** | str,  | str,  | Address of the sender of the transaction. | 
**id** | str,  | str,  | The unique identifier for the transaction entity. | 
**to** | str,  | str,  | Address of the receiver of the transaction. It can be contract address or player address if it is a transfer transaction. | 
**chain_name** | str,  | str,  | Chain name identifier: Ethereum, Goerli, Sepolia, PolygonPoS, etc. | 
**[events](#events)** | list, tuple,  | tuple,  | List of events that were emitted in the transaction | 
**transaction_hash** | str,  | str,  | Unique transaction hash in the blockchain. | 
**game_id** | str,  | str,  | The unique identifier of the game that the transaction is associated with. This allows developers to organize their transactions by game and helps with tracking and reporting. | 
**status** | str,  | str,  | Transaction status in Blockchain. Can be pending, success or fail | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# events

List of events that were emitted in the transaction

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of events that were emitted in the transaction | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

