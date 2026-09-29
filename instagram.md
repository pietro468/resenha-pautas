# Carrossel do Instagram (@resenharentavel)

Toda matéria ganha um post no Instagram: carrossel ou imagem única. O Instagram do Resenha é um perfil de notícias: o post precisa parar o dedo de quem está rolando o feed. O site monta as imagens sozinho a partir do arquivo `carrossel.json` que você salva na pasta do artigo (mesma pasta do .md). Você escreve os textos; o site desenha os slides com as fotos da matéria e publica no Instagram na hora em que a matéria entra no ar.

## Identidade visual (sempre a mesma)

O visual é sempre o de empresa de notícias: foto forte em tela cheia, degradê escuro, texto branco, detalhe em verde e o logo pequeno no topo. Nada de estilo "print de tweet" ou fundo branco com texto. O que varia é o **formato** e o **jeito de escrever o gancho**, nunca a identidade.

## Os dois formatos de post

- **Imagem única** (`"formato": "unico"`): uma foto com uma frase, sem slides. Use para **notícia urgente ou de hoje**, quando a frase já é a notícia ("Governo publica MP que proíbe as bets"). O texto sai em frase normal, alinhado à esquerda, com a chamada em cima ("URGENTE:", "ÀS VÉSPERAS DO 1º TURNO:", "AGORA:"). A legenda conta a notícia.
- **Carrossel** (`"formato": "carrossel"`, o padrão): capa + slides. Use para explicativos, rankings, comparações, biografias e temas livres.

Para as notícias do dia, prefira a imagem única quando o fato é simples e acabou de acontecer; carrossel quando a notícia pede explicação ("o que muda para você"). Ao longo do dia, **intercale**: não publique 3 posts seguidos no mesmo formato e com o mesmo tipo de gancho.

## A capa é o que importa

A capa decide se a pessoa arrasta ou passa reto. Ela é sempre: foto da matéria em tela cheia, degradê escuro embaixo, a **chamada** pequena em verde e o **gancho** grande.

**Foto:** a capa usa a foto de capa da matéria (`"capa": "capa"`). Se outra foto da matéria for mais forte (um rosto conhecido, uma cena marcante, algo que explica a notícia sozinho), use o nome do arquivo dela. Por isso, escolha a foto de capa do artigo já pensando no Instagram: pessoa reconhecível, emoção, cena icônica. Evite foto genérica, prédio sem graça ou pessoa de costas.

**Gancho:** NÃO é o título do site (que é feito para o Google). É a frase que faz a pessoa **parar de rolar o feed**. De 6 a 14 palavras, no máximo 95 caracteres. Escreva **5 opções**, de tipos diferentes, e fique com a mais forte pelo teste abaixo.

**Teste do gancho (pedido do Pietro: o gancho precisa ser muito chamativo).** Antes de escolher, responda: se essa frase aparecesse no feed de alguém que nunca ouviu falar do assunto, a pessoa pararia para ler? O gancho forte tem pelo menos uma destas coisas:
- **Contradição ou surpresa:** algo que parece não fazer sentido. "O Brasil nunca teve tanto emprego. E nunca teve tanta conta atrasada"
- **Você no centro:** mostra o efeito na vida de quem lê. "Seu salário já chega pela metade no fim do mês"
- **Número que choca, concreto:** "R$ 29 de cada R$ 100 do seu salário já são do banco"
- **Segredo ou bastidor:** "O dinheiro de Steve Jobs não veio da Apple"
- **Perda, risco ou conflito:** "Quem tem carteira assinada também está atrasando as contas"
- **Pergunta que a pessoa quer ver respondida:** "Por que o diesel sobe se o Brasil produz petróleo?"

