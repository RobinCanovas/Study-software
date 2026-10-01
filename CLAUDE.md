# Project context

Two small CLI tools for preparing French engineering-school entrance
orals, sharing one codebase (config, API client, cost tracking):

1. **Oral exam simulator** — current focus.
2. **Anki card generator** — next.

I build this because I need it. It is not a portfolio piece.

## Who I am
Third-year Computer Science student (BUT Informatique, IUT d'Orsay),
on a work-study contract at a scientific publisher. Over the next 18
months I'm preparing competitive oral exams for French engineering
schools (CUEC, dominante informatique). Five orals, 30 minutes each,
no preparation: two in computer science, one in mathematics, one
interview, one in English.

## Shared stack
- Python 3.11+
- Anthropic API (Claude)
- CLI first. No web interface for now.
- Default model: Claude Sonnet 5.5 (`claude-sonnet-5-5`). Opus is
  available via a `--model` flag for subtler exercises or finer
  feedback. Budget: ~100 USD for 18 months.

## Shared constraints
- API key in a `.env` file, never committed. `.gitignore` it from the
  first commit.
- Keep API costs low: limited credits. Flag anything that would
  increase API cost significantly.
- Source PDFs live in `pdfs/`, which is git-ignored. Teachers'
  handouts are not ours to publish; never commit them, never quote
  them at length in committed files.
- Course material is in French. Prompts, exercises, dialogue and card
  content in French; code and comments in English.

## How I want you to work
- Small, reviewable steps. Show the plan before writing much code.
- Explain design choices briefly — I'm learning, not just shipping.
- Flag anything that would increase API cost significantly.

---

## Tool 1 — Oral exam simulator

### What this is
I pick a chapter, the model gives me one exercise, and acts as an
examiner: no solutions, only progressive hints, then feedback on my
reasoning at the end.

It mirrors a specific exam format: 30 minutes, at the board, with no
preparation time. The examiner expects you to think out loud, to say
when you're stuck, and to react to hints.

Session transcripts are saved as JSON for later review.

### Core behaviour — this is the whole project
The examiner must:
- give ONE exercise, never the solution
- give hints only when I'm actually stuck, and only the next step
- ask me to justify every claim ("why is that a basis?")
- let me fail and say so, rather than rescuing me
- at the end, report: what I got right, where I stalled, which
  hypotheses I forgot to state

The examiner must NOT:
- validate an answer I haven't justified
- move on when I change the subject
- produce a full worked solution at any point

### Constraints
- Short system prompt, no resending the whole transcript every turn
  if avoidable.

### Subject scope
Start with linear algebra (vector spaces, linear maps, kernel, image,
rank-nullity, change of basis, diagonalisation). Later: formal
languages and automata, graph theory, complexity, probability.
Exercises must stay within the official CUEC programme (the PDF is in
`pdfs/`).

### First milestone
A CLI where I type a chapter name, get one exercise, and have a
back-and-forth with hints. Transcript saved at the end. Nothing else.

---

## Tool 2 — Anki card generator

### What this is
Takes a course PDF (lecture notes, textbook chapter) and produces
high-quality Anki cards: exact theorem statements with their
hypotheses, definitions, and method triggers ("when I see X, I do Y").

Output format: tab-separated text file, importable into Anki, with a
tags column.

### What a good card looks like
- Front: a precise question, not a topic name.
- Back: the exact statement, including hypotheses. Hypotheses are
  where marks are lost.
- One idea per card. If the back has two ideas, split it.
- Prefer "state the rank-nullity theorem in full" over "rank-nullity
  theorem".

### Decisions already made
- Select content with page ranges: `--pages 12-40`. No bookmark or
  heading detection for now; add bookmark detection only if page
  ranges become painful.
- Source PDFs are LaTeX-generated with extractable text, no scans.
- `pdftotext` tested on the automata handout (pandoc + xdvipdfmx,
  no Type 3 fonts, all fonts have Unicode maps): prose and symbols
  extract correctly as Unicode math letters (𝑄, 𝒜, 𝛿, Σ∗, ⟺).
  Known losses:
  - sub/superscripts are flattened: `𝑞𝑖+1` (q_{i+1}), `𝛿 ∗`, `𝑞 ′`;
  - figures (automaton diagrams) vanish entirely, so exercises that
    rely on a drawing lose their content;
  - do NOT apply NFKC normalisation: it maps both 𝐴 (an automaton)
    and 𝒜 (the alphabet) to plain `A`.
- Chunk the PDF and only send what's needed.

### First milestone
A CLI that takes a PDF path and a page range, and writes an
Anki-importable file. Nothing else.
