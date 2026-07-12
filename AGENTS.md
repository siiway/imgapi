# Agent Notes

This repository is a small FastAPI service that returns random image redirects. Read [CONTRIBUTING.md](./CONTRIBUTING.md) for setup, validation commands, source-plugin rules, and documentation expectations.

## Project Shape

- `main.py` defines the FastAPI app, routes, OpenAPI customization, fallback routing, and the `VERSION` string.
- `imgapi.py` defines the `ImageAPI` source plugin interface and loads enabled `sites/*.py` files at startup.
- `config.py` defines `config.yaml` parsing with Pydantic models. `config.yaml` is local and ignored by git.
- `utils.py` contains shared helpers for paths, UA parsing, timing, and sync/async callable dispatch.
- `sites.md` is the human-facing catalog for image sources. Keep it in sync when adding, replacing, disabling, or changing a source.
- `sites/*.py` files are enabled source plugins. `sites/*.py.disabled` files are intentionally disabled and are not imported.

## Agent Workflow

- Do not stage or commit unless the user explicitly asks.
- Keep changes minimal and aligned with existing patterns; source plugins should usually be a single small `ImageAPI(...)` declaration.
- Preserve ignored local files such as `config.yaml`, logs, caches, virtualenvs, and generated `__pycache__` files.
- When changing sources, verify external behavior with `curl` where practical, use image redirect URLs in code, and document JSON formats in `sites.md` only when they are not used by runtime code.
- When changing runtime behavior, consider whether `main.py`'s `VERSION` should be bumped.
- Prefer running targeted checks first, then `prek run --all-files` before handoff when practical.

## Validation

Primary checks are defined in `prek.toml`:

```bash
prek run --all-files
```

Useful direct checks:

```bash
ruff check .
ruff format --check .
ty check .
```
