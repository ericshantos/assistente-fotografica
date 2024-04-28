# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo reponsável por capturar dados sobre as fotos
"""


class InformacoesFoto:
    """
    Classe para gerenciar informações sobre fotos.

    Attributes:
        nome_arquivo_zip (str): O nome do arquivo zip que será gerado.
        nome_foto (str): O nome das fotos que serão baixadas.
    """

    def __init__(self) -> None:
        """
        Inicializa uma instância da classe InformacoesFoto.

        Initializes:
            nome_arquivo_zip (None): O nome do arquivo zip que será gerado.
            nome_foto (None): O nome das fotos que serão baixadas.
        """
        self.nome_arquivo_zip = None
        self.nome_foto = None

    def pegar_nome_foto(self):
        """
        Solicita ao usuário o nome das fotos e armazena na variável nome_foto.

        Returns:
            str: O nome das fotos fornecido pelo usuário.
        """
        # Solicita o nome das fotos ao usuário e armazena na variável nome_foto
        self.nome_foto = input("Qual deve ser o nome das fotos:")
        return self.nome_foto

    def pegar_nome_arquivo_zip(self):
        """
        Solicita ao usuário o nome do diretório para download das fotos e armazena na variável nome_arquivo_zip.

        Returns:
            str: O nome do diretório fornecido pelo usuário.
        """
        # Solicita o nome do diretório para o download das fotos ao usuário e armazena na variável nome_arquivo_zip
        self.nome_arquivo_zip = input(
            "Qual deve ser o nome do diretório para download: "
        )
        return self.nome_arquivo_zip
