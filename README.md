
🔑# Gerador de Senha

Este é um gerador de senhas simples, desenvolvido em Python, que permite ao usuário criar senhas aleatórias com base em suas preferências de comprimento, letras maiúsculas, números e símbolos. O programa também oferece a opção de copiar a senha gerada para a área de transferência.

🛠️## Funcionalidades

- Geração de senhas aleatórias com letras minúsculas, maiúsculas, números e símbolos.
- Permite ao usuário escolher o comprimento da senha.
- Possui a opção de copiar a senha gerada para a área de transferência.

## Como Usar o Executável

1. Baixe o arquivo `gerador_senha.exe` na pasta `dist/`.
2. Clique duas vezes no arquivo `gerador_senha.exe` para executar o programa.

   **Durante a execução, o programa pedirá:**
   - O comprimento da senha (recomendado 12 caracteres).
   - Se você deseja incluir letras maiúsculas.
   - Se você deseja incluir números.
   - Se você deseja incluir símbolos.

3. O programa exibirá a senha gerada.
4. O programa perguntará se você deseja copiar a senha para a área de transferência. Responda `s` para copiar a senha.

   - Se optar por copiar, a senha será copiada e você poderá colá-la onde desejar.
   - Se não quiser copiar, o programa terminará.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
Gerador_de_Senha/
│
├── src/                    # Código-fonte
│   ├── gerador_senha.py     # Script Python para gerar senhas
│   └── icone.ico            # Ícone do executável (caso esteja gerando um executável)
│
└── dist/                   # Pasta contendo o executável gerado
    └── gerador_senha.exe    # Executável gerado pelo PyInstaller
```

## Dependências

Este projeto usa a biblioteca `pyperclip` para copiar a senha para a área de transferência.

Caso deseje rodar o código fonte diretamente em Python, instale as dependências executando o seguinte comando:

```bash
pip install pyperclip
```

## Como Rodar o Código Fonte

Se você deseja rodar o código-fonte, siga estas etapas:

1. Clone ou baixe este repositório.
2. Navegue até a pasta `src/` e execute o script `gerador_senha.py`:

   ```bash
   python gerador_senha.py
   ```

3. O programa pedirá que você insira as preferências e exibirá a senha gerada.


