# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo reponsável por criar o arquivo zip.
"""

import os, zipfile, shutil, tempfile
from PIL import Image
import config_imagem


def criar_zip(**kwargs_imagem: dict) -> None:
    """
    Cria um arquivo zip contendo as imagens tratadas.

    Args:
        nome_zip (str): O nome do arquivo zip a ser criado.
        imagens (list): Uma lista contendo os caminhos das imagens tratadas.
    """

    # Verifica se já existe uma pasta com o mesmo nome na pasta de downloads
    pasta_download, pasta_destino = config_imagem.verificar_pasta_existente(
        f"{kwargs_imagem['nome_zip']}.zip"
    )

    # LIsta os arquivos temporários
    arquivos_temporarios = []

    # Cria o arquivo zip
    with zipfile.ZipFile(pasta_destino, "w") as zip_file:

        for indice, imagem in enumerate(kwargs_imagem["lista_imagens"]):
            nome_imagem = f"{kwargs_imagem['nome_foto']}{indice + 1}.jpeg"  # Define o nome da imagem no zip

            # Trabalhando com os arquivos temporários
            imagem_temporaria = salvar_imagem_temporaria(imagem)
            arquivos_temporarios.append(imagem_temporaria)

            # Carregar a imagem
            with Image.open(imagem_temporaria) as img:
                # Insere os metadados do autor
                config_imagem.inserir_metadados_autor(img)

            # Adiciona as imagens processadas ao aquivo .zip
            zip_file.write(imagem_temporaria, os.path.join(pasta_destino, nome_imagem))

    # Move o arquivo zip para a pasta de downloads
    destino_zip = os.path.join(pasta_download, pasta_destino)
    shutil.move(pasta_destino, destino_zip)

    # Remove os arquivos temporários
    for arquivo_temporario in arquivos_temporarios:

        os.remove(arquivo_temporario)


def salvar_imagem_temporaria(imagem: Image) -> str:
    """
    Salva a imagem tratada em um arquivo temporário e retorna o caminho do arquivo.
    """
    # Gere um nome de arquivo temporário único
    with tempfile.NamedTemporaryFile(
        suffix=".jpeg", delete=False
    ) as arquivo_temporario:

        # Salva a imagem tratada no arquivo temporário
        imagem.save(arquivo_temporario.name)

    # Retorna o caminho do arquivo temporário
    return arquivo_temporario.name
