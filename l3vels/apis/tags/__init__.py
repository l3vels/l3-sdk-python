# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from l3vels.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    L3VELS = "L3vels"
    GAME = "Game"
    ASSET = "Asset"
    COLLECTION = "Collection"
    CONTRACT = "Contract"
    MINT = "Mint"
    PLAYER = "Player"
    TRANSACTION = "Transaction"
    UTILITIES = "Utilities"
    DEFAULT = "default"
