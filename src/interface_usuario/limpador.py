# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo reponsável por limpar o terminal
"""

import os


def limpar_terminal():
    """Limpa o terminal."""

    # Verifica o sistema operacional
    if os.name == "nt":  # Windows

        os.system("cls")

    else:  # Outros sistemas (Linux, macOS)

        os.system("clear")
