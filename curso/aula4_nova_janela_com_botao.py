import customtkinter as ctk #importando biblioteca

janela = ctk.CTk() #Criar a janela

#Configura o tipo (título) da janela = Aula 02
janela.title("Curso CustonTkInter")

#Conferindo a janela principal
janela.geometry("700x400") #Configura a dimenção da janela
janela.maxsize(width=1920, height=1080)#Configura o limete maximo de tamanho da janela
janela.minsize(width=700, height=400)#Configura o limete mínimo de tamanho da janela
janela.resizable(width=True,height=True)#Delimita o tamanho da janela
#janela.iconify()#Fecha a janela automaticamente
#janela.deiconify()#Reabre a janela automaticamente

"""
Customizando o tema da aplicação = Aula 03
"""
janela._set_appearance_mode("Dark")#Define a aparencia da janela(COR)

#Criando nova janela = Aula 04
def nova_tela():
    #nova_janela._set_appearance_mode("Dark")
    nova_janela = ctk.CTkToplevel(janela, fg_color="Black")#Nesse tipo usa - se fg_color para trocar o background
    nova_janela.geometry("500x250")
    

btn_novaTela = ctk.CTkButton(master=janela, text="Abrir nova janela", command=nova_tela).place(x=300,y=100)#MASTER = Onde fica o botão; TEXT = Oque está escrito no botão; place(x=,y=) Onde ficará localizado o botão; command= chama o comando que o botão irá realizar

janela.mainloop()

