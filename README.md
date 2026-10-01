# Study software

Outils en ligne de commande pour préparer les oraux du CUEC. Voir `CLAUDE.md`
pour le contexte et les décisions.

## Installation

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e '.[dev]'
cp .env.example .env   # puis renseigner ANTHROPIC_API_KEY
```

Les PDF de cours vont dans `pdfs/` (ignoré par git).

## Simulateur d'oral

```bash
oral --list                                # chapitres disponibles
oral --chapitre reduction --dry-run        # affiche le prompt examinateur, sans appel payant
```

Options : `--model` (défaut `claude-sonnet-5-5`), `--effort low|medium|high`
(défaut `medium`).

## Tests

```bash
pytest
```
