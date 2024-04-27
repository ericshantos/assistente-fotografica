# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo responsável por criar o arquivo .zip.
"""

import os, zipfile
from PIL import Image
import config_imagem


def criar_zip(arquivo_zip: str, objetos: list[str]) -> None:
    """
    Cria um arquivo zip contendo as imagens processadas.

    Parâmetros:
    - arquivo_zip (str): O nome do arquivo zip a ser criado.
    - objetos (list): Uma lista de caminhos para os objetos a serem adicionados ao arquivo zip.

    Retorna:
    None
    """
    # Obtém o diretório de Downloads
    diretorio_downloads = os.path.join(os.path.expanduser("~"), "Downloads")

    # Caminho completo para o arquivo zip na pasta de Downloads
    caminho_zip = os.path.join(diretorio_downloads, arquivo_zip)

    with zipfile.ZipFile(caminho_zip, "w") as zip:

        for contador, objeto in enumerate(objetos, start=1):

            # Obtem o nome do arquivo da parte final do caminho
            nome_arquivo = os.path.basename(objeto)

            # Constrói o novo nome do arquivo com o sufixo e contador
            novo_nome_arquivo = (
                f"_tireifoto_{contador}{os.path.splitext(nome_arquivo)[1]}"
            )

            # Carregar a imagem
            with Image.open(objeto) as img:

                # Insere os metadados do autor
                config_imagem.inserir_metadados_autor(img)

            # Adiciona o objeto ao arquivo zip no diretório raiz
            zip.write(objeto, arcname=novo_nome_arquivo)
