# coding: utf-8

"""
    L3vels Api

    L3vels API for Game developers  # noqa: E501

    The version of the OpenAPI document: 0.3
    Contact: support@l3vels.xyz
    Generated by: https://openapi-generator.tech
"""

from l3vels.paths.v1_game.post import CreateGame
from l3vels.paths.v1_game.get import GameControllerGetGames
from l3vels.paths.v1_game_game_id.get import GetGameById


class GameApi(
    CreateGame,
    GameControllerGetGames,
    GetGameById,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
