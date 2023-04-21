import typing_extensions

from l3vels.apis.tags import TagValues
from l3vels.apis.tags.l3vels_api import L3velsApi
from l3vels.apis.tags.game_api import GameApi
from l3vels.apis.tags.asset_api import AssetApi
from l3vels.apis.tags.collection_api import CollectionApi
from l3vels.apis.tags.contract_api import ContractApi
from l3vels.apis.tags.mint_api import MintApi
from l3vels.apis.tags.player_api import PlayerApi
from l3vels.apis.tags.transaction_api import TransactionApi
from l3vels.apis.tags.utilities_api import UtilitiesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.L3VELS: L3velsApi,
        TagValues.GAME: GameApi,
        TagValues.ASSET: AssetApi,
        TagValues.COLLECTION: CollectionApi,
        TagValues.CONTRACT: ContractApi,
        TagValues.MINT: MintApi,
        TagValues.PLAYER: PlayerApi,
        TagValues.TRANSACTION: TransactionApi,
        TagValues.UTILITIES: UtilitiesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.L3VELS: L3velsApi,
        TagValues.GAME: GameApi,
        TagValues.ASSET: AssetApi,
        TagValues.COLLECTION: CollectionApi,
        TagValues.CONTRACT: ContractApi,
        TagValues.MINT: MintApi,
        TagValues.PLAYER: PlayerApi,
        TagValues.TRANSACTION: TransactionApi,
        TagValues.UTILITIES: UtilitiesApi,
    }
)