Gancho fraco, que não pode: frase que só descreve o fato em tom de relatório ("Emprego e inadimplência batem recorde"), palavra técnica, "Entenda", "Saiba", "Confira", nome de órgão no começo ("IBGE divulga...", "Banco Central informa..."), e frases longas com vírgula. Compare:
- Fraco: "Emprego e inadimplência batem recorde no Brasil". Forte: "Nunca teve tanta gente trabalhando no Brasil. Então por que tanta conta atrasada?"
- Fraco: "Steve Jobs: como criou a Apple". Forte: "Steve Jobs foi demitido da própria empresa e ficou bilionário fora dela"

O gancho **não precisa ser a matéria em si**. Muitas vezes o melhor gancho é um ângulo lateral, algo do dia a dia do leitor ligado ao assunto, e o carrossel leva até a matéria. Exemplo: numa matéria sobre inflação, em vez de "Inflação de 2026 fica em X%", o gancho "O que dava pra comprar com R$ 50 em 2000 e o que dá hoje?", com os slides comparando produto por produto. Tipos de gancho, para alternar:
- **Ângulo lateral e concreto:** uma pergunta do dia a dia que a matéria responde ("O que dava pra comprar com R$ 50 em 2000 x 2026?").
- **Frase forte, curta, que provoca:** uma verdade que incomoda, com uma palavra de impacto ("A inflação é um imposto que ninguém votou"). Precisa ser sustentada pela matéria e não pode ser opinião política.
- **Número ou dinheiro concreto:** "Beto Carrero cria área da Galinha Pintadinha com R$ 50 milhões".
- **Fala com você:** "O que faz e quanto ganha cada político em quem você vota neste ano".
- **Ranking ou lista:** "Top 10 jogadores com mais partidas por seleções".
- **Nome famoso + fato inesperado:** "O filme mais caro da história não se pagou no cinema".
- **Notícia seca, verbo no presente:** "Governo proíbe as bets e dá 10 dias para sacar o saldo".
- **Curiosidade ou contradição:** "Por que o país que sedia a Copa quase sempre perde dinheiro".

Regras do gancho: verdadeiro e fiel à matéria (nada de exagero ou promessa que o texto não cumpre), sem travessão, sem ponto final, sem clickbait mentiroso, neutro em política. O gancho da capa sai sempre em **frase normal** (fonte Plex em negrito, não em caixa alta), no carrossel e na imagem única: o Pietro achou mais fácil de ler. Por isso, **todo carrossel.json leva `"estilo": "frase"`**. Os títulos dos slides de dentro continuam na Brim.

**Chamada:** 2 a 5 palavras em cima do gancho. No carrossel promete continuação ("DESLIZE PARA VER", "ENTENDA", "VEJA OS NÚMEROS", "VEJA O RANKING"); na imagem única dá o contexto ("URGENTE:", "AGORA:", "ÀS VÉSPERAS DO 1º TURNO:").

## Linguagem simples em todos os slides e na legenda

O Instagram é lido rápido, no celular, por gente que não entende de economia. Escreva como quem explica para um amigo no WhatsApp:
- **Palavra do dia a dia no lugar da técnica:** "conta atrasada" ou "calote" em vez de inadimplência; "gente trabalhando" em vez de população ocupada; "o que sobra do salário" em vez de comprometimento de renda; "juros" em vez de spread; "subiu 1 ponto" em vez de "1 p.p.". Se precisar do termo técnico, explique na mesma frase.
- **Frases curtas:** no máximo umas 15 palavras cada, uma ideia por frase. No máximo 30 palavras por slide.
- **Um número por slide**, e sempre traduzido para algo concreto: "6% do crédito atrasado" vira "de cada R$ 100 emprestados às famílias, R$ 6 estão atrasados".
- **Títulos dos slides também simples e com gancho:** "Por que isso acontece?", "E o seu bolso?", "O problema dos juros", em vez de "Contexto" ou "Dados do Banco Central".
- Antes de enviar, leia cada slide e pergunte: um adolescente de 15 anos entenderia de primeira? Se não, reescreva.

## Variedade: o que alternar

O visual é o mesmo, mas **nenhum post pode parecer cópia do anterior**. Alterne sempre estas três coisas:

