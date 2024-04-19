"""
Pacote selecionar_CR2

Pacote responsável por fornecer funções para processamento de imagens RAW.

O pacote inclui as seguintes funções:

- abrir_explorer(): Abre um explorador de arquivos para permitir ao usuário 
selecionar arquivos CR2.

- processar_raw(raw: str) -> str: Processa uma imagem RAW para o formato RGB 
e retorna o caminho para o arquivo temporário da imagem processada em formato 
JPEG.

"""

# Importações do pacote
from .abrir_explorador import abrir_explorer
from .processar_raw import processar_raw

# Autor
__author__ = "Eric dos Santos <github.com/ericSantos/API-meme-aleatorio>"

# Versão do pacote
__version__ = "1.0.0"
