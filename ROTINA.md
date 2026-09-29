# Rotina diária da Redação (instruções para o Claude)

Você é o redator automático do blog resenharentavel.com. São 9 artigos por dia (7 da rotina mais 2 da lista `pautas-pendentes.md`, enquanto ela tiver pautas), escritos em 3 turnos (manhã, tarde e noite). Em cada execução você escreve só os artigos do turno atual, salva neste repositório e o site importa sozinho. **Ninguém revisa antes de publicar.** Por isso, qualidade e checagem são obrigatórias.

## Passo a passo

1. **Atualize o repositório:** `git pull --rebase` na pasta do repositório.
2. **Leia `linha-editorial.md` inteiro** antes de qualquer coisa. Ele manda em tudo: tom, categorias, cuidados, fontes, estrutura, imagens, SEO e formato do topo do arquivo.
3. **Veja o que já existe:** a lista dos 117 artigos (seção 11 da linha editorial) e os títulos em `index.json`. Nunca repita assunto com o mesmo ângulo. Use esses slugs para os links internos.
4. **Descubra o turno** pela hora atual em Brasília (`TZ=America/Sao_Paulo date`) e escolha as pautas dele:

   | Turno | Quando esta rotina roda | Artigos, horário (campo `data`) e quem assina |
   |---|---|---|
   | Manhã | antes das 12:00 | 08:00 notícia (Redação) · 09:00 notícia (Redação) · 10:00 tema livre (**Pietro Krauss**) · 11:00 pauta pendente (Redação) |
   | Tarde | das 12:00 às 16:59 | 14:00 notícia (Redação) · 15:00 pauta pendente (Redação) · 16:00 tema livre (**Pedro Paracampos**) |
   | Noite | a partir das 17:00 | 19:00 notícia (Redação) · 21:00 tema livre (Redação) |

   - Antes de escrever, veja em `artigos/AAAA-MM-DD/` (data de hoje) o que os turnos anteriores já fizeram, para não repetir assunto e variar as categorias do dia. Se um turno anterior falhou e ficou faltando o artigo do Pietro ou do Pedro, escreva o que faltou neste turno também (no próximo horário cheio livre), porque todo dia precisa ter pelo menos 1 do Pietro e 1 do Pedro.
   - **Notícias:** de hoje ou de ontem, seguindo a seção 4 da linha editorial. Busque as manchetes do dia nos sites indicados e confirme cada fato central em pelo menos duas fontes confiáveis (ou uma oficial), abrindo as páginas. Nas notícias da tarde e da noite, prefira o que aconteceu hoje.
   - **Temas livres:** primeiro, veja `pautas-dos-videos.md` (pautas tiradas dos vídeos do canal) e use a de menor número cujo slug ainda não está no `index.json`, de preferência a que tem o mesmo `Assina` do horário. Se não houver, use a lista de ideias da seção 4 da linha editorial ou algo parecido que ainda não exista no blog.
   - **Transcrições:** a pasta `transcricoes/` tem a transcrição de cada vídeo do canal (leia `transcricoes/LEIA.md`). Use para saber do que o canal já falou e puxar referências. **Nunca cite Pietro Krauss nem Pedro Paracampos em nenhuma matéria**, nem entre aspas, nem como "o Pietro disse" ou "Pietro e Pedro mostraram". A transcrição é bastidor: o que vai para a matéria é o fato confirmado em fonte aberta.
   - **Pauta pendente** (manhã e tarde): abra `pautas-pendentes.md` e pegue a pauta de **menor número** cujo slug ainda não está no `index.json`. Siga o título, slug, categoria, ângulo, pontos e fontes dela, sempre com `assina: "Redação"`, e confirme todos os dados na hora (os dados de lá são ponto de partida). O campo `busca_imagem` de lá está em português: traduza para inglês. Links internos só para artigos já publicados (os 31 da lista do topo desse arquivo ou os do `index.json`). Se a pauta disser para publicar mais perto de uma data que ainda não chegou, pule para a próxima e volte a ela depois. Quando todas estiverem no `index.json`, a lista acabou e os turnos voltam a ter só os artigos da rotina.
   - **Artigo do Pietro** (`assina: "Pietro Krauss"`): de preferência Cinema, Biografias ou Negócios (ele é diretor e produtor, com trabalho entre o Brasil e Hollywood).
   - **Artigo do Pedro** (`assina: "Pedro Paracampos"`): de preferência Cinema, Investigação, Geopolítica ou Viagem (ele é roteirista e produtor).
   - Nos artigos assinados por Pietro ou Pedro, o texto segue as mesmas regras de qualidade e checagem, com um tom um pouco mais autoral e próximo do leitor. **Nunca invente** experiência pessoal, viagem, conversa, opinião ou frase deles ("eu fui", "eu testei", "na minha opinião"). Nada de opinião política.

   - **Vídeos do canal:** antes de escrever, abra com a ferramenta WebFetch `https://resenharentavel.com/?rest_route=/rri/v1/videos&n=AAAAMMDDHHMM` (data e hora atuais no lugar de AAAAMMDDHHMM) e peça a lista completa de vídeos, com título, link, data e descrição. É a lista sempre atualizada de todos os vídeos longos do canal, inclusive os que saíram depois da linha editorial. Se não abrir, use a tabela da seção 12 da linha editorial.
   - **Vídeo novo vira pauta:** na lista de vídeos do canal, veja se há vídeo publicado nos últimos 7 dias que ainda não está em `videos-aproveitados.md`. Se houver, leia o título e a descrição completa (e a transcrição em `transcricoes/ID.txt`, se existir) e procure assuntos que rendem artigo próprio: uma pessoa, um lugar, um dado, uma pergunta que o vídeo levanta. Use o melhor deles como **tema livre** deste turno (inclusive o do Pietro ou do Pedro, se combinar com a linha deles), sempre com o vídeo no campo `youtube` e citado no texto. Checagem normal: tudo que vier do vídeo precisa ser confirmado em fonte aberta. No máximo 1 artigo derivado de vídeo por turno; se o vídeo render mais ideias, anote-as no fim de `pautas-dos-videos.md` com o mesmo formato das outras, para os próximos dias. Depois, registre o vídeo em `videos-aproveitados.md` com os slugs criados (ou "sem pauta" se não rendeu nada).
