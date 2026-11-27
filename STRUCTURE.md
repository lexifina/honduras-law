# Estructura / Structure

| Carpeta | Contenido |
| --- | --- |
| `constitucion/` | Constitución de la República (Decreto 131 de 1982) |
| `codigos/<codigo>/` | Un código, p. ej. `codigos/codigo-civil/`, `codigos/codigo-de-comercio/` |
| `decretos/<año>/<NNN>-<objeto>/` | Decreto del Congreso Nacional por año y número, p. ej. `decretos/2026/198-ley-de-justicia-energetica/` |
| `decretos-ejecutivos/<año>/pcm-<NNN>-<objeto>/` | Decreto Ejecutivo del Presidente en Consejo de Ministros (PCM) |
| `acuerdos/<año>/<numero>-<objeto>/` | Acuerdo ejecutivo o ministerial |

Cada carpeta tiene un archivo por artículo (`art-001.md`) y un `README.md`. Los códigos de más de 1.000 artículos
(Civil, de Comercio) los agrupan en bloques: `codigos/codigo-civil/arts-1001-2000/art-1176.md`. Un decreto que reforma o interpreta otra
ley y cita los artículos que reescribe se guarda en un solo archivo (`texto.md`). Ninguna carpeta tiene más de 1.000
entradas.

Each folder holds one file per article (`art-001.md`) and a `README.md` (codes of more than 1,000 articles, the Civil
and Commercial codes, group them in blocks of 1,000: `arts-0001-1000/`, `arts-1001-2000/`, ...); an amending decree, which quotes the articles
it rewrites, is one file (`texto.md`). No folder holds more than 1,000 entries.

## Fechas / Dates

Each version is one commit dated 12:00 America/Tegucigalpa on the day it took effect, repeated in its `In-force:`
trailer; `In-force-basis:` says where that day comes from:

- a decree or acuerdo from a La Gaceta extract: its own commencement clause read against the issue's masthead day
  (the day of publication, the day after, or N days after). A clause tied to approval or signature, business days,
  or no clause at all: the instrument is held, not dated;
- consolidated editions (CEDIJ, OAS): as each commit says (the edition's own date);
- the Código de Comercio: its promulgation, 1 May 1950, from WIPO Lex (`Source-status: secondary copy`).

Dates before 1970, which git cannot store, are stamped 1970-01-01 with the real day in the subject and `In-force:`.
No date in this repository is the day we downloaded anything.
