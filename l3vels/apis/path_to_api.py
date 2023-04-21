import typing_extensions

from l3vels.paths import PathValues
from l3vels.apis.paths.v1_utilities_health import V1UtilitiesHealth
from l3vels.apis.paths.v1_game_id import V1GameId
from l3vels.apis.paths.v1_contract_collection_size import V1ContractCollectionSize
from l3vels.apis.paths.v1_contract_contract_uri import V1ContractContractUri
from l3vels.apis.paths.v1_contract_sale_status import V1ContractSaleStatus
from l3vels.apis.paths.v1_collection import V1Collection
from l3vels.apis.paths.v1_collection_count_project_id import V1CollectionCountProjectId
from l3vels.apis.paths.v1_collection_project_id_id import V1CollectionProjectIdId
from l3vels.apis.paths.v1_asset import V1Asset
from l3vels.apis.paths.v1_asset_count_project_id import V1AssetCountProjectId
from l3vels.apis.paths.v1_asset_project_id_id import V1AssetProjectIdId
from l3vels.apis.paths.v1_asset_id import V1AssetId
from l3vels.apis.paths.v1_transaction_webhook import V1TransactionWebhook
from l3vels.apis.paths.v1_transaction import V1Transaction
from l3vels.apis.paths.v1_transaction_project_id_id import V1TransactionProjectIdId
from l3vels.apis.paths.v1_player_asset_project_id_id import V1PlayerAssetProjectIdId
from l3vels.apis.paths.v1_player_asset import V1PlayerAsset
from l3vels.apis.paths.v1_player_project_id_id import V1PlayerProjectIdId
from l3vels.apis.paths.v1_player import V1Player
from l3vels.apis.paths.v1_player_count_project_id import V1PlayerCountProjectId
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
        PathValues.V1_COLLECTION_COUNT_PROJECT_ID: V1CollectionCountProjectId,
        PathValues.V1_COLLECTION_PROJECT_ID_ID: V1CollectionProjectIdId,
        PathValues.V1_ASSET: V1Asset,
        PathValues.V1_ASSET_COUNT_PROJECT_ID: V1AssetCountProjectId,
        PathValues.V1_ASSET_PROJECT_ID_ID: V1AssetProjectIdId,
        PathValues.V1_ASSET_ID: V1AssetId,
        PathValues.V1_TRANSACTION_WEBHOOK: V1TransactionWebhook,
        PathValues.V1_TRANSACTION: V1Transaction,
        PathValues.V1_TRANSACTION_PROJECT_ID_ID: V1TransactionProjectIdId,
        PathValues.V1_PLAYERASSET_PROJECT_ID_ID: V1PlayerAssetProjectIdId,
        PathValues.V1_PLAYERASSET: V1PlayerAsset,
        PathValues.V1_PLAYER_PROJECT_ID_ID: V1PlayerProjectIdId,
        PathValues.V1_PLAYER: V1Player,
        PathValues.V1_PLAYER_COUNT_PROJECT_ID: V1PlayerCountProjectId,
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
        PathValues.V1_COLLECTION_COUNT_PROJECT_ID: V1CollectionCountProjectId,
        PathValues.V1_COLLECTION_PROJECT_ID_ID: V1CollectionProjectIdId,
        PathValues.V1_ASSET: V1Asset,
        PathValues.V1_ASSET_COUNT_PROJECT_ID: V1AssetCountProjectId,
        PathValues.V1_ASSET_PROJECT_ID_ID: V1AssetProjectIdId,
        PathValues.V1_ASSET_ID: V1AssetId,
        PathValues.V1_TRANSACTION_WEBHOOK: V1TransactionWebhook,
        PathValues.V1_TRANSACTION: V1Transaction,
        PathValues.V1_TRANSACTION_PROJECT_ID_ID: V1TransactionProjectIdId,
        PathValues.V1_PLAYERASSET_PROJECT_ID_ID: V1PlayerAssetProjectIdId,
        PathValues.V1_PLAYERASSET: V1PlayerAsset,
        PathValues.V1_PLAYER_PROJECT_ID_ID: V1PlayerProjectIdId,
        PathValues.V1_PLAYER: V1Player,
        PathValues.V1_PLAYER_COUNT_PROJECT_ID: V1PlayerCountProjectId,
        PathValues.V1_MINT: V1Mint,
        PathValues.V1_MINT_BATCH: V1MintBatch,
        PathValues.V1_MINT_AWARD: V1MintAward,
        PathValues.V1_MINT_AIRDROP: V1MintAirdrop,
        PathValues.V1_MINT_PLAYER: V1MintPlayer,
        PathValues.V1_MINT_BATCHPLAYER: V1MintBatchPlayer,
    }
)
