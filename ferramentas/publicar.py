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
        if meta.get("categoria") and meta["categoria"] not in CATS: e.append(f"categoria '{meta['categoria']}' não existe")
        if meta.get("assina") != "Redação": e.append("assina precisa ser \"Redação\"")
        if meta.get("data") and not re.match(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$', meta["data"]): e.append("data fora do formato AAAA-MM-DD HH:MM")
        if slug and not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', slug): e.append("slug só pode ter letras minúsculas, números e hífens")
        if slug in antigos: e.append("slug já usado num dos 117 artigos da linha editorial")
        if slug in ja and ja[slug]["pasta"] != pasta: e.append("slug já usado por outro artigo do index.json")
        if len(meta.get("titulo", "")) > 70: avisos.append(f"{rel}: título com mais de 70 caracteres")
        n = len(re.findall(r'\w+', corpo))
        if n < 600: avisos.append(f"{rel}: só {n} palavras")
        for img in re.findall(r'^!\[[^\]]*\]\(([^)\s]+)\)\s*$', corpo, re.M):
            f = os.path.basename(img)
            if not os.path.exists(os.path.join(os.path.dirname(md), f)) and f not in txt.split('---', 2)[1]:
                e.append(f"imagem '{f}' não está na pasta nem na lista imagens:")
        if e:
            erros += [f"{rel}: {x}" for x in e]; continue
        arquivos = [os.path.basename(md)] + sorted(f for f in os.listdir(os.path.dirname(md)) if f.lower().endswith(IMG_EXT))
        item = {"slug": slug, "pasta": pasta, "arquivos": arquivos, "titulo": meta["titulo"], "data": meta["data"]}
        if slug not in ja: novos.append(item)
        ja[slug] = item
    idx["artigos"] = sorted(ja.values(), key=lambda a: (a.get("data", ""), a["slug"]))
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
