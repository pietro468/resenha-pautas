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

**Primeiro teste, antes de tudo: dá para entender do que se trata?** Quem vê o post não leu a matéria e não sabe do caso. O gancho precisa dizer **o assunto** (quem ou o quê) com palavras que qualquer pessoa reconhece: INSS, aposentados, Petrobras, Neymar, Pix, aluguel. Leia o gancho sozinho, sem a foto e sem a matéria: se alguém perguntaria "sair de onde?", "quem?", "do que você está falando?", ele está confuso e precisa ser reescrito.
- Confuso: "R$ 6,3 bilhões saíram da aposentadoria de quem nunca assinou nada" (não diz que é o INSS, nem o que "saíram" quer dizer).
- Claro e chamativo: "Aposentados perderam ==R$ 6,3 bilhões== em descontos do INSS que nunca autorizaram"; "Descontos falsos no INSS tiraram ==R$ 6,3 bilhões== de aposentados"
- Número e mistério só funcionam **junto** com o assunto, nunca no lugar dele.

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

**A foto da capa tem que mostrar o assunto.** Se a notícia é sobre um foguete, o foguete aparece inteiro e reconhecível; se é sobre uma pessoa, o rosto dela; se é sobre um produto, o produto. Foto só de fumaça, de multidão de costas, de detalhe abstrato ou em que o assunto fica pequeno no canto não serve como capa, mesmo sendo bonita. Lembre que a capa corta a foto no formato 4:5 (em pé) e que o texto cobre a parte de baixo: prefira fotos em pé ou quadradas com o assunto no meio ou na metade de cima.

**Olhe a foto antes de usar.** Coloque em `previa/baixar.txt` uma linha por foto (`nome.jpg URL`), faça commit e push, espere 1 minuto, rode `git pull` e abra os arquivos de `previa/fotos/` com a ferramenta de leitura de imagem. Confira se o assunto aparece bem. Depois apague a pasta `previa/` no mesmo commit do artigo. O Flickr bloqueia esse download de prévia: para ver uma foto do Flickr, procure a cópia dela no Commons pelo número (seção 8 da linha editorial). Na prévia também dá para fazer as buscas: uma linha `nome.json URL_DA_BUSCA`. Veja várias opções (umas 10 a 20 miniaturas numa folha só) antes de escolher.

**Enquadramento (`"capa_foco"`, opcional):** quando o assunto não está no meio da foto ou está pequeno, diga onde ele está: `"capa_foco": "x,y"` em porcentagem da foto (`"80,40"` = à direita, um pouco acima do meio) ou `"x,y,zoom"` para aproximar (`"50,38,1.5"` = no meio, aproxima 1,5 vez; zoom de 1 a 3). Nos slides, o mesmo vale com `"foco"`. Sem esse campo, a capa usa o meio da foto (e a parte de cima em fotos em pé). Zoom demais estoura a foto: passe de 2 só em fotos grandes.

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

**Nunca repita foto:** cada slide com foto usa uma foto diferente, e nenhuma repete a capa do post. Slide de texto sem foto nova fica **sem o campo `"foto"`**: ele sai com o fundo verde da marca, que é melhor do que a mesma foto de novo. A capa do post é a foto que mais combina com o gancho, e pode ser diferente da capa do site (`"capa": "arquivo.jpg"`). Para ter fotos suficientes, a matéria lista em `imagens:` todas as fotos que vai usar, inclusive as que só aparecem no Instagram. O `publicar.py` recusa foto repetida. Cada slide tem **uma ideia** e cabe numa olhada: no máximo umas 45 palavras. Cada slide pode ter `"foto"` (arquivo de uma foto da matéria, ou `"capa"`) para o fundo, e `"fonte"` (de onde veio o dado).

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


## "Hoje na história" (post só do Instagram, todo dia às 10:00)

