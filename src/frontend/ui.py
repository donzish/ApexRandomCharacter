"""Streamlit layout and components."""

from __future__ import annotations

import streamlit as st

from src.frontend.state import (
    ADD_MESSAGE_KEY,
    LEGENDS_KEY,
    LOCK_A_KEY,
    LOCK_B_KEY,
    MISSION_RESULT_KEYS,
    NEW_LEGEND_KEY,
    PICK_A_KEY,
    PICK_B_KEY,
    WEAPON_GROUP_KEY,
    character_checkbox_key,
    get_enabled_names,
    handle_add_character,
    initialize_session_state,
    randomize_duo,
    randomize_mission,
    randomize_weapon_group,
    remove_disabled_characters,
    reroll_slot,
    select_all_characters,
)
from src.frontend.styles import APP_CSS


def render_app() -> None:
    """Render the complete Streamlit application."""
    st.set_page_config(page_title="Apex Legends Duo Picker", page_icon="🎯", layout="wide")
    initialize_session_state()
    st.markdown(APP_CSS, unsafe_allow_html=True)

    render_sidebar()
    render_header()
    render_controls()
    render_results()
    render_weapon_group()
    render_missions()


def render_header() -> None:
    """Render the page header."""
    st.markdown(
        """
        <div class="app-hero">
            <div class="app-kicker">Apex Legends</div>
            <h1>Duo Random Picker</h1>
            <p>
                Scegli le leggende disponibili, blocca gli slot che vuoi mantenere
                e rilancia il duo quando serve.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar() -> None:
    """Render character selection and list management."""
    with st.sidebar:
        st.header("Leggende")
        st.caption("Gestisci la lista e scegli quali personaggi includere nell'estrazione.")

        col_on, col_off = st.columns(2)
        col_on.button(
            "Seleziona tutto",
            on_click=select_all_characters,
            args=(True,),
            use_container_width=True,
        )
        col_off.button(
            "Deseleziona tutto",
            on_click=select_all_characters,
            args=(False,),
            use_container_width=True,
        )

        enabled_count = len(get_enabled_names())
        total_count = len(st.session_state[LEGENDS_KEY])
        st.progress(enabled_count / total_count if total_count else 0)
        st.caption(f"{enabled_count} di {total_count} leggende abilitate")

        st.divider()
        for index, character in enumerate(st.session_state[LEGENDS_KEY]):
            character["enabled"] = st.checkbox(
                str(character["name"]),
                value=bool(character["enabled"]),
                key=character_checkbox_key(character, index),
            )

        st.divider()
        st.text_input("Aggiungi personaggio", key=NEW_LEGEND_KEY, placeholder="Es. Axle")
        st.button("Aggiungi", on_click=handle_add_character, use_container_width=True)

        message = st.session_state[ADD_MESSAGE_KEY]
        if message:
            if message["success"]:
                st.success(message["text"])
            else:
                st.warning(message["text"])

        st.button(
            "Rimuovi disabilitate",
            on_click=remove_disabled_characters,
            use_container_width=True,
        )


def render_controls() -> None:
    """Render duo randomization controls."""
    st.markdown('<div class="section-label">Estrazione duo</div>', unsafe_allow_html=True)
    col_random, col_reroll_a, col_reroll_b, col_lock_a, col_lock_b = st.columns(
        [2.2, 1, 1, 1, 1]
    )

    col_random.button(
        "🎲 Randomizza duo",
        on_click=randomize_duo,
        use_container_width=True,
        type="primary",
    )
    col_reroll_a.button("Reroll 1°", on_click=reroll_slot, args=("a",), use_container_width=True)
    col_reroll_b.button("Reroll 2°", on_click=reroll_slot, args=("b",), use_container_width=True)

    st.session_state[LOCK_A_KEY] = col_lock_a.toggle(
        "Blocca 1°",
        value=st.session_state[LOCK_A_KEY],
    )
    st.session_state[LOCK_B_KEY] = col_lock_b.toggle(
        "Blocca 2°",
        value=st.session_state[LOCK_B_KEY],
    )


def render_results() -> None:
    """Render selected legends."""
    col_a, col_b = st.columns(2, gap="large")
    with col_a:
        render_result_card(
            "1° leggenda",
            st.session_state[PICK_A_KEY],
            st.session_state[LOCK_A_KEY],
        )
    with col_b:
        render_result_card(
            "2° leggenda",
            st.session_state[PICK_B_KEY],
            st.session_state[LOCK_B_KEY],
        )


def render_weapon_group() -> None:
    """Render the weapon group extraction section."""
    st.markdown('<div class="section-label">Gruppo di armi</div>', unsafe_allow_html=True)
    col_value, col_action = st.columns([2, 1])

    with col_value:
        render_result_card(
            "Gruppo estratto",
            st.session_state[WEAPON_GROUP_KEY],
            False,
            extra_class="weapon-card",
        )

    with col_action:
        st.write("")
        st.write("")
        st.button(
            "Estrai gruppo",
            on_click=randomize_weapon_group,
            use_container_width=True,
            type="primary",
        )
        st.caption("Il valore resta stabile finche non estrai di nuovo.")


def render_missions() -> None:
    """Render mission extraction cards for each game mode."""
    st.markdown('<div class="section-label">Missioni modalita</div>', unsafe_allow_html=True)
    first_row = st.columns(2, gap="large")
    second_row = st.columns(2, gap="large")

    mission_cards = (
        ("Battle Royal", "battle_royal"),
        ("Gun Run", "gun_run"),
        ("Team Deathmatch", "team_deathmatch"),
        ("Control", "control"),
    )

    for column, (title, mode_key) in zip([*first_row, *second_row], mission_cards, strict=True):
        with column:
            render_mission_card(title, mode_key)


def render_mission_card(title: str, mode_key: str) -> None:
    """Render one game-mode mission card."""
    render_result_card(
        title,
        st.session_state[MISSION_RESULT_KEYS[mode_key]],
        False,
        extra_class="mission-card",
    )
    st.button(
        f"Estrai {title}",
        on_click=randomize_mission,
        args=(mode_key,),
        use_container_width=True,
    )


def render_result_card(
    title: str,
    value: object | None,
    locked: bool,
    extra_class: str = "",
) -> None:
    """Render a compact result card."""
    badge = "BLOCCATO" if locked else "ATTIVO"
    display_value = (
        value if value is not None else '<span class="result-card__empty">Nessun risultato</span>'
    )

    st.markdown(
        f"""
        <div class="result-card {extra_class}">
            <div class="result-card__top">
                <span>{title}</span>
                <span class="result-card__badge">{badge}</span>
            </div>
            <div class="result-card__value">{display_value}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
