# coding: utf-8

"""
    L3vels Api

    L3vels API for Game developers  # noqa: E501

    The version of the OpenAPI document: 0.3
    Contact: support@l3vels.xyz
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from l3vels import schemas  # noqa: F401


class UpdateAssetInput(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "collection_id",
            "game_id",
        }
        
        class properties:
            collection_id = schemas.StrSchema
            game_id = schemas.StrSchema
            name = schemas.StrSchema
            description = schemas.StrSchema
            price = schemas.NumberSchema
            supply = schemas.NumberSchema
            asset_url = schemas.StrSchema
            custom_props = schemas.DictSchema
            __annotations__ = {
                "collection_id": collection_id,
                "game_id": game_id,
                "name": name,
                "description": description,
                "price": price,
                "supply": supply,
                "asset_url": asset_url,
                "custom_props": custom_props,
            }
    
    collection_id: MetaOapg.properties.collection_id
    game_id: MetaOapg.properties.game_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collection_id"]) -> MetaOapg.properties.collection_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["game_id"]) -> MetaOapg.properties.game_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supply"]) -> MetaOapg.properties.supply: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["asset_url"]) -> MetaOapg.properties.asset_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_props"]) -> MetaOapg.properties.custom_props: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["collection_id", "game_id", "name", "description", "price", "supply", "asset_url", "custom_props", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collection_id"]) -> MetaOapg.properties.collection_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["game_id"]) -> MetaOapg.properties.game_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> typing.Union[MetaOapg.properties.price, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supply"]) -> typing.Union[MetaOapg.properties.supply, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["asset_url"]) -> typing.Union[MetaOapg.properties.asset_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_props"]) -> typing.Union[MetaOapg.properties.custom_props, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["collection_id", "game_id", "name", "description", "price", "supply", "asset_url", "custom_props", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        collection_id: typing.Union[MetaOapg.properties.collection_id, str, ],
        game_id: typing.Union[MetaOapg.properties.game_id, str, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        price: typing.Union[MetaOapg.properties.price, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        supply: typing.Union[MetaOapg.properties.supply, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        asset_url: typing.Union[MetaOapg.properties.asset_url, str, schemas.Unset] = schemas.unset,
        custom_props: typing.Union[MetaOapg.properties.custom_props, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateAssetInput':
        return super().__new__(
            cls,
            *_args,
            collection_id=collection_id,
            game_id=game_id,
            name=name,
            description=description,
            price=price,
            supply=supply,
            asset_url=asset_url,
            custom_props=custom_props,
            _configuration=_configuration,
            **kwargs,
        )