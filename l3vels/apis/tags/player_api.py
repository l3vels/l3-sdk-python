# coding: utf-8

"""
    L3vels Api

    L3vels API for Game developers  # noqa: E501

    The version of the OpenAPI document: 0.3
    Contact: support@l3vels.xyz
    Generated by: https://openapi-generator.tech
"""

from l3vels.paths.v1_player_asset_project_id_id.get import PlayerAssetControllerPlayerAssetById
from l3vels.paths.v1_player_asset.get import PlayerAssetControllerPlayerAssets
from l3vels.paths.v1_player.post import PlayerControllerCreatePlayer
from l3vels.paths.v1_player.delete import PlayerControllerDeletePlayer
from l3vels.paths.v1_player.get import PlayerControllerGetPlayers
from l3vels.paths.v1_player_project_id_id.get import PlayerControllerPlayerById
from l3vels.paths.v1_player_count_project_id.get import PlayerControllerPlayersCountByGameId
from l3vels.paths.v1_player.put import PlayerControllerUpdatePlayer


class PlayerApi(
    PlayerAssetControllerPlayerAssetById,
    PlayerAssetControllerPlayerAssets,
    PlayerControllerCreatePlayer,
    PlayerControllerDeletePlayer,
    PlayerControllerGetPlayers,
    PlayerControllerPlayerById,
    PlayerControllerPlayersCountByGameId,
    PlayerControllerUpdatePlayer,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
