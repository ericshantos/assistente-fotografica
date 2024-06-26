"""
Pacote config_imagem

Pacote responsável por fornecer funções para o tratamento e download de imagens.

O pacote inclui as seguintes funções:

- tratar_imagem(imagem_rgb: str) -> Image: Aplica tratamento de imagem suavizando-a
e adicionando metadados do autor.

- download(img: Image, contador_download: ContadorDownload) -> None: Salva uma imagem
em formato JPEG na pasta de downloads do usuário, adicionando um contador ao nome do arquivo.

"""

# Autor
__author__ = "Eric dos Santos <github.com/ericSantos/API-meme-aleatorio>"

# Versão do pacote
__version__ = "1.1.1"
