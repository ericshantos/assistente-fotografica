"""
Pacote config_imagem

Pacote responsável por fornecer funções para o tratamento e download de imagens.

O pacote inclui as seguintes funções:

- tratar_imagem(imagem_rgb: str) -> Image: Aplica tratamento de imagem suavizando-a
e adicionando metadados do autor.

- download(img: Image, contador_download: ContadorDownload) -> None: Salva uma imagem
em formato JPEG na pasta de downloads do usuário, adicionando um contador ao nome do arquivo.

"""

# Importações do pacote
from .tratar_imagem import tratar_imagem, inserir_metadados_autor
from .verificar_pastas_existentes import verificar_pasta_existente
from .download import download
from .criar_zip import criar_zip

# Autor
__author__ = "Eric dos Santos <github.com/ericSantos/API-meme-aleatorio>"

# Versão do pacote
__version__ = "1.0.1"
