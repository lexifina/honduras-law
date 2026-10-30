# How this repository was made (Honduras)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| OEA: Constitución de la República de Honduras (actualizada noviembre 2021) | <https://www.oas.org/ext/Portals/33/adam/Content/RsU8CsGIXU29uci6sllzCw/Text/ConstituciondelaRepublica(actualizadanoviembre2021).pdf> | 2026-10-29 | No licence stated; the Honduran Constitution is an official legal text |
| Tribunal Superior de Cuentas: Decreto No. 130-2017, Código Penal (La Gaceta No. 34,940, 10 de mayo de 2019) | <https://www.tsc.gob.hn/web/leyes/Decreto_130-2017.pdf> | 2026-10-30 | No licence stated; official legal text published in the Diario Oficial La Gaceta |
| Tribunal Superior de Cuentas: Código del Trabajo (Decreto 189-59), edition of the Centro Electrónico de Documentación e Información Judicial (CEDIJ) | <https://www.tsc.gob.hn/web/leyes/codigo_de_trabajo.pdf> | 2026-10-30 | No licence stated; official legal text published by State bodies. |
| Poder Judicial de Honduras, CEDIJ: Código Procesal Penal (actualizado noviembre 2021) | <http://www.poderjudicial.gob.hn/CEDIJ/Leyes/Documents/CodigoProcesalPenal(ActualizadoNoviembre2021).pdf> | 2026-10-30 | No licence stated; official legal text published by the Poder Judicial. |
| Poder Judicial de Honduras, CEDIJ: Código Civil (actualizado mayo 2018) | <http://www.poderjudicial.gob.hn/CEDIJ/Leyes/Documents/C%C3%B3digoCivil(actualizadomayo2018).pdf> | 2026-10-30 | No licence stated; official legal text published by the Poder Judicial. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitucion` | Constitución de la República de Honduras (Decreto 131 de 1982) | 1 | 2021-01-28 to 2021-01-28 |
| `codigo-penal` | Código Penal (Decreto 130-2017) | 1 | 2020-06-25 to 2020-06-25 |
| `codigo-del-trabajo` | Código del Trabajo (Decreto 189-59) | 1 | 2015-03-02 to 2015-03-02 |
| `codigo-procesal-penal` | Código Procesal Penal (Decreto 9-99-E) | 1 | 2021-11-26 to 2021-11-26 |
| `codigo-civil` | Código Civil (Decreto 76-1906) | 1 | 2020-09-16 to 2020-09-16 |

The build made 5 commits:

| Commits | Kind |
| ---: | --- |
| 5 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futuro`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 1 laws in the record.
- 6 tags.

## Dates

Each commit is dated at noon (America/Tegucigalpa) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: The text carries the footnotes of the last reform, Decreto 3-2021 (ratifying Decreto 192-2020), published in La Gaceta No. 35,500 on 28 January 2021. The source gives only "actualizada noviembre 2021", so the version is dated by the publication of that last reform. https://www.oas.org/ext/Portals/33/adam/Content/RsU8CsGIXU29uci6sllzCw/Text/ConstituciondelaRepublica(actualizadanoviembre2021).pdf

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `c7744a4e74d1755395e384ae4929af4e3420ebe8f63e77803d77ba9330360f72` (2646521 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

5 versions of 5 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 5 history commits and 6 tags (history tip `f637dd435c04dcefdc6685accaa3660e611a085b`).

## Decisions made by hand

- Single version: no official Honduran host of a consolidated Constitution was reachable (the transparency portal sits behind a bot check, the judiciary and Congress sites did not answer). The only text used is the OAS-hosted consolidated copy updated to November 2021; it is recorded as the oldest version available.
- Dated 2021-01-28, the publication of the last reform footnoted in the text (Decreto 3-2021), because the source gives no day.
- Footnote numbers after article numbers and the footnotes naming reform decrees were removed; Title, Chapter and Section headings are kept as their own files.
- Wrapped lines were joined into paragraphs by sentence punctuation.
- Código Penal: one version, the text of Decreto 130-2017 as published in La Gaceta 34,940 on 10 May 2019, from the Tribunal Superior de Cuentas copy. In force 2020-06-25: Art. 635 as reformed by Decreto 46-2020 (La Gaceta 35,247, 9 May 2020) sets that date (Decreto 119-2019 had moved the original six months to 10 May 2020).
- Later reforms to the Código Penal (for example Decretos 93-2021, 59-2024, 84-2026, 103-2026, 111-2026) are not applied: only the Gaceta text is available as text here. Art. 635 is printed as published (six months after publication).
- Código Penal units: one file per article (art-001 to art-635); Libro, Título, Capítulo and Sección headings, page headers and page numbers are left out. Article titles stay in the first line of the text. Paragraph breaks are rebuilt from the line layout (a line ending in . : or ; followed by a capital starts a new paragraph, as do numbered and lettered items).
- Civil and commercial codes of Honduras are not built in this pass.
- Código del Trabajo: one version, the CEDIJ edition hosted by the Tribunal Superior de Cuentas, credited to the publisher as "oldest version available" and dated 2015-03-02, the creation date of the edition's PDF; its latest reform footnote is Decreto 278-2013 (La Gaceta 33,316 of 30 December 2013). Later reforms are not applied.
- Código del Trabajo: one unit per article (art-NNN, art-060-a and art-120-a for the lettered articles). Headings, page numbers, the reform footnotes and their markers and the signatures are left out. Paragraphs are rebuilt from the line layout (a line ending in . : or ; followed by a capital starts a new paragraph, as do numbered and lettered items).
- Código Procesal Penal: one version, the CEDIJ (Poder Judicial) edition "actualizado noviembre 2021", credited to the publisher as "oldest version available" and dated 2021-11-26, the creation date of the edition's PDF; its latest reform footnote is Decreto 93-2021 of 7 October 2021. Later reforms are not applied.
- Código Procesal Penal: one unit per article (art-NNN, lettered articles as art-026-b); epigraphs are kept at the start of the article. Headings, the running header, page numbers, the reform footnotes and their markers, the enacting formula and the signatures are left out. Paragraphs are rebuilt from the line layout (a line ending in . : or ; followed by a capital starts a new paragraph, as do numbered and lettered items).
- Código Civil: one version, the CEDIJ (Poder Judicial) edition "actualizado mayo 2018", credited to the publisher as "oldest version available" and dated 2020-09-16, the creation date of the edition's PDF (the title gives only the month of updating). Later reforms, if any, are not applied. Articles 21 to 36, printed as one repealed block, are the single unit art-021-036; art. 1381, printed twice with the same text, is kept once; art. 565, printed run on after art. 564, is its own unit.
- Código Civil: one unit per article (art-NNN, lettered articles as art-026-b); epigraphs are kept at the start of the article. Headings, the running header, page numbers, the reform footnotes and their markers, the enacting formula and the signatures are left out. Paragraphs are rebuilt from the line layout (a line ending in . : or ; followed by a capital starts a new paragraph, as do numbered and lettered items).

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
- none
- none
- none
- none