Post de curiosidade, que não vira matéria no site: o fato do dia que mais combina com o Resenha (personalidade do nicho, empresa, produto, filme, marco da economia, da geopolítica ou da corrida espacial).

**Capa:** `"capa_estilo": "hoje"`. Em cima do gancho sai pequeno o `"ha"` ("Há 55 anos") e o gancho é **direto**, dizendo o que aconteceu, sem enfeite: "Abria a ==Walt Disney World==, na Flórida"; "Morria ==Steve Jobs==, o fundador da Apple"; "A ==União Soviética== lançava o Sputnik e começava a corrida espacial". Pessoa muito famosa: o nome vai no gancho, com destaque. Pessoa pouco conhecida: descreva quem ela foi pelo feito ("Nascia o homem que ==venceu Thomas Edison== na guerra da eletricidade"). Cuidado com exageros que geram ataque: "um dos rostos mais famosos", nunca "o rosto mais famoso". Datas de morte com `"luto": true` (capa em preto e branco); as outras, coloridas.

**Carrossel: só fotos, sem texto nenhum.** De 4 a 8 slides `{"tipo": "foto", "foto": "arquivo.jpg"}` (sem o campo `texto`), com as melhores fotos **da época e do próprio acontecimento** (o dia da abertura, o lançamento, a pessoa naquele tempo). Fontes de fotos antigas livres: Wikimedia Commons, Library of Congress, NASA, arquivos públicos (Florida Memory, Arquivo Nacional, Agência Brasil), acervos em domínio público. Se não houver boas fotos livres do fato, escolha outro fato do dia. Por último, `{"tipo": "final"}`.

**Legenda muito bem elaborada** (é ela que conta a história): primeira linha com um título curto em caixa alta ("HÁ 55 ANOS, A DISNEY ABRIA SEU MAIOR PARQUE"); depois 4 a 6 parágrafos curtos, como uma reportagem: o que aconteceu naquele dia, o contexto, os números (quanto custou, quantas pessoas, quanto rende hoje), um detalhe curioso que pouca gente sabe, e o que aquilo significa hoje. Pode citar especialista ou documento, sempre real e com fonte. No fim, o crédito das fotos entre parênteses e o "Siga o @resenharentavel...". Sem "link na bio", sem travessão, no máximo 3 hashtags.

Arquivo: `instagram/AAAA-MM-DD/hoje-SLUG/post.json`. Modelo:

```json
{
  "titulo": "Hoje na história: abertura da Walt Disney World",
  "data": "2026-10-01 10:00",
  "fotos": [
    {"arquivo": "hoje-disney-1971-1.jpg", "url": "link direto da foto livre", "credito": "Autor/Acervo (licença)"}
  ],
  "carrossel": {
    "formato": "carrossel", "estilo": "frase", "capa": "capa", "capa_estilo": "hoje",
    "ha": "Há 55 anos",
    "gancho": "Abria a ==Walt Disney World==, na Flórida",
    "slides": [
      {"tipo": "foto", "foto": "hoje-disney-1971-2.jpg"},
      {"tipo": "foto", "foto": "hoje-disney-1971-3.jpg"},
      {"tipo": "final"}
    ],
    "legenda": "HÁ 55 ANOS, A DISNEY ABRIA SEU MAIOR PARQUE\n\n..."
  }
}
```

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
- Gancho de capa: curto, de preferência até 10 palavras (no máximo 3 linhas na capa), para o texto não subir e cobrir a foto. Ex.: "Por que a guerra do Irã deixou o ==diesel== mais caro?". O rosto ou o assunto da foto não pode ficar coberto pelo texto.
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

## Placar (post só do Instagram, terça e quinta, às 17:30)