**1. Estilo da capa** (`"capa_estilo"`):
- `"classico"` (padrão): uma foto em tela cheia. O estilo mais usado, mas não em todos.
- `"circulo"`: foto principal + uma segunda foto num círculo no canto (`"capa_extra": "arquivo.jpg"`). Bom quando a notícia junta duas coisas (uma empresa e um produto, uma pessoa e um lugar).
- Em `circulo` e `dupla`, use só fotos que você tem certeza que vão baixar (as da lista `imagens:` da matéria, com link testado). Se a segunda foto não existir, o site volta sozinho para a capa simples.
- `"dupla"`: a tela dividida em duas fotos, com um X no meio (`"capa_extra"` e `"rotulos": ["2000", "2026"]` ou `["Antes", "Depois"]`, `["Brasil", "EUA"]`). Bom para comparações e versus.
- Imagem única (`"formato": "unico"`), para notícia urgente.

**2. Destaque no gancho:** marque com `==...==` a palavra ou o número que mais chama atenção; ele sai em verde ("BETO CARRERO CRIA ÁREA DA GALINHA PINTADINHA COM ==R$ 50 MILHÕES=="). Use em mais ou menos metade dos posts, só em 1 a 3 palavras.

**3. Tipos de slide de dentro** (misture 2 ou 3 tipos no mesmo carrossel):
- `"texto"`: foto de fundo escurecida, título verde e texto. `==Rótulo:==` sai em verde, `**trecho**` em negrito, linha em branco separa parágrafos.
- `"texto_claro"`: fundo creme, título grande verde-escuro e texto escuro. Quebra o ritmo entre slides escuros; ótimo para "por que isso acontece" e conclusões.
- `"foto_texto"`: foto grande em cima e o texto num painel verde embaixo. Bom para contar uma história ou mostrar uma pessoa ou lugar (`"foto"`, `"titulo"`, `"texto"`).
- `"numero"`: um número gigante em verde + uma frase. Para o dado que choca.
- `"comparacao"`: duas colunas lado a lado (`"titulo"`, `"esquerda": {"rotulo": "2000", "valor": "1.000", "detalhe": "pães com R$ 50"}`, `"direita"`: {...}, `"texto"` opcional embaixo). Para antes e depois, A x B, preço de ontem x hoje.
- `"citacao"`: aspas grandes, a frase e quem disse (`"texto"`, `"autor"`, `"contexto"`). Só frase real, confirmada, com fonte; nunca de Pietro ou Pedro.
- `"ranking"`: `"posicao": "10°"`, `"nome"`, `"detalhe"` e a foto. Um item por slide.
- `"foto"`: só a foto (com `"texto"` opcional curto embaixo). Bom quando o assunto é visual.

Regra do dia: entre os posts de um mesmo dia, varie o estilo de capa e o tipo de gancho; o `classico` pode ser o mais comum, mas nunca 3 seguidos. Antes de escrever o carrossel, olhe os `carrossel.json` já feitos hoje em `artigos/AAAA-MM-DD/`.

## Os slides de dentro: sempre início, meio, fim e CTA

Todo carrossel conta uma história completa, na ordem abaixo. Nunca termine no meio (só contexto, sem conclusão).

1. **Capa (início):** o gancho, a parte mais chamativa.
2. **A notícia (início):** 1 slide que dá o fato de verdade, direto: o que aconteceu, quem, quanto, quando.
3. **Meio (2 a 4 slides):** contexto (por que aconteceu, como chegou até aqui, os números que explicam) e **implicação na vida das pessoas** (o que muda no bolso, no trabalho, no dia a dia de quem está lendo).
4. **Fim (1 slide):** a conclusão. Amarra tudo numa ideia final: o que isso significa, o que esperar a seguir ou a lição da história. Use de preferência `texto_claro`, com título como "No fim das contas", "O que fica", "E agora?" ou algo próprio do assunto. Não é resumo do que já foi dito: é a leitura final.
5. **CTA (último slide):** `{"tipo": "final"}`. O site desenha sozinho o slide de seguir o perfil, com o texto padrão ("O Instagram provavelmente nunca mais vai mostrar esta página para você." e "Se você quer mais resenhas como esta, é só seguir a gente."). Se quiser variar, use `"titulo"` e `"texto"` com a mesma ideia, curtos e sem travessão. Se esquecer, o site coloca o CTA padrão.

