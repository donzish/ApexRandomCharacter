import random
import streamlit as st

st.set_page_config(page_title="Apex Legends – Duo Random Picker", page_icon="🎯", layout="centered")

# Lista predefinita (include Sparrow e Random_Choose)
DEFAULT_LEGENDS = [
    "Bloodhound","Gibraltar","Lifeline","Pathfinder","Wraith","Bangalore","Caustic","Mirage","Octane",
    "Wattson","Crypto","Revenant","Loba","Rampart","Horizon","Fuse","Valkyrie","Seer","Ash","Mad Maggie",
    "Newcastle","Vantage","Catalyst","Ballistic","Conduit","Alter","Sparrow","Random_Choose",
]

# Stato iniziale
if "legends" not in st.session_state:
    st.session_state.legends = [{"name": n, "enabled": True} for n in DEFAULT_LEGENDS]
if "pickA" not in st.session_state: st.session_state.pickA = None
if "pickB" not in st.session_state: st.session_state.pickB = None
if "lockA" not in st.session_state: st.session_state.lockA = False
if "lockB" not in st.session_state: st.session_state.lockB = False
if "newLegend" not in st.session_state: st.session_state.newLegend = ""

def enabled_names():
    return [l["name"] for l in st.session_state.legends if l["enabled"]]

def sample_two_distinct(pool, avoid=None):
    avoid = set(avoid or [])
    pool2 = [x for x in pool if x not in avoid]
    if len(pool2) < 2:
        return None, None
    a = random.choice(pool2)
    pool3 = [x for x in pool2 if x != a]
    b = random.choice(pool3)
    return a, b

st.title("Apex Legends – Duo Random Picker")
st.caption("Seleziona le Leggende, poi premi **Randomizza (2)**. Puoi bloccare uno slot e rifare l'altro.")

# --- Sidebar: gestione lista ---
with st.sidebar:
    st.subheader("Lista Leggende")
    # toggle globale
    col_on, col_off = st.columns(2)
    if col_on.button("Seleziona tutto"):
        for l in st.session_state.legends: l["enabled"] = True
    if col_off.button("Deseleziona tutto"):
        for l in st.session_state.legends: l["enabled"] = False

    st.write(f"**Abilitate**: {len(enabled_names())}/{len(st.session_state.legends)}")

    # Griglia abilitazioni
    for i, l in enumerate(st.session_state.legends):
        st.session_state.legends[i]["enabled"] = st.checkbox(
            l["name"], value=l["enabled"], key=f"en_{l['name']}"
        )

    st.divider()
    st.text_input("Aggiungi nuova leggenda", key="newLegend", placeholder="Nome leggenda…")
    cols = st.columns([1,1])
    if cols[0].button("Aggiungi"):
        name = st.session_state.newLegend.strip()
        if name and name.lower() not in [x["name"].lower() for x in st.session_state.legends]:
            st.session_state.legends.append({"name": name, "enabled": True})
        st.session_state.newLegend = ""
    if cols[1].button("Rimuovi selezionate (disabilitate)"):
        st.session_state.legends = [l for l in st.session_state.legends if l["enabled"]]

# --- Pannello controlli ---
c1, c2, c3, c4, c5 = st.columns([2,1,1,1,1])
if c1.button("🎲 Randomizza (2)", use_container_width=True):
    pool = enabled_names()
    if st.session_state.lockA and st.session_state.lockB:
        pass
    elif st.session_state.lockA and st.session_state.pickA:
        pool2 = [n for n in pool if n != st.session_state.pickA]
        if len(pool2) >= 1: st.session_state.pickB = random.choice(pool2)
    elif st.session_state.lockB and st.session_state.pickB:
        pool2 = [n for n in pool if n != st.session_state.pickB]
        if len(pool2) >= 1: st.session_state.pickA = random.choice(pool2)
    else:
        a, b = sample_two_distinct(pool)
        st.session_state.pickA, st.session_state.pickB = a, b

if c2.button("Reroll 1°"):
    if not st.session_state.lockA:
        pool = [n for n in enabled_names() if n != st.session_state.pickB]
        if pool: st.session_state.pickA = random.choice(pool)

if c3.button("Reroll 2°"):
    if not st.session_state.lockB:
        pool = [n for n in enabled_names() if n != st.session_state.pickA]
        if pool: st.session_state.pickB = random.choice(pool)

st.session_state.lockA = c4.toggle("Blocca 1°", value=st.session_state.lockA)
st.session_state.lockB = c5.toggle("Blocca 2°", value=st.session_state.lockB)

st.divider()

# --- Visualizzazione risultati ---
colA, colB = st.columns(2, gap="large")
def card(title, value, locked):
    bg = "#0b1220"
    badge = "LOCK" if locked else "FREE"
    st.markdown(f"""
<div style="padding:16px;border-radius:16px;background:{bg};border:1px solid #1f2937;">
  <div style="display:flex;justify-content:space-between;align-items:center;font-size:12px;opacity:.7;letter-spacing:.15em;text-transform:uppercase;">
    <span>{title}</span><span style="padding:2px 8px;border-radius:999px;background:#1f2937;font-size:10px;">{badge}</span>
  </div>
  <div style="margin-top:8px;font-size:28px;font-weight:800;min-height:2.2em;">
    {value if value else "<span style='opacity:.5'>— nessuna —</span>"}
  </div>
</div>
""", unsafe_allow_html=True)

with colA: card("1°", st.session_state.pickA, st.session_state.lockA)
with colB: card("2°", st.session_state.pickB, st.session_state.lockB)

st.caption("Nota: le modifiche alla lista restano finché la pagina rimane aperta (sessione corrente).")
