# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo reponsável por abrir o explorador de arquivos
"""

import tkinter as tk
from tkinter import filedialog


def abrir_explorer() -> tuple[str]:
    """
    Abre um explorador de arquivos para permitir ao usuário selecionar arquivos CR2.

    Returns:
        None: Se nenhum arquivo for selecionado ou se o explorador for cancelado.
        list: Uma lista contendo os caminhos dos arquivos CR2 selecionados pelo usuário.
    """
    root = tk.Tk()
    root.withdraw() # Oculta a janela principal

    # Abre o explorador de arquivos
    caminho_arquivo = filedialog.askopenfilenames(filetypes=[('CR2 files','*.cr2')])

    if caminho_arquivo:

        # Se o usuário selecionar um arquivo, faça o procedimento
        return caminho_arquivo
