# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo responsável por converter as imagem selecionadas
em um formato execultável
"""

import rawpy
import tempfile
from PIL import Image


def processar_raw(raw):

    try:
        # Carrega a imagem RAW
        with rawpy.imread(raw) as raw:
            # Processa a imagem RAW para o formato RGB
            imagem_rgb = raw.postprocess()

            # Salva a imagem temporariamente
            with tempfile.NamedTemporaryFile(delete=False, suffix='.jpeg') as temp_file:
                temp_path = temp_file.name
                # Salva a imagem processada em disco
                Image.fromarray(imagem_rgb).save(temp_path)

    except rawpy.LibRawIOError as e:

        print(f"Erro de E/S ao processar o arquivo RAW '{raw}': {e}")

    return temp_path
