# Jornada Python Automacao

Repositorio com os projetos desenvolvidos durante a Jornada Python, cobrindo automacao, analise de dados, machine learning e um espaco para a evolucao do chatbot em tempo real.

## Projetos

| Projeto | Conteudo | Arquivos principais |
| --- | --- | --- |
| Projeto 1 - Automacao de Tarefas | Cadastro automatico de produtos em um sistema web a partir de um CSV | `codigo.py`, `gabarito.py`, `pegar_posicao.py`, `produtos.csv` |
| Projeto 2 - Analisando Dados | Analise exploratoria de cancelamentos com notebook e visualizacoes | `inicial.ipynb`, `gabarito.ipynb`, `cancelamentos.csv` |
| Projeto 3 - Previsao com Machine Learning | Classificacao e previsao de clientes com modelos de ML | `inicial.ipynb`, `gabarito.ipynb`, `clientes.csv`, `novos_clientes.csv` |
| Projeto 4 - Chatbot com IA em Tempo Real | Chatbot com interface Streamlit e IA local gratuita executada pelo Ollama | `chatbot.py`, `main.py`, `auxiliar.py` |

## Requisitos

Os projetos usam bibliotecas diferentes. Em geral, voce vai precisar de:

- Python 3
- `pandas`
- `pyautogui`
- `plotly`
- `scikit-learn`
- `openpyxl`
- `nbformat`
- `ipykernel`
- `streamlit`
- Ollama com o modelo `qwen2.5:1.5b`

## Instalacao

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Instale as dependencias mais comuns:

```bash
pip install pandas pyautogui plotly scikit-learn openpyxl nbformat ipykernel streamlit
```

Para executar o chatbot gratuitamente no macOS, instale o Ollama e baixe o modelo local:

```bash
brew install ollama
brew services start ollama
ollama pull qwen2.5:1.5b
```

## Como executar

### Projeto 1

```bash
python "Projeto 1 - Automacao de Tarefas\codigo.py"
```

Se necessario, use o auxiliar para descobrir coordenadas do mouse:

```bash
python "Projeto 1 - Automacao de Tarefas\pegar_posicao.py"
```

### Projetos 2 e 3

Abra os notebooks em Jupyter, VS Code ou PyCharm e execute as celulas normalmente.

### Projeto 4

Execute o chatbot Streamlit a partir da raiz do repositorio:

```bash
streamlit run "Projeto 4 - Chatbot com IA em Tempo Real/chatbot.py"
```

Depois, acesse `http://localhost:8501` no navegador. O chatbot usa o modelo local `qwen2.5:1.5b`, portanto nao precisa de chave da OpenAI nem gera cobranca por mensagem.

## Observacoes

- O Projeto 1 foi montado para automacao por coordenadas de tela; pequenas mudancas de resolucao, zoom ou janela podem afetar os cliques.
- O fluxo do Projeto 1 usa Safari no macOS, mas o arquivo `codigo.py` tambem possui alternativa comentada para Windows.
- Os arquivos CSV devem permanecer nas pastas dos respectivos projetos para que os notebooks e scripts encontrem os dados corretamente.
- No primeiro uso do Projeto 4, o download do modelo ocupa aproximadamente 1 GB. As respostas sao processadas localmente e podem levar alguns segundos, dependendo do computador.