No total, de 5 a 8 slides depois da capa, contando o CTA (limite do Instagram: 10 imagens com a capa). Nada de slide de "leia no link da bio".

**Varie as fotos:** não repita a mesma foto em todos os slides. Se a matéria tem 2 ou mais fotos, cada slide de fundo escuro usa uma foto diferente (capa, depois as fotos do texto, alternando), e a capa do post usa a foto mais forte. Por isso, toda matéria deve ter pelo menos 2 fotos no texto além da capa, sempre que existir foto livre boa do assunto. Cada slide tem **uma ideia** e cabe numa olhada: no máximo umas 45 palavras. Cada slide pode ter `"foto"` (arquivo de uma foto da matéria, ou `"capa"`) para o fundo, e `"fonte"` (de onde veio o dado).

Como a estrutura fica em cada tipo de matéria:
- **Notícia:** capa, "O que aconteceu", 2 slides de contexto e "O que muda para você", conclusão, CTA.
- **Explicativo:** capa, a resposta direta, um slide por item comparado (mesma estrutura de rótulos), conclusão, CTA.
- **Ranking:** capa, um slide `ranking` por item, conclusão (o que o ranking mostra), CTA.
- **Biografia:** capa com o rosto da pessoa, o fato mais marcante, as fases da vida (`foto_texto` funciona muito bem) e os números da fortuna, a lição da trajetória como conclusão, CTA.
- **Imagem única** (`"formato": "unico"`): continua sem slides e sem CTA; a conclusão vai na legenda.

## Legenda

A legenda é uma matéria curta: primeira linha com a notícia ou o gancho em frase normal; depois 3 a 5 parágrafos curtos com os fatos e números principais (com a fonte); depois o crédito das fotos entre parênteses; e por fim "Siga o @resenharentavel para entender como o dinheiro move o mundo." Sem hashtags em excesso (no máximo 3, no fim, se fizer sentido). Sem travessão. Nunca citar Pietro ou Pedro.

## Modelo do carrossel.json

Imagem única: só `formato`, `chamada`, `gancho`, `capa` e `legenda` (sem `slides`).

Carrossel:

```json
{
  "formato": "carrossel",
  "estilo": "frase",
  "gancho": "Fim das bets pode devolver até R$ 117 bilhões por ano ao comércio",
  "chamada": "Deslize para ver",
  "capa": "capa",
  "slides": [
    {"tipo": "numero", "numero": "R$ 117 bi", "texto": "é quanto as apostas online podem tirar do comércio **por ano**, segundo a ==CNC== e o ==IDV==.", "foto": "proibicao-das-bets-varejo-supermercado.jpg", "fonte": "CNC e IDV, via Mercado & Consumo"},
    {"tipo": "texto", "titulo": "O que diz a MP", "texto": "==Sites fora do ar:== até **6 de outubro**.\n\n==Saque do saldo:== até **5/10, às 23h59**.", "foto": "capa", "fonte": "Agência Senado"},
    {"tipo": "texto_claro", "titulo": "No fim das contas", "texto": "A conclusão da história em 2 ou 3 frases.", "fonte": "..."},
    {"tipo": "final"}
  ],
  "legenda": "O fim das bets pode devolver ao comércio parte dos bilhões que iam para as apostas.\n\n..."
}
```

Todo número do carrossel precisa estar na matéria, com fonte. O `ferramentas/publicar.py` confere o arquivo.


## "Hoje na história" (post só do Instagram)

