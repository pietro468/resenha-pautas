# Eleições 2026: pautas combinadas com o Pietro (2 a 5 de outubro)

Este arquivo manda nas datas abaixo. Onde ele conflitar com a grade normal da `ROTINA.md`, vale ele.
Leia antes `linha-editorial.md`, `instagram.md` e as regras do fim da `ROTINA.md`. Tudo continua valendo: sem travessão, fonte para cada fato, fotos livres ou de reprodução com origem (nunca agência), títulos com estrutura variada (no máximo 1 em cada 3 com dois-pontos), sem "link na bio".

## Regras especiais da eleição (não podem falhar)

- **Neutralidade total.** Nunca sugerir voto, nunca adjetivo para candidato, nunca "favorito", nunca pesquisa eleitoral. Todos os candidatos com o mesmo espaço e o mesmo tratamento, em ordem alfabética quando for lista.
- **Nenhum número de resultado antes das 17h de 4/10** (horário de Brasília). Parcial só com o arquivo `eleicao/apuracao.json`, que o GitHub atualiza a cada 10 minutos a partir das 17h. Diga sempre a porcentagem de urnas apuradas e a hora do TSE.
- **"Eleito", "2º turno" e "Não eleito" só quando o TSE confirmar** (campo `st` do `apuracao.json`). Antes disso, é "lidera", "está à frente".
- Categoria: explicadores de eleição e resultados vão em **Opinião** (é a categoria de política e cidadania da seção 3). Custo da eleição vai em **Economia**. Tudo assinado pela **Redação**.
- **Fonte oficial primeiro:** TSE (tse.jus.br), TREs, Câmara, Senado, Planalto. O guia do site em https://resenharentavel.com/guia-do-eleitor/ já tem os fatos confirmados de horário, documentos, justificativa e multa, com as fontes no fim (não abra esse endereço com WebFetch; as fontes estão listadas aqui embaixo).
- **Links do site** para usar no texto (sem abrir): candidatos em https://resenharentavel.com/candidatos/ ("Quem está na sua urna"), guia em https://resenharentavel.com/guia-do-eleitor/ ("Tira-dúvidas do eleitor") e apuração em https://resenharentavel.com/apuracao/.
- Fontes já checadas pelo Pietro e por mim (use e confirme): [Manual do Eleitor TSE](https://www.tse.jus.br/comunicacao/noticias/2026/Setembro/manual-do-eleitor-veja-como-se-preparar-para-a-votacao), [horário](https://www.tse.jus.br/comunicacao/noticias/2026/Setembro/faltam-26-dias-votacao-comeca-e-termina-no-mesmo-horario-em-todo-o-pais), [ordem dos 6 votos (TRE-SP)](https://www.tre-sp.jus.br/comunicacao/noticias/2026/Agosto/eleicoes-2026-confira-a-ordem-dos-6-votos-na-urna-e-como-usar-a-colinha-eleitoral), [regras do dia](https://www.tse.jus.br/comunicacao/noticias/2026/Setembro/por-dentro-das-eleicoes-confira-as-regras-para-o-dia-da-votacao), [justificativa](https://www.tse.jus.br/comunicacao/noticias/2026/Setembro/faltam-13-dias-saiba-como-justificar-a-ausencia-nas-eleicoes-2026), [multa R$ 3,51 (CNN)](https://www.cnnbrasil.com.br/eleicoes/eleicoes-2026-saiba-qual-o-valor-da-multa-para-quem-nao-votar/), [quem é obrigado (TRE-RS)](https://www.tre-rs.jus.br/comunicacao/noticias/2026/Setembro/eleicoes-2026-quem-e-obrigado-a-votar-nas-eleicoes-2026-veja-as-regras-e-as-consequencias-de-nao-comparecer), [caminho do voto](https://www.tse.jus.br/comunicacao/noticias/2026/Setembro/faltam-7-dias-veja-qual-e-o-caminho-do-voto-depois-de-encerrada-a-votacao), [calendário](https://www.tse.jus.br/comunicacao/noticias/2026/Marco/eleicoes-2026-confira-as-principais-datas-do-calendario-eleitoral).
- **Candidatos a presidente:** são 13 na urna. A lista oficial, com número, partido, vice, bens e dinheiro de campanha, está em `candidatos/2026/br.json` (use só os que têm `"urna": 1`). Os planos de governo oficiais, em texto, estão em `eleicao/planos/` (o GitHub baixa do TSE; `arquivos.txt` lista os PDFs originais). Fotos oficiais: `https://resultados.tse.jus.br/oficial/ele2026/6257/fotos/br/SQ.jpeg` (SQ = campo `sq`), crédito `Reprodução/TSE`.
- **Imagens do dia:** urna eletrônica, seção eleitoral, fila de votação, mesários (Commons tem fotos livres do TSE e da Agência Brasil com licença livre; confira a licença). Nunca foto de candidato em ato de campanha.
- **Instagram junto com o site:** todo artigo destas datas sai no site e no Instagram na mesma hora (o `carrossel.json` usa o horário do artigo). Posts só do Instagram vão em `instagram/AAAA-MM-DD/SLUG/post.json`.

## Sexta, 2/10 (a grade normal continua; estas 4 são a mais)

Escritas na rodada extra de quinta à noite, já com a data de sexta. Pasta `artigos/2026-10-02/`.

| Hora | Onde | Pauta |
|---|---|---|
| 09:00 | Site + IG (carrossel) | **O que faz e quanto ganha cada cargo que você vai eleger.** Presidente, governador, senador, deputado federal e deputado estadual: o que cada um faz (Constituição), tempo de mandato (4 anos; senador 8) e o salário (subsídio) atual com fonte oficial (Câmara, Senado, Planalto, Assembleias). Diga que o de governador e deputado estadual muda de estado para estado e dê um exemplo com fonte. Carrossel: um slide por cargo. |
| 13:00 | Site + IG (carrossel) | **Os 6 votos na ordem da urna.** Ordem, quantos dígitos cada um tem, o cuidado com os 2 votos de senador (3 dígitos, candidatos diferentes), confirma, branco e nulo, colinha de papel pode e celular não. Link para "Quem está na sua urna" para montar a colinha. Carrossel no estilo passo a passo. |
| 15:00 | Site + IG (carrossel) | **O que prometem os 13 candidatos a presidente.** Um bloco por candidato, em **ordem alfabética**, mesmo tamanho para todos: nome, número, partido, vice e de 3 a 5 propostas principais tiradas do plano oficial registrado no TSE (arquivos em `eleicao/planos/`), com as palavras do plano, sem julgar se é bom ou ruim. Link para o plano oficial no site do TSE (DivulgaCandContas) e para "Quem está na sua urna". No carrossel: capa neutra (sem foto de um candidato só; use a urna ou `"capa":"nenhuma"`) e um slide por candidato com a foto oficial do TSE. Se o plano de algum candidato não estiver no TSE, diga isso no bloco dele. |
| 18:00 | Site + IG (carrossel) | **Quanto custa uma eleição no Brasil.** Orçamento do TSE para as eleições de 2026, número de urnas, seções e mesários, e o dinheiro público das campanhas (Fundo Especial de Financiamento de Campanha, o "fundão") com o valor oficial de 2026. Categoria Economia. Só números oficiais. |

## Sábado, 3/10 (a grade normal continua; estas 2 são a mais)

Escritas na rodada extra de sexta à noite. Pasta `artigos/2026-10-03/` e `instagram/2026-10-03/`.

| Hora | Onde | Pauta |
|---|---|---|
| 09:00 | Site + IG (carrossel) | **O que é proibido amanhã, no dia da eleição.** Boca de urna é crime, manifestação só individual e silenciosa (camiseta, broche, adesivo pode), celular fora da cabine, distribuir camiseta não pode, eleitor não pode ser preso de 29/9 a 6/10 salvo exceções, direito de sair do trabalho para votar. Diga que a venda de bebida alcoólica depende de cada estado e só cite estado com fonte oficial. |
| 18:00 | IG (imagem única) | **Checklist para amanhã:** documento com foto (ou e-Título com foto), colinha de papel, local de votação no e-Título, das 8h às 17h de Brasília. `"formato": "unico"`, `"capa_estilo": "hoje"` ou `urgente` com chamada "AMANHÃ É DIA DE VOTAR:". Legenda com os detalhes e link do guia escrito por extenso. |

## Domingo, 4/10 (só eleição)

**A grade normal não roda neste dia** (sem notícia, Pietro, Pedro, pauta pendente, biografia, hoje na história, curiosidades). As rodadas normais de domingo só conferem se tudo abaixo está no repositório e corrigem o que faltar.

Madrugada e manhã: escritas na rodada extra de sábado à noite. Pasta `artigos/2026-10-04/` e `instagram/2026-10-04/`.

| Hora | Onde | Pauta |
|---|---|---|
| 05:30 | Site + IG | **Não vai votar? Como justificar hoje ou depois.** e-Título ou formulário em qualquer seção, sem comprovante no dia; depois, até 3/12 com documento; multa de R$ 3,51 por turno; o que acontece com 3 faltas seguidas. |
| 06:00 | Site + IG | **Voto útil no 1º turno: o que é e por que ele aparece.** Explicador neutro: voto útil é deixar de votar no candidato preferido para tentar barrar outro. No 1º turno, se ninguém passar de 50% dos válidos, os dois primeiros vão ao 2º turno, então o 1º turno é o momento de votar em quem você prefere; o voto estratégico existe e é uma escolha do eleitor. Nada de "matematicamente impossível", nenhum nome de candidato como exemplo, nenhuma pesquisa. |
| 06:30 | Site + IG | **Horário e documento: o que levar para votar hoje.** 8h às 17h de Brasília e os horários locais (AC, AM, RO, MT, MS, RR, Noronha); fila às 17h vota; documentos que valem e os que não valem; e-Título só com foto. |
| 07:00 | IG (frase do dia) | Já planejada: Lyndon B. Johnson, 1965 (`instagram/frases-planejadas.md`). A rodada normal de sábado à noite faz. |
| 07:15 | Site + IG | **Onde eu voto?** Como achar a seção no e-Título e no site do TSE com título ou CPF; o local pode ter mudado. |
| 07:30 | Site + IG | **A ordem dos 6 votos (colinha).** Versão curta e prática da matéria de sexta, com link para ela e para "Quem está na sua urna". |
| 08:00 | IG (imagem única) | **Urnas abertas.** Chamada "AGORA:", "Urnas abertas em todo o Brasil até as 17h (horário de Brasília)". Foto de urna ou seção eleitoral. |
| 12:30 | IG (frase do dia) | Abraham Lincoln: "O voto é mais forte do que a bala." Legenda explicando que a frase vem do relato de jornal de um discurso de 1856 (confirme a fonte) e o contexto. |
| 16:00 | IG (imagem única) | **Falta 1 hora para fechar as urnas.** Quem estiver na fila às 17h vota. |
| 17:05 | Site + IG | **Urnas fechadas: o que acontece agora.** Boletim de urna, transmissão, assinatura digital, totalização e onde acompanhar (link da apuração do site). Pode ser escrita no sábado. |

Noite: rodadas extras às 18h, 19h30, 21h e 22h45. Cada uma lê `eleicao/apuracao.json` (faça `git pull` antes; confira o campo `gerado`).

| Quando | Onde | Pauta |
|---|---|---|
| Rodada das 18h, 19h30 e 21h | IG (imagem única) | **Parcial de presidente**, `"capa_estilo": "placar"`, chamada "APURAÇÃO AO VIVO:", gancho com a % de urnas apuradas ("Com ==X% das urnas apuradas==, veja como está a votação para presidente"), 4 linhas com os 4 primeiros (nome, % dos válidos), `"fonte": "TSE, às HH:MM"`. `"data"` = hora atual + 5 minutos. Só se `pres.pst` for maior que 0. Se nada mudou muito desde a última parcial (menos de 10 pontos de urnas apuradas), pule. |
| Assim que o TSE definir (campo `st` de todos os 13 preenchido, ou `final: true`) | Site + IG | **Resultado para presidente.** Se alguém foi eleito: quem, com quantos votos e %; os demais em ordem de votos. Se tem 2º turno: título dizendo quem disputa. Números exatos do TSE, hora da totalização. |
| Junto, ou na rodada seguinte | Site + IG | **Quem vai para o 2º turno para presidente e o que acontece até 25 de outubro.** Os dois candidatos (número, partido, vice, % no 1º turno), a data (25/10, das 8h às 17h), que no 2º turno só há presidente e governador onde houver, propaganda na TV de 9 a 23/10, e link para "Quem está na sua urna". Se não houver 2º turno para presidente, troque por "O que acontece agora até a posse, em 5 de janeiro". |

## Segunda, 5/10 (tudo até as 11h)

Escritas na rodada extra de segunda às 4h30. Pasta `artigos/2026-10-05/`. Se a matéria do 2º turno de presidente não saiu no domingo, ela é a primeira (06:30). Na rodada normal da manhã, **não faça a notícia das 08:00** (estas são as notícias do dia) e mande o "Hoje na história" para as 11:30; o resto da grade segue normal.

| Hora | Onde | Pauta |
|---|---|---|
| 07:00 | Site + IG | **Governadores: quem foi eleito e onde tem 2º turno.** Os 27 estados em tabela (eleitos e os que vão para o 2º turno, com os dois nomes), números do TSE. |
| 08:30 | Site + IG | **Os senadores eleitos em cada estado.** Dois por estado, com partido e votos. |
| 10:00 | Site + IG | **Os deputados federais mais votados do Brasil.** Os 10 ou 20 primeiros de `dep_federal_top`, com estado, partido e votos. Explique rápido por que mais voto não garante vaga (as vagas vão primeiro para os partidos). |
