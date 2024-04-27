import sys

sys.path.append(rf"C:\Users\erics\PycharmProjects\assistente-fotografica")
sys.path.append(
    rf"C:\Users\erics\PycharmProjects\assistente-fotografica\src\config_imagem"
)

from src.config_imagem.download import download
import unittest
from unittest.mock import MagicMock
from PIL import Image
import os


class TestDownloadFunction(unittest.TestCase):

    def test_download(self):
        # Simulando a variável de ambiente
        os.environ["USERNAME"] = "usuario_teste"

        # Criando um mock para ContadorDownload
        contador_mock = MagicMock()
        contador_mock.contador = 1

        # Criando uma imagem mock com o método save
        img_mock = MagicMock(spec=Image)
        img_mock.save = MagicMock()

        # Chamando a função download
        download(img_mock, contador_mock)

        # Verificando se o método incrementar de ContadorDownload foi chamado
        contador_mock.incrementar.assert_called_once()

        # Verificando se a imagem foi salva com o nome de arquivo correto
        caminho_esperado = rf"C:\Users\usuario_teste\Downloads\_tireifoto_1.jpeg"
        img_mock.save.assert_called_once_with(caminho_esperado)


if __name__ == "__main__":
    unittest.main()
