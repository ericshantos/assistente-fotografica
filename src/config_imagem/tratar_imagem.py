# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Pacote que trata a imagem PIL e a retorna como JPEG
"""

import os
from io import BytesIO
from PIL import Image, ImageFilter


def tratar_imagem(imagem_rgb: Image) -> BytesIO:
    """
    Aplica tratamento de imagem suavizando-a e adicionando metadados do autor.

    Parameters:
    imagem_rgb (str): O caminho para o arquivo de imagem RGB a ser tratado.

    Returns:
    Image: Um objeto de imagem contendo a imagem tratada.

    """
    # Carrega a imagem RGB
    with Image.open(imagem_rgb) as imagem:

        # Suaviza a imagem
        imagem_suavizada = imagem.filter(ImageFilter.SMOOTH)

        # Acentua a nitidez da imagem
        imagem_nitida = imagem_suavizada.filter(ImageFilter.SHARPEN)

        # Suaviza ainda mais a imagem
        imagem_final = imagem_nitida.filter(ImageFilter.SMOOTH_MORE)

        # Cria um objeto BytesIO para armazenar dados de imagem em memória
        imagem_jpeg_buffer = BytesIO()

        # Converte para JPEG
        imagem_final.save(imagem_jpeg_buffer, format="JPEG", quality=100)

        # Retorna  ao início do buffer de imagem
        imagem_jpeg_buffer.seek(0)

        # Cria uma nova imagem a partir do buffer JPEG
        imagem_jpeg = Image.open(imagem_jpeg_buffer)

        # Apaga o arquivo temporário
        os.remove(imagem_rgb)

    return inserir_metadados_autor(imagem_jpeg)


def inserir_metadados_autor(imagem_jpeg: Image) -> Image:

    # Inclui metadados do autor da imagem
    autor = "Eric dos Santos"
    imagem_jpeg.info["author"] = autor

    return imagem_jpeg
