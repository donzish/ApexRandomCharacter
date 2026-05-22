"""Random extraction helpers for legends and weapon groups."""

from __future__ import annotations

import random
from collections.abc import Sequence

MIN_WEAPON_GROUP = 1
MAX_WEAPON_GROUP = 5


def normalize_character_name(name: str) -> str:
    """Return a display-safe character name with repeated whitespace collapsed."""
    return " ".join(name.strip().split())


def character_exists(characters: Sequence[dict[str, object]], name: str) -> bool:
    """Return True when a character already exists, ignoring case."""
    normalized_name = normalize_character_name(name).casefold()
    return any(str(character["name"]).casefold() == normalized_name for character in characters)


def add_character(characters: list[dict[str, object]], name: str) -> tuple[bool, str]:
    """Add a character to the list when valid and not duplicated.

    Returns a tuple with the operation result and a user-facing message.
    """
    normalized_name = normalize_character_name(name)
    if not normalized_name:
        return False, "Inserisci un nome valido."

    if character_exists(characters, normalized_name):
        return False, f"{normalized_name} e gia presente."

    characters.append({"name": normalized_name, "enabled": True})
    return True, f"{normalized_name} aggiunto alla lista."


def enabled_character_names(characters: Sequence[dict[str, object]]) -> list[str]:
    """Return enabled character names preserving the current list order."""
    return [str(character["name"]) for character in characters if character.get("enabled")]


def sample_two_distinct(
    pool: Sequence[str],
    avoid: Sequence[str] | None = None,
    rng: random.Random | None = None,
) -> tuple[str | None, str | None]:
    """Extract two distinct names from a pool, excluding optional names."""
    random_source = rng or random
    excluded = set(avoid or [])
    available = [name for name in pool if name not in excluded]

    if len(available) < 2:
        return None, None

    first = random_source.choice(available)
    second_pool = [name for name in available if name != first]
    second = random_source.choice(second_pool)
    return first, second


def sample_one(
    pool: Sequence[str],
    avoid: Sequence[str] | None = None,
    rng: random.Random | None = None,
) -> str | None:
    """Extract one name from a pool, excluding optional names."""
    random_source = rng or random
    excluded = set(avoid or [])
    available = [name for name in pool if name not in excluded]

    if not available:
        return None

    return random_source.choice(available)


def sample_weapon_group(rng: random.Random | None = None) -> int:
    """Extract a weapon group number in the supported range."""
    random_source = rng or random
    return random_source.randint(MIN_WEAPON_GROUP, MAX_WEAPON_GROUP)


def sample_mission(missions: Sequence[str], rng: random.Random | None = None) -> str | None:
    """Extract a mission from a non-empty mission pool."""
    if not missions:
        return None

    random_source = rng or random
    return random_source.choice(list(missions))
