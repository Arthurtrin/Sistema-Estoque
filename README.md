# 📦 Sistema de Estoque - Django + Django REST Framework

> Um sistema completo para gerenciar produtos em estoque, construído com Django, Django REST Framework e uma interface moderna usando Bootstrap. Ideal para quem quer aprender APIs REST com frontend integrado.

---

## 🚀 Funcionalidades

- 🛠 **CRUD completo** (Criar, Ler, Atualizar, Deletar) de produtos via API REST.
- 🎨 Interface web responsiva e amigável construída com Bootstrap 5.
- 📊 Visualização intuitiva do estoque com cards interativos.
- 🔔 Feedback instantâneo com mensagens toast para sucesso ou erro.
- 📦 Campos essenciais: nome, descrição, quantidade, preço unitário, preço total e prateleira.
- 🔒 Estrutura preparada para futuras implementações de autenticação e permissões.

---

## 🧰 Tecnologias utilizadas

| Backend                      | Frontend                 | Outras ferramentas      |
|-----------------------------|--------------------------|-------------------------|
| Python 3.x                  | HTML5                    | Git/GitHub              |
| Django 4.x                  | Bootstrap 5              | Visual Studio Code (opcional) |
| Django REST Framework       | JavaScript (Fetch API)   |                         |

---

## 🎯 Como executar o projeto localmente

### Pré-requisitos

- Python 3 instalado
- Git instalado


### Passos

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# Crie e ative o ambiente virtual
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Aplique as migrations para criar o banco
python manage.py migrate

# Inicie o servidor Django
python manage.py runserver
```
## 🛠️ Como usar

- Use o painel inicial para acessar as funcionalidades via cards.
- Cadastre novos produtos preenchendo o formulário intuitivo.
- Consulte a lista de produtos e veja detalhes atualizados em tempo real.
- Edite e exclua produtos diretamente pela interface.
- As operações usam chamadas API via JavaScript para interação dinâmica.

## 📄 Licença

Este projeto está licenciado sob a licença **MIT** — veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📫 Contato

Feito com ❤️ por Seu Nome  
📧 seu.email@exemplo.com

