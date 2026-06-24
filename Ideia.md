# Cliente: "Guilda Arcana" — Sistema de Gerenciamento de RPG

Olá! Estou procurando um desenvolvedor para criar um sistema para gerenciamento de personagens e campanhas de RPG. Atualmente tudo é feito em papel ou planilhas, e queremos centralizar as informações em uma plataforma.

## Objetivo do projeto

Criar uma aplicação que permita aos jogadores criar personagens, gerenciar inventário e acompanhar a evolução deles ao longo das aventuras.

---

# Requisitos do sistema

## 1. Cadastro e login

Os usuários deverão poder:

* Criar uma conta.
* Fazer login com e-mail e senha.
* Alterar senha.
* Recuperar senha.
* Editar perfil.

### Dados do usuário

* Nome
* E-mail
* Senha
* Foto de perfil
* Data de criação

---

## 2. Personagens

Cada usuário pode possuir vários personagens.

### Dados do personagem

* Nome
* Classe
* Raça
* Nível
* Experiência
* Vida máxima
* Mana máxima
* Força
* Agilidade
* Inteligência
* Defesa
* Ouro

### Classes iniciais

* Guerreiro
* Arqueiro
* Mago
* Ladino

### Ações

* Criar personagem.
* Editar personagem.
* Excluir personagem.
* Visualizar ficha completa.

---

## 3. Inventário

Cada personagem possui um inventário.

### Item

Informações:

* Nome
* Tipo

  * Arma
  * Armadura
  * Poção
  * Material
  * Consumível
* Descrição
* Peso
* Valor
* Quantidade

### Funcionalidades

* Adicionar item.
* Remover item.
* Atualizar quantidade.
* Buscar item.
* Ordenar inventário.

---

## 4. Equipamentos

Um personagem pode equipar:

* Capacete
* Peitoral
* Luvas
* Calças
* Botas
* Arma principal
* Escudo
* Acessório

Ao equipar um item, seus atributos devem ser somados automaticamente.

Exemplo:

Espada Longa:

+10 Força

Armadura de Ferro:

+15 Defesa

---

## 5. Sistema de experiência

O personagem recebe experiência após aventuras.

### Funções

* Adicionar experiência.
* Verificar subida de nível.
* Aumentar atributos automaticamente.
* Histórico de evolução.

---

## 6. Missões

### Dados da missão

* Título
* Descrição
* Recompensa em ouro
* Recompensa em experiência
* Status

  * Em andamento
  * Concluída
  * Falhou

### Funcionalidades

* Aceitar missão.
* Concluir missão.
* Cancelar missão.
* Listar missões ativas.

---

## 7. Bestiário

Cadastro de monstros.

### Dados

* Nome
* Nível
* Vida
* Ataque
* Defesa
* Experiência concedida
* Ouro concedido

### Exemplos

Goblin

Lobo

Esqueleto

Dragão

---

## 8. Sistema de combate

### Ações possíveis

* Atacar.
* Defender.
* Usar item.
* Fugir.

### Regras

O dano será calculado por:

```
dano = ataque - defesa
```

Nunca inferior a 1.

Ao derrotar um inimigo:

* Recebe experiência.
* Recebe ouro.
* Pode receber itens.

Todo combate deverá ser registrado em um histórico.

---

## 9. Histórico

Registrar:

* Criação de personagem.
* Ganho de experiência.
* Subida de nível.
* Combates realizados.
* Itens obtidos.
* Missões concluídas.

---

## 10. API REST

Desejo que todas as informações sejam acessíveis por uma API.

Endpoints esperados:

### Usuários

```
POST /users
POST /login
GET /users/{id}
PUT /users/{id}
```

### Personagens

```
GET /characters
POST /characters
GET /characters/{id}
PUT /characters/{id}
DELETE /characters/{id}
```

### Inventário

```
GET /characters/{id}/inventory
POST /characters/{id}/inventory
DELETE /characters/{id}/inventory/{item_id}
```

### Missões

```
GET /quests
POST /quests
PUT /quests/{id}
```

### Combate

```
POST /battle/start
POST /battle/attack
POST /battle/use-item
POST /battle/end
```

---

# Requisitos técnicos

### Backend

Python 3.13

### Framework

FastAPI

### Banco de dados

MySQL

### ORM

SQLAlchemy

### Autenticação

JWT

### Documentação

Swagger automática do FastAPI

### Testes

Pytest

---

# Diferenciais desejados

* Upload de imagem do personagem.
* Exportar ficha para JSON.
* Ranking dos personagens mais fortes.
* Sistema de conquistas.
* Geração de relatório PDF.
* WebSocket para chat entre jogadores.
* Docker para facilitar a instalação.

---

# Entregas esperadas

### Fase 1

Usuários + Login + Personagens.

### Fase 2

Inventário + Equipamentos.

### Fase 3

Missões + Sistema de experiência.

### Fase 4

Combate + Bestiário.

### Fase 5

Chat + Conquistas + Ranking.

---

## Observação do cliente

Não é necessário criar interface inicialmente. O sistema pode ser desenvolvido como uma API, e todos os testes poderão ser feitos pelo Swagger do FastAPI ou pelo Postman. Desejo que a arquitetura seja organizada e escalável, permitindo futuramente adicionar uma interface web ou um jogo propriamente dito.
