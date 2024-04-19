# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Módulo principal, responsável pela execulção da aplicação.
"""

from config_imagem.download import ContadorDownload
import selecionar_CR2
import config_imagem


def main() -> None:

    contador = ContadorDownload()

    # Abre a janela do explorador de arquivos para selecionar as imagens RAW (.CR2)
    imagens_selecionadas = selecionar_CR2.abrir_explorer()

    for imagem in imagens_selecionadas:

        # Processa as imagens RAW para convertê-las em formato RGB
        imagem_rgb = selecionar_CR2.processar_raw(imagem)

        # Aplica tratamento de imagem nas imagens RGB selecionadas
        imagem_jpeg = config_imagem.tratar_imagem(imagem_rgb)

        config_imagem.download(imagem_jpeg, contador)

    # Mensagem de conclusão do processo
    print('Processo realizado com sucesso!!')

if __name__ == '__main__':
    main()