Arquivo: `instagram/AAAA-MM-DD/placar-SLUG/post.json`, `"data"` às 17:30. Imagem única, sem foto (`"fotos": []`). `"formato": "unico"`, `"capa_estilo": "placar"`, com `"gancho"` curto (a pergunta ou a conclusão, com `==destaque==`), `"chamada"` ("Em números"), `"fonte"` e `"linhas"`: lista de 3 a 5 itens `{"rotulo", "valor", "num", "destaque"}` (o `num` é o número puro que define o tamanho da barra; `"destaque": 1` pinta de verde o item principal, normalmente o Brasil ou o maior). Temas: preços entre países, empresas mais valiosas, fortunas, salários, gastos de clubes, custo de vida. Todos os números com fonte confiável e atual, com o ano do dado. Legenda: explica o que os números mostram em 2 a 4 parágrafos curtos, com as fontes, e termina com uma pergunta.


## História real (post só do Instagram, 3 por semana: segunda, quarta e sexta, às 20:00)

História de superação **real e confirmada**, sempre com **fotos da própria pessoa** (na capa e nos slides; se não houver fotos livres dela, escolha outra história), ligada a carreira, negócio, dinheiro ou esporte: alguém que saiu de baixo, quase quebrou, foi rejeitado ou demitido e deu a volta (ex.: o filho de agricultor que criou um chocolate copiado pelas gigantes; o ator que dormia em banco de praça e virou James Bond). Nada de doença, tragédia pessoal explorada ou pessoa comum sem autorização; nada de Pietro ou Pedro; nada de política.

Arquivo: `instagram/AAAA-MM-DD/historia-SLUG/post.json`, `"data"` às 20:00. Capa: `"capa_estilo": "historia"` (faixas pretas de cinema em cima e embaixo, "HISTÓRIA REAL" no canto, gancho em frase normal com `==destaque==`). Gancho em até 12 palavras, com o momento mais baixo ou mais surpreendente da história. **Se a pessoa for muito famosa, diga o nome no gancho**, com destaque ("==Steve Jobs== foi expulso da empresa que ele mesmo criou"); se for pouco conhecida, descreva quem ela era ("Esse filho de agricultor criou um chocolate que a Nestlé copiou"). Corpo: 5 a 8 slides `foto` ou `foto_texto`, contando em ordem, **cada slide terminando com uma frase de suspense** que puxa o próximo; a virada perto do fim; conclusão com a lição; `{"tipo": "final"}`. Legenda conta a história em parágrafos curtos, com as fontes, e termina com uma pergunta.

## Curiosidades (post só do Instagram, todo dia às 12:30)

Listas de curiosidades sobre dinheiro e luxo, com números: "Quem são os donos das casas mais caras do mundo", "Quais são as casas mais caras do mundo", "Qual o carro mais caro do mundo", "Quem são as pessoas mais ricas do Brasil hoje", "Quanto ganham os jogadores mais bem pagos do mundo", "Os iates mais caros", "Os prédios mais altos"...

Arquivo: `instagram/AAAA-MM-DD/curiosidade-SLUG/post.json`, `"data"` às 12:30. Capa: `"capa_estilo": "trio"` com a primeira foto da lista e mais duas em `"capa_extras": ["arquivo2.jpg", "arquivo3.jpg"]` (três fotos lado a lado), `"chamada": "Curiosidades"` e o gancho em forma de pergunta, curto ("Quais são os ==prédios mais altos== do mundo?"). Corpo: um slide por item, do menor para o maior (o topo fica para o fim), com `{"tipo": "item", "foto", "posicao": "3º lugar", "detalhe": "Cidade, país ou o que é", "nome", "valor": "US$ 60 milhões", "fonte"}`; de 5 a 8 itens; depois `{"tipo": "final"}`. Todo número com fonte confiável e atual (Forbes, Bloomberg, relatórios oficiais), com o ano do dado na legenda. Fotos com licença livre (Wikimedia, Pexels, agências públicas); se não houver foto livre da pessoa, use foto do bem (a casa, o carro, o prédio). Legenda: os itens em lista curta com os valores e a fonte, e uma pergunta no fim ("Qual desses você escolheria?").
