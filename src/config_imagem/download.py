import os
from PIL import Image

class ContadorDownload:

    def __init__(self) -> None:
        self._contador = 0

    def incrementar(self) -> int:
        self._contador += 1

    @property
    def contador(self) -> int:
        return self._contador


def download(img: Image, contador_download: ContadorDownload) -> None:
    """
    Salva uma imagem em formato JPEG na pasta de downloads do usuário,
    adicionando um contador ao nome do arquivo.

    Parameters:
    img (Image): O objeto de imagem a ser salvo.
    contador_download (ContadorDownload): O objeto contador que mantém o
    controle do número de downloads.

    Returns:
    None

    """

    # Obtém o nome do usuário do ambiente
    nome_do_usuario = os.environ.get('USERNAME')

    # Incrementa o contador de downloads
    contador_download.incrementar()

    # Define o caminho completo para salvar a imagem com o contador no nome
    caminho_com_contador = fr"C:\Users\{nome_do_usuario}\Downloads\_tireifoto_{contador_download.contador}.jpeg"

    # Salva a imagem no caminho especificado
    img.save(caminho_com_contador)
