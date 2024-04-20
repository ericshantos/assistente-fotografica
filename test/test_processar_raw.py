import sys

sys.path.append(rf"C:\Users\erics\PycharmProjects\assistente-fotografica")
sys.path.append(
    rf"C:\Users\erics\PycharmProjects\assistente-fotografica\src\selecionar_CR2"
)

import unittest
from unittest.mock import MagicMock, patch
from tempfile import NamedTemporaryFile
from PIL import Image
import rawpy
from src.selecionar_CR2.processar_raw import processar_raw


class TestProcessarRAW(unittest.TestCase):

    @patch("rawpy.imread")
    @patch("PIL.Image.fromarray")
    @patch("tempfile.NamedTemporaryFile")
    def test_processar_raw_sucesso(
        self, mock_tempfile, mock_image_fromarray, mock_rawpy_imread
    ):
        # Mocks
        mock_rawpy = MagicMock()
        mock_rawpy.postprocess.return_value = "imagem_rgb"
        mock_rawpy_imread.return_value.__enter__.return_value = mock_rawpy

        mock_tempfile_instance = MagicMock(spec=NamedTemporaryFile)
        mock_tempfile_instance.name = "temp_path.jpeg"
        mock_tempfile.return_value.__enter__.return_value = mock_tempfile_instance

        mock_image_fromarray_instance = MagicMock(spec=Image.Image)
        mock_image_fromarray.return_value = mock_image_fromarray_instance

        # Teste
        resultado = processar_raw("caminho/para/arquivo.raw")

        # Verificações
        self.assertEqual(resultado, "temp_path.jpeg")
        mock_rawpy_imread.assert_called_once_with("caminho/para/arquivo.raw")
        mock_rawpy.postprocess.assert_called_once()
        mock_image_fromarray.assert_called_once_with("imagem_rgb")
        mock_image_fromarray_instance.save.assert_called_once_with("temp_path.jpeg")

    @patch("rawpy.imread")
    def test_processar_raw_erro_io(self, mock_rawpy_imread):
        # Mocks
        mock_rawpy_imread.side_effect = rawpy.LibRawIOError("Erro de E/S")

        # Teste
        resultado = processar_raw("caminho/para/arquivo_inexistente.raw")

        # Verificações
        self.assertIsNone(resultado)


if __name__ == "__main__":
    unittest.main()
