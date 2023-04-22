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


class SetSaleStatusInput(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "collection_id",
            "sale_status",
            "game_id",
        }
        
        class properties:
            game_id = schemas.StrSchema
            collection_id = schemas.StrSchema
            sale_status = schemas.DictSchema
            __annotations__ = {
                "game_id": game_id,
                "collection_id": collection_id,
                "sale_status": sale_status,
            }
    
    collection_id: MetaOapg.properties.collection_id
    sale_status: MetaOapg.properties.sale_status
    game_id: MetaOapg.properties.game_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["game_id"]) -> MetaOapg.properties.game_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collection_id"]) -> MetaOapg.properties.collection_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sale_status"]) -> MetaOapg.properties.sale_status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["game_id", "collection_id", "sale_status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["game_id"]) -> MetaOapg.properties.game_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collection_id"]) -> MetaOapg.properties.collection_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sale_status"]) -> MetaOapg.properties.sale_status: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["game_id", "collection_id", "sale_status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        collection_id: typing.Union[MetaOapg.properties.collection_id, str, ],
        sale_status: typing.Union[MetaOapg.properties.sale_status, dict, frozendict.frozendict, ],
        game_id: typing.Union[MetaOapg.properties.game_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SetSaleStatusInput':
        return super().__new__(
            cls,
            *_args,
            collection_id=collection_id,
            sale_status=sale_status,
            game_id=game_id,
            _configuration=_configuration,
            **kwargs,
        )