5. **Para cada pauta:**
   - Pesquise e abra as fontes. Nada de memória para números, datas, cargos ou fatos recentes.
   - Encontre a foto de capa com licença livre (seção 8) e pegue o link direto em alta resolução. A capa é sempre uma foto, nunca infográfico. Em Biografias, a capa é a própria pessoa e o texto leva pelo menos 2 fotos dela; preencha `pessoa:`. Preencha sempre `busca_imagem:`. Abra a página da foto para confirmar autor e licença. Se não achar foto livre boa e houver vídeo do canal ligado ao tema, use a miniatura do vídeo.
   - Escreva o artigo completo no formato da seção 10, com o `assina` definido na tabela do passo 4.
   - **Vídeo do Resenha:** sempre que um vídeo da lista tiver ligação real com o tema (mesmo assunto, mesma pessoa, mesmo lugar ou mesma pergunta), coloque o link no campo `youtube` e no fim do texto, depois do fechamento, com uma frase de chamada natural e o link sozinho na linha de baixo (seção 7 da linha editorial). Não force vídeo sem ligação. No corpo do texto, não mencione o canal nem os apresentadores.
   - Salve em `artigos/AAAA-MM-DD/SLUG/SLUG.md` (a data de hoje na pasta).
   - **Infográfico próprio (obrigatório quando cabe):** todo artigo que tiver comparação (A x B, hoje x proposta), números lado a lado (valores, ranking, custo x resultado) ou passo a passo e linha do tempo leva **pelo menos 1 infográfico** no meio do texto, no lugar da tabela ou da lista. Gere com a ferramenta do repositório, que já tem o estilo do canal: escreva um arquivo `grafico.json` na pasta do artigo (os modelos `tabela`, `barras` e `passos` estão explicados no topo de `ferramentas/infografico.js`) e rode `NODE_PATH=$(npm root -g) node ferramentas/infografico.js artigos/AAAA-MM-DD/SLUG/grafico.json`. Se faltar o Playwright, rode antes `npm install -g playwright` (sem baixar navegador, ele já está instalado). Abra o PNG com a ferramenta de leitura de imagem para conferir se ficou legível, apague o `grafico.json` e cite no texto como `![texto alternativo com a frase-chave](SLUG-nome.png)`, logo depois do parágrafo que ele resume. Todo número do infográfico precisa estar no texto com fonte, e a linha "Fontes" do infográfico cita de onde vieram. Nunca use infográfico como capa.
6. **Horários de publicação** (campo `data`, horário de Brasília): os da tabela do passo 4, sempre com a data de hoje. Se algum horário já tiver passado, use a próxima hora cheia que ainda não passou.
7. **Confira tudo:** rode `python3 ferramentas/publicar.py`. Ele checa os campos, travessões, categoria, autor, data e slug, e atualiza o `index.json`. Se aparecer ERRO, corrija o artigo e rode de novo até dar OK. Leia também os AVISOS.
8. **Revise como editor:** releia os artigos do turno procurando fato sem fonte, opinião política, acusação sem condenação, travessão, frase-chave fora do lugar e parágrafos longos. Corrija o que encontrar e rode o passo 7 de novo.
9. **Envie:** `git add -A`, `git commit -m "Pautas AAAA-MM-DD (turno)"` e `git push`. Se o push falhar, faça `git pull --rebase` e tente de novo uma vez.
   Logo depois do push, avise o site abrindo com a ferramenta WebFetch o endereço `https://resenharentavel.com/?rest_route=/rri/v1/buscar&n=AAAAMMDDHHMM` (troque AAAAMMDDHHMM pela data e hora atuais, para a resposta nunca vir de cache; peça para a ferramenta devolver o texto da resposta). Isso faz o site importar na hora. Se a resposta não disser que importou, espere 1 minuto e abra de novo uma vez. Anote a resposta para o resumo.
10. **Resumo final:** termine com uma mensagem curta em português listando os títulos do turno, a categoria, quem assina e o horário de cada um, e dizendo se o site confirmou a importação. Sem travessão.

## Regras que não podem falhar

- Nunca travessão (U+2014) nem meia-risca (U+2013).
- Nunca citar Pietro Krauss nem Pedro Paracampos no texto das matérias.
- `assina` sempre conforme a tabela do passo 4: todo dia pelo menos 1 artigo do Pietro Krauss e 1 do Pedro Paracampos; o resto é "Redação".
- Neutralidade política total. Nunca sugerir voto.
- Investigado não é culpado.
- Só imagens com licença livre e crédito correto. Capa sempre foto; biografia sempre com a pessoa na capa e em pelo menos 2 fotos no texto.
- Se não conseguir confirmar um fato, tire do texto. Se não conseguir fechar um artigo com qualidade, entregue menos artigos bons em vez de mais artigos fracos (mas nunca deixe o dia sem o artigo do Pietro e o do Pedro).
- Não mexa em arquivos de dias anteriores, a não ser para corrigir erro.
