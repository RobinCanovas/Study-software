from study.oral.chapters import CHAPTERS
from study.oral.prompts import END_OF_ORAL, EXAMINER_RULES, Exercise, examiner_system

EX = Exercise(statement="Énoncé.", steps=("a", "b"), hypotheses=("h",))


def test_prompt_is_deterministic():
    # Byte-identical prompts are required for the prompt cache to hit.
    for chapter in CHAPTERS.values():
        assert examiner_system(chapter, EX) == examiner_system(chapter, EX)


def test_prompt_contains_scope_and_hidden_key():
    s = examiner_system(CHAPTERS["reduction"], EX)
    assert "Cayley-Hamilton" in s  # listed as out of scope
    assert "1. a\n2. b" in s
    assert "Corrigé confidentiel" in s


def test_chapter_without_out_of_scope_has_no_empty_section():
    s = examiner_system(CHAPTERS["matrices"], EX)
    assert "Hors programme" not in s


def test_end_marker_is_in_rules():
    assert END_OF_ORAL in EXAMINER_RULES
