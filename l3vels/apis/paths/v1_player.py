from l3vels.paths.v1_player.get import ApiForget
from l3vels.paths.v1_player.put import ApiForput
from l3vels.paths.v1_player.post import ApiForpost
from l3vels.paths.v1_player.delete import ApiFordelete


class V1Player(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
