<div align="center">

# 🐍 Jornada Python: Automação, Dados e Inteligência Artificial

Repositório com projetos desenvolvidos durante uma jornada prática de Python, abrangendo automação de tarefas, análise de dados, machine learning e inteligência artificial local.

![Python](https://img.shields.io/badge/Python-Projetos-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Análise_de_Dados-150458?style=for-the-badge\&logo=pandas\&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine_Learning-F7931E?style=for-the-badge\&logo=scikitlearn\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Interface-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído_com_evoluções-success?style=for-the-badge)

</div>

---

## 📌 Sobre o repositório

Este repositório reúne quatro projetos desenvolvidos para praticar diferentes aplicações da linguagem Python.

Os projetos percorrem uma sequência de aprendizado que começa com automação de tarefas e avança para:

* manipulação de dados;
* análise exploratória;
* visualização;
* machine learning;
* construção de interfaces;
* integração com modelos de linguagem executados localmente.

Cada projeto possui finalidade educacional e demonstra uma área diferente do ecossistema Python.

---

## 🚀 Projetos

| Projeto   | Tema                    | Resultado                                      |
| --------- | ----------------------- | ---------------------------------------------- |
| Projeto 1 | Automação de tarefas    | Cadastro automático de produtos em sistema web |
| Projeto 2 | Análise de dados        | Investigação de motivos de cancelamento        |
| Projeto 3 | Machine learning        | Classificação e previsão de clientes           |
| Projeto 4 | Inteligência artificial | Chatbot local com Streamlit e Ollama           |

---

# 1️⃣ Automação de tarefas

## Objetivo

Automatizar o cadastro repetitivo de produtos em um sistema web.

Os dados são carregados de um arquivo CSV e inseridos automaticamente nos campos da aplicação.

## Conceitos praticados

* leitura de arquivos CSV;
* manipulação de dados com Pandas;
* automação de teclado e mouse;
* repetição de tarefas;
* pausas entre ações;
* preenchimento de formulários;
* identificação de coordenadas da tela.

## Ferramentas

* Python;
* Pandas;
* PyAutoGUI.

## Fluxo

```text
Arquivo CSV
    ↓
Leitura com Pandas
    ↓
Abertura do navegador
    ↓
Login no sistema
    ↓
Preenchimento dos campos
    ↓
Cadastro de cada produto
```

## Execução

```bash
python "Projeto 1 - Automacao de Tarefas/codigo.py"
```

Para descobrir a posição atual do mouse:

```bash
python "Projeto 1 - Automacao de Tarefas/pegar_posicao.py"
```

## Limitação

A automação depende de coordenadas da tela.

Mudanças em:

* resolução;
* escala do sistema;
* posição da janela;
* zoom do navegador;
* layout da página;

podem fazer os cliques ocorrerem no local errado.

---

# 2️⃣ Análise de dados

## Objetivo

Analisar uma base de clientes e identificar fatores relacionados ao cancelamento de serviços.

O projeto utiliza notebooks para:

* importar os dados;
* verificar valores ausentes;
* remover informações inválidas;
* gerar estatísticas;
* comparar grupos;
* criar visualizações;
* identificar possíveis padrões.

## Conceitos praticados

* Pandas;
* limpeza de dados;
* análise exploratória;
* agrupamentos;
* filtros;
* estatísticas descritivas;
* gráficos;
* interpretação de resultados.

## Arquivos principais

```text
inicial.ipynb
gabarito.ipynb
cancelamentos.csv
```

## Perguntas de negócio

A análise pode ajudar a investigar:

* quais perfis cancelam mais;
* quais contratos apresentam maior cancelamento;
* se o tempo como cliente influencia a saída;
* quais serviços aparecem com maior frequência nos cancelamentos;
* quais mudanças podem reduzir a evasão.

> Os resultados encontrados representam a base utilizada no exercício e não devem ser generalizados para qualquer empresa.

---

# 3️⃣ Previsão com machine learning

## Objetivo

Treinar modelos capazes de classificar ou prever o comportamento de clientes a partir de dados históricos.

## Conceitos praticados

* preparação de dados;
* codificação de variáveis categóricas;
* separação entre treino e teste;
* treinamento de modelos;
* avaliação de acurácia;
* comparação de algoritmos;
* previsão de novos registros.

## Ferramentas

* Pandas;
* Scikit-learn;
* Jupyter Notebook.

## Arquivos principais

```text
inicial.ipynb
gabarito.ipynb
clientes.csv
novos_clientes.csv
```

## Fluxo do projeto

```text
Base histórica
      ↓
Limpeza e preparação
      ↓
Separação entre treino e teste
      ↓
Treinamento
      ↓
Avaliação
      ↓
Escolha do modelo
      ↓
Previsão de novos clientes
```

## Observação importante

Uma boa acurácia não garante que o modelo seja adequado para produção.

Também é necessário avaliar:

* qualidade dos dados;
* desbalanceamento das classes;
* precisão;
* recall;
* matriz de confusão;
* risco de vieses;
* atualização do modelo;
* impacto das previsões.

---

# 4️⃣ Jarvis ChatBot

## Objetivo

Criar uma interface de conversa com inteligência artificial utilizando um modelo executado localmente.

O chatbot utiliza:

* Streamlit para a interface;
* Ollama para executar o modelo;
* API local para comunicação;
* estado de sessão para preservar o histórico.

## Modelo utilizado

```text
qwen2.5:1.5b
```

O modelo é executado no computador do usuário.

Não é necessária uma chave de API de um serviço externo.

## Fluxo

```text
Usuário
   ↓
Interface Streamlit
   ↓
Histórico da conversa
   ↓
API local do Ollama
   ↓
Modelo qwen2.5:1.5b
   ↓
Resposta exibida na interface
```

## Funcionalidades

* interface de chat;
* histórico durante a sessão;
* tema visual personalizado;
* execução local;
* tratamento básico de indisponibilidade;
* ausência de cobrança por mensagem;
* indicação do modelo utilizado.

## Execução

```bash
streamlit run "Projeto 4 - Chatbot com IA em Tempo Real/chatbot.py"
```

Depois, acesse:

```text
http://localhost:8501
```

---

## 🦙 Configuração do Ollama

### macOS

Instale o Ollama:

```bash
brew install ollama
```

Inicie o serviço:

```bash
brew services start ollama
```

Baixe o modelo:

```bash
ollama pull qwen2.5:1.5b
```

### Windows e Linux

Instale o Ollama conforme o procedimento correspondente ao seu sistema operacional.

Depois, execute:

```bash
ollama pull qwen2.5:1.5b
```

Verifique os modelos instalados:

```bash
ollama list
```

---

## 📁 Estrutura geral

```text
Jornada-Python-Automacao/
│
├── Projeto 1 - Automacao de Tarefas/
│   ├── codigo.py
│   ├── gabarito.py
│   ├── pegar_posicao.py
│   └── produtos.csv
│
├── Projeto 2 - Analisando Dados/
│   ├── inicial.ipynb
│   ├── gabarito.ipynb
│   └── cancelamentos.csv
│
├── Projeto 3 - Previsao com Machine Learning/
│   ├── inicial.ipynb
│   ├── gabarito.ipynb
│   ├── clientes.csv
│   └── novos_clientes.csv
│
├── Projeto 4 - Chatbot com IA em Tempo Real/
│   ├── chatbot.py
│   ├── main.py
│   └── auxiliar.py
│
├── README.md
└── requirements.txt
```

> Os nomes devem ser ajustados caso a estrutura atual utilize grafia ou diretórios diferentes.

---

## 🛠️ Tecnologias

| Tecnologia   | Utilização                     |
| ------------ | ------------------------------ |
| Python       | Linguagem principal            |
| Pandas       | Manipulação e análise de dados |
| PyAutoGUI    | Automação de teclado e mouse   |
| Plotly       | Visualização de dados          |
| Scikit-learn | Machine learning               |
| Jupyter      | Execução dos notebooks         |
| Streamlit    | Interface do chatbot           |
| Ollama       | Execução local do modelo       |
| Qwen 2.5     | Modelo de linguagem            |
| Git          | Controle de versão             |
| GitHub       | Publicação dos projetos        |

---

## 🚀 Instalação

### Clone o repositório

```bash
git clone https://github.com/ONestoDev/Jornada-Python-Automacao.git
```

### Acesse a pasta

```bash
cd Jornada-Python-Automacao
```

### Crie um ambiente virtual

```bash
python -m venv .venv
```

### Ative no Windows

```powershell
.venv\Scripts\activate
```

### Ative no Linux ou macOS

```bash
source .venv/bin/activate
```

### Instale as dependências

```bash
pip install pandas pyautogui plotly scikit-learn openpyxl nbformat ipykernel streamlit
```

O ideal é manter essas dependências em um arquivo:

```text
requirements.txt
```

E instalá-las com:

```bash
pip install -r requirements.txt
```

---

## 📦 Dependências sugeridas

```text
pandas
pyautogui
plotly
scikit-learn
openpyxl
nbformat
ipykernel
streamlit
```

O Ollama é instalado separadamente e não deve aparecer como pacote do `pip`.

---

## ⚠️ Limitações

### Automação

* depende das coordenadas da tela;
* pode clicar em locais incorretos;
* não confirma visualmente cada cadastro;
* pode falhar se a página demorar para carregar;
* depende do layout do sistema externo.

### Análise de dados

* os resultados dependem da qualidade da base;
* correlações não demonstram causalidade;
* os dados podem representar apenas um cenário educacional.

### Machine learning

* o modelo não está preparado para produção;
* não existe API de inferência;
* não há monitoramento;
* não há controle de versões do modelo;
* não há avaliação detalhada de vieses.

### Chatbot

* depende do Ollama ativo;
* depende dos recursos do computador;
* o histórico é perdido ao encerrar a sessão;
* não existe autenticação;
* não há persistência;
* não utiliza recuperação de documentos;
* não possui moderação;
* o modelo pode fornecer respostas incorretas.

---

## 🔐 Privacidade

No chatbot, as mensagens são processadas pelo modelo local enquanto o Ollama estiver configurado dessa forma.

Ainda assim, não insira:

* senhas;
* dados bancários;
* documentos pessoais;
* informações empresariais sigilosas;
* dados médicos;
* credenciais;
* chaves de API.

Nos projetos de análise, utilize bases públicas, fictícias ou anonimizadas.

---

## 🗺️ Melhorias futuras

* adicionar `requirements.txt`;
* criar `.gitignore`;
* remover arquivos da IDE;
* documentar cada projeto separadamente;
* adicionar capturas de tela;
* refatorar a automação para usar seletores;
* adicionar tratamento de exceções;
* criar testes;
* separar configurações;
* persistir o histórico do chatbot;
* permitir seleção de modelos;
* exibir erro quando o modelo não estiver instalado;
* adicionar botão para limpar a conversa;
* criar uma interface para os modelos de machine learning.

---

## 🧪 Testes recomendados

| Projeto   | Cenário           | Resultado esperado                  |
| --------- | ----------------- | ----------------------------------- |
| Automação | CSV válido        | Todos os produtos processados       |
| Automação | Campo ausente     | Registro ignorado ou erro informado |
| Dados     | Valores nulos     | Tratamento documentado              |
| ML        | Base de teste     | Métricas exibidas                   |
| Chatbot   | Ollama desligado  | Mensagem de erro amigável           |
| Chatbot   | Modelo ausente    | Orientação para download            |
| Chatbot   | Resposta inválida | Erro tratado                        |
| Chatbot   | Conversa longa    | Interface permanece funcional       |

---

## 📚 Aprendizados desenvolvidos

* automação de tarefas;
* leitura de CSV;
* Pandas;
* análise exploratória;
* visualização de dados;
* machine learning;
* preparação de dados;
* notebooks;
* criação de interfaces;
* consumo de API local;
* inteligência artificial local;
* organização de projetos Python.

---

## 🎓 Contexto educacional

Os projetos foram desenvolvidos durante uma jornada prática de Python.

O repositório registra a evolução desde uma automação de tarefas até aplicações de análise de dados, machine learning e inteligência artificial.

---

## 👨‍💻 Autor

Desenvolvido por **Ernesto — ONestoDev**.

[![GitHub](https://img.shields.io/badge/GitHub-ONestoDev-181717?style=for-the-badge\&logo=github)](https://github.com/ONestoDev)

---

## 📄 Licença

Adicione um arquivo `LICENSE` para definir as condições de uso, modificação e distribuição do conteúdo.
