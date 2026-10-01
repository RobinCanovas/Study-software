# Project context

## What this is
A spaced-repetition card generator for exam prep. It takes a course
PDF (lecture notes, textbook chapter) and produces high-quality Anki
cards: exact theorem statements with their hypotheses, definitions,
and method triggers ("when I see X, I do Y").

Output format: tab-separated text file, importable into Anki, with a
tags column.

## Who I am
Third-year Computer Science student (BUT Informatique, IUT d'Orsay),
on a work-study contract at a scientific publisher. I'm preparing
competitive entrance exams for French engineering schools over the
next 18 months, so I will be generating decks for many subjects:
linear algebra, formal languages and automata, graph theory,
complexity, probability.

I build this because I need it. It is not a portfolio piece.

## Stack
- Python 3.11+
- Anthropic API (Claude) for card generation
- PDF text extraction: pypdf or pdfplumber
- CLI first. No web interface for now.

## Constraints
- API key in a `.env` file, never committed. `.gitignore` it from the
  first commit.
- Keep API costs low: I have limited credits. Chunk the PDF and only
  send what's needed.
- Source PDFs live in `pdfs/`, which is git-ignored. Teachers' handouts
  are not ours to publish; never commit them, never quote them at length
  in committed files.
- Must handle French course material — prompts and card content in
  French, code and comments in English.

## What a good card looks like
- Front: a precise question, not a topic name.
- Back: the exact statement, including hypotheses. Hypotheses are
  where marks are lost.
- One idea per card. If the back has two ideas, split it.
- Prefer "state the rank-nullity theorem in full" over "rank-nullity
  theorem".

## First milestone
A CLI that takes a PDF path and a chapter range, and writes an
Anki-importable file. Nothing else.

## How I want you to work
- Small, reviewable steps. Show me the plan before writing a lot of
  code.
- Explain design choices briefly — I'm learning, not just shipping.
- Flag anything that would increase API cost significantly.
