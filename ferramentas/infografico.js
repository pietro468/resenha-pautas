#!/usr/bin/env node
/*
  Gera infográficos no estilo do Resenha Rentável (PNG, 1600 px de largura).

  Uso:
    NODE_PATH=$(npm root -g) node ferramentas/infografico.js caminho/do/grafico.json

  O .json diz o tipo e os dados. O PNG sai no caminho do campo "saida"
  (relativo ao .json). Depois de gerar, o .json pode ser apagado.

  Tipo "tabela" (comparação lado a lado, ex.: hoje x proposta, deputado x senador):
  {
    "tipo": "tabela",
    "saida": "fim-da-escala-6x1-tabela.png",
    "chapeu": "PEC 221/2019",
    "titulo": "Fim da escala 6x1: hoje x proposta",
    "colunas": ["", "Como é hoje", "O que a PEC propõe"],
    "linhas": [
      ["Jornada semanal", "Até 44 horas", "Até 40 horas, sem redução de salário"],
      ["Folga semanal", "1 dia", "2 dias remunerados"]
    ],
    "fonte": "Câmara dos Deputados, Agência Senado"
  }

  Tipo "barras" (números para comparar, com 1 ou 2 séries):
  {
    "tipo": "barras",
    "saida": "filmes-mais-caros-custo-bilheteria.png",
    "titulo": "Custo x bilheteria dos filmes mais caros",
    "subtitulo": "Custo de produção e bilheteria mundial, em dólares",
    "series": ["Custo de produção", "Bilheteria mundial"],
    "itens": [
      {"nome": "Star Wars: O Despertar da Força", "detalhe": "2015",
       "valores": [638.9, 2070], "rotulos": ["US$ 638,9 mi", "US$ 2,07 bi"], "nota": "Lucro com folga"}
    ],
    "fonte": "Fortune (jun/2026), Forbes"
  }

  Tipo "passos" (linha do tempo ou passo a passo, de 3 a 6 etapas):
  {
    "tipo": "passos",
    "saida": "como-uma-lei-e-aprovada.png",
    "titulo": "Como uma lei federal é aprovada",
    "passos": [
      {"rotulo": "1", "titulo": "Projeto apresentado", "texto": "Deputado, senador, presidente ou cidadãos"},
      {"rotulo": "2", "titulo": "Casa iniciadora", "texto": "Comissões e plenário votam"}
    ],
    "fonte": "Câmara dos Deputados"
  }
*/
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const spec_path = process.argv[2];
if (!spec_path) { console.error('Uso: node ferramentas/infografico.js grafico.json'); process.exit(1); }
const S = JSON.parse(fs.readFileSync(spec_path, 'utf8'));
const out = path.resolve(path.dirname(spec_path), S.saida || 'infografico.png');

const all = JSON.stringify(S);
if (/[–—]/.test(all)) { console.error('ERRO: o infográfico tem travessão ou meia-risca. Troque por vírgula, dois-pontos ou parênteses.'); process.exit(1); }

const FONTES = path.join(__dirname, 'fontes');
const ff = (n) => 'file://' + path.join(FONTES, n);
const esc = (s) => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

const css = `
@font-face{font-family:A;font-weight:800;src:url(${ff('archivo-latin-800-normal.woff2')})}
@font-face{font-family:A;font-weight:900;src:url(${ff('archivo-latin-900-normal.woff2')})}
@font-face{font-family:P;font-weight:400;src:url(${ff('ibm-plex-sans-latin-400-normal.woff2')})}
@font-face{font-family:P;font-weight:600;src:url(${ff('ibm-plex-sans-latin-600-normal.woff2')})}
body{margin:0}
#c{width:1600px;background:#f5f4ee;color:#1d3b2f;padding:80px 90px 60px;box-sizing:border-box;font-family:P}
.kick{font-family:A;font-weight:800;font-size:24px;letter-spacing:3px;color:#557060;margin:0 0 12px;text-transform:uppercase}
h1{font-family:A;font-weight:900;font-size:66px;margin:0 0 14px;line-height:1.05}
.sub{font-size:28px;margin:0 0 40px;color:#3d5a4d}
.foot{display:flex;justify-content:space-between;align-items:flex-end;margin-top:44px;font-size:20px;color:#557060;gap:30px}
.foot b{font-family:A;font-weight:900;color:#1d3b2f;letter-spacing:3px;font-size:22px;white-space:nowrap}
/* tabela */
table{width:100%;border-collapse:collapse;margin-top:30px}
th{font-family:A;font-weight:800;font-size:30px;text-align:left;padding:0 20px 22px 0}
td{font-size:27px;line-height:1.4;padding:26px 20px 26px 0;border-top:2px solid #d9dccf;vertical-align:top}
td.k{font-family:A;font-weight:800;font-size:21px;letter-spacing:2.5px;text-transform:uppercase;color:#4f7a62;width:22%;padding-top:30px}
/* barras */
.leg{display:flex;gap:40px;font-size:24px;font-weight:600;margin-bottom:36px}
.leg span{display:inline-block;width:26px;height:26px;border-radius:6px;vertical-align:-5px;margin-right:10px}
.row{display:grid;grid-template-columns:420px 1fr;gap:30px;align-items:center;padding:28px 0;border-top:2px solid #d9dccf}
.name{font-family:A;font-weight:800;font-size:32px;line-height:1.15}
.name small{display:block;font-family:P;font-weight:400;font-size:22px;color:#557060;margin-top:6px}
.bl{display:flex;align-items:center;gap:14px;margin:6px 0;font-weight:600;font-size:22px;white-space:nowrap}
.bar{height:40px;border-radius:8px;min-width:6px}
.s0{background:#1d3b2f}.s1{background:#a9c5b0}
.nota{font-weight:600;font-size:22px;margin-top:6px}
/* passos */
.steps{display:grid;gap:26px;margin-top:30px}
.step{display:grid;grid-template-columns:110px 1fr;gap:28px;align-items:start;padding:26px 0;border-top:2px solid #d9dccf}
.num{width:96px;height:96px;border-radius:50%;background:#1d3b2f;color:#f5f4ee;font-family:A;font-weight:900;font-size:40px;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1}
.step h3{font-family:A;font-weight:800;font-size:34px;margin:6px 0 8px}
.step p{font-size:26px;line-height:1.4;margin:0;color:#2f4d40}
`;

