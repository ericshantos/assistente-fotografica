# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo principal, responsável pela execulção da aplicação.
"""

import interface_usuario
import selecionar_CR2, config_imagem
from tqdm import tqdm


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

    # Imagens processadas
    imagens_processadas = []

    # Barra de progresso
    progress_bar = tqdm(
        total=len(imagens_selecionadas), desc="Progresso", unit="iterações"
    )

    # Processa as imagens RAW para convertê-las em formato RGB
    for indice, imagem in enumerate(imagens_selecionadas):

        imagem_rgb = selecionar_CR2.processar_raw(
            imagem
        )  # Converte a imagem RAW em RGB

        # Aplica tratamento de imagem nas imagens RGB selecionadas
        imagem_tratada = config_imagem.tratar_imagem(imagem_rgb)

        if len(imagens_selecionadas) > 1:  # Se mais de uma imagem for selecionada

            imagens_processadas.append(imagem_tratada)

            if (
                indice == len(imagens_selecionadas) - 1
            ):  # Executa apenas na última iteração

                config_imagem.criar_zip(
                    nome_zip=nome_arquivo_zip,
                    lista_imagens=imagens_processadas,
                    nome_foto=nome_foto,
                )  # Cria um arquivo zip

        else:  # Se apenas uma imagem for selecionada

            config_imagem.download(
                imagem_tratada, f"{nome_foto}.jpeg"
            )  # Realiza o download da imagem tratada

        progress_bar.update(1)  # Atualiza a barra de progresso

    progress_bar.close()  # Fecha a barra de progresso ao finalizar o loop

    # Mensagem de conclusão do processo
    print("Processo realizado com sucesso!!")


if __name__ == "__main__":
    main()
