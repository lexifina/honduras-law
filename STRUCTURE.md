# Estructura / Structure

| Carpeta | Contenido |
| --- | --- |
| `constitucion/` | ConstituciÃ³n de la RepÃºblica (Decreto 131 de 1982) |
| `codigos/<codigo>/` | Un cÃ³digo, p. ej. `codigos/codigo-civil/`, `codigos/codigo-de-comercio/` |
| `decretos/<aÃ±o>/<NNN>-<objeto>/` | Decreto del Congreso Nacional por aÃ±o y nÃºmero, p. ej. `decretos/2026/198-ley-de-justicia-energetica/` |
| `decretos-ejecutivos/<aÃ±o>/pcm-<NNN>-<objeto>/` | Decreto Ejecutivo del Presidente en Consejo de Ministros (PCM) |
| `acuerdos/<aÃ±o>/<numero>-<objeto>/` | Acuerdo ejecutivo o ministerial |

Cada carpeta tiene un archivo por artÃ­culo (`art-001.md`) y un `README.md`. Un decreto que reforma o interpreta otra
ley y cita los artÃ­culos que reescribe se guarda en un solo archivo (`texto.md`). Ninguna carpeta tiene mÃ¡s de 1.000
entradas.

Each folder holds one file per article (`art-001.md`) and a `README.md`; an amending decree, which quotes the articles
it rewrites, is one file (`texto.md`). No folder holds more than 1,000 entries.

## Fechas / Dates

Each version is one commit dated 12:00 America/Tegucigalpa on the day it took effect, repeated in its `In-force:`
trailer; `In-force-basis:` says where that day comes from:

- a decree or acuerdo from a La Gaceta extract: its own commencement clause read against the issue's masthead day
  (the day of publication, the day after, or N days after). A clause tied to approval or signature, business days,
  or no clause at all: the instrument is held, not dated;
- consolidated editions (CEDIJ, OAS): as each commit says (the edition's own date);
- the CÃ³digo de Comercio: its promulgation, 1 May 1950, from WIPO Lex (`Source-status: secondary copy`).

Dates before 1970, which git cannot store, are stamped 1970-01-01 with the real day in the subject and `In-force:`.
No date in this repository is the day we downloaded anything.
