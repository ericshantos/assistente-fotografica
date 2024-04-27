# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo reponsável por criar o arquivo zip.
"""

import os, zipfile, shutil, re
from PIL import Image
import config_imagem


def criar_zip(nome_zip: str, imagens: list) -> None:
    """
    Cria um arquivo zip contendo as imagens tratadas.

    Args:
        nome_zip (str): O nome do arquivo zip a ser criado.
        imagens (list): Uma lista contendo os caminhos das imagens tratadas.
    """

    # Verifica se já existe uma pasta com o mesmo nome na pasta de downloads
    pasta_download, pasta_destino = verificar_pasta_existente(nome_zip)

    # Cria o arquivo zip
    with zipfile.ZipFile(pasta_destino, "w") as zip_file:
        for indice, imagem in enumerate(imagens):
            nome_imagem = (
                f"_tireifoto_{indice + 1}.jpg"  # Define o nome da imagem no zip
            )

            # Carregar a imagem
            with Image.open(imagem) as img:

                # Insere os metadados do autor
                config_imagem.inserir_metadados_autor(img)

            zip_file.write(imagem, os.path.join(pasta_destino, nome_imagem))

    # Move o arquivo zip para a pasta de downloads
    destino_zip = os.path.join(pasta_download, f"{pasta_destino}")
    shutil.move(pasta_destino, destino_zip)


def verificar_pasta_existente(nome_da_pasta: str) -> str:
    """
    Verifica se uma pasta com o nome especificado já existe no diretório de downloads.
    Se a pasta existir, adiciona um número ao nome para diferenciá-la.

    Args:
        nome_da_pasta (str): O nome da pasta a ser verificada.

    Returns:
        Tuple[str, str]: Uma tupla contendo o caminho para o diretório de downloads e o nome do arquivo ZIP.
    """

    # Caminho para o diretório de downloads
    diretorio_download = os.path.join(os.path.expanduser("~"), "Downloads")

    # Conta o número de cópias da pasta com o mesmo nome no diretório de downloads
    contador = contar_copias(diretorio_download, nome_da_pasta)

    # Verifica se já existe pelo menos uma cópia da pasta
    if contador >= 1:
        nome_zip = f"{nome_da_pasta}({contador + 1})"
    else:
        nome_zip = nome_da_pasta

    # Retorna o caminho para o diretório de downloads e o nome do arquivo ZIP
    return diretorio_download, f"{nome_zip}.zip"


def contar_copias(diretorio: str, arquivo: str) -> int:
    """
    Conta o número de cópias de um arquivo com o nome especificado no diretório fornecido.

    Args:
        diretorio (str): O caminho para o diretório onde os arquivos serão contados.
        arquivo (str): O nome do arquivo base para procurar cópias.

    Returns:
        int: O número de cópias encontradas do arquivo.
    """

    # Inicializa o contador de cópias
    contagem = 0

    # Percorre todos os arquivos no diretório
    for nome_arquivo in os.listdir(diretorio):

        # Verifica se o nome do arquivo corresponde ao padrão esperado
        if re.match(rf"{re.escape(arquivo)}(\(\d+\))?(\..+)?$", nome_arquivo):
            contagem += 1

    return contagem
