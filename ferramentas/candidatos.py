#!/usr/bin/env python3
"""
Gera os arquivos de "Quem está na sua urna" (candidatos de 2026) a partir dos dados abertos do TSE.

Roda no GitHub (candidatos.yml), porque o TSE bloqueia downloads daqui.
Saída (lida pelo site):
  candidatos/2026/{uf}.json         lista de candidatos (br = presidente)
  candidatos/2026/perfil/{uf}.json  bens, candidaturas anteriores, doadores e gastos de cada um
"""
import csv, io, json, os, sys, zipfile, urllib.request, collections, datetime

BASE = 'https://cdn.tse.jus.br/estatistica/sead/odsele/'
ARQ = {
    'cand': 'consulta_cand/consulta_cand_2026.zip',
    'comp': 'consulta_cand_complementar/consulta_cand_complementar_2026.zip',
    'bens': 'bem_candidato/bem_candidato_2026.zip',
    'hist': 'historico_candidatura/historico_candidatura_2026.zip',
    'contas': 'prestacao_contas/prestacao_de_contas_eleitorais_candidatos_2026.zip',
}
TITULAR = {'1': 'pres', '3': 'gov', '5': 'sen', '6': 'df', '7': 'de', '8': 'de'}
VICE = {'2': ('1', 'vice'), '4': ('3', 'vice'), '9': ('5', 'sup1'), '10': ('5', 'sup2')}
OUT = sys.argv[1] if len(sys.argv) > 1 else 'candidatos/2026'
TMP = '/tmp/tse'
csv.field_size_limit(10**9)


def baixar(k):
    os.makedirs(TMP, exist_ok=True)
    dest = os.path.join(TMP, k + '.zip')
    if not os.path.exists(dest):
        req = urllib.request.Request(BASE + ARQ[k], headers={'User-Agent': 'Mozilla/5.0 ResenhaRentavel/1.0'})
        with urllib.request.urlopen(req, timeout=900) as r, open(dest, 'wb') as f:
            while True:
                b = r.read(1 << 20)
                if not b:
                    break
                f.write(b)
    return zipfile.ZipFile(dest)


def linhas(z, filtro):
    nomes = [n for n in z.namelist() if n.lower().endswith('.csv') and filtro(n)]
    br = [n for n in nomes if 'BRASIL' in n.upper()]
    if br and filtro is not None and getattr(filtro, 'brasil', True):
        nomes = br  # o arquivo BRASIL já tem todos os estados
    for n in nomes:
        if not n.lower().endswith('.csv') or not filtro(n):
            continue
        with z.open(n) as f:
            for row in csv.DictReader(io.TextIOWrapper(f, encoding='latin-1'), delimiter=';'):
                yield n, row


def limpo(v):
    v = (v or '').strip()
    return '' if v in ('#NULO', '#NULO#', '#NE', 'NÃO DIVULGÁVEL', 'Não divulgável', '-1', '-3', '-4') else v


def titulo(s):
    s = limpo(s)
    if not s:
        return ''
    out = []
    for i, w in enumerate(s.lower().split()):
        out.append(w if (i and w in ('da', 'de', 'do', 'das', 'dos', 'e')) else w[:1].upper() + w[1:])
    return ' '.join(out)


def num(v):
    try:
        return float(str(v).replace('.', '').replace(',', '.')) if ',' in str(v) else float(v)
    except Exception:
        return 0.0


