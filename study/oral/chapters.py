"""Chapters available for the oral, scoped to the CUEC 2026 programme.

The topic lists summarise the official programme (pdfs/, not committed) in
short keyword form. They go into the examiner's system prompt so that
exercises and hints stay within what the exam can ask.

`out_of_scope` lists classic tools a model would reach for by default but
that the programme does not include. Only list what is clearly absent from
the programme.
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Chapter:
    key: str
    title: str
    programme_ref: str
    topics: tuple[str, ...]
    out_of_scope: tuple[str, ...] = field(default_factory=tuple)


CHAPTERS: dict[str, Chapter] = {
    c.key: c
    for c in [
        Chapter(
            key="espaces-vectoriels",
            title="Espaces vectoriels et dimension finie",
            programme_ref="2.5",
            topics=(
                "structure de K-espace vectoriel, produit fini d'espaces, espace de fonctions",
                "sous-espaces : caractérisation, intersection, sous-espace engendré",
                "familles libres, liées, génératrices ; bases, coordonnées",
                "somme et somme directe de deux puis d'un nombre fini de sous-espaces",
                "dimension finie : existence de bases, base extraite, base incomplète",
                "en dimension n : n vecteurs libres ou générateurs forment une base",
                "rang d'une famille de vecteurs",
                "dimension d'un sous-espace, cas d'égalité ; existence d'un supplémentaire",
                "base adaptée à une somme directe ; formule de Grassmann",
            ),
        ),
        Chapter(
            key="applications-lineaires",
            title="Applications linéaires",
            programme_ref="2.8.1",
            topics=(
                "application linéaire, isomorphisme, L(E,F) espace vectoriel",
                "image et image réciproque d'un sous-espace ; noyau et injectivité",
                "image d'une famille génératrice, d'une base par un isomorphisme",
                "rang, invariance par composition avec un isomorphisme",
                "projecteurs (p² = p) et symétries (s² = Id)",
                "application linéaire déterminée par l'image d'une base",
                "dimensions égales finies : injective ⇔ surjective ⇔ bijective",
                "dimension de L(E,F) ; théorème du rang",
                "formes linéaires ; hyperplan comme noyau d'une forme linéaire non nulle",
            ),
            out_of_scope=("espace dual et base duale", "espaces quotients"),
        ),
        Chapter(
            key="matrices",
            title="Matrices et changements de base",
            programme_ref="2.7",
            topics=(
                "M_{n,p}(K), base canonique, dimension",
                "produit matriciel, formule du binôme, matrices inversibles, GL_n(K)",
                "matrices diagonales, triangulaires, transposée",
                "matrice d'une application linéaire dans des bases, d'une composée",
                "noyau, image, rang d'une matrice ; inversibilité ⇔ noyau nul",
                "matrices par blocs",
                "changement de base, matrice de passage",
                "rang r ⇔ équivalente à J_r ; invariance du rang par transposition",
                "rang et matrices extraites",
                "matrices semblables, trace, tr(AB) = tr(BA), trace d'un endomorphisme",
                "opérations élémentaires et rang ; systèmes linéaires, systèmes de Cramer",
            ),
        ),
        Chapter(
            key="determinants",
            title="Déterminants",
            programme_ref="2.8",
            topics=(
                "formes n-linéaires alternées, antisymétrie, effet d'une permutation",
                "déterminant d'un endomorphisme, d'une composée ; caractérisation des automorphismes",
                "déterminant d'une matrice carrée, d'un produit ; caractérisation des matrices inversibles",
                "effet des opérations élémentaires",
                "cofacteurs, développement selon une ligne ou une colonne",
                "déterminant d'une matrice triangulaire, triangulaire par blocs",
            ),
        ),
        Chapter(
            key="reduction",
            title="Réduction des endomorphismes et des matrices carrées",
            programme_ref="2.9",
            topics=(
                "sous-espace stable, endomorphisme induit",
                "valeurs propres, vecteurs propres, sous-espaces propres, spectre",
                "une somme finie de sous-espaces propres est directe ; au plus n valeurs propres",
                "polynôme caractéristique (unitaire) ; valeurs propres = racines",
                "polynôme caractéristique d'une matrice triangulaire, d'un endomorphisme induit",
                "multiplicité ; dim E_λ ≤ multiplicité de λ",
                "matrices semblables : même spectre, même polynôme caractéristique",
                "diagonalisable ⇔ somme des sous-espaces propres = E ⇔ somme des dimensions = n",
                "diagonalisable ⇔ χ scindé et dim E_λ = multiplicité pour tout λ ; cas χ scindé à racines simples",
                "cas des projecteurs et des symétries",
                "trigonalisable ⇔ χ scindé ; trace et déterminant via les valeurs propres",
                "nilpotents : caractérisation par χ, indice de nilpotence ≤ dim E",
            ),
            out_of_scope=(
                "polynôme annulateur et polynôme minimal",
                "théorème de Cayley-Hamilton",
                "lemme des noyaux",
                "réduction de Jordan, décomposition de Dunford",
            ),
        ),
    ]
}
