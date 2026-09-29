#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Confere os artigos da pasta artigos/ e atualiza o index.json que o site lê.

Uso:  python3 ferramentas/publicar.py
Sai com código 1 se algum artigo novo tiver erro (nesse caso, corrija e rode de novo).
"""
import json, os, re, sys, glob, datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(RAIZ, 'index.json')
CATS = {"Economia", "Geopolítica", "Negócios", "Investigação", "Biografias", "Cinema", "Opinião", "Viagem"}
OBRIG = ["titulo", "subtitulo", "data", "categoria", "assina", "frase_chave", "meta_descricao", "slug", "capa_url", "capa_credito"]
IMG_EXT = (".png", ".jpg", ".jpeg", ".webp", ".gif")

def front(txt):
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', txt, re.S)
    if not m: return None, txt
    meta = {}
    for ln in m.group(1).split('\n'):
        mm = re.match(r'^([A-Za-z_]+)\s*:\s*(.*)$', ln)
        if mm:
            v = mm.group(2).strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in '"\'': v = v[1:-1]
            meta[mm.group(1).lower()] = v
    return meta, txt[m.end():]

def slugs_da_linha():
    p = os.path.join(RAIZ, 'linha-editorial.md')
    if not os.path.exists(p): return set()
    return set(re.findall(r'\|\s*[^|\n]+\|\s*([a-z0-9][a-z0-9-]+)\s*\|\s*$', open(p, encoding='utf-8').read(), re.M))

def main():
    idx = json.load(open(INDEX, encoding='utf-8')) if os.path.exists(INDEX) else {"artigos": []}
    ja = {a["slug"]: a for a in idx.get("artigos", [])}
    antigos = slugs_da_linha()
    # pautas pendentes ainda não foram escritas: os slugs delas estão liberados
    pp = os.path.join(RAIZ, 'pautas-pendentes.md')
    if os.path.exists(pp):
        _pp = open(pp, encoding='utf-8').read()
        pendentes = set(re.findall(r'\*\*Slug:\*\*\s*([a-z0-9-]+)', _pp))
        antigos -= pendentes
        antigos |= set(re.findall(r'^- \d+\. ([a-z0-9-]+)\s*$', _pp, re.M))
    # artigos que já existem no site: os da linha editorial que não estão pendentes + os do index.json
    no_ar = set(antigos) | set(ja)
    novos_slugs = {os.path.basename(os.path.dirname(m)) for m in glob.glob(os.path.join(RAIZ, 'artigos', '**', '*.md'), recursive=True)}
    erros, novos, avisos = [], [], []
    for md in sorted(glob.glob(os.path.join(RAIZ, 'artigos', '**', '*.md'), recursive=True)):
        txt = open(md, encoding='utf-8').read()
        meta, corpo = front(txt)
        rel = os.path.relpath(md, RAIZ)
        if meta is None:
            erros.append(f"{rel}: sem o bloco --- no topo"); continue
        slug = meta.get("slug", "")
        pasta = os.path.relpath(os.path.dirname(md), RAIZ).replace(os.sep, '/')
        e = []
        for k in OBRIG:
            if not meta.get(k): e.append(f"campo '{k}' vazio")
        if '—' in txt or '–' in txt: e.append("tem travessão ou meia-risca (troque por vírgula, dois-pontos ou parênteses)")
        if meta.get("categoria") == "Biografias" and meta.get("assina") != "Redação": e.append("biografia sempre sai assinada pela Redação")
        if meta.get("categoria") and meta["categoria"] not in CATS: e.append(f"categoria '{meta['categoria']}' não existe")
        if meta.get("assina") not in ("Redação", "Pietro Krauss", "Pedro Paracampos"): e.append("assina precisa ser \"Redação\", \"Pietro Krauss\" ou \"Pedro Paracampos\"")
        if meta.get("data") and not re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$', meta["data"]): e.append("data fora do formato AAAA-MM-DD HH:MM")
        if slug and not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', slug): e.append("slug só pode ter letras minúsculas, números e hífens")
        if slug in antigos: e.append("slug já usado num dos 117 artigos da linha editorial")
        if slug in ja and ja[slug]["pasta"] != pasta: e.append("slug já usado por outro artigo do index.json")
        for ln in re.findall(r'resenharentavel\.com/([a-z0-9-]+)/?\)', corpo):
            if ln not in no_ar and ln != slug and ln not in novos_slugs: e.append(f"link interno para '{ln}', que ainda não está publicado (use só artigos que já estão no ar)")
        if len(meta.get("titulo", "")) > 70: avisos.append(f"{rel}: título com mais de 70 caracteres")
        n = len(re.findall(r'\w+', corpo))
        if n < 600: avisos.append(f"{rel}: só {n} palavras")
        for img in re.findall(r'^!\[[^\]]*\]\(([^)\s]+)\)\s*$', corpo, re.M):
            f = os.path.basename(img)
            if not os.path.exists(os.path.join(os.path.dirname(md), f)) and f not in txt.split('---', 2)[1]:
                e.append(f"imagem '{f}' não está na pasta nem na lista imagens:")
        fm_txt = txt.split('---', 2)[1]
        if meta.get("categoria") == "Biografias":
            if not meta.get("pessoa"): e.append("biografia sem o campo pessoa")
            if len(re.findall(r'^\s*-\s*arquivo:', fm_txt, re.M)) < 2: e.append("biografia precisa de pelo menos 2 fotos da pessoa em imagens:")
        if re.search(r'\.png\s*$', meta.get("capa_url", ""), re.I): avisos.append(f"{rel}: capa em PNG parece gráfico; a capa deve ser foto")
        if not meta.get("busca_imagem"): avisos.append(f"{rel}: sem busca_imagem")
        if e:
            erros += [f"{rel}: {x}" for x in e]; continue
        arquivos = [os.path.basename(md)] + sorted(f for f in os.listdir(os.path.dirname(md)) if f.lower().endswith(IMG_EXT))
        cj = os.path.join(os.path.dirname(md), 'carrossel.json')
        if os.path.exists(cj):
            arquivos.append('carrossel.json')
            try:
                car = json.load(open(cj, encoding='utf-8'))
                ctxt = json.dumps(car, ensure_ascii=False)
                if '\u2014' in ctxt or '\u2013' in ctxt or '—' in ctxt or '–' in ctxt: e.append("carrossel.json tem travessão ou meia-risca")
                if car.get("estilo") != "frase": e.append('carrossel.json sem "estilo": "frase" (o gancho da capa sai sempre em frase normal, ver instagram.md)')
                if not car.get("gancho"): e.append("carrossel.json sem gancho")
                elif len(car["gancho"]) > 95: e.append("gancho do carrossel com mais de 95 caracteres")
                if car.get("formato", "carrossel") != "unico" and meta.get("data", "") >= "2026-09-29 13:00":  # regra de início, meio, fim e CTA
                    sl = car.get("slides", [])
                    if not sl or sl[-1].get("tipo") not in ("final", "cta"): e.append('carrossel.json: o último slide precisa ser o CTA {"tipo": "final"} (ver instagram.md)')
                    elif len(sl) < 5: e.append("carrossel.json com poucos slides: precisa de notícia, meio, conclusão e CTA (mínimo 5 depois da capa)")
                if len(car.get("slides", [])) > 9: e.append("carrossel com mais de 9 slides além da capa (limite do Instagram é 10)")
                if len(car.get("legenda", "")) > 2100: e.append("legenda do carrossel com mais de 2100 caracteres")
                if not car.get("legenda"): e.append("carrossel.json sem legenda")
            except Exception as ex:
                e.append(f"carrossel.json inválido ({ex})")
        else:
            avisos.append(f"{rel}: sem carrossel.json (o post não vai para o Instagram)")
        if e:
            erros += [f"{rel}: {x}" for x in e]; continue
        item = {"slug": slug, "pasta": pasta, "arquivos": arquivos, "titulo": meta["titulo"], "data": meta["data"]}
        if slug not in ja: novos.append(item)
        ja[slug] = item
    idx["artigos"] = sorted(ja.values(), key=lambda a: (a.get("data", ""), a["slug"]))
    # títulos: no máximo 1 em cada 3 com dois-pontos no mesmo dia (vale a partir de 30/09/2026)
    dias = {}
    for a in idx["artigos"]:
        if a.get("data", "") >= "2026-09-30": dias.setdefault(a["data"][:10], []).append(a)
    for d, arts in dias.items():
        c = [a["titulo"] for a in arts if ":" in a["titulo"]]
        if len(c) > max(1, len(arts) // 3):
            erros.append(f"{d}: títulos demais com dois-pontos ({len(c)} de {len(arts)}). Reescreva com outra estrutura (ver regra do título na linha editorial): " + " | ".join(c))
    idx["atualizado"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    for a in avisos: print("AVISO:", a)
    if erros:
        print("\nERROS (corrija antes de enviar):")
        for x in erros: print(" -", x)
        sys.exit(1)
    json.dump(idx, open(INDEX, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f"OK. {len(novos)} artigo(s) novo(s) no index.json:")
    for a in novos: print(f"  {a['data']}  {a['titulo']}")

if __name__ == '__main__':
    main()
