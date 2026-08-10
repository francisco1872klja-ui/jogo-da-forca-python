# 🪓 Jogo da Forca em Python (POO)

Um jogo da forca interativo desenvolvido em Python utilizando conceitos de **Programação Orientada a Objetos (POO)**, manipulação de arquivos dinâmicos e arte em ASCII.

## 🚀 Funcionalidades

- **Menu de Categorias:** Escolha o tema das palavras antes de começar a jogar (ex: *Tecnologia*, *Frutas*).
- **Leitura Dinâmica:** As palavras são carregadas diretamente de arquivos `.txt` organizados na pasta `Categorias/`.
- **Arte ASCII:** Visualização gráfica da forca e do boneco a cada tentativa incorreta.
- **Suporte a UTF-8:** Leitura correta de palavras com acentuação e caracteres especiais em português.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- Módulos nativos: `os`, `random`

## 📁 Estrutura do Projeto

```text
jogo_forca/
│
├── Categorias/
│   ├── Tecnologia.txt
│   └── Frutas.txt
│
├── .gitignore
├── jogo_forca.py
├── __main__.py
└── README.md
