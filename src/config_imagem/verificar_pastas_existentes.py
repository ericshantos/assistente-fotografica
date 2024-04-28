# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo reponsável por verificar se há arquivos duplicados.
"""

import re, os


def verificar_pasta_existente(item_de_sistema: str) -> str:
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

    # Obtém a extensão so item de sistema
    extensao = os.path.splitext(item_de_sistema)[1]

    # Obtém o nome do item de sistema
    nome_item_do_sistema = os.path.splitext(item_de_sistema)[0]

    # Conta o número de cópias da pasta com o mesmo nome no diretório de downloads
    contador = contar_copias(diretorio_download, nome_item_do_sistema)

    # Verifica se já existe pelo menos uma cópia da pasta
    if contador >= 1:
        retorno = f"{nome_item_do_sistema}({contador + 1})"
    else:
        retorno = nome_item_do_sistema

    # Retorna o caminho para o diretório de downloads e o nome do arquivo ZIP
    return diretorio_download, f"{retorno}{extensao}"


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
