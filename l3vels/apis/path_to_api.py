import typing_extensions

from l3vels.paths import PathValues
from l3vels.apis.paths.v1_utilities_health import V1UtilitiesHealth
from l3vels.apis.paths.v1_game_id import V1GameId
from l3vels.apis.paths.v1_contract_collection_size import V1ContractCollectionSize
from l3vels.apis.paths.v1_contract_contract_uri import V1ContractContractUri
from l3vels.apis.paths.v1_contract_sale_status import V1ContractSaleStatus
from l3vels.apis.paths.v1_collection import V1Collection
from l3vels.apis.paths.v1_collection_count_game_id import V1CollectionCountGameId
from l3vels.apis.paths.v1_collection_game_id_id import V1CollectionGameIdId
from l3vels.apis.paths.v1_asset import V1Asset
from l3vels.apis.paths.v1_asset_count_game_id import V1AssetCountGameId
from l3vels.apis.paths.v1_asset_game_id_id import V1AssetGameIdId
from l3vels.apis.paths.v1_asset_id import V1AssetId
from l3vels.apis.paths.v1_transaction_webhook import V1TransactionWebhook
from l3vels.apis.paths.v1_transaction import V1Transaction
from l3vels.apis.paths.v1_transaction_game_id_id import V1TransactionGameIdId
from l3vels.apis.paths.v1_player_asset_game_id_id import V1PlayerAssetGameIdId
from l3vels.apis.paths.v1_player_asset import V1PlayerAsset
from l3vels.apis.paths.v1_player_game_id_id import V1PlayerGameIdId
from l3vels.apis.paths.v1_player import V1Player
from l3vels.apis.paths.v1_player_count_game_id import V1PlayerCountGameId
from l3vels.apis.paths.v1_mint import V1Mint
from l3vels.apis.paths.v1_mint_batch import V1MintBatch
from l3vels.apis.paths.v1_mint_award import V1MintAward
from l3vels.apis.paths.v1_mint_airdrop import V1MintAirdrop
from l3vels.apis.paths.v1_mint_player import V1MintPlayer
from l3vels.apis.paths.v1_mint_batch_player import V1MintBatchPlayer

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_UTILITIES_HEALTH: V1UtilitiesHealth,
        PathValues.V1_GAME_ID: V1GameId,
        PathValues.V1_CONTRACT_COLLECTIONSIZE: V1ContractCollectionSize,
        PathValues.V1_CONTRACT_CONTRACTURI: V1ContractContractUri,
        PathValues.V1_CONTRACT_SALESTATUS: V1ContractSaleStatus,
        PathValues.V1_COLLECTION: V1Collection,
        PathValues.V1_COLLECTION_COUNT_GAME_ID: V1CollectionCountGameId,
        PathValues.V1_COLLECTION_GAME_ID_ID: V1CollectionGameIdId,
        PathValues.V1_ASSET: V1Asset,
        PathValues.V1_ASSET_COUNT_GAME_ID: V1AssetCountGameId,
        PathValues.V1_ASSET_GAME_ID_ID: V1AssetGameIdId,
        PathValues.V1_ASSET_ID: V1AssetId,
        PathValues.V1_TRANSACTION_WEBHOOK: V1TransactionWebhook,
        PathValues.V1_TRANSACTION: V1Transaction,
        PathValues.V1_TRANSACTION_GAME_ID_ID: V1TransactionGameIdId,
        PathValues.V1_PLAYERASSET_GAME_ID_ID: V1PlayerAssetGameIdId,
        PathValues.V1_PLAYERASSET: V1PlayerAsset,
        PathValues.V1_PLAYER_GAME_ID_ID: V1PlayerGameIdId,
        PathValues.V1_PLAYER: V1Player,
        PathValues.V1_PLAYER_COUNT_GAME_ID: V1PlayerCountGameId,
        PathValues.V1_MINT: V1Mint,
        PathValues.V1_MINT_BATCH: V1MintBatch,
        PathValues.V1_MINT_AWARD: V1MintAward,
        PathValues.V1_MINT_AIRDROP: V1MintAirdrop,
        PathValues.V1_MINT_PLAYER: V1MintPlayer,
        PathValues.V1_MINT_BATCHPLAYER: V1MintBatchPlayer,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_UTILITIES_HEALTH: V1UtilitiesHealth,
        PathValues.V1_GAME_ID: V1GameId,
        PathValues.V1_CONTRACT_COLLECTIONSIZE: V1ContractCollectionSize,
        PathValues.V1_CONTRACT_CONTRACTURI: V1ContractContractUri,
        PathValues.V1_CONTRACT_SALESTATUS: V1ContractSaleStatus,
        PathValues.V1_COLLECTION: V1Collection,
        PathValues.V1_COLLECTION_COUNT_GAME_ID: V1CollectionCountGameId,
        PathValues.V1_COLLECTION_GAME_ID_ID: V1CollectionGameIdId,
        PathValues.V1_ASSET: V1Asset,
        PathValues.V1_ASSET_COUNT_GAME_ID: V1AssetCountGameId,
        PathValues.V1_ASSET_GAME_ID_ID: V1AssetGameIdId,
        PathValues.V1_ASSET_ID: V1AssetId,
        PathValues.V1_TRANSACTION_WEBHOOK: V1TransactionWebhook,
        PathValues.V1_TRANSACTION: V1Transaction,
        PathValues.V1_TRANSACTION_GAME_ID_ID: V1TransactionGameIdId,
        PathValues.V1_PLAYERASSET_GAME_ID_ID: V1PlayerAssetGameIdId,
        PathValues.V1_PLAYERASSET: V1PlayerAsset,
        PathValues.V1_PLAYER_GAME_ID_ID: V1PlayerGameIdId,
        PathValues.V1_PLAYER: V1Player,
        PathValues.V1_PLAYER_COUNT_GAME_ID: V1PlayerCountGameId,
        PathValues.V1_MINT: V1Mint,
        PathValues.V1_MINT_BATCH: V1MintBatch,
        PathValues.V1_MINT_AWARD: V1MintAward,
        PathValues.V1_MINT_AIRDROP: V1MintAirdrop,
        PathValues.V1_MINT_PLAYER: V1MintPlayer,
        PathValues.V1_MINT_BATCHPLAYER: V1MintBatchPlayer,
    }
)
