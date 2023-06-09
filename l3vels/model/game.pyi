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


class Game(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "modified_on",
            "contact_phone",
            "social_links",
            "description",
            "instagram",
            "logo_image",
            "web_link",
            "created_by",
            "url",
            "contact_email",
            "medias",
            "twitter",
            "account_id",
            "discord",
            "created_on",
            "modified_by",
            "name",
            "main_media",
            "id",
            "category",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            description = schemas.StrSchema
            category = schemas.StrSchema
            logo_image = schemas.StrSchema
            
            
            class medias(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'medias':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class social_links(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'social_links':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            main_media = schemas.StrSchema
            url = schemas.StrSchema
            web_link = schemas.StrSchema
            discord = schemas.StrSchema
            twitter = schemas.StrSchema
            instagram = schemas.StrSchema
            contact_phone = schemas.StrSchema
            contact_email = schemas.StrSchema
            status = schemas.StrSchema
            account_id = schemas.StrSchema
            created_on = schemas.DateTimeSchema
            modified_on = schemas.DateTimeSchema
            created_by = schemas.StrSchema
            modified_by = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "description": description,
                "category": category,
                "logo_image": logo_image,
                "medias": medias,
                "social_links": social_links,
                "main_media": main_media,
                "url": url,
                "web_link": web_link,
                "discord": discord,
                "twitter": twitter,
                "instagram": instagram,
                "contact_phone": contact_phone,
                "contact_email": contact_email,
                "status": status,
                "account_id": account_id,
                "created_on": created_on,
                "modified_on": modified_on,
                "created_by": created_by,
                "modified_by": modified_by,
            }
    
    modified_on: MetaOapg.properties.modified_on
    contact_phone: MetaOapg.properties.contact_phone
    social_links: MetaOapg.properties.social_links
    description: MetaOapg.properties.description
    instagram: MetaOapg.properties.instagram
    logo_image: MetaOapg.properties.logo_image
    web_link: MetaOapg.properties.web_link
    created_by: MetaOapg.properties.created_by
    url: MetaOapg.properties.url
    contact_email: MetaOapg.properties.contact_email
    medias: MetaOapg.properties.medias
    twitter: MetaOapg.properties.twitter
    account_id: MetaOapg.properties.account_id
    discord: MetaOapg.properties.discord
    created_on: MetaOapg.properties.created_on
    modified_by: MetaOapg.properties.modified_by
    name: MetaOapg.properties.name
    main_media: MetaOapg.properties.main_media
    id: MetaOapg.properties.id
    category: MetaOapg.properties.category
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo_image"]) -> MetaOapg.properties.logo_image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["medias"]) -> MetaOapg.properties.medias: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["social_links"]) -> MetaOapg.properties.social_links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["main_media"]) -> MetaOapg.properties.main_media: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["web_link"]) -> MetaOapg.properties.web_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["discord"]) -> MetaOapg.properties.discord: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["twitter"]) -> MetaOapg.properties.twitter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instagram"]) -> MetaOapg.properties.instagram: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contact_phone"]) -> MetaOapg.properties.contact_phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contact_email"]) -> MetaOapg.properties.contact_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_on"]) -> MetaOapg.properties.created_on: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modified_on"]) -> MetaOapg.properties.modified_on: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_by"]) -> MetaOapg.properties.created_by: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modified_by"]) -> MetaOapg.properties.modified_by: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "description", "category", "logo_image", "medias", "social_links", "main_media", "url", "web_link", "discord", "twitter", "instagram", "contact_phone", "contact_email", "status", "account_id", "created_on", "modified_on", "created_by", "modified_by", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo_image"]) -> MetaOapg.properties.logo_image: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["medias"]) -> MetaOapg.properties.medias: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["social_links"]) -> MetaOapg.properties.social_links: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["main_media"]) -> MetaOapg.properties.main_media: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["web_link"]) -> MetaOapg.properties.web_link: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["discord"]) -> MetaOapg.properties.discord: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["twitter"]) -> MetaOapg.properties.twitter: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instagram"]) -> MetaOapg.properties.instagram: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contact_phone"]) -> MetaOapg.properties.contact_phone: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contact_email"]) -> MetaOapg.properties.contact_email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_on"]) -> MetaOapg.properties.created_on: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modified_on"]) -> MetaOapg.properties.modified_on: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_by"]) -> MetaOapg.properties.created_by: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modified_by"]) -> MetaOapg.properties.modified_by: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "description", "category", "logo_image", "medias", "social_links", "main_media", "url", "web_link", "discord", "twitter", "instagram", "contact_phone", "contact_email", "status", "account_id", "created_on", "modified_on", "created_by", "modified_by", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        modified_on: typing.Union[MetaOapg.properties.modified_on, str, datetime, ],
        contact_phone: typing.Union[MetaOapg.properties.contact_phone, str, ],
        social_links: typing.Union[MetaOapg.properties.social_links, list, tuple, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        instagram: typing.Union[MetaOapg.properties.instagram, str, ],
        logo_image: typing.Union[MetaOapg.properties.logo_image, str, ],
        web_link: typing.Union[MetaOapg.properties.web_link, str, ],
        created_by: typing.Union[MetaOapg.properties.created_by, str, ],
        url: typing.Union[MetaOapg.properties.url, str, ],
        contact_email: typing.Union[MetaOapg.properties.contact_email, str, ],
        medias: typing.Union[MetaOapg.properties.medias, list, tuple, ],
        twitter: typing.Union[MetaOapg.properties.twitter, str, ],
        account_id: typing.Union[MetaOapg.properties.account_id, str, ],
        discord: typing.Union[MetaOapg.properties.discord, str, ],
        created_on: typing.Union[MetaOapg.properties.created_on, str, datetime, ],
        modified_by: typing.Union[MetaOapg.properties.modified_by, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        main_media: typing.Union[MetaOapg.properties.main_media, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        category: typing.Union[MetaOapg.properties.category, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Game':
        return super().__new__(
            cls,
            *_args,
            modified_on=modified_on,
            contact_phone=contact_phone,
            social_links=social_links,
            description=description,
            instagram=instagram,
            logo_image=logo_image,
            web_link=web_link,
            created_by=created_by,
            url=url,
            contact_email=contact_email,
            medias=medias,
            twitter=twitter,
            account_id=account_id,
            discord=discord,
            created_on=created_on,
            modified_by=modified_by,
            name=name,
            main_media=main_media,
            id=id,
            category=category,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )
