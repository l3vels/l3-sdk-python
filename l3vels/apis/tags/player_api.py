# coding: utf-8

"""
    L3vels Api

    L3vels API for Game developers  # noqa: E501

    The version of the OpenAPI document: 0.3
    Contact: support@l3vels.xyz
    Generated by: https://openapi-generator.tech
"""

from l3vels.paths.v1_player_count_game_id.get import CountPlayersByGameId
from l3vels.paths.v1_player.post import CreatePlayer
from l3vels.paths.v1_player_asset_game_id_id.get import GetPlayerAssetById
from l3vels.paths.v1_player_game_id_id.get import GetPlayerById
from l3vels.paths.v1_player.get import GetPlayers
from l3vels.paths.v1_player_asset.get import PlayerAssets
from l3vels.paths.v1_player.put import UpdatePlayer


class PlayerApi(
    CountPlayersByGameId,
    CreatePlayer,
    GetPlayerAssetById,
    GetPlayerById,
    GetPlayers,
    PlayerAssets,
    UpdatePlayer,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
