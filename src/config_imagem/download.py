import os
from PIL import Image
import config_imagem


def download(img: Image, nome_foto: str) -> None:
    """
    Salva uma imagem no diretório de downloads com o nome especificado.

    Args:
        img (PIL.Image): A imagem a ser salva.
        nome_foto (str): O nome desejado para a imagem.

    Raises:
        IOError: Se ocorrer um erro ao salvar a imagem.

    Example:
        Para salvar uma imagem chamada "minha_imagem.png" no diretório de downloads:
        download(imagem, "minha_imagem.png")
    """
    # Caminho para o diretório de downloads
    diretorio_download, nome_imagem = config_imagem.verificar_pasta_existente(nome_foto)

    # Define o caminho completo para salvar a imagem com o contador no nome
    caminho_com_contador = os.path.join(diretorio_download, nome_imagem)

    try:
        # Salva a imagem no caminho especificado
        img.save(caminho_com_contador)

    except IOError as e:
        # Se ocorrer um erro ao salvar a imagem, levanta a exceção para informar o problema
        raise IOError(f"Erro ao salvar a imagem: {str(e)}")
