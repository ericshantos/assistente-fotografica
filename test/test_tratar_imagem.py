import sys

sys.path.append(rf"C:\Users\erics\PycharmProjects\assistente-fotografica")
sys.path.append(
    rf"C:\Users\erics\PycharmProjects\assistente-fotografica\src\config_imagem"
)

import unittest
from PIL import Image
from io import BytesIO
from src.config_imagem.tratar_imagem import tratar_imagem


class TestTratarImagem(unittest.TestCase):

    def setUp(self):
        # Cria uma imagem de teste
        self.imagem_teste = Image.new("RGB", (100, 100), "white")

    def tearDown(self):
        # Limpa os recursos
        self.imagem_teste.close()

    def test_tratar_imagem(self):
        # Salva a imagem de teste em memória
        buffer_imagem = BytesIO()
        self.imagem_teste.save(buffer_imagem, format="JPEG")
        buffer_imagem.seek(0)

        # Chama a função tratar_imagem
        imagem_tratada = tratar_imagem(buffer_imagem)

        # Verifica se os metadados do autor foram adicionados
        self.assertTrue("author" in imagem_tratada.info)
        self.assertEqual(imagem_tratada.info["author"], "Eric dos Santos")


if __name__ == "__main__":
    unittest.main()
