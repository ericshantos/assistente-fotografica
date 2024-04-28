# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo principal, responsável pela execulção da aplicação.
"""

import os, tempfile
import interface_usuario
import selecionar_CR2, config_imagem
from PIL import Image


def salvar_imagem_temporaria(imagem: Image) -> None:
    """
    Salva a imagem tratada em um arquivo temporário e retorna o caminho do arquivo.
    """
    # Gere um nome de arquivo temporário único
    arquivo_temporario = tempfile.NamedTemporaryFile(suffix=".jpeg", delete=False)

    # Salva a imagem tratada no arquivo temporário
    imagem.save(arquivo_temporario.name)

    # Retorna o caminho do arquivo temporário
    return arquivo_temporario.name


def main() -> None:
    """
    Realiza o processamento de imagens RAW (.CR2) e fornece opções de saída com base
    na quantidade de imagens selecionadas.

    Esta função realiza as seguintes etapas:
    1. Abre a janela do explorador de arquivos para selecionar imagens RAW (.CR2).
    2. Converte as imagens RAW em formato RGB.
    3. Aplica tratamento de imagem nas imagens RGB selecionadas.
    4. Cria um arquivo zip contendo as imagens tratadas, se mais de uma imagem for selecionada.
    5. Realiza o download das imagens tratadas, se apenas uma imagem for selecionada.
    6. Exibe uma mensagem indicando a conclusão do processo.
    """

    # Abre a janela do explorador de arquivos para selecionar as imagens RAW (.CR2)
    imagens_selecionadas = selecionar_CR2.abrir_explorer()

    informacoes_foto = interface_usuario.InformacoesFoto()

    # Solicita o nome das fotos ao usuário e armazena na variável nome_fotos
    nome_foto = informacoes_foto.pegar_nome_foto()

    if len(imagens_selecionadas) > 1:

        # Solicita o nome do diretório para o download das fotos ao usuário e armazena na variável nome_arquivo_zip
        nome_arquivo_zip = informacoes_foto.pegar_nome_arquivo_zip()

    imagens_tratadas = []  # Lista para armazenar caminhos das imagens tratadas

    # Processa as imagens RAW para convertê-las em formato RGB
    for indice, imagem in enumerate(imagens_selecionadas):
        imagem_rgb = selecionar_CR2.processar_raw(
            imagem
        )  # Converte a imagem RAW em RGB

        # Aplica tratamento de imagem nas imagens RGB selecionadas
        imagem_tratada = config_imagem.tratar_imagem(imagem_rgb)

        if len(imagens_selecionadas) > 1:  # Se mais de uma imagem for selecionada

            # Salva a imagem tratada em um arquivo temporário e obtém o caminho do arquivo
            caminho_imagem_temporaria = salvar_imagem_temporaria(imagem_tratada)

            # Adiciona o caminho do arquivo temporário à lista
            imagens_tratadas.append(caminho_imagem_temporaria)

            if (
                indice == len(imagens_selecionadas) - 1
            ):  # Executa apenas na última iteração
                config_imagem.criar_zip(
                    nome_arquivo_zip, imagens_tratadas, nome_foto
                )  # Cria um arquivo zip

                # Remove os arquivos temporários após o término do processo
                for imagem_temporaria in imagens_tratadas:
                    os.remove(imagem_temporaria)

        else:  # Se apenas uma imagem for selecionada
            config_imagem.download(
                imagem_tratada, nome_foto
            )  # Realiza o download da imagem tratada
            os.remove(imagem_rgb)  # Remove a imagem tratada após o download

    # Mensagem de conclusão do processo
    print("Processo realizado com sucesso!!")


if __name__ == "__main__":
    main()
