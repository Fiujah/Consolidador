import os
import pandas as pd
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import tkinter as tk

# Função para selecionar pasta de origem
def selecionar_entrada_pasta():
    pasta_entrada_selecionada = filedialog.askdirectory()
    entrada_pasta.set(pasta_entrada_selecionada)

# Função para selecionar pasta de saída
def selecionar_pasta_saida():
    pasta_saida_selecionada = filedialog.askdirectory()
    saida_pasta.set(pasta_saida_selecionada)

# Função para Adicionar Cada Linha de Cada Arquivo na DataTable Pra Depois Exportar Como Um Só Arquivo





# Função para consolidar arquivos
def consolidar_arquivos():
    entrada = entrada_pasta.get()
    saida = saida_pasta.get()
    tipo_arquivo = tipo_de_arquivo.get()
    nome_arquivo_consolidado = nome_arquivo_consolidado_var.get()

   
    all_files = []
    for root, dirs, files in os.walk(entrada):

        for file in files:
            if file.endswith(tipo_arquivo):
                all_files.append(os.path.join(root, file))
    # Validação para verificar se há arquivos do tipo especificado
    if not all_files:
        if tipo_arquivo == '.xlsx':
            messagebox.showinfo(f"ERRO !", "Não foram encontrados arquivos com a extensão (xlsx) na pasta de origem.")
        else:
            messagebox.showinfo(f"ERRO !", "Não foram encontrados arquivos com a extensão (csv) na pasta de origem.")
        root.exit(1)  # Interrompe a execução do programa

    #return all_files        

    df_list = []
    for file in all_files:
        if tipo_arquivo == '.xlsx':
            df = pd.read_excel(file)
        else:
            df = pd.read_csv(file)
        df_list.append(df)

    final_df = pd.concat(df_list, ignore_index=True)
    
    if tipo_arquivo == '.xlsx':
        final_df.to_excel(os.path.join(saida, nome_arquivo_consolidado + '.xlsx'), index=False)
    else:
        final_df.to_csv(os.path.join(saida, nome_arquivo_consolidado + '.csv'), index=False)

    messagebox.showinfo("Sucesso", "Consolidação completa!")

# Configurações da janela principal
ctk.set_appearance_mode("dark")  # Modo escuro
#ctk.set_default_color_theme("green")  # Tema verde
ctk.set_default_color_theme("green") #Definir tema com Json



root = ctk.CTk()
root.title("Consolidador de Arquivos")
root.geometry("700x370")

# Definindo o ícone para a barra de tarefas e janela
icon_window = "image.ico"
icon_path = "image.ico"
icon_image = ImageTk.PhotoImage(Image.open(icon_path))
# Carrega a imagem com CTkImage


root.iconbitmap(icon_window)  # Para Windows
root.iconphoto(True, icon_image)

# Variáveis
entrada_pasta = ctk.StringVar()
saida_pasta = ctk.StringVar()
tipo_de_arquivo = ctk.StringVar(value=".csv")
file_type_output = ctk.StringVar(value=".xlsx")
nome_arquivo_consolidado_var = ctk.StringVar()

# Frame principal
main_frame = ctk.CTkFrame(root)
main_frame.pack(fill='both', expand=True, padx=20, pady=20)

# Layout
ctk.CTkLabel(main_frame, text="Pasta de Origem:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
ctk.CTkEntry(main_frame, textvariable=entrada_pasta, width=300).grid(row=0, column=1, columnspan=7, padx=10, pady=10, sticky='ew')
ctk.CTkButton(main_frame, text="Selecionar", command=selecionar_entrada_pasta).grid(row=0, column=8, padx=10, pady=10, sticky='ew')

ctk.CTkLabel(main_frame, text="Pasta de Saída:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
ctk.CTkEntry(main_frame, textvariable=saida_pasta, width=300).grid(row=1, column=1, columnspan=7, padx=10, pady=10, sticky='ew')
ctk.CTkButton(main_frame, text="Selecionar", command=selecionar_pasta_saida).grid(row=1, column=8, padx=10, pady=10, sticky='ew')

#ctk.CTkLabel(main_frame, text="Tipo de Arquivo de Saída:").grid(row=3, column=0, padx=10, pady=10, sticky='w')
#ctk.CTkOptionMenu(main_frame, variable=file_type_output, values=[".xlsx", ".csv"]).grid(row=3, column=1, padx=10, pady=10, sticky='ew')

ctk.CTkLabel(main_frame, text="Nome do Arquivo Final:").grid(row=4, column=0, padx=10, pady=10, sticky='w')
ctk.CTkEntry(main_frame, textvariable=nome_arquivo_consolidado_var, width=300).grid(row=4, column=1, columnspan=7, padx=10, pady=10, sticky='ew')

#ctk.CTkLabel(main_frame, text="Tipo de Arquivo de Entrada:").grid(row=4, column=5, padx=10, pady=10, sticky='w')
ctk.CTkOptionMenu(main_frame, variable=tipo_de_arquivo, values=[".xlsx", ".csv"]).grid(row=4, column=8, padx=10, pady=10, sticky='ew')

ctk.CTkButton(main_frame, text="Consolidar Arquivos", command=consolidar_arquivos).grid(row=5, column=0, columnspan=10, padx=10, pady=20, sticky='ew')

# Carrega a imagem com CTkImage
image = ctk.CTkImage(light_image=Image.open(icon_path),
                     dark_image=Image.open(icon_path), size=(64, 64))
# Cria um CTkLabel e adiciona a imagem a ele
image_label = ctk.CTkLabel(main_frame, text="", image=image).grid(row=10, column=0, padx=10, pady=10, sticky='ew')

#Assinatura
ctk.CTkLabel(main_frame, text="Desenvolvido por: Renan Fiuja", text_color="#00FF00").grid(row=10, column=1, padx=15, pady=15, sticky='ew')

# Tornar as colunas responsivas
main_frame.grid_columnconfigure(1, weight=0)
main_frame.grid_columnconfigure(2, weight=1)
main_frame.grid_columnconfigure(3, weight=1)
main_frame.grid_columnconfigure(4, weight=1)
main_frame.grid_columnconfigure(5, weight=1)
main_frame.grid_columnconfigure(6, weight=1)
main_frame.grid_columnconfigure(7, weight=1)

# Iniciar a interface
root.mainloop()
