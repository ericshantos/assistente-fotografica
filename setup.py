from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="asistente-fotografica",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["src", "selecionar_CR2", "config_imagem"],
    author="Eric dos Santos",
    author_email="ericshantos13@gmail.com",
    description="aplicação que fornece suporte para fotos tiradas com câmera Canon",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ericshantos/assistente-fotografica",
    license="MIT",
    keywords=["fotografia", "Canon"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Development Status :: 2 - Pre-Alpha",
        "Development Status :: 5 - Production/Stable"
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