let body = '';
if (S.chapeu) body += `<div class="kick">${esc(S.chapeu)}</div>`;
body += `<h1>${esc(S.titulo)}</h1>`;
if (S.subtitulo) body += `<p class="sub">${esc(S.subtitulo)}</p>`;

if (S.tipo === 'tabela') {
  const cols = S.colunas || [];
  body += '<table><thead><tr>' + cols.map((c) => `<th>${esc(c)}</th>`).join('') + '</tr></thead><tbody>';
  for (const l of S.linhas || []) {
    body += '<tr>' + l.map((c, i) => `<td class="${i === 0 ? 'k' : ''}">${esc(c)}</td>`).join('') + '</tr>';
  }
  body += '</tbody></table>';
} else if (S.tipo === 'barras') {
  const series = S.series || [];
  if (series.length > 1) body += '<div class="leg">' + series.map((s, i) => `<div><span class="s${i}"></span>${esc(s)}</div>`).join('') + '</div>';
  const max = Math.max(...(S.itens || []).flatMap((it) => it.valores || [0]), 1);
  for (const it of S.itens || []) {
    body += `<div class="row"><div class="name">${esc(it.nome)}${it.detalhe ? `<small>${esc(it.detalhe)}</small>` : ''}</div><div>`;
    (it.valores || []).forEach((v, i) => {
      const w = Math.round((v / max) * 760);
      body += `<div class="bl"><div class="bar s${i % 2}" style="width:${w}px"></div>${esc((it.rotulos || [])[i] || v)}</div>`;
    });
    if (it.nota) body += `<div class="nota">${esc(it.nota)}</div>`;
    body += '</div></div>';
  }
} else if (S.tipo === 'passos') {
  body += '<div class="steps">';
  (S.passos || []).forEach((p, i) => {
    body += `<div class="step"><div class="num">${esc(p.rotulo || i + 1)}</div><div><h3>${esc(p.titulo)}</h3>${p.texto ? `<p>${esc(p.texto)}</p>` : ''}</div></div>`;
  });
  body += '</div>';
} else {
  console.error('ERRO: "tipo" precisa ser "tabela", "barras" ou "passos".'); process.exit(1);
}
body += `<div class="foot"><div>${S.fonte ? 'Fontes: ' + esc(S.fonte) : ''}</div><b>RESENHA RENTÁVEL</b></div>`;

const html = `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body><div id="c">${body}</div></body></html>`;

(async () => {
  const opts = {};
  if (fs.existsSync('/opt/pw-browsers/chromium')) opts.executablePath = '/opt/pw-browsers/chromium';
  let b;
  try { b = await chromium.launch(opts); } catch (e) { b = await chromium.launch(); }
  const p = await b.newPage({ viewport: { width: 1600, height: 900 } });
  const tmp = path.join(require('os').tmpdir(), 'rr-info-' + process.pid + '.html');
  fs.writeFileSync(tmp, html);
  await p.goto('file://' + tmp);
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  await (await p.$('#c')).screenshot({ path: out });
  await b.close();
  fs.unlinkSync(tmp);
  console.log('OK: ' + out);
})().catch((e) => { console.error('ERRO ao gerar: ' + e.message); process.exit(1); });