Post de curiosidade, que não vira matéria no site. Sai só quando a data é realmente forte: morte ou nascimento de uma grande personalidade do nicho (Steve Jobs, Michael Jackson, Walt Disney, Senna, Warren Buffett...), de preferência em ano redondo, ou um fato histórico muito curioso do mundo do dinheiro. Nunca force: sem data forte, sem post. No máximo 2 por semana.

Arquivo: `instagram/AAAA-MM-DD/hoje-SLUG/post.json` (AAAA-MM-DD é o dia em que o post sai). Modelo:

```json
{
  "titulo": "Hoje na história: 5 de outubro de 2011, morre Steve Jobs",
  "data": "2026-10-05 10:00",
  "fotos": [
    {"arquivo": "hoje-jobs-2010.jpg", "url": "link direto da foto livre", "credito": "Autor/Acervo (licença)"}
  ],
  "carrossel": {
    "formato": "carrossel", "estilo": "frase", "capa": "capa", "capa_estilo": "hoje",
    "chamada": "Hoje na história", "data_evento": "5 out", "ano": "2011", "ha": "Há 15 anos",
    "gancho": "Morria Steve Jobs, o homem que foi ==demitido da própria empresa== e voltou para salvá-la",
    "slides": [
      {"tipo": "foto", "foto": "hoje-jobs-macintosh-1984.jpg", "texto": "Uma frase curta sobre esta foto."},
      {"tipo": "final"}
    ],
    "legenda": "Hoje, há 15 anos, ..."
  }
}
```

Regras: a capa usa sempre `"capa_estilo": "hoje"` (foto em tela cheia em preto e branco, moldura fina, folha de calendário com o selo "Hoje na história", "HÁ X ANOS" em verde e o gancho em branco; escolha para a capa uma foto de rosto forte, com espaço livre no canto de cima à direita); a primeira foto da lista é a capa. Dentro, **só slides de foto** (`"tipo": "foto"`), de 3 a 6, cada um com uma frase curta (até umas 20 palavras) que conta a história em ordem, e o último é `{"tipo": "final"}`. Fotos sempre com licença livre (Wikimedia Commons: use o arquivo original ou miniatura de 1280px), de preferência da própria pessoa em momentos diferentes da vida. Legenda com a história em 3 a 5 parágrafos curtos, fatos com fonte, crédito das fotos e o "Siga o @resenharentavel...". Mesmas regras de sempre: sem travessão, linguagem simples, nada de polêmica pessoal.


## Frase do dia (post só do Instagram, 1 por dia)

Uma imagem só, sem foto: **o centro é a frase**. Fundo creme, faixa verde-escura na lateral, aspas gigantes em verde-claro ao fundo, "FRASE DO DIA" no canto, a frase grande em verde-escuro (`==trecho==` sai em verde médio, use no trecho mais forte), e embaixo o nome da pessoa e o que ela é. Sai todo dia às 07:00 (escrita no turno da noite do dia anterior).

Arquivo: `instagram/AAAA-MM-DD/frase-SLUG/post.json`. Modelo:

```json
{
  "titulo": "Frase do dia: Warren Buffett e a maré",
  "data": "2026-09-30 07:00",
  "fotos": [],
  "carrossel": {
    "formato": "unico", "estilo": "frase", "capa": "capa", "capa_estilo": "frase_do_dia",
    "gancho": "a frase, sem os ==",
    "frase": "Só quando a maré baixa você descobre quem estava ==nadando pelado==.",
    "autor": "Warren Buffett",
    "cargo": "Investidor, comandou a Berkshire Hathaway por 60 anos",
    "legenda": "..."
  }
}
```

**A legenda explica a frase** (é o que dá valor ao post): 1) a frase entre aspas e o autor; 2) "O que ele quis dizer", em linguagem simples; 3) um exemplo real ou do dia a dia; 4) "A lição para o seu bolso", prática; 5) uma frase sobre quem é a pessoa; 6) "Siga o @resenharentavel...". Sem travessão.

