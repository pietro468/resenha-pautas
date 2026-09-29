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

**Gancho:** NÃO é o título do site (que é feito para o Google). É uma frase de 7 a 14 palavras, no máximo 95 caracteres, que faz a pessoa querer saber o resto. Escreva 3 opções, de tipos diferentes, e fique com a mais forte.

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

## Os slides de dentro

De 3 a 8 slides depois da capa. O último slide é conteúdo, como no concorrente: **não** faça slide de "leia no link da bio". Cada slide tem **uma ideia** e cabe numa olhada: no máximo umas 45 palavras. Cada slide pode ter `"foto"` (arquivo de uma foto da matéria, ou `"capa"`) para o fundo, e `"fonte"` (de onde veio o dado).

Formatos por tipo de matéria:
- **Notícia:** capa + 3 a 5 slides ("O que aconteceu", "O que muda para você", "Próximos passos").
- **Explicativo:** capa + um slide por item comparado, sempre com a mesma estrutura de rótulos.
- **Ranking:** capa + um slide `ranking` por item.
- **Biografia:** capa com o rosto da pessoa + 4 a 6 slides com as fases da vida (`foto_texto` funciona muito bem) e os números da fortuna.

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
    {"tipo": "texto", "titulo": "O que diz a MP", "texto": "==Sites fora do ar:== até **6 de outubro**.\n\n==Saque do saldo:== até **5/10, às 23h59**.", "foto": "capa", "fonte": "Agência Senado"}
  ],
  "legenda": "O fim das bets pode devolver ao comércio parte dos bilhões que iam para as apostas.\n\n..."
}
```

Todo número do carrossel precisa estar na matéria, com fonte. O `ferramentas/publicar.py` confere o arquivo.
