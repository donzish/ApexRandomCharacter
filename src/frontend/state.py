"""Session-state helpers for the Streamlit interface."""

from __future__ import annotations

from typing import Any

import streamlit as st

from src.backend.randomizer import (
    add_character,
    enabled_character_names,
    sample_mission,
    sample_one,
    sample_two_distinct,
    sample_weapon_group,
)
from src.constants.characters import DEFAULT_CHARACTERS
from src.constants.missions import MISSION_POOLS

LEGENDS_KEY = "legends"
PICK_A_KEY = "pick_a"
PICK_B_KEY = "pick_b"
LOCK_A_KEY = "lock_a"
LOCK_B_KEY = "lock_b"
NEW_LEGEND_KEY = "new_legend"
ADD_MESSAGE_KEY = "add_message"
WEAPON_GROUP_KEY = "weapon_group"
MISSION_RESULT_KEYS: dict[str, str] = {
    "battle_royal": "battle_royal_mission",
    "gun_run": "gun_run_mission",
    "team_deathmatch": "team_deathmatch_mission",
    "control": "control_mission",
}


def initialize_session_state() -> None:
    """Initialize all keys used by the app without resetting existing values."""
    defaults: dict[str, Any] = {
        LEGENDS_KEY: [{"name": name, "enabled": True} for name in DEFAULT_CHARACTERS],
        PICK_A_KEY: None,
        PICK_B_KEY: None,
        LOCK_A_KEY: False,
        LOCK_B_KEY: False,
        NEW_LEGEND_KEY: "",
        ADD_MESSAGE_KEY: None,
        WEAPON_GROUP_KEY: None,
        **{state_key: None for state_key in MISSION_RESULT_KEYS.values()},
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def get_enabled_names() -> list[str]:
    """Return the enabled names from Streamlit session state."""
    return enabled_character_names(st.session_state[LEGENDS_KEY])


def character_checkbox_key(character: dict[str, object], index: int) -> str:
    """Return the stable widget key for a character checkbox."""
    return f"character_enabled_{character['name']}_{index}"


def select_all_characters(enabled: bool) -> None:
    """Enable or disable every character in session state."""
    for index, character in enumerate(st.session_state[LEGENDS_KEY]):
        character["enabled"] = enabled
        st.session_state[character_checkbox_key(character, index)] = enabled


def remove_disabled_characters() -> None:
    """Remove characters currently disabled in session state."""
    st.session_state[LEGENDS_KEY] = [
        character for character in st.session_state[LEGENDS_KEY] if character.get("enabled")
    ]


def handle_add_character() -> None:
    """Add the character from the text input and clear the input safely."""
    success, message = add_character(
        st.session_state[LEGENDS_KEY],
        st.session_state[NEW_LEGEND_KEY],
    )
    st.session_state[ADD_MESSAGE_KEY] = {"success": success, "text": message}
    st.session_state[NEW_LEGEND_KEY] = ""


def randomize_duo() -> None:
    """Randomize the duo while respecting locked slots."""
    pool = get_enabled_names()
    pick_a = st.session_state[PICK_A_KEY]
    pick_b = st.session_state[PICK_B_KEY]
    lock_a = st.session_state[LOCK_A_KEY]
    lock_b = st.session_state[LOCK_B_KEY]

    if lock_a and lock_b:
        return

    if lock_a and pick_a:
        st.session_state[PICK_B_KEY] = sample_one(pool, avoid=[pick_a])
        return

    if lock_b and pick_b:
        st.session_state[PICK_A_KEY] = sample_one(pool, avoid=[pick_b])
        return

    st.session_state[PICK_A_KEY], st.session_state[PICK_B_KEY] = sample_two_distinct(pool)


def reroll_slot(slot: str) -> None:
    """Reroll one duo slot unless it is locked."""
    if slot == "a":
        if st.session_state[LOCK_A_KEY]:
            return
        st.session_state[PICK_A_KEY] = sample_one(
            get_enabled_names(),
            avoid=[st.session_state[PICK_B_KEY]],
        )
        return

    if st.session_state[LOCK_B_KEY]:
        return
    st.session_state[PICK_B_KEY] = sample_one(
        get_enabled_names(),
        avoid=[st.session_state[PICK_A_KEY]],
    )


def randomize_weapon_group() -> None:
    """Extract and store a stable weapon group number."""
    st.session_state[WEAPON_GROUP_KEY] = sample_weapon_group()


def randomize_mission(mode_key: str) -> None:
    """Extract and store a stable mission for the requested mode."""
    st.session_state[MISSION_RESULT_KEYS[mode_key]] = sample_mission(MISSION_POOLS[mode_key])