Regras: frase curta (até umas 25 palavras), em português natural; frase real e confirmada numa fonte confiável; tema de dinheiro, trabalho, negócios, risco, disciplina ou carreira; `cargo` curto; nunca frase do Pietro, do Pedro, de político em atividade ou de gente polêmica; não repetir a pessoa em 7 dias.

**Posição do texto em todos os posts:** o texto fica na metade de baixo da imagem, mas nunca encostado na borda: termina a uns 240 px do fim (o site já faz isso sozinho). Na capa "Hoje na história", o selo mostra só "HOJE NA HISTÓRIA", o `ha` ("Há 15 anos") sai pequeno em cima do gancho, o gancho é curto (até umas 10 palavras) e o destaque `==...==` vai no **nome da pessoa**; a capa só fica em preto e branco quando a data é de morte (`"luto": true`); nas outras datas, colorida.


## Aprendizados das referências (set/2026): valem para todo carrossel

**Capa**
- Rosto grande e próximo vence prédio, objeto ou paisagem. Em lista ou ranking de pessoas, use 2 ou 3 rostos (`dupla` ou `circulo`).
- `"subgancho"` é opcional: uma frase bem curta (até 8 palavras) embaixo do gancho, com um número ou fato ("O diesel S10 já custa R$ 7,33 nos postos."). Só use quando o gancho for curto; gancho e subgancho juntos, no máximo umas 20 palavras. Pouco texto na capa: a foto precisa aparecer.
- Gancho de capa: de preferência até 12 palavras. O rosto ou o assunto da foto não pode ficar coberto pelo texto.
- Ganchos que mais funcionaram: nome famoso + fato forte ("Paul Walker morreu aos 40, mas deixou uma frase..."), número chocante ("73 diagnósticos de câncer"), eliminação ("o vencedor não foi corrida, musculação ou natação"), segredo ("quase ninguém sabe o verdadeiro motivo"), pequeno contra gigante ("filho de agricultor criou um chocolate que a Nestlé copiou"), comparação que indigna ("quanto cada país cobra de imposto?"). Terminar com dois-pontos ou pergunta ajuda.

**Corpo**
- Cada slide termina puxando o próximo: uma frase curta de suspense no fim ("Mas ainda faltava uma peça.", "E aí veio a crise de 2008.", "Só que tem um detalhe."). É o que faz a pessoa arrastar até o fim.
- Guarde a revelação principal para perto do fim (slide 5 a 7), não entregue tudo no slide 2.
- Uma foto por slide, sempre ligada ao texto do slide. Texto curto: no máximo umas 35 palavras.
- Posts de dados: pouco texto, número grande, mesma estrutura repetida em cada slide.

**Legenda**
- Primeira linha forte (repete ou amplia o gancho), parágrafos de 1 a 2 frases, e **termine com uma pergunta** simples para puxar comentários ("E você, já caiu num golpe assim?"), antes do "Siga o @resenharentavel".

## Imagem única de notícia urgente

Para fato novo e simples ("AGORA", "URGENTE", "ATENÇÃO"), use `"formato": "unico"` com `"capa_estilo": "urgente"`: foto em cima, painel verde-escuro sólido embaixo, etiqueta vermelha com a `chamada` ("AGORA", "URGENTE", "ATENÇÃO") e a manchete em frase normal, sem data. Linguagem de notícia, nada informal. É visualmente diferente de todo carrossel. Use só quando o fato é mesmo novidade do dia.

## Placar (post de dados, só Instagram, se aprovado)

`"formato": "unico"`, `"capa_estilo": "placar"`, com `"gancho"`, `"chamada"` ("Em números"), `"fonte"` e `"linhas"`: lista de até 5 itens `{"rotulo", "valor", "num", "destaque"}` (o `num` define o tamanho da barra; `"destaque": 1` pinta de verde o item principal). Todos os números com fonte.
