import random

from src.backend.randomizer import (
    add_character,
    sample_mission,
    sample_two_distinct,
    sample_weapon_group,
)
from src.constants.characters import DEFAULT_CHARACTERS
from src.constants.missions import MISSION_POOLS


def test_axle_is_available_by_default() -> None:
    assert "Axle" in DEFAULT_CHARACTERS


def test_add_character_appends_enabled_character() -> None:
    characters = [{"name": "Wraith", "enabled": True}]

    success, message = add_character(characters, "  Axle  ")

    assert success is True
    assert message == "Axle aggiunto alla lista."
    assert characters[-1] == {"name": "Axle", "enabled": True}


def test_add_character_rejects_duplicate_case_insensitive() -> None:
    characters = [{"name": "Axle", "enabled": True}]

    success, message = add_character(characters, "axle")

    assert success is False
    assert message == "axle e gia presente."
    assert characters == [{"name": "Axle", "enabled": True}]


def test_sample_two_distinct_returns_two_different_names() -> None:
    first, second = sample_two_distinct(["A", "B", "C"], rng=random.Random(1))

    assert first in {"A", "B", "C"}
    assert second in {"A", "B", "C"}
    assert first != second


def test_weapon_group_is_between_one_and_five() -> None:
    rng = random.Random(7)

    values = [sample_weapon_group(rng) for _ in range(50)]

    assert all(1 <= value <= 5 for value in values)


def test_sample_mission_returns_value_from_pool() -> None:
    missions = ("one", "two", "three")

    mission = sample_mission(missions, rng=random.Random(2))

    assert mission in missions


def test_all_mission_pools_are_available() -> None:
    assert set(MISSION_POOLS) == {"battle_royal", "gun_run", "team_deathmatch", "control"}
    assert all(MISSION_POOLS.values())
