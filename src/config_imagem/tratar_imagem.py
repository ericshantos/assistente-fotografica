# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Pacote que trata a imagem PIL e a retorna como JPEG
"""

from io import BytesIO
from PIL import Image, ImageFilter

def tratar_imagem(imagem_rgb):

    # Carrega a imagem RGB
    with Image.open(imagem_rgb) as imagem:

        imagem_suavizada = imagem.filter(ImageFilter.SMOOTH)

        # Cria um objeto BytesIO para armazenar dados de imagem em memória
        imagem_jpeg_buffer = BytesIO()

        # Converte para JPEG
        imagem_suavizada.save(imagem_jpeg_buffer, format='JPEG', quality=100)

        # Retorna  ao início do buffer de imagem
        imagem_jpeg_buffer.seek(0)

        # Cria uma nova imagem a partir do buffer JPEG
        imagem_jpeg = Image.open(imagem_jpeg_buffer)

    return inserir_metadados_autor(imagem_jpeg)

def inserir_metadados_autor(imagem_jpeg):

    # Inclui metadados do autor na imagem
    autor = 'Eric dos Santos'
    imagem_jpeg.info['author'] = autor

    return imagem_jpeg
