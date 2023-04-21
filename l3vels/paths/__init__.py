# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from l3vels.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_UTILITIES_HEALTH = "/v1/utilities/health"
    V1_GAME_ID = "/v1/game/{id}"
    V1_CONTRACT_COLLECTIONSIZE = "/v1/contract/collection-size"
    V1_CONTRACT_CONTRACTURI = "/v1/contract/contract-uri"
    V1_CONTRACT_SALESTATUS = "/v1/contract/sale-status"
    V1_COLLECTION = "/v1/collection"
    V1_COLLECTION_COUNT_PROJECT_ID = "/v1/collection/count/{project_id}"
    V1_COLLECTION_PROJECT_ID_ID = "/v1/collection/{project_id}/{id}"
    V1_ASSET = "/v1/asset"
    V1_ASSET_COUNT_PROJECT_ID = "/v1/asset/count/{project_id}"
    V1_ASSET_PROJECT_ID_ID = "/v1/asset/{project_id}/{id}"
    V1_ASSET_ID = "/v1/asset/{id}"
    V1_TRANSACTION_WEBHOOK = "/v1/transaction/webhook"
    V1_TRANSACTION = "/v1/transaction"
    V1_TRANSACTION_PROJECT_ID_ID = "/v1/transaction/{project_id}/{id}"
    V1_PLAYERASSET_PROJECT_ID_ID = "/v1/player-asset/{project_id}/{id}"
    V1_PLAYERASSET = "/v1/player-asset"
    V1_PLAYER_PROJECT_ID_ID = "/v1/player/{project_id}/{id}"
    V1_PLAYER = "/v1/player"
    V1_PLAYER_COUNT_PROJECT_ID = "/v1/player/count/{project_id}"
    V1_MINT = "/v1/mint"
    V1_MINT_BATCH = "/v1/mint/batch"
    V1_MINT_AWARD = "/v1/mint/award"
    V1_MINT_AIRDROP = "/v1/mint/airdrop"
    V1_MINT_PLAYER = "/v1/mint/player"
    V1_MINT_BATCHPLAYER = "/v1/mint/batch-player"
