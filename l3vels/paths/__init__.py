# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from l3vels.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_UTILITIES_HEALTH = "/v1/utilities/health"
    V1_GAME_GAME_ID = "/v1/game/{game_id}"
    V1_GAME_NAME_NAME = "/v1/game/name/{name}"
    V1_GAME = "/v1/game"
    V1_CONTRACT_COLLECTIONSIZE = "/v1/contract/collection-size"
    V1_CONTRACT_CONTRACTURI = "/v1/contract/contract-uri"
    V1_CONTRACT_SALESTATUS = "/v1/contract/sale-status"
    V1_COLLECTION = "/v1/collection"
    V1_COLLECTION_COUNT_GAME_ID = "/v1/collection/count/{game_id}"
    V1_COLLECTION_GAME_ID_ID = "/v1/collection/{game_id}/{id}"
    V1_PLAYER_GAME_ID_ID = "/v1/player/{game_id}/{id}"
    V1_PLAYER = "/v1/player"
    V1_PLAYER_COUNT_GAME_ID = "/v1/player/count/{game_id}"
    V1_TRANSACTION = "/v1/transaction"
    V1_TRANSACTION_GAME_ID_ID = "/v1/transaction/{game_id}/{id}"
    V1_ASSET = "/v1/asset"
    V1_ASSET_COUNT_GAME_ID = "/v1/asset/count/{game_id}"
    V1_ASSET_GAME_ID_ID = "/v1/asset/{game_id}/{id}"
    V1_ASSET_ID = "/v1/asset/{id}"
    V1_PLAYERASSET_GAME_ID_ID = "/v1/player-asset/{game_id}/{id}"
    V1_PLAYERASSET = "/v1/player-asset"
    V1_MINT = "/v1/mint"
    V1_MINT_BATCH = "/v1/mint/batch"
    V1_MINT_AWARD = "/v1/mint/award"
    V1_MINT_AIRDROP = "/v1/mint/airdrop"
    V1_MINT_PLAYER = "/v1/mint/player"
    V1_MINT_BATCHPLAYER = "/v1/mint/batch-player"
    V1_CHAT_WEBHOOK = "/v1/chat/webhook"
    V1_CHAT_REPORT = "/v1/chat/report"
