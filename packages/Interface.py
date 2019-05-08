from tkinter import Label, Entry, Button, StringVar, OptionMenu, Frame, Tk
from PIL import ImageTk, Image
from tkinter import messagebox

class Interface:

    def inicio(self, master):
        master.title("BATMAN NEED'S FIND JOKER")

        frame = Frame(master, bg="#070B19")
        frame.pack()

        self.label0 = Label(frame, text="Ajude o Batman a encontrar o Coringa informando as configurações.\n\n" + 
            "O mapa de Gotham no projeto esta situado em uma matriz 5x5, conforme imagem abaixo.\n\n" +
                "Insira uma posição para o Batman e uma para o Coringa, com valores entre 1 e 25",
                fg= "white",
                bg = "#070B19"
                )
        self.label0.pack()

        #ABRE O ARQUIVO PARA MOSTRAR O MAPA NA TELA
        path = "Images/map.png"
        img = Image.open(path)
        img = img.resize((500, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(frame, image=img, bg="black")
        panel.photo = img
        panel.pack()

        #CONTEUDOS DO FRAME
        self.lbCoringa = Label(frame, text = "\nInforme a posição do Coringa (1 a 25):", bg = "#070B19", fg="white")
        self.lbCoringa.pack()

        self.txtCoringa = Entry(frame)
        self.txtCoringa.pack()

        self.lbBatman = Label(frame, text = "\nInforme a posição do Batman (1 a 25):", bg = "#070B19", fg="white")
        self.lbBatman.pack()

        self.txtBatman = Entry(frame)
        self.txtBatman.pack()        

        self.label1 = Label(frame, text="\nInforme o algorítmo que deseja utilizar para ajudar o Batman.", bg = "#070B19", fg="white")
        self.label1.pack()

        ALGORITMOS = [
                    "Amplitude",
                    "Profundidade",
                    "Profundidade Limitada",
                    "Aprofundamento Interativo",
                    "Bidirecional",
                    "Custo uniforme",
                    "Greedy",
                    "A*"
                    ] #etc
        self.variable = StringVar(frame)
        self.variable.set(ALGORITMOS[0])

        self.w = OptionMenu(frame, self.variable, *ALGORITMOS)
        self.w.pack()

        self.btContinuar = Button(frame, text="Continuar", command=self.continuar, bg="#084B8A")
        self.btContinuar.pack(padx=30, pady=30)


    def quit(self):
        root.destroy()

    #CLICK DO EVENTO DO BOTÃO, SALVANDO OS VALORES NOS ARQUIVOS E DANDO CONTINUIDADE A APLICAÇÃO DO ALGORITMO
    def continuar(self): 
        algoritmo = self.variable.get()
        posicaoBatman = self.txtBatman.get()
        posicaoCoringa = self.txtCoringa.get()
        
        if int(posicaoBatman) < 0 or int(posicaoBatman) > 25 or int(posicaoCoringa) < 0 or int(posicaoCoringa) > 25:
            messagebox.showinfo("Atenção", "Por favor, informe as posições de maneira correta!")
        else:
            arqBatman = open("Files/batman.txt", "w+")
            arqBatman.write(posicaoBatman)
            arqBatman.close()

            arqCoringa = open("Files/coringa.txt", "w+")
            arqCoringa.write(posicaoCoringa)
            arqCoringa.close()

            arqAlgoritmo = open("Files/algoritmo.txt", "w+")
            arqAlgoritmo.write(str(algoritmo))
            arqAlgoritmo.close

            root.destroy()

root = Tk()

#PERSONALIZA O FRAME PARA SER EXIBIDO NO CENTRO DA TELA
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

positionRight = int(root.winfo_screenwidth()/3 - windowWidth/3)
positionDown = int(root.winfo_screenheight()/10 - windowHeight/10)

root.geometry("+{}+{}".format(positionRight, positionDown))

app = Interface() 
app.inicio(root)
root.mainloop()
