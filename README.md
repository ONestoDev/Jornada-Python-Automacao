# Jornada Python Automacao

Projeto de automacao com Python para cadastrar produtos em um sistema web a partir de uma planilha CSV.

O script principal abre o navegador, acessa a pagina de login, preenche as credenciais e cadastra automaticamente cada produto listado no arquivo `produtos.csv`.

## Arquivos do projeto

- `codigo.py`: script principal da automacao.
- `produtos.csv`: base de produtos usada no cadastro.
- `pegar_posicao.py`: script auxiliar para descobrir a posicao atual do mouse na tela.
- `gabarito.py`: versao de referencia do passo a passo da automacao.

## Requisitos

- Python 3 instalado.
- Navegador Safari, conforme configurado no `codigo.py`.
- Permissao de acessibilidade para o terminal ou IDE controlar mouse e teclado no macOS.
- Bibliotecas Python:
  - `pyautogui`
  - `pandas`

## Instalacao

Crie e ative um ambiente virtual, se desejar:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependencias:

```bash
pip install pyautogui pandas
```

## Configuracao

Antes de executar, edite as variaveis no inicio do arquivo `codigo.py`:

```python
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "seu_email@mail.com"
senha = "sua_senha"
```

Substitua `email` e `senha` pelas credenciais corretas do sistema.

## Como executar

Com o ambiente configurado, execute:

```bash
python codigo.py
```

Durante a execucao, evite mexer no mouse ou teclado. O PyAutoGUI usa coordenadas fixas da tela, entao qualquer mudanca de janela, zoom, resolucao ou navegador pode afetar os cliques.

## Ajuste de coordenadas

Se os cliques nao estiverem acertando os campos corretos, use o script auxiliar:

```bash
python pegar_posicao.py
```

Depois de executar, posicione o mouse sobre o ponto desejado antes da contagem terminar. O script imprime a coordenada atual do mouse, que pode ser usada para ajustar chamadas como:

```python
pyautogui.click(x=685, y=451)
```

## Estrutura esperada do CSV

O arquivo `produtos.csv` deve conter as seguintes colunas:

```text
codigo,marca,tipo,categoria,preco_unitario,custo,obs
```

Cada linha representa um produto que sera cadastrado automaticamente.

## Observacoes

- O fluxo atual foi configurado para macOS, usando `command + space` para abrir o Safari.
- Em Windows, o proprio `codigo.py` possui um trecho comentado com uma alternativa usando a tecla `win` e o Chrome.
- Como a automacao depende da interface visual, valide as coordenadas antes de rodar o cadastro completo.
