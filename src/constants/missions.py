"""Mission pools for each game mode."""

BATTLE_ROYAL_MISSIONS: tuple[str, ...] = (
    "Get at least 7 kills and 1800 damage with this legend.",
    "Use at least one sniper rifle throughout the match.",
    "Use at least two different shotguns throughout the match.",
    "Use only light ammo weapons.",
    "Use only heavy ammo weapons.",
    "Use only energetic ammo weapons.",
    "Perform 3 executions during the match.",
    "You can kill only performing executions during the match.",
    "Don't use light or heavy ammo weapons throughout the match.",
    "Decrease the field of view in the settings to the minimum (72).",
    "Get at least two kills with a red-tier weapon.",
    "Use the wingman and get at least 1 kill.",
    "Finish the match with at least 2000 damage.",
    "Finsh the match with at least 8 kills.",
    "Craft at least 5 times using the replicator during the match.",
    "Use the first two weapons you come across.",
    "Swap the weapons you're using with those of your opponents (at least one weapon).",
    "Use only shotguns weapons.",
    "Use only shotguns and snipers weapons.",
    "Play without using any sights.",
    "Play with only one weapon.",
    "Use only pistols.",
)

CONTROL_MISSIONS: tuple[str, ...] = (
    "Use the first weapon set.",
    "Use the second weapon set.",
    "Use the third weapon set.",
    "Use the fourth weapon set.",
    "Use the fifth weapon set.",
    "Use only red or gold tier weapons.",
    "Perform 5 executions during the match.",
    "Finish the match with at least 2500 damage.",
    "Finsh the match with at least 15 kills.",
    "Capture at least 4 zones.",
    "You can die a maximum of 8 times during the match.",
)

GUN_RUN_MISSIONS: tuple[str, ...] = (
    "The match can last a maximum of 7 minutes.",
    "You can die a maximum of 4 times during the match.",
    "Finsh the match with at least 9 kills.",
    "Finish the match with at least 2000 damage.",
    "Kill at least 3 opponents with a punch.",
)

TEAM_DEATHMATCH_MISSIONS: tuple[str, ...] = (
    "Use the first weapon set.",
    "Use the second weapon set.",
    "Use the third weapon set.",
    "Use the fourth weapon set.",
    "Use the fifth weapon set.",
    "Use only red or gold tier weapons.",
    "Perform 5 executions during the match.",
    "Finish the match with at least 2500 damage.",
    "Finsh the match with at least 15 kills.",
    "You can die a maximum of 5 times during the match.",
    "The match can last a maximum of 7 minutes.",
)

MISSION_POOLS: dict[str, tuple[str, ...]] = {
    "battle_royal": BATTLE_ROYAL_MISSIONS,
    "gun_run": GUN_RUN_MISSIONS,
    "team_deathmatch": TEAM_DEATHMATCH_MISSIONS,
    "control": CONTROL_MISSIONS,
}
