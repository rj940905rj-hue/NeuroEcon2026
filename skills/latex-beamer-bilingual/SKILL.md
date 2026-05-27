---
name: latex-beamer-bilingual
description: Use when the user asks for a LaTeX slide deck, Beamer presentation, `.tex` presentation file, academic lecture slides, class presentation, or help editing/compiling Beamer files. Default to a Chinese deck when the user says they want a LaTeX presentation without specifying language. Switch to an English deck only when the user explicitly asks for English slides. Prefer XeLaTeX with `ctexbeamer` for Chinese decks unless the existing project already uses another setup.
---

# LaTeX Beamer Slides

## Overview

Use this skill for new or existing LaTeX Beamer presentations. The default output language is Chinese. Only switch to English when the user explicitly asks for an English deck.

Assume the user wants a real Beamer `.tex` workflow, not PowerPoint, unless they explicitly ask for another format.

## Default Rules

1. If the user says `LaTeX簡報`, `Beamer`, `latex slides`, or similar without specifying language, default to Chinese slides.
2. If the user explicitly says `英文簡報`, `English slides`, or asks for English output, switch to the English rules.
3. For new Chinese decks, prefer `ctexbeamer` plus `xelatex`.
4. For English-only decks, keep the existing repo setup if present; otherwise plain `beamer` is acceptable.
5. Do not mix Chinese and English styles by default unless the user asks for bilingual output.
6. Prefer standard packages that are likely to exist in a normal TeX installation. Avoid fragile theme or font dependencies unless the user asks for them.
7. Keep each slide message-first: one takeaway, short bullets, strong section titles, and minimal paragraph text.
8. If the user simply says they want a LaTeX presentation, default to a compilable Chinese Beamer deck with a clean academic style.

## Language Modes

### Chinese-default mode

- Use Chinese for slide titles, bullets, transitions, and takeaways.
- Keep technical terms in English only when they are standard course vocabulary.
- For a new deck, start from `assets/chinese-beamer-starter.tex`.
- Prefer `ctexbeamer` and `xelatex`.

### English mode

- Use English consistently across titles, bullets, and speaker-facing structure.
- Keep Chinese out of the deck unless the user explicitly asks for bilingual support.
- For a new deck, start from `assets/english-beamer-starter.tex`.
- Prefer plain `beamer` unless the repo already uses `ctexbeamer` or mixed-language content.

## Workflow

### 1. Determine the job

- If files already exist, preserve the current structure, class, theme, and bibliography workflow unless they are broken.
- If this is a new deck, start from the language-appropriate asset template and adapt it.
- If the user does not specify language, choose the Chinese template.
- If the user mentions Chinese, CJK text, or mixed Chinese-English slides, stay with `ctexbeamer` and `xelatex`.
- If the user explicitly asks for English slides, follow the English mode rules instead.

### 2. Build the slide structure first

Unless the user gives a fixed outline, organize the deck around:

1. Title
2. Motivation / question
3. Method or setup
4. Core results or argument
5. Interpretation
6. Limitations or critique
7. Takeaway

For classroom presentations, prefer fewer stronger slides over many dense slides.

### 3. Write Beamer in a robust style

- Use stock themes such as `Madrid` unless the project already has a preferred theme.
- Use `\framesubtitle{}` only when it adds real structure.
- Prefer `itemize`, `enumerate`, `columns`, `block`, `alertblock`, `table`, and simple figures.
- Avoid oversized tables and long equations on one slide; split them across frames when needed.
- Prefer explicit section titles over decorative slide names.

### 4. Compile and verify

- Compile with `xelatex`.
- Run compilation twice when references, TOC, or cross-references are involved.
- If bibliography is added, follow the project's existing toolchain; do not switch bibliography systems casually.
- If the environment allows it, compile before finishing so the user gets a working deck, not only source edits.

## Chinese Rules

- Use Chinese for explanation and slide structure by default.
- Introduce core technical terms as `中文（English）` on first mention when useful.
- Keep bullet length short; Chinese slides read better with fewer lines.
- Use full-width punctuation naturally in Chinese slides.

## English Rules

- Use English consistently for titles, bullets, and transitions.
- Avoid inserting Chinese explanations unless the user explicitly asks for bilingual support.
- Prefer shorter noun-phrase slide titles and claim-driven bullets.
- Keep wording natural for oral presentation, not like a literal translation.

## Mixed-language Guidance

- Only use this when the user explicitly asks for bilingual output.
- On the first appearance of an important term, prefer `中文（English）` or `English（中文）`, then stay consistent.
- Keep bullet length short; bilingual slides become crowded quickly.
- For math-heavy content, keep prose outside equations and avoid mixing long Chinese sentences inside formulas.
- If a slide is visually crowded, split it rather than shrinking the font.

## Starter Pattern

For a new Chinese deck, use this pattern or adapt the Chinese asset template:

```tex
\documentclass[aspectratio=169]{ctexbeamer}
\usetheme{Madrid}
\usecolortheme{default}
\usepackage{amsmath, amssymb, booktabs, graphicx}
\title{簡報標題}
\subtitle{副標題}
\author{Name}
\institute{Course or Department}
\date{\today}

\begin{document}

\frame{\titlepage}

\begin{frame}{Research Question}
\begin{itemize}
  \item 中文重點一句話。
  \item 補一句支持這個重點的說明。
\end{itemize}
\end{frame}

\end{document}
```

For a new English deck, a plain Beamer setup is fine:

```tex
\documentclass[aspectratio=169]{beamer}
\usetheme{Madrid}
\usecolortheme{default}
\usepackage{amsmath, amssymb, booktabs, graphicx}
\title{Title}
\subtitle{Subtitle}
\author{Name}
\institute{Course or Department}
\date{\today}
```

## Common Tasks

### New deck

- Create a clean `main.tex`.
- Add only the packages the deck actually needs.
- Keep comments short and useful when the structure is not obvious.

### Edit an existing deck

- Respect the current theme and macros.
- Fix Chinese rendering by moving to `xelatex` only when needed and when that change will not break the repo's current workflow.
- Prefer small targeted edits over wholesale rewrites.

### Convert notes into slides

- Compress prose aggressively.
- Turn each paragraph into one claim, one method point, or one result.
- If needed, add a final discussion slide with critique and open questions rather than overloading result slides.

## Troubleshooting

- Chinese text renders incorrectly: use `ctexbeamer` and compile with `xelatex`.
- English deck accidentally uses Chinese template defaults: switch to the English asset and remove unused CJK-specific content if the project does not need it.
- Missing custom theme or font: fall back to stock Beamer themes and default CJK-safe fonts.
- Overfull slides: shorten bullets, split frames, or move details into speaker notes/comments instead of shrinking everything.
- Tables too wide: reduce columns, abbreviate labels, or split across slides.
- Too much text: convert explanation into a figure, process diagram, or two-step reveal.

## Assets

- For a fresh Chinese Beamer deck, start from `assets/chinese-beamer-starter.tex`.
- For a fresh English Beamer deck, start from `assets/english-beamer-starter.tex`.
