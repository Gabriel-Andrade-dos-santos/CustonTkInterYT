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

#Aula 05 = Frames
Frame1 = ctk.CTkFrame(master=janela, width=200,height=330, fg_color="Blue",
                      bg_color="transparent",border_width=10, corner_radius=30,
                      border_color="Red").place(x=10,y=60)#fg_color = cor do fundo; bg_color = cor do contorno; border_color = cor da borda
Frame2 = ctk.CTkFrame(master=janela, width=200, height=330, fg_color="Blue",
                      bg_color="Black").place(x=230,y=60)#border_width = tamanho da borda; corner_radius = raio das bordas
Frame3 = ctk.CTkFrame(master=janela, width=200,height=330, fg_color="Blue",
                      bg_color="Black").place(x=450,y=60)

janela.mainloop()

