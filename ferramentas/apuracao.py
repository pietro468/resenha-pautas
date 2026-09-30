#!/usr/bin/env python3
"""
Resumo da apuração de 2026 (dados oficiais do TSE), para a rotina escrever parciais e resultados.
Roda no GitHub (eleicao.yml), porque o TSE bloqueia o acesso direto da rotina.

Saída: eleicao/apuracao.json
  pres: {pst, final, hora, cands:[{nome, partido, n, votos, pct, st}]}
  gov/sen: {uf: {pst, final, hora, cands:[...]}}   (governador: 4 primeiros; senado: 6 primeiros)
  dep_federal_top: os 30 deputados federais mais votados do Brasil
  pres_t2 / gov_t2: mesmo formato, 2º turno (quando existir)
"""
import json, os, sys, urllib.request, datetime

BASE = 'https://resultados.tse.jus.br/oficial/ele2026/'
UFS = 'ac al ap am ba ce df es go ma mt ms mg pa pb pr pe pi rj rn rs ro rr sc sp se to'.split()
OUT = sys.argv[1] if len(sys.argv) > 1 else 'eleicao/apuracao.json'


def baixa(ele, uf, cargo):
    url = '%s%s/dados/%s/%s-c%04d-e%06d-u.json' % (BASE, ele, uf, uf, cargo, int(ele))
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 ResenhaRentavel/1.0'})
        return json.load(urllib.request.urlopen(req, timeout=60))
    except Exception:
        return None


def nome(s):
    out = []
    for i, w in enumerate((s or '').lower().split()):
        out.append(w if (i and w in ('da', 'de', 'do', 'das', 'dos', 'e')) else w[:1].upper() + w[1:])
    return ' '.join(out)


def num(v):
    try:
        return float(str(v).replace(',', '.'))
    except Exception:
        return 0.0


def resumo(d, n=None, uf=None):
    if not d or not d.get('carg'):
        return None
    cands = []
    for a in d['carg'][0]['agr']:
        for p in a['par']:
            for x in p['cand']:
                c = {'nome': nome(x.get('nmu') or x.get('nm')), 'partido': p['sg'], 'n': x['n'],
                     'votos': int(x.get('vap') or 0), 'pct': round(num(x.get('pvapn') or x.get('pvap')), 2), 'st': x.get('st', '')}
                if uf:
                    c['uf'] = uf.upper()
                cands.append(c)
    cands.sort(key=lambda c: -c['votos'])
    s = d.get('s', {})
    return {'pst': num(s.get('pstn', 0)), 'final': d.get('tf') == 's', 'hora': ('%s %s' % (d.get('dt', ''), d.get('ht', ''))).strip(),
            'cands': cands[:n] if n else cands}


def main():
    out = {'gerado': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%MZ'), 'fonte': 'TSE, resultados.tse.jus.br'}
    out['pres'] = resumo(baixa('6257', 'br', 1))
    out['gov'], out['sen'], deps = {}, {}, []
    for uf in UFS:
        g = resumo(baixa('6259', uf, 3), 4)
        if g:
            out['gov'][uf] = g
        s = resumo(baixa('6259', uf, 5), 6)
        if s:
            out['sen'][uf] = s
        d = resumo(baixa('6259', uf, 6), 40, uf)
        if d:
            deps += d['cands']
    deps.sort(key=lambda c: -c['votos'])
    out['dep_federal_top'] = deps[:30]
    t2 = resumo(baixa('6258', 'br', 1))
    if t2:
        out['pres_t2'] = t2
    out['gov_t2'] = {}
    for uf in UFS:
        g = resumo(baixa('6260', uf, 3))
        if g:
            out['gov_t2'][uf] = g
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    p = out['pres'] or {}
    print('pres', p.get('pst'), [(c['nome'], c['pct']) for c in (p.get('cands') or [])[:3]])


if __name__ == '__main__':
    main()
