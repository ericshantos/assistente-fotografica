import sys

sys.path.append(
    rf"C:\Users\erics\PycharmProjects\assistente-fotografica"
)
sys.path.append(
    rf"C:\Users\erics\PycharmProjects\assistente-fotografica\src\selecionar_CR2"
)

import unittest
from unittest.mock import patch
from src.selecionar_CR2.selecionar_CR2 import abrir_explorer


class TestAbrirExplorer(unittest.TestCase):

    @patch("src.selecionar_CR2.selecionar_CR2.tk.Tk")
    @patch("src.selecionar_CR2.selecionar_CR2.filedialog.askopenfilenames")
    def test_abrir_explorer_sucesso(self, mock_askopenfilenames, mock_tk):
        # Mock do retorno da seleção do arquivo
        mock_askopenfilenames.return_value = (
            "caminho/arquivo1.cr2",
            "caminho/arquivo2.cr2",
        )

        # Chamando a função
        resultado = abrir_explorer()

        # Verificando se o explorador foi aberto corretamente
        mock_tk.assert_called_once()
        mock_askopenfilenames.assert_called_once_with(
            filetypes=[("CR2 files", "*.cr2")]
        )

        # Verificando o resultado
        self.assertEqual(resultado, ("caminho/arquivo1.cr2", "caminho/arquivo2.cr2"))

    @patch("src.selecionar_CR2.selecionar_CR2.tk.Tk")
    @patch("src.selecionar_CR2.selecionar_CR2.filedialog.askopenfilenames")
    def test_abrir_explorer_cancelado(self, mock_askopenfilenames, mock_tk):
        # Mock do retorno da seleção do arquivo
        mock_askopenfilenames.return_value = ""

        # Chamando a função
        resultado = abrir_explorer()

        # Verificando se o explorador foi aberto corretamente
        mock_tk.assert_called_once()
        mock_askopenfilenames.assert_called_once_with(
            filetypes=[("CR2 files", "*.cr2")]
        )

        # Verificando o resultado
        self.assertIsNone(resultado)


if __name__ == "__main__":
    unittest.main()
