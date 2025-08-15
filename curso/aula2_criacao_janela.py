import customtkinter as ctk #importando biblioteca

janela = ctk.CTk() #Criar a janela

#Configura o tipo (título) da janela
janela.title("Curso CustonTkInter")

#Conferindo a janela principal
janela.geometry("700x400") #Configura a dimenção da janela
janela.maxsize(width=1920, height=1080)#Configura o limete maximo de tamanho da janela
janela.minsize(width=700, height=400)#Configura o limete mínimo de tamanho da janela
#janela.resizable(width=True,height=True)#Delimita o tamanho da janela
#janela.iconify()#Fecha a janela automaticamente
#janela.deiconify()#Reabre a janela automaticamente

janela.mainloop()