def main():
    # ---------- candidatos ----------
    z = baixar('cand')
    cands, vices = {}, collections.defaultdict(dict)
    for _, r in linhas(z, lambda n: True):
        cd = r['CD_CARGO']
        uf = r['SG_UF'].lower()
        if cd in TITULAR:
            sq = r['SQ_CANDIDATO']
            cands[sq] = {
                'sq': sq, 'uf': uf, 'cargo': TITULAR[cd], 'cd': int(cd), 'n': r['NR_CANDIDATO'],
                'nome': titulo(r['NM_URNA_CANDIDATO']), 'nc': titulo(r['NM_CANDIDATO']),
                'p': limpo(r['SG_PARTIDO']), 'pn': titulo(r['NM_PARTIDO']),
                'fed': limpo(r['NM_FEDERACAO']), 'col': limpo(r['NM_COLIGACAO']).strip(),
                'comp': limpo(r['DS_COMPOSICAO_COLIGACAO']),
                'g': titulo(r['DS_GENERO']), 'cor': titulo(r['DS_COR_RACA']),
                'instr': titulo(r['DS_GRAU_INSTRUCAO']), 'ocup': titulo(r['DS_OCUPACAO']),
                'ec': titulo(r['DS_ESTADO_CIVIL']), 'nuf': limpo(r['SG_UF_NASCIMENTO']),
                'nasc': limpo(r['DT_NASCIMENTO']), 'sit': titulo(r['DS_SITUACAO_CANDIDATURA']),
            }
        elif cd in VICE:
            tit, campo = VICE[cd]
            vices[(uf, tit, r['NR_CANDIDATO'])][campo] = titulo(r['NM_URNA_CANDIDATO'])
    for c in cands.values():
        for k, v in vices.get((c['uf'], str(c['cd']), c['n']), {}).items():
            c[k] = v
    print('candidatos', len(cands))

    # ---------- complementar ----------
    z = baixar('comp')
    for _, r in linhas(z, lambda n: True):
        c = cands.get(r['SQ_CANDIDATO'])
        if not c:
            continue
        c['idade'] = limpo(r['NR_IDADE_DATA_POSSE'])
        c['nmun'] = titulo(r['NM_MUNICIPIO_NASCIMENTO'])
        c['lim'] = round(num(r['VR_DESPESA_MAX_CAMPANHA']), 2)
        c['reel'] = 1 if r['ST_REELEICAO'] == 'S' else 0
        jul = titulo(r.get('DS_SITUACAO_JULGAMENTO_URNA') or r.get('DS_SITUACAO_JULGAMENTO') or r.get('DS_DETALHE_SITUACAO_CAND'))
        c['sit'] = jul  # Deferido, Indeferido com recurso, Renúncia...
        c['voto'] = limpo(r.get('NM_TIPO_DESTINACAO_VOTOS', ''))  # Válido, Anulado sub judice...
        c['urna'] = 0 if limpo(r.get('ST_CANDIDATO_INSERIDO_URNA', '')).upper().startswith('N') else 1

    # ---------- bens ----------
    perfil = collections.defaultdict(lambda: {'bens': [], 'hist': [], 'doad': [], 'forn': []})
    z = baixar('bens')
    for _, r in linhas(z, lambda n: True):
        sq = r['SQ_CANDIDATO']
        if sq not in cands:
            continue
        v = num(r['VR_BEM_CANDIDATO'])
        perfil[sq]['bens'].append([limpo(r['DS_TIPO_BEM_CANDIDATO']), limpo(r['DS_BEM_CANDIDATO'])[:160], round(v, 2)])
        cands[sq]['bens'] = round(cands[sq].get('bens', 0) + v, 2)

    # ---------- candidaturas anteriores ----------
    z = baixar('hist')
    for _, r in linhas(z, lambda n: True):
        sq = r['SQ_CANDIDATO_ATUAL']
        if sq not in cands or r['ANO_ELEICAO'] == '2026':
            continue
        perfil[sq]['hist'].append([int(r['ANO_ELEICAO']), titulo(r['DS_CARGO']), titulo(r['NM_UE']), limpo(r['SG_PARTIDO']), titulo(r['DS_SIT_TOT_TURNO'])])

    # ---------- dinheiro da campanha ----------
    z = baixar('contas')
    def usa_rec(n): return n.startswith('receitas_candidatos_2026_') and 'doador' not in n
    def usa_desp(n): return n.startswith('despesas_contratadas_candidatos_2026_')
    usa_rec.brasil = False  # lê todos e tira repetidos pelo número da receita
    usa_desp.brasil = False
    visto = set()
    doad = collections.defaultdict(lambda: collections.Counter())
    for n, r in linhas(z, usa_rec):
        sq = r['SQ_CANDIDATO'].strip('"')
        if sq not in cands:
            continue
        chave = ('r', r['SQ_RECEITA'])
        if chave in visto:
            continue
        visto.add(chave)
        v = num(r['VR_RECEITA'])
        cands[sq]['rec'] = round(cands[sq].get('rec', 0) + v, 2)
        quem = titulo(r['NM_DOADOR_RFB'] or r['NM_DOADOR']) or titulo(r['DS_ORIGEM_RECEITA'])
        doad[sq][quem] += v
    forn = collections.defaultdict(lambda: collections.Counter())
    for n, r in linhas(z, usa_desp):
        sq = r['SQ_CANDIDATO'].strip('"')
        if sq not in cands:
            continue
        chave = ('d', r['SQ_DESPESA'])
        if chave in visto:
            continue
        visto.add(chave)
        v = num(r['VR_DESPESA_CONTRATADA'])
        cands[sq]['desp'] = round(cands[sq].get('desp', 0) + v, 2)
        quem = titulo(r['NM_FORNECEDOR_RFB'] or r['NM_FORNECEDOR']) or titulo(r['DS_ORIGEM_DESPESA'])
        forn[sq][quem] += v
    for sq, cnt in doad.items():
        perfil[sq]['doad'] = [[k, round(v, 2)] for k, v in cnt.most_common(10)]
    for sq, cnt in forn.items():
        perfil[sq]['forn'] = [[k, round(v, 2)] for k, v in cnt.most_common(10)]

    # ---------- gravar ----------
    os.makedirs(os.path.join(OUT, 'perfil'), exist_ok=True)
    agora = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%MZ')
    grupos = collections.defaultdict(list)
    for c in cands.values():
        grupos[c['uf']].append(c)
    for uf, lista in grupos.items():
        lista.sort(key=lambda c: (c['cd'], c['nome']))
        with open(os.path.join(OUT, uf + '.json'), 'w') as f:
            json.dump({'gerado': agora, 'c': lista}, f, ensure_ascii=False, separators=(',', ':'))
        pf = {}
        for c in lista:
            p = perfil.get(c['sq'])
            if p:
                p['bens'].sort(key=lambda b: -b[2])
                p['hist'].sort(key=lambda h: -h[0])
                pf[c['sq']] = p
        with open(os.path.join(OUT, 'perfil', uf + '.json'), 'w') as f:
            json.dump({'gerado': agora, 'p': pf}, f, ensure_ascii=False, separators=(',', ':'))
        print(uf, len(lista))


if __name__ == '__main__':
    main()
