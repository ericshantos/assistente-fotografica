# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo responsável por converter as imagem selecionadas
em um formato execultável
"""
import rawpy
import tempfile
from PIL import Image


def processar_raw(raw: str) -> str:
    """
    Processa uma imagem RAW para o formato RGB.

    Parameters:
    raw (str): O caminho para o arquivo de imagem RAW a ser processado.

    Returns:
    str: O caminho para o arquivo temporário da imagem processada em formato JPEG. Retorna None em caso de erro.

    Raises:
    Nenhum.

    """
    try:
        # Carrega a imagem RAW
        with rawpy.imread(raw) as raw:
            # Processa a imagem RAW para o formato RGB
            imagem_rgb = raw.postprocess()

            # Salva a imagem temporariamente
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpeg") as temp_file:
                temp_path = temp_file.name
                # Salva a imagem processada em disco
                Image.fromarray(imagem_rgb).save(temp_path)

    # Captura e imprime erros de E/S ao processar o arquivo RAW
    except rawpy.LibRawIOError as e:
        print(f"Erro de E/S ao processar o arquivo RAW '{raw}': {e}")
        print("A função está retornando None devido a um erro de E/S.")
        return None

    return temp_path  # Retorna o caminho para o arquivo temporário da imagem processada
