# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo reponsável por criar o arquivo zip.
"""

import os, zipfile, shutil
from PIL import Image
import config_imagem


def criar_zip(nome_zip: str, imagens: list, nome_foto: str) -> None:
    """
    Cria um arquivo zip contendo as imagens tratadas.

    Args:
        nome_zip (str): O nome do arquivo zip a ser criado.
        imagens (list): Uma lista contendo os caminhos das imagens tratadas.
    """

    # Verifica se já existe uma pasta com o mesmo nome na pasta de downloads
    pasta_download, pasta_destino = config_imagem.verificar_pasta_existente(
        f"{nome_zip}.zip"
    )

    # Cria o arquivo zip
    with zipfile.ZipFile(pasta_destino, "w") as zip_file:
        for indice, imagem in enumerate(imagens):
            nome_imagem = (
                f"{nome_foto}{indice + 1}.jpg"  # Define o nome da imagem no zip
            )

            # Carregar a imagem
            with Image.open(imagem) as img:

                # Insere os metadados do autor
                config_imagem.inserir_metadados_autor(img)

            zip_file.write(imagem, os.path.join(pasta_destino, nome_imagem))

    # Move o arquivo zip para a pasta de downloads
    destino_zip = os.path.join(pasta_download, pasta_destino)
    shutil.move(pasta_destino, destino_zip)
