# Honduras: law history in git

The law of Honduras as a git history. Each provision is one file, each law gets one commit on the day it took effect, and the law that made each change is the commit's author. `git blame` names the law behind every paragraph and `git log` lists every change to an article.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `hn/`.

This is an early build: the Constitution and four codes, each as one version.

## What is in it now

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitucion/` | Constitución de la República de Honduras (Decreto 131 de 1982) | 1 | Consolidated text updated to November 2021, dated 28 January 2021 (last reform footnoted); earlier versions are not in the record |
| `codigo-penal/` | Código Penal (Decreto 130-2017) | 1 | As enacted, published in La Gaceta No. 34,940 of 10 May 2019, in force 25 June 2020; later reforms are not applied |
| `codigo-del-trabajo/` | Código del Trabajo (Decreto 189-59) | 1 | The edition of the judiciary's documentation centre (CEDIJ) with reforms to Decreto 278-2013, dated 2 March 2015 (the edition's date); earlier versions are not in the record |
| `codigo-procesal-penal/` | Código Procesal Penal (Decreto 9-99-E) | 1 | CEDIJ (Poder Judicial) edition updated to November 2021, with reforms to Decreto 93-2021, dated 26 November 2021 (the edition's date) |
| `codigo-civil/` | Código Civil (Decreto 76-1906) | 1 | CEDIJ (Poder Judicial) edition "actualizado mayo 2018", dated 16 September 2020 (the date of the edition's file) |

## Where the text comes from

The text is the consolidated Constitución de la República de Honduras (Decreto 131 of 11 January 1982, published in La Gaceta No. 23,612 of 20 January 1982), in the PDF titled "actualizada noviembre 2021" published by the Organization of American States (oas.org), retrieved on 29 October 2026. Its footnotes name each reform decree and the La Gaceta issue that published it; the latest is Decreto 192-2020, ratified by Decreto 3-2021 (La Gaceta No. 35,500 of 28 January 2021). The OAS does not say who consolidated the text, and it is not on a Honduran official site, so it should be checked against La Gaceta. The Honduran official sites (the transparency portal, the judiciary and Congress) could not be read.

The Código Penal is the text of La Gaceta No. 34,940 as hosted by the Tribunal Superior de Cuentas (tsc.gob.hn), and the Código del Trabajo is the CEDIJ edition hosted by the Tribunal Superior de Cuentas (https://www.tsc.gob.hn/web/leyes/codigo_de_trabajo.pdf), both retrieved on 30 October 2026. The Código Procesal Penal and the Código Civil are the editions of the judiciary's Centro Electrónico de Documentación e Información Judicial (CEDIJ, poderjudicial.gob.hn), read from Internet Archive copies of December 2021. The codes' reform footnotes are not reproduced.

Language: Spanish (official), as in the source.

## Not included yet

- Reforms after November 2021, if any.
- Earlier versions of the Constitution and the text of each reform decree.
- Reforms to the codes after the editions used here.
- Every other Honduran law, including the Código de Comercio.

## Dates

The single version is dated 28 January 2021, the publication of the last reform footnoted in the text, because the source gives only "November 2021". The Constitution itself entered into force on 20 January 1982 (art. 379). The commit is authored by the publisher as "oldest version available" and dated noon, America/Tegucigalpa, on that day.

## How it is checked

Every version is read back from git on the day it took effect and on the day before; both must match the corpus the repository was built from. The results are in `REPRODUCE.md`.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file.

## What "author" means

The author of a commit is the law that made the change. Its e-mail address cannot exist, so `git blame` and `git log --author` name laws. A version with no law of its own (the oldest version available) is authored by the publisher and says so. The committer is always Lexifina.
