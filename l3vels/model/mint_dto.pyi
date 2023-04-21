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


class MintDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "collection_id",
            "project_id",
            "asset",
        }
        
        class properties:
            project_id = schemas.StrSchema
            collection_id = schemas.StrSchema
            
            
            class asset(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            TokenDto,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'asset':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            contract_id = schemas.StrSchema
            player_address = schemas.StrSchema
            player_id = schemas.StrSchema
            __annotations__ = {
                "project_id": project_id,
                "collection_id": collection_id,
                "asset": asset,
                "contract_id": contract_id,
                "player_address": player_address,
                "player_id": player_id,
            }
    
    collection_id: MetaOapg.properties.collection_id
    project_id: MetaOapg.properties.project_id
    asset: MetaOapg.properties.asset
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project_id"]) -> MetaOapg.properties.project_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collection_id"]) -> MetaOapg.properties.collection_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["asset"]) -> MetaOapg.properties.asset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contract_id"]) -> MetaOapg.properties.contract_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["player_address"]) -> MetaOapg.properties.player_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["player_id"]) -> MetaOapg.properties.player_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["project_id", "collection_id", "asset", "contract_id", "player_address", "player_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project_id"]) -> MetaOapg.properties.project_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collection_id"]) -> MetaOapg.properties.collection_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["asset"]) -> MetaOapg.properties.asset: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contract_id"]) -> typing.Union[MetaOapg.properties.contract_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["player_address"]) -> typing.Union[MetaOapg.properties.player_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["player_id"]) -> typing.Union[MetaOapg.properties.player_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["project_id", "collection_id", "asset", "contract_id", "player_address", "player_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        collection_id: typing.Union[MetaOapg.properties.collection_id, str, ],
        project_id: typing.Union[MetaOapg.properties.project_id, str, ],
        asset: typing.Union[MetaOapg.properties.asset, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        contract_id: typing.Union[MetaOapg.properties.contract_id, str, schemas.Unset] = schemas.unset,
        player_address: typing.Union[MetaOapg.properties.player_address, str, schemas.Unset] = schemas.unset,
        player_id: typing.Union[MetaOapg.properties.player_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MintDto':
        return super().__new__(
            cls,
            *_args,
            collection_id=collection_id,
            project_id=project_id,
            asset=asset,
            contract_id=contract_id,
            player_address=player_address,
            player_id=player_id,
            _configuration=_configuration,
            **kwargs,
        )

from l3vels.model.token_dto import TokenDto
