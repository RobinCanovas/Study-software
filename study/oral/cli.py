"""Command-line entry point for the oral simulator.

Milestone 1, steps 1-2: only --list and --dry-run work. The exercise
generation and the dialogue loop come next.
"""

import argparse
import sys

from study.llm import DEFAULT_MODEL, EFFORTS, PRICES, has_api_key, make_client
from study.oral.chapters import CHAPTERS
from study.oral.prompts import Exercise, examiner_system

# Stands in for the generated exercise so --dry-run can show the full prompt.
PLACEHOLDER_EXERCISE = Exercise(
    statement="<énoncé généré par le modèle>",
    steps=("<étape 1>", "<étape 2>", "<étape 3>"),
    hypotheses=("<hypothèse 1>", "<hypothèse 2>"),
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(prog="oral", description="Simulateur d'oral (CUEC).")
    p.add_argument("--chapitre", choices=sorted(CHAPTERS), help="chapitre de l'exercice")
    p.add_argument("--list", action="store_true", help="lister les chapitres disponibles")
    p.add_argument("--model", choices=sorted(PRICES), default=DEFAULT_MODEL)
    p.add_argument("--effort", choices=EFFORTS, default="medium",
                   help="profondeur de réflexion du modèle (coût en tokens de sortie)")
    p.add_argument("--dry-run", action="store_true",
                   help="afficher le prompt système et sa taille, sans appel payant")
    return p.parse_args(argv)


def count_tokens(model: str, system: str) -> int | None:
    """Exact prompt size via the token-counting endpoint (free of charge).

    Returns None when no API key is configured.
    """
    if not has_api_key():
        return None
    # The endpoint needs at least one message; this one adds a few tokens.
    resp = make_client().messages.count_tokens(
        model=model,
        system=system,
        messages=[{"role": "user", "content": "."}],
    )
    return resp.input_tokens


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    if args.list:
        for c in CHAPTERS.values():
            print(f"{c.key:22} {c.title} (§{c.programme_ref})")
        return 0

    if not args.chapitre:
        print("Indique un chapitre avec --chapitre (voir --list).", file=sys.stderr)
        return 2

    chapter = CHAPTERS[args.chapitre]

    if args.dry_run:
        system = examiner_system(chapter, PLACEHOLDER_EXERCISE)
        print(system)
        print("\n" + "-" * 60)
        print(f"{len(system)} caractères")
        tokens = count_tokens(args.model, system)
        if tokens is None:
            print("Nombre de tokens : ANTHROPIC_API_KEY absente, comptage exact impossible.")
        else:
            print(f"{tokens} tokens ({args.model})")
        return 0

    print("Pas encore implémenté : génération de l'exercice (étape 3).", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
