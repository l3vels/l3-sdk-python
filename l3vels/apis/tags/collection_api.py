# coding: utf-8

"""
    L3vels Api

    L3vels API for Game developers  # noqa: E501

    The version of the OpenAPI document: 0.3
    Contact: support@l3vels.xyz
    Generated by: https://openapi-generator.tech
"""

from l3vels.paths.v1_collection.post import CollectionControllerCreateCollection
from l3vels.paths.v1_collection_count_game_id.get import CountCollectionsByGameId
from l3vels.paths.v1_collection_game_id_id.get import GetCollectionById
from l3vels.paths.v1_collection.get import GetCollections


class CollectionApi(
    CollectionControllerCreateCollection,
    CountCollectionsByGameId,
    GetCollectionById,
    GetCollections,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
