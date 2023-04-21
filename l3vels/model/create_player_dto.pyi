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


class CreatePlayerDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "project_id",
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            project_id = schemas.StrSchema
            unique_id = schemas.StrSchema
            username = schemas.StrSchema
            email = schemas.StrSchema
            avatar = schemas.StrSchema
            is_create_wallet = schemas.BoolSchema
            
            
            class custom_props(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'custom_props':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "project_id": project_id,
                "unique_id": unique_id,
                "username": username,
                "email": email,
                "avatar": avatar,
                "is_create_wallet": is_create_wallet,
                "custom_props": custom_props,
            }
    
    project_id: MetaOapg.properties.project_id
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project_id"]) -> MetaOapg.properties.project_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unique_id"]) -> MetaOapg.properties.unique_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["avatar"]) -> MetaOapg.properties.avatar: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_create_wallet"]) -> MetaOapg.properties.is_create_wallet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_props"]) -> MetaOapg.properties.custom_props: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "project_id", "unique_id", "username", "email", "avatar", "is_create_wallet", "custom_props", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project_id"]) -> MetaOapg.properties.project_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unique_id"]) -> typing.Union[MetaOapg.properties.unique_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["avatar"]) -> typing.Union[MetaOapg.properties.avatar, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_create_wallet"]) -> typing.Union[MetaOapg.properties.is_create_wallet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_props"]) -> typing.Union[MetaOapg.properties.custom_props, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "project_id", "unique_id", "username", "email", "avatar", "is_create_wallet", "custom_props", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        project_id: typing.Union[MetaOapg.properties.project_id, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        unique_id: typing.Union[MetaOapg.properties.unique_id, str, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        avatar: typing.Union[MetaOapg.properties.avatar, str, schemas.Unset] = schemas.unset,
        is_create_wallet: typing.Union[MetaOapg.properties.is_create_wallet, bool, schemas.Unset] = schemas.unset,
        custom_props: typing.Union[MetaOapg.properties.custom_props, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreatePlayerDto':
        return super().__new__(
            cls,
            *_args,
            project_id=project_id,
            name=name,
            unique_id=unique_id,
            username=username,
            email=email,
            avatar=avatar,
            is_create_wallet=is_create_wallet,
            custom_props=custom_props,
            _configuration=_configuration,
            **kwargs,
        )
