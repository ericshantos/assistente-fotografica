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


def download(img: Image, contador_download: ContadorDownload):

    nome_do_usuario = os.environ.get('USERNAME')

    contador_download.incrementar()

    caminho_com_contador = fr"C:\Users\{nome_do_usuario}\Downloads\_tireifoto_{contador_download.contador}.jpeg"

    img.save(caminho_com_contador)
