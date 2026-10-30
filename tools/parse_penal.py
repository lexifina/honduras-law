"""Honduras Codigo Penal (Decreto 130-2017) from La Gaceta 34,940 (TSC copy) -> corpus.d/20-codigo-penal.json. No network."""
import hashlib, json, re, sys
from pathlib import Path
import pymupdf

HERE = Path(__file__).resolve().parent
PDF = HERE / '.cache' / 'penal.pdf'
URL = 'https://www.tsc.gob.hn/web/leyes/Decreto_130-2017.pdf'
RETRIEVED = '2026-10-30'


def norm(s):
    s = s.replace('\xa0', ' ').replace('\t', ' ').replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('–', '-').replace('—', '-')
    return re.sub(r' {2,}', ' ', s).strip()


LET = 'A-ZÁÉÍÓÚÑ'


def despace(p):
    # titles typeset with letter-spacing come out as "C I R C U N S TA N C I A S": join runs of short tokens with 3+ single letters
    def fix(m):
        run = m.group(0)
        return run.replace(' ', '') if len(re.findall(rf'(?<![\w])[{LET}](?![\w])', run)) >= 3 else run
    return re.sub(rf'(?<![\w])(?:[{LET}]{{1,2}} ){{3,}}[{LET}]{{1,2}}(?![\w])', fix, p)


raw = '\n'.join(p.get_text() for p in pymupdf.open(PDF))
lines = [norm(l) for l in raw.split('\n')]
JUNK = re.compile(r'^(\d{1,3}|La Gaceta|A\.|Sección\s+A\s+Acuerdos y Leyes|REPÚBLICA DE HONDURAS.*No\. 34,940|DIARIO OFICIAL DE LA REPÚBLICA DE HONDURAS|DECANO DE LA PRENSA HONDUREÑA|PARA MEJOR SEGURIDAD DE SUS PUBLICACIONES)$')
lines = [l for l in lines if l and not JUNK.match(l)]
start = lines.index('CÓDIGO PENAL')
lines = lines[start:]
text = '\n'.join(lines)
# spaced-out "A RT Í C U L O 7 1 . -" forms
ART = re.compile(r'(?m)^A ?R ?T ?[ÍI] ?C ?U ?L ?O ((?:\d ?)+)(?:\. ?- ?|\.(?= )|- ?)')
ms = list(ART.finditer(text))
HEAD = re.compile(r'^(LIBRO|TÍTULO|TITULO|CAPÍTULO|CAPITULO|SECCIÓN|SECCION|SUBSECCIÓN|SUBSECCION|PARTE ESPECIAL|PARTE GENERAL|DISPOSICIONES|DISPOSICIÓN)\b')
units, nums = {}, []
for i, m in enumerate(ms):
    n = int(m.group(1).replace(' ', ''))
    body = text[m.end():ms[i + 1].start() if i + 1 < len(ms) else len(text)]
    bl = body.split('\n')
    cut = next((k for k, l in enumerate(bl) if HEAD.match(l) and l.upper() == l), None)
    if i + 1 == len(ms):
        cut = next((k for k, l in enumerate(bl) if l.startswith('Dado en la ciudad')), cut)
    if cut is not None:
        bl = bl[:cut]
    # paragraphs
    paras, cur = [], ''
    for l in bl:
        item = re.match(r'^(\d+\)|[a-zñ]\)|\d+\.)\s*(.*)$', l)
        if re.fullmatch(r'(\d+\)|[a-zñ]\)|\d+\.)', l):
            if cur: paras.append(cur)
            cur = l
            continue
        if item and cur and not re.fullmatch(r'(\d+\)|[a-zñ]\))', cur):
            paras.append(cur); cur = l
        elif cur and re.fullmatch(r'(\d+\)|[a-zñ]\)|\d+\.)', cur):
            cur += ' ' + l
        elif cur and cur[-1] in '.:;' and l[:1].isupper():
            paras.append(cur); cur = l
        else:
            cur = (cur + ' ' + l).strip()
    if cur: paras.append(cur)
    paras = [re.sub(r' {2,}', ' ', p) for p in paras]
    paras = [despace(p) for p in paras]
    nums.append(n)
    units['art-%03d' % n] = {'label': 'Art. %d' % n, 'kind': 'art', 'text': '# Artículo %d\n' % n + '\n'.join(paras) + '\n'}
assert nums == list(range(1, 636)), [x for x in range(1, 636) if x not in nums][:10]
sha = hashlib.sha256(PDF.read_bytes()).hexdigest()
part = {
    'sources': [{'name': 'Tribunal Superior de Cuentas: Decreto No. 130-2017, Código Penal (La Gaceta No. 34,940, 10 de mayo de 2019)',
                 'url': URL, 'retrieved': RETRIEVED, 'licence': 'No licence stated; official legal text published in the Diario Oficial La Gaceta',
                 'notes': 'Text-layer PDF of the Gaceta issue (140 pages), hosted by the Tribunal Superior de Cuentas. robots.txt allows it.'}],
    'laws': {
        'decreto-130-2017': {'label': 'Decreto 130-2017', 'title': 'Código Penal', 'kind': 'law', 'enacted': '2018-01-18', 'published': '2019-05-10',
                             'url': URL, 'temporary_until': None, 'restores': None, 'note': None}},
    'acts': [{'slug': 'codigo-penal', 'short': 'CP', 'title': 'Código Penal (Decreto 130-2017)', 'url': URL,
              'first_law': 'decreto-130-2017', 'earlier_laws': [],
              'versions': [{'from': '2020-06-25', 'source_url': URL, 'sha256': sha, 'units': units, 'credits': {},
                            'note': 'The Código Penal as published in La Gaceta No. 34,940 (10 May 2019), in force from 25 June 2020. Later reforms are not applied here.'}]}],
    'decisions': [
        'Código Penal: one version, the text of Decreto 130-2017 as published in La Gaceta 34,940 on 10 May 2019, from the Tribunal Superior de Cuentas copy. In force 2020-06-25: Art. 635 as reformed by Decreto 46-2020 (La Gaceta 35,247, 9 May 2020) sets that date (Decreto 119-2019 had moved the original six months to 10 May 2020).',
        'Later reforms to the Código Penal (for example Decretos 93-2021, 59-2024, 84-2026, 103-2026, 111-2026) are not applied: only the Gaceta text is available as text here. Art. 635 is printed as published (six months after publication).',
        'Código Penal units: one file per article (art-001 to art-635); Libro, Título, Capítulo and Sección headings, page headers and page numbers are left out. Article titles stay in the first line of the text. Paragraph breaks are rebuilt from the line layout (a line ending in . : or ; followed by a capital starts a new paragraph, as do numbered and lettered items).',
        'Civil and commercial codes of Honduras are not built in this pass.'],
    'ai_use': ['none'],
}
out = HERE / 'corpus.d' / '20-codigo-penal.json'
tmp = out.with_suffix('.tmp')
tmp.write_text(json.dumps(part, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')
tmp.replace(out)
print('articles', len(nums))
