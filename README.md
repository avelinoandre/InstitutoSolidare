# 🌟 Projeto Nosso Sonho 

## 📝 Descrição

Este projeto foi desenvolvido na disciplina Projetos 2 da [CESAR School](https://www.cesar.school/), em colaboração com a ONG [Instituto Solidare](https://institutosolidare.org.br/), uma organização que atua no apoio a crianças e jovens em situação de vulnerabilidade social.

Nosso objetivo é prototipar uma nova solução para o programa de apadrinhamento do Instituto Solidare, promovendo uma reformulação do sistema atual para torná-lo mais eficiente, acessível e alinhado às necessidades tanto da ONG quanto dos padrinhos e das crianças atendidas.

---

## 🌐 Google Site

> ❗ **Importante:** A maioria dos requisitos de C.C podem ser encontrados também no Google site na aba superior **Status Report**

https://sites.google.com/cesar.school/grupo6/home

---

## 👥 Equipe

- [**Mircio Ferreira**](https://github.com/Mircio-Ferreira) – [C.C]
- [**Gabriel Miranda**](https://github.com/GMiranda21ML) – [C.C]
- [**Ricardo Sergio**](https://github.com/whosricardo) – [C.C]
- [**André Avelino**](https://github.com/avelinoandre) – [C.C]
- [**Eric Gonçalve**](https://github.com/eric-albuquer) – [C.C]
- [**Thiago Fernandes**](https://github.com/ThIagoMedeiros21) – [C.C]
- [**Caio Mathews**](https://github.com/CaioMathews) – [C.C]
- [**Gabriel Aniceto**](https://github.com/gabrielaniceto1) – [C.C]
- [**João Passos**](https://github.com/iampassos) – [C.C]

- **Guilherme José** – [Designer]
- [**Rafael Lima**](https://www.linkedin.com/in/rafael-rocha-a89150361/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) – [Designer]
- [**Gabriela Britto**](https://www.linkedin.com/in/gabriela-sampaio-98b587362) – [Designer]


---

## 🎓 Orientadores

- [**Manuela Beatriz**](https://www.linkedin.com/in/manucorreia/) – [Designer]
- **Eduardo Nascimento** – [C.C]
- [**Ana Carolina**](https://www.linkedin.com/in/carolmello--/) – [C.C]

---

## 🌐 Site no ar

https://projeto-2-app-ftb7gqecdxgthher.brazilsouth-01.azurewebsites.net/

### Super usuário (Usado para logar como AMD)

- **login:** institutoadmg6  
- **senha:** ADM%G6

> ❗ **Importante:**O super usuario também é usado para acessar as telas de adm.

---

## 📦 Tecnologias Utilizadas

<img src="https://static.djangoproject.com/img/logos/django-logo-negative.svg" alt="Django" width="120"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/f/fa/Microsoft_Azure.svg" alt="Azure" width="80"/>

---

## 📨 Entregas

<details open>
<summary><strong>📁 SR1 – Primeira Entrega</strong></summary>

<details>
<summary><strong>📜 Histórias de Usuário</strong></summary>

<details>
<summary><strong>📌 História 1 - Cadastro de Padrinho</strong></summary>

**Como** um usuário interessado em participar do sistema de apadrinhamento,  
**Quero** me cadastrar,  
**Para** poder acessar a plataforma e iniciar minha jornada como padrinho.

#### 🎯 Cenário 1: Falha no Cadastro devido ao Erro no Preenchimento de Campos
- **Dado** que o usuário está fazendo o cadastramento e deixou um ou mais campos obrigatórios em branco,  
- **Quando** o usuário seleciona em "confirmar cadastro",  
- **Então** o sistema alerta que não pode seguir para a próxima etapa, pois o cadastro precisa estar totalmente preenchido.

#### ✅ Cenário 2: Sucesso na Visualização
- **Dado** que o usuário preencheu todos os campos obrigatórios corretamente,  
- **Quando** o usuário seleciona em "prosseguir",  
- **Então** o sistema deve registrar os dados do usuário,  
- **E** exibir uma mensagem de sucesso,  
- **E** redirecionar o usuário para a próxima etapa da plataforma.

</details>

<details>
<summary><strong>📌 História 2 - Cadastro e Gerenciamento de Apadrinhados</strong></summary>

**Como** administrador,  
**Quero** poder cadastrar e gerenciar apadrinhados,  
**Para** garantir que os dados dos apadrinhados sejam registrados e mantidos atualizados.

#### 🎯 Cenário 1: Falha no Cadastramento devido a Campos Não Preenchidos Corretamente
- **Dado** que o usuário preencheu os dados de cadastramento, mas não preencheu todos de forma correta,  
- **Quando** o usuário seleciona a opção "efetuar cadastramento",  
- **Então** o sistema alerta quais campos não foram cadastrados de forma correta e pede para que eles sejam preenchidos.

#### ✅ Cenário 2: Sucesso no Cadastramento de um Apadrinhado
- **Dado** que o usuário preencheu os dados de cadastramento corretamente,  
- **Quando** o usuário seleciona a opção "efetuar cadastramento",  
- **Então** o sistema alerta que o cadastramento foi efetuado com sucesso, demonstrando os dados cadastrados e exibindo se ele deseja cadastrar outro apadrinhado.

#### ❌ Cenário 3: Excluir Apadrinhado do Sistema
- **Dado** que o usuário está na página de gerenciar apadrinhados,  
- **Quando** o administrador seleciona o apadrinhado e clica em "apagar do sistema",  
- **Então** o sistema alerta se deseja prosseguir e, caso confirmado, o sistema deleta todos os dados do banco de dados.

</details>

</details>

<details>
<summary><strong>🔄 Diagrama de Atividade</strong></summary>

### História 1  
![Diagrama da História 1](img_readme/diagrama_atividade_1.png)

### História 2  
![Diagrama da História 2](img_readme/diagrama_atividade_2.png)

</details>

<details>
<summary><strong>🖼️ Storyboards</strong></summary>

- Link do docs com as Storyboards:  
  https://docs.google.com/document/d/150L9B3V2XvXIusJl3Vr5C6oQqQGo3yqRpPE7NPLYsRU/edit?usp=sharing

</details>

<details>
<summary><strong>📝 Relatório de Programação</strong></summary>

- Link do docs com o relatório de programação:  
  https://docs.google.com/document/d/1653YvO_WiZROmIwClfyujsrUe28AltAdsSxwCvJg4WQ/edit?tab=t.0

</details>

<details>
<summary><strong>🚨 Issue / Bug Tracker</strong></summary>

### Bug Open 1:
![Open 1](img_readme/BUGOPEN1.PNG)

### Bug Open 2:
![Open 2](img_readme/BUGOPEN2.PNG)

### Bug closed 1:
![Closed 1](img_readme/BUGCLOSED1.PNG)

### Bug closed 2:
![Closed 2](img_readme/BUGCLOSED2.PNG)

### Bug closed 3:
![Closed 3](img_readme/BUGCLOSED3.PNG)

### Bug closed 4:
![Closed 4](img_readme/BUGCLOSED4.PNG)

</details>

</details>

---

<details>
<summary><strong>📁 SR2 – Segunda Entrega</strong></summary>

<details>
<summary><strong>📜 Histórias de Usuário</strong></summary>

<details>
<summary><strong>📌 História 1 - [Apadrinhando de mais uma criança]</strong></summary>

**Como** [um usuário interessado em participar do sistema de apadrinhamento e quero poder realizar mais um sonho de uma criança ao apadrinhá-la.],  

#### ✅ Cenário 1: [Sucesso do apadrinhamento]
- **Dado** que [o usuário está logado e na aba de apadrinhar novamente],  
- **Quando** [o usuário escolhe uma criança para a filha],  
- **Então** [o sistema redireciona o usuário a tela de doação e após concluir, o sistema alerta o sucesso da ação.].

#### ❌ Cenário 2: [Falha ao apadrinhar devido a não ter apadrinhados disponíveis, normalmente por que todos já estão apadrinhados.]
- **Dado** que [o usuário está logado na aba de feed.],  
- **Quando** [o usuário seleciona o campo de apadrinhar novamente.],  
- **Então** [resultado o sistema alerta que não existem apadrinhados disponíveis no momento.].

</details>

<details>
<summary><strong>📌 História 2 - [Cadastro e Gerenciamento de Apadrinhados]</strong></summary>

**Como** [administrador,quero poder cadastrar e gerenciar apadrinhados,
 para garantir que os dados dos apadrinhados sejam registrados e atualizados.],  

#### ❌ Cenário 1: [Falha no Cadastro por Campos Incorretos]
- **Dado** que [do que o adm está logado e na página de cadastrar um afilhado, mas não preencheu todos os campos exigidos.],  
- **Quando** [clicar em "Efetuar cadastramento".],  
- **Então** [o sistema informa que nem todos campos foram preenchidos.].

#### ✅ Cenário 2: [Sucesso no Cadastro]
- **Dado** que [do que o adm está logado e na página de cadastrar um afilhado.],  
- **Quando** [clicar em "Efetuar cadastramento".],  
- **Então** [o sistema exibe mensagem de sucesso e opção de cadastrar outro.].

</details>

<details>
<summary><strong>📌 História 3 - [Doação Livre]</strong></summary>

**Como** [usuário comum, quero realizar uma doação livre para a instituição, para contribuir com os projetos sociais.],  

#### ✅ Cenário 1: [O usuário preenche o valor e as informações corretamente para a doação e consegue enviar a doação sem problemas.]
- **Dado** que [o usuário está logado e na página de doação
E preenche o campo com o valor de 20.00 Reais
E escolhe a forma de pagamento.],  
- **Quando** [clica em "Doar".],  
- **Então** [a doação é processada com sucesso e exibe agradecimento.].

#### ❌ Cenário 2: [ O usuário tenta realizar uma doação, mas não preenche o valor da doação.]
- **Dado** que [o usuário está logado e na página de doação.],  
- **Quando** [clica em "Doar" sem preencher o valor.],  
- **Então** [o sistema alerta que o campo de valor é obrigatório.].

</details>

<details>
<summary><strong>📌 História 4 - [Publicação de Notícias]</strong></summary>

**Como** [administrador, quero cadastrar notícias no feed para informar os usuários sobre novidades da ong e notícias do apadrinhado.]

#### ✅ Cenário 1: [O administrador acessa a área de gerenciamento de notícias da plataforma. Ele deseja publicar uma notícia direcionada a todos os usuários do sistema.]
- **Dado** que [que o adm está logado na plataforma e acessar a área de cadastrar uma notícia no feed.],  
- **Quando** [o adm escreve toda notícia e clica em publicar],  
- **Então** [a notícia é salva e todos os usuário do sistema tem acesso a ela].

#### ✅ Cenário 2: [Remoção de Notícia]
- **Dado** que [que o adm está logado na plataforma e está na área de gerenciar uma notícia já publicada.],  
- **Quando** [clica em "Excluir" ao lado de uma notícia],  
- **Então** [ela é removida do banco de dados].

</details>

<details>
<summary><strong>📌 História 5 - [Acesso ao Feed de Notícias]</strong></summary>

**Como** [padrinho, quero acessar o feed de notícias, para acompanhar novidades da ONG e atualizações do meu afilhado.],  
**Quero** [objetivo],  
**Para** [benefício].

#### ✅ Cenário 1: [O usuário quer reagir a um post da ong.]
- **Dado** que [o usuário está logado e na página inicial do feed de notícias.],  
- **Quando** [escolhe uma postagem e reage com um emoji],  
- **Então** [o sistema atualiza a quantidade de likes do sistema].

#### ❌ Cenário 2: [ Erro ao carregar Feed por não existir notícias cadastradas.]
- **Dado** que [ o usuário está logado e em uma página do sistema que não seja o feed (ex cartas)],  
- **Quando** [o usuário clicar em feed.],  
- **Então** [o usuário é redirecionado para o feed e constata que não há notícias cadastradas.].

</details>

<details>
<summary><strong>📌 História 6 - [Envio e Visualização de Cartas]</strong></summary>

**Como** [padrinho, padrinho, quero poder enviar e visualizar cartas trocadas com meus afilhados, para que eu possa manter uma comunicação afetiva com eles e acompanhar melhor seu crescimento],

#### ✅ Cenário 1: [Envio de Carta com Sucesso]
- **Dado** que [o padrinho está logado na aba de carta com afilhado selecionado e carta redigida,],  
- **Quando** [clica em "Enviar carta"],  
- **Então** [a carta é enviada ao administrador e uma mensagem de sucesso é exibida.].

#### ❌ Cenário 2: [Falha no Envio por erro na formatação.]
- **Dado** que [o padrinho está logado na aba de cartas e com a carta redigida mas não selecionou o apadrinhado.],  
- **Quando** [o usuário clica em enviar uma carta.],  
- **Então** [o sistema exibe mensagem de erro que nem todos os campos foram preenchidos.].

</details>

<details>
<summary><strong>📌 História 7 - [Visualização e Resposta de Cartas pelo Administrador]</strong></summary>

**Como** [administrador, quero visualizar e responder as cartas dos padrinhos, para manter o acompanhamento e comunicação com os usuários.],  

#### ✅ Cenário 1: [Sucesso na Resposta]
- **Dado** que [o administrador está logado e na tela de gerenciamento e seleciona uma carta,],  
- **Quando** [o usuário clicar em envia uma resposta,],  
- **Então** [o sistema exibe "Resposta enviada com sucesso!" e marcada como respondida.].

#### ❌ Cenário 2: [Falha no Envio por erro na formatação.]
- **Dado** que [o adm está logado na aba de cartas e com a carta redigida mas não selecionou o título da carta a ser respondida.],  
- **Quando** [o usuário clicar em enviar uma resposta.],  
- **Então** [o sistema exibe mensagem de erro que nem todos os campos foram preenchidos].

</details>

</details>

<details>
<summary><strong>🔄 Diagrama de Atividade</strong></summary>

### História 1 
![Diagrama da História 1](img_readmeSR2/diagrama_de_atividades/historia1.png)

### História 2 
![Diagrama da História 2](img_readmeSR2/diagrama_de_atividades/historia2.png)

### História 3  
![Diagrama da História 3](img_readmeSR2/diagrama_de_atividades/historia3.png)

### História 4  
![Diagrama da História 4](img_readmeSR2/diagrama_de_atividades/historia4.png)

### História 5  
![Diagrama da História 5](img_readmeSR2/diagrama_de_atividades/historia5.png)

### História 6  
![Diagrama da História 6](img_readmeSR2/diagrama_de_atividades/historia6.png)

### História 7
![Diagrama da História 7](img_readmeSR2/diagrama_de_atividades/historia7.png)


</details>

<details>
<summary><strong>🖼️ Storyboards</strong></summary>

- Link do docs com as Storyboards (recomenda-se fortimente o donwload para poder visualizar os textos com mais nitidez!):  
  [https://drive.google.com/file/d/1XP1DY3Ywq-NRN-gGRSASNHxE3urc7zLh/view]

</details>

<details>
<summary><strong>📝 Relatório de Programação</strong></summary>

- Link do docs com o relatório de programação: 
  [https://docs.google.com/document/d/1ZZ6xdAR2GiylmETsNl9Uh1YymUSbXP-ndzaITF-LueI/edit?tab=t.0]

</details>

<details>
<summary><strong>🚨 Issue / Bug Tracker</strong></summary>

### Bug closed 7:
![Close 7](img_readmeSR2/bug_tracker/bugclosed7.png)

### Bug closed 8:
![Close 8](img_readmeSR2/bug_tracker/bugclosed8.png)

### Bug closed 9:
![Close 9](img_readmeSR2/bug_tracker/bugclosed9.png)

### Bug closed 10:
![Close 10](img_readmeSR2/bug_tracker/bugclosed10.png)

### Bug closed 11:
![Close 11](img_readmeSR2/bug_tracker/bugclosed11.png)

### Bug closed 12:
![Close 12](img_readmeSR2/bug_tracker/bugclosed12.png)

### Bug closed 14:
![Close 14](img_readmeSR2/bug_tracker/bugclosed14.png)

</details>

<details>
<summary><strong>🎥 Screenquest</strong></summary>

- [**Video do deploy**](https://www.youtube.com/watch?v=_K1LFwxl_1c)

- [**Testes automatizados**]()

- [**CI/CD**](https://www.youtube.com/watch?v=JfaiVXdjmGQ)

</details>

</details>
