# Consolidador de Arquivos

Este projeto é uma aplicação em Python com uma interface gráfica moderna desenvolvida com **customtkinter**, projetada para consolidar arquivos **Excel (.xlsx)** ou **CSV (.csv)** de uma pasta de origem em um único arquivo de saída. É especialmente útil para automatizar o processo de unificação de múltiplos arquivos em um só.

## 📋 Funcionalidades

- **Seleção de pastas**: Permite escolher uma pasta de origem para ler os arquivos e uma pasta de saída para salvar o consolidado.
- **Tipos de arquivos suportados**: Suporta arquivos no formato .xlsx e .csv.
- **Configuração personalizada**: O usuário pode definir o nome do arquivo final e o tipo de arquivo de saída.
- **Adição de coluna**: Inclui automaticamente uma coluna no consolidado com o nome do arquivo original de onde a linha foi extraída.
- **Interface Responsiva e Moderna**: Interface escura, configurável com tema verde para uma melhor experiência de usuário.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal para o desenvolvimento do programa.
- **customtkinter**: Utilizado para criar uma interface gráfica responsiva e personalizada.
- **Pandas**: Gerencia e manipula os dados durante a consolidação.
- **Pillow**: Para o tratamento de imagens e ícones.
- **tkinter**: Para elementos adicionais da interface gráfica.

## 🚀 Como Usar

1. Clone o repositório para a sua máquina local:
   ```bash
   git clone <link-do-repositorio>
   
   Na interface:
Escolha a Pasta de Origem e a Pasta de Saída.
Defina o Tipo de Arquivo de Entrada (CSV ou Excel).
Insira o Nome do Arquivo Final (sem extensão).
Clique em Consolidar Arquivos para iniciar o processo.

## 📂 Estrutura do Projeto

main.py: Arquivo principal que contém o código do programa.
requirements.txt: Lista de dependências necessárias para o projeto.
image.ico 

## ⚠️ Observações

A pasta de origem deve conter arquivos no formato selecionado (CSV ou Excel), ou uma mensagem de erro será exibida.
A opção de arquivo de saída permite gerar o consolidado em formato .xlsx ou .csv, independentemente do tipo dos arquivos de entrada.

## Autor

Renan Fiuja - renanfiujah@gmail.com