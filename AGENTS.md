# AGENTS.md

## Project context
This is a public Python Streamlit application.

## Git workflow
- Work directly on the local `main` branch.
- Do not create feature branches.
- Do not create pull requests.
- Before editing, run `git status` and ensure the working tree is clean.
- Pull the latest changes from `origin/main` before starting.
- Do not push until the user has manually reviewed the local demo.
- Commit directly to `main` only after tests and user approval.
- Push directly to `origin/main` only after explicit user approval.
- Never commit secrets, tokens, `.env`, credentials, `.streamlit/secrets.toml`, private files, or local-only configuration.

## Architecture expectations
Keep the repository well structured.

Preferred structure:
- `app.py` as the lightweight Streamlit entry point.
- `src/frontend/` for UI layout, components, styling, and Streamlit components.
- `src/backend/` for business logic and application services.
- `src/constants/` for constants such as available characters.
- `src/utils/` for reusable helpers.
- `tests/` for automated tests.

Avoid putting business logic inside `app.py`.

## Coding standards
- Use clear, simple Python.
- Use type hints where useful.
- Add docstrings to public functions and non-trivial helpers.
- Keep functions small and focused.
- Use clear variable and function names.
- Separate Streamlit UI code from testable backend logic.
- Avoid unnecessary dependencies.
- Prefer Streamlit-native components before adding third-party UI libraries.

## Streamlit rules
- Use `st.session_state` consistently.
- Initialize session state in a dedicated helper.
- Avoid accidental state resets on rerun.
- Button actions should update session state predictably.
- Random results should remain stable after extraction until the user clicks again.

## Required features
Implement these changes:
1. Improve the frontend so it looks polished and professionally designed.
2. Fix backend/button bugs, especially character addition.
3. Add a new available character named `Axle`.
4. Add a section called `Gruppo di armi`.
5. The `Gruppo di armi` section must randomly extract an integer from 1 to 5.
6. The extracted number must remain visible and stable until the user extracts again.

## Testing
Before considering the task complete:
- Run `python -m pytest` if tests exist.
- Add minimal tests for backend logic where possible.
- Run `ruff check .` if Ruff is configured.
- Start the Streamlit app locally.
- Provide the local demo URL to the user.
- Wait for explicit user approval before committing and pushing.

## Documentation
- Update `README.md` if the project structure, run commands, or behavior changes.
- Document important functions with docstrings.
- Keep comments useful and not redundant.

## Done means
The task is done only when:
- the app starts locally;
- the user has seen the local demo;
- tests pass or any missing tests are clearly explained;
- no secrets are staged;
- the user explicitly approves commit and push to `origin/main`.