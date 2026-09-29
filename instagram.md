# Carrossel do Instagram (@resenharentavel)

Toda matéria ganha um carrossel. O Instagram do Resenha é um perfil de notícias: o post precisa parar o dedo de quem está rolando o feed. O site monta as imagens sozinho a partir do arquivo `carrossel.json` que você salva na pasta do artigo (mesma pasta do .md). Você escreve os textos; o site desenha os slides com as fotos da matéria e publica no Instagram na hora em que a matéria entra no ar.

## A capa é o que importa

A capa (primeiro slide) decide se a pessoa arrasta ou passa reto. Ela é sempre: foto da matéria em tela cheia, degradê escuro embaixo, a **chamada** pequena em verde e o **gancho** grande em caixa alta.

**Foto:** a capa usa a foto de capa da matéria (`"capa": "capa"`). Se outra foto da matéria for mais forte (um rosto conhecido, uma cena marcante, algo que explica a notícia sozinho), use o nome do arquivo dela. Por isso, escolha a foto de capa do artigo já pensando no Instagram: pessoa reconhecível, emoção, cena icônica. Evite foto genérica, prédio sem graça ou pessoa de costas.

**Gancho:** NÃO é o título do site (que é feito para o Google). É uma frase de 7 a 14 palavras, no máximo 95 caracteres, que faz a pessoa querer saber o resto. Escreva 3 opções e escolha a mais forte. Fórmulas que funcionam:
- **Número ou dinheiro concreto:** "BETO CARRERO CRIA ÁREA DA GALINHA PINTADINHA COM R$ 50 MILHÕES"
- **Fala com você:** "O QUE FAZ E QUANTO GANHA CADA POLÍTICO EM QUEM VOCÊ VOTA NESTE ANO"
- **Ranking ou lista:** "TOP 10 JOGADORES COM MAIS PARTIDAS POR SELEÇÕES"
- **Nome famoso + fato inesperado:** "O FILME MAIS CARO DA HISTÓRIA NÃO SE PAGOU NO CINEMA"
- **Notícia seca, verbo no presente:** "GOVERNO PROÍBE AS BETS E DÁ 10 DIAS PARA SACAR O SALDO"
- **Curiosidade ou contradição:** "POR QUE O PAÍS QUE SEDIA A COPA QUASE SEMPRE PERDE DINHEIRO"

Regras do gancho: verdadeiro e fiel à matéria (nada de exagero ou promessa que o texto não cumpre), sem travessão, sem ponto final, sem clickbait mentiroso, neutro em política.

**Chamada:** 2 a 4 palavras que prometem continuação: "DESLIZE PARA VER", "ENTENDA", "VEJA OS NÚMEROS", "VEJA O RANKING", "O QUE MUDA".

## Os slides de dentro

De 3 a 8 slides depois da capa. Cada slide tem **uma ideia** e cabe numa olhada: no máximo uns 45 palavras. Tipos:

- `"texto"`: título curto em verde + texto. Use `==Rótulo:==` para os rótulos em verde e `**trecho**` para destacar em negrito. Parágrafos separados por linha em branco. Bom para "O que diz / O que muda / Quem ganha / O que falta".
- `"numero"`: um número gigante + uma frase explicando. Use quando existe um dado que choca.
- `"ranking"`: `"posicao": "10º"`, `"nome"`, `"detalhe"` e a foto da pessoa ou coisa. Um item por slide.
- `"foto"`: só a foto (com `"texto"` opcional curto embaixo). Bom quando o assunto é visual.
- `"final"`: slide de fechamento com o símbolo do Resenha, "Matéria completa no link da bio" e o @. Use sempre como último.

Cada slide pode ter `"foto"` (arquivo de uma foto da matéria, ou `"capa"`) para o fundo, e `"fonte"` (de onde veio o dado).

Formatos por tipo de matéria:
- **Notícia:** capa + 3 a 5 slides de texto ("O que aconteceu", "O que muda para você", "Próximos passos") + final.
- **Explicativo:** capa + um slide por item comparado, sempre com a mesma estrutura de rótulos + final.
- **Ranking:** capa + um slide `ranking` por item + final.
- **Biografia:** capa com o rosto da pessoa + 4 a 6 slides com as fases da vida e os números da fortuna (use as fotos da pessoa da matéria) + final.

## Legenda

A legenda é uma matéria curta: primeira linha com a notícia ou o gancho em frase normal; depois 3 a 5 parágrafos curtos com os fatos e números principais (com a fonte); depois "A matéria completa está no link da bio."; depois o crédito das fotos entre parênteses; e por fim "Siga o @resenharentavel para entender como o dinheiro move o mundo." Sem hashtags em excesso (no máximo 3, no fim, se fizer sentido). Sem travessão. Nunca citar Pietro ou Pedro.

## Modelo do carrossel.json

```json
{
  "gancho": "Fim das bets pode devolver até R$ 117 bilhões por ano ao comércio",
  "chamada": "Deslize para ver",
  "capa": "capa",
  "slides": [
    {"tipo": "numero", "numero": "R$ 117 bi", "texto": "é quanto as apostas online podem tirar do comércio **por ano**, segundo a ==CNC== e o ==IDV==.", "foto": "proibicao-das-bets-varejo-supermercado.jpg", "fonte": "CNC e IDV, via Mercado & Consumo"},
    {"tipo": "texto", "titulo": "O que diz a MP", "texto": "==Sites fora do ar:== até **6 de outubro**.\n\n==Saque do saldo:== até **5/10, às 23h59**.", "foto": "capa", "fonte": "Agência Senado"},
    {"tipo": "final"}
  ],
  "legenda": "O fim das bets pode devolver ao comércio parte dos bilhões que iam para as apostas.\n\n..."
}
```

Todo número do carrossel precisa estar na matéria, com fonte. O `ferramentas/publicar.py` confere o arquivo.
