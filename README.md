# Apex Legends - Duo Random Picker (Streamlit)

App Streamlit per estrarre due Leggende di Apex Legends, gestire la lista dei
personaggi disponibili, sorteggiare un `Gruppo di armi` da 1 a 5 e scegliere
missioni casuali per Battle Royal, Gun Run, Team Deathmatch e Control.

## Avvio locale

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Sviluppo

```bash
pip install -r requirements-dev.txt
python -m pytest
ruff check .
```

## Struttura

- `app.py`: entry point Streamlit.
- `src/frontend/`: layout, componenti, stili e gestione session state.
- `src/backend/`: logica testabile di randomizzazione e gestione personaggi.
- `src/constants/`: costanti statiche, inclusa la lista personaggi.
- `tests/`: test automatici della logica backend.
