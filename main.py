import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random
from PIL import Image, ImageTk

df = pd.read_excel("perguntas.xlsx")
perguntas = df.sample(n=10).values.tolist()  # Vai pegar as perguntas aleatórias

# -----------------------------------------------------------------------------
# VARIAVEIS GLOBAIS
pontos = 0
pergunta_atual = 0
pergunta_resp_correta = -1  # Inicialmente, a resposta correta é -1

# -----------------------------------------------------------------------------
# FUNÇÃO VERIFICA A RESPOSTA


def verifica_resposta(resposta):
    global pontos, pergunta_atual
    if resposta == pergunta_resp_correta:
        pontos += 1

    pergunta_atual += 1

    if pergunta_atual < len(perguntas):
        perguntas_na_tela()
    else:
        mostrar_resultado()

# --------------------------------------------------------------------------------
# EXIBINDO A PRÓXIMA PERGUNTA


def perguntas_na_tela():
    global pergunta_resp_correta
    pergunta, opcao1, opcao2, opcao3, opcao4, resposta = perguntas[pergunta_atual]
    perguntas_label.config(text=pergunta)
    opcao_1_btn.config(
        text=opcao1, state=tk.NORMAL, command=lambda: verifica_resposta(1))
    opcao_2_btn.config(
        text=opcao2, state=tk.NORMAL, command=lambda: verifica_resposta(2))
    opcao_3_btn.config(
        text=opcao3, state=tk.NORMAL, command=lambda: verifica_resposta(3))
    opcao_4_btn.config(
        text=opcao4, state=tk.NORMAL, command=lambda: verifica_resposta(4))
    pergunta_resp_correta = resposta  # Atualiza a resposta correta

# --------------------------------------------------------------------------------
# EXIBIR O RESULTADO FINAL

# Declare a variável global para armazenar a imagem
imagem = None
def mostrar_resultado():
    global imagem
    #janela personalizada
    janela2 = tk.Toplevel()
    janela2.title("QUIZ FINALIZADO")
    janela2.geometry("300x120")
    largura_janela = 400
    altura_janela = 400
    largura_tela = janela2.winfo_screenwidth()
    altura_tela = janela2.winfo_screenheight()
    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2
    janela2.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
    janela2.config(bg="#32CD32")
    lbl_mensagem = tk.Label(janela2, text=f"Parabéns! Você terminou o quiz!\nSua pontuação foi {pontos} / de {len(perguntas)}", font="Arial 16 bold", fg="black",bg="#32CD32")
    # Carregue a imagem
    imagem = PhotoImage(file="D:\\PYTHON\\Jogo_1\\fim.png")
    # Crie um Label para exibir a imagem
    imagem_label = tk.Label(janela2, image=imagem, bg="#32CD32")
    imagem_label.pack()

    lbl_mensagem.pack()




    # messagebox.showinfo(
    #     "Quiz finalizado", f"Parabéns! Você terminou o quiz!\nSua pontuação foi {pontos}/ de {len(perguntas)}")
    opcao_1_btn.config(state=tk.DISABLED)
    opcao_2_btn.config(state=tk.DISABLED)
    opcao_3_btn.config(state=tk.DISABLED)
    opcao_4_btn.config(state=tk.DISABLED)
    jogar_de_novo_btn.pack()

# ABRINDO O BOTÃO JOGAR NOVAMENTE


def jogar_de_novo():
    global pontos, pergunta_atual, pergunta_resp_correta
    pontos = 0
    pergunta_atual = 0
    random.shuffle(perguntas)
    pergunta_resp_correta = -1  # Reseta a resposta correta
    opcao_1_btn.config(state=tk.NORMAL)
    opcao_2_btn.config(state=tk.NORMAL)
    opcao_3_btn.config(state=tk.NORMAL)
    opcao_4_btn.config(state=tk.NORMAL)
    jogar_de_novo_btn.pack_forget()

# -----------------------------------------------------------------------------
janela = tk.Tk()
janela.title("Quiz")
janela.geometry("400x500")
janela.option_add("Font", "Arial")
# ----------------------------------------------------------------
# ICONE NA TELA
app_icone = PhotoImage(file="quiz2.png")
app_label_icone = tk.Label(janela, image=app_icone)
app_label_icone.pack(pady=10)
# -------------------------------------------------------------------
# APRESENTANDO AS PERGUNTAS
# wraplength dimensiona o tamanho do texto no quadro
perguntas_label = tk.Label(
    janela, text="", wraplength=380, fg="#000000", font=("Arial", 12, "bold"))
perguntas_label.pack(pady=20)
# -------------------------------------------------------------------
pergunta_resp_correta = tk.IntVar()  # busca pergunta correta
# ----------------------------------------------------------------
# botões na tela
opcao_1_btn = tk.Button(janela, text="", width=30,
                        bg="#008080", fg="#DCDCDC",
                        state=tk.DISABLED, font=("Arial", 12, "bold"))
opcao_1_btn.pack(pady=10)

opcao_2_btn = tk.Button(janela, text="", width=30,
                        bg="#008080", fg="#DCDCDC",
                        state=tk.DISABLED, font=("Arial", 12, "bold"))
opcao_2_btn.pack(pady=5)

opcao_3_btn = tk.Button(janela, text="", width=30,
                        bg="#008080", fg="#DCDCDC",
                        state=tk.DISABLED, font=("Arial", 12, "bold"))
opcao_3_btn.pack(pady=10)

opcao_4_btn = tk.Button(janela, text="", width=30,
                        bg="#008080", fg="#DCDCDC",
                        state=tk.DISABLED, font=("Arial", 12, "bold"))
opcao_4_btn.pack(pady=10)

jogar_de_novo_btn = tk.Button(janela, text="Jogar Novamente", width=30,
                              bg="#008080", fg="#DCDCDC",
                              font=("Arial", 12, "bold"), command=jogar_de_novo)

# -----------------------------------------------------------------------

perguntas_na_tela()
janela.mainloop()
