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

https://projeto-2-gacghzg8cjg8e6a2.brazilsouth-01.azurewebsites.net/

### Super usuário (Usado para logar como AMD)

- **login:** institutoadmg6  
- **senha:** ADM%G6

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
<summary><strong>📌 História 1 - [Título da História]</strong></summary>

**Como** [persona],  
**Quero** [objetivo],  
**Para** [benefício].

#### 🎯 Cenário 1: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

#### ✅ Cenário 2: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

#### ❌ Cenário 3: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

</details>

<details>
<summary><strong>📌 História 2 - [Título da História]</strong></summary>

**Como** [persona],  
**Quero** [objetivo],  
**Para** [benefício].

#### 🎯 Cenário 1: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

#### ✅ Cenário 2: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

#### ❌ Cenário 3: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

</details>

<details>
<summary><strong>📌 História 3 - [Título da História]</strong></summary>

**Como** [persona],  
**Quero** [objetivo],  
**Para** [benefício].

#### 🎯 Cenário 1: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

#### ✅ Cenário 2: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

#### ❌ Cenário 3: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

</details>

<details>
<summary><strong>📌 História 4 - [Título da História]</strong></summary>

**Como** [persona],  
**Quero** [objetivo],  
**Para** [benefício].

#### 🎯 Cenário 1: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

#### ✅ Cenário 2: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

#### ❌ Cenário 3: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

</details>

<details>
<summary><strong>📌 História 5 - [Título da História]</strong></summary>

**Como** [persona],  
**Quero** [objetivo],  
**Para** [benefício].

#### 🎯 Cenário 1: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

#### ✅ Cenário 2: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

#### ❌ Cenário 3: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

</details>


<details>
<summary><strong>📌 História 6 - [Título da História]</strong></summary>

**Como** [persona],  
**Quero** [objetivo],  
**Para** [benefício].

#### 🎯 Cenário 1: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

#### ✅ Cenário 2: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

#### ❌ Cenário 3: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

</details>


<details>
<summary><strong>📌 História 7 - [Título da História]</strong></summary>

**Como** [persona],  
**Quero** [objetivo],  
**Para** [benefício].

#### 🎯 Cenário 1: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

#### ✅ Cenário 2: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

#### ❌ Cenário 3: [Título do Cenário]
- **Dado** que [contexto],  
- **Quando** [ação],  
- **Então** [resultado].

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

- Link do docs com as Storyboards:  
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

![Site em Ar]()

![Testes automatizados]()

</details>

<details>
<summary><strong>????</strong></summary>


</details>

</details>
