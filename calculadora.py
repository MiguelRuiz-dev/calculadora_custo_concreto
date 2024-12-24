from tkinter import *
from tkinter import messagebox

root = Tk()


class Aplicativo():
    def __init__(self):
        self.root = root
        self.tela()
        self.parte_tela()
        self.botoes_tela()
        self.mostrar_aviso()
        self.itens_tela()
        self.entrada_tela()
        self.resultados_tela()
        root.mainloop()

    def tela(self):
        self.root.title('Calculadora Custo Concreto')
        self.root.configure(background='#DCDCDC')
        self.root.geometry('1000x600')
        self.root.resizable(False, False)

    def parte_tela(self):
        # Parte 1 - Frame principal
        self.parte_1 = Frame(self.root, bd=4, bg='white')

        self.parte_1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.7)

        # Parte 2 - Frame inferior (onde ficam os botões e o total)
        self.parte_2 = Frame(self.root, bd=4, bg='white')

        self.parte_2.place(relx=0.01, rely=0.72, relwidth=0.98, relheight=0.14)

    def mostrar_aviso(self):
        # Exibindo o aviso de boas-vindas
        messagebox.showinfo("Seja Bem-Vindo!", "Direitos Reservados: Miguel Ruiz")

    def botoes_tela(self):
        # Botão para "Calcular"
        self.bt_calcular = Button(self.parte_2, text='Calcular', command=self.calcular)
        self.bt_calcular.place(relx=0.009, rely=0.27, relwidth=0.15, relheight=0.4)

        # Botão para "Apagar Tudo"
        self.bt_apagar = Button(self.parte_2, text='Apagar Tudo', command=self.limpar_campos)
        self.bt_apagar.place(relx=0.18, rely=0.27, relwidth=0.15, relheight=0.4)

        # Botão para "Buscar"
        self.bt_buscar = Button(self.parte_1, text='Buscar', command=self.limpar_campos)
        self.bt_buscar.place(relx=0.9, rely=0.01, relwidth=0.05, relheight=0.06)


    def calcular(self):
        # Lógica de cálculo para o total
        try:
            # Pegando os valores dos preços
            preco_cimento = float(self.preco_cimento.get())
            preco_areia = float(self.preco_areia.get())
            preco_po = float(self.preco_po.get())
            preco_brita0 = float(self.preco_brita0.get())
            preco_brita1 = float(self.preco_brita1.get())
            preco_aditivo1 = float(self.preco_aditivo1.get())
            preco_aditivo2 = float(self.preco_aditivo2.get())

            # Pegando as quantidades (em KG/M³)
            quantidade_cimento = float(self.quantidade_cimento.get())
            quantidade_areia = float(self.quantidade_areia.get())
            quantidade_po = float(self.quantidade_po.get())
            quantidade_brita0 = float(self.quantidade_brita0.get())
            quantidade_brita1 = float(self.quantidade_brita1.get())
            quantidade_aditivo1 = float(self.quantidade_aditivo1.get())
            quantidade_aditivo2 = float(self.quantidade_aditivo2.get())

            # Calculando o custo total
            custo_total = (
                    preco_cimento * quantidade_cimento +
                    preco_areia * quantidade_areia +
                    preco_po * quantidade_po +
                    preco_brita0 * quantidade_brita0 +
                    preco_brita1 * quantidade_brita1 +
                    preco_aditivo1 * quantidade_aditivo1 +
                    preco_aditivo2 * quantidade_aditivo2
            )

            # Exibindo o total na tela
            self.resultado_total.config(text=f'Total: R${custo_total:.2f}')
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira informações válidas.")

    def limpar_campos(self):
        # Limpa todos os campos de entrada e o resultado
        self.preco_cimento.delete(0, END)
        self.preco_areia.delete(0, END)
        self.preco_po.delete(0, END)
        self.preco_brita0.delete(0, END)
        self.preco_brita1.delete(0, END)
        self.preco_aditivo1.delete(0, END)
        self.preco_aditivo2.delete(0, END)

        self.quantidade_cimento.delete(0, END)
        self.quantidade_areia.delete(0, END)
        self.quantidade_po.delete(0, END)
        self.quantidade_brita0.delete(0, END)
        self.quantidade_brita1.delete(0, END)
        self.quantidade_aditivo1.delete(0, END)
        self.quantidade_aditivo2.delete(0, END)

        # Resetando o resultado
        self.resultado_total.config(text='Total: R$0.00')

    def itens_tela(self):
        # Labels para os itens

        self.aviso_virgula = Label(self.parte_1, text = '⚠️ AVISO IMPORTANTE: USE PONTO NO LUGAR DA VÍRGULA EM CASAS DECIMAIS!',
                                   bg= 'white', fg = '#000000' )
        self.aviso_virgula.place(relx=0.01, rely=0.8, relwidth=0.5, relheight=0.2)

        self.quantidade = Label(self.parte_1, text='KG/M³:', bg='white')
        self.quantidade.place(relx=0.025, rely=0.001, relwidth=0.2, relheight=0.03)

        self.preco_coluna = Label(self.parte_1, text='Preço em KG/M³:', bg='white')
        self.preco_coluna.place(relx=0.14, rely=0.00001, relwidth=0.2, relheight=0.03)

        # Labels de materiais
        self.cimento = Label(self.parte_1, text='Cimento:', bg='white')
        self.cimento.place(relx=0.01, rely=0.050, relwidth=0.1, relheight=0.03)

        self.areia = Label(self.parte_1, text='Areia:', bg='white')
        self.areia.place(relx=0.01, rely=0.1, relwidth=0.1, relheight=0.08)

        self.po = Label(self.parte_1, text='Pó:', bg='white')
        self.po.place(relx=0.01, rely=0.22, relwidth=0.1, relheight=0.03)

        self.brita0 = Label(self.parte_1, text='Brita 0:', bg='white')
        self.brita0.place(relx=0.01, rely=0.3, relwidth=0.1, relheight=0.08)

        self.brita1 = Label(self.parte_1, text='Brita 1:', bg='white')
        self.brita1.place(relx=0.01, rely=0.4, relwidth=0.1, relheight=0.08)

        self.aditivo1 = Label(self.parte_1, text='Aditivo 1:', bg='white')
        self.aditivo1.place(relx=0.01, rely=0.5, relwidth=0.1, relheight=0.08)

        self.aditivo2 = Label(self.parte_1, text='Aditivo 2:', bg='white')
        self.aditivo2.place(relx=0.01, rely=0.6, relwidth=0.1, relheight=0.08)

    def entrada_tela(self):
        # Entradas para os campos de preço de cada item (KG/M³)
        self.preco_cimento = Entry(self.parte_1, bg='#D6DEE2')
        self.preco_cimento.place(relx=0.21, rely=0.045, relwidth=0.05, relheight=0.04)

        self.preco_areia = Entry(self.parte_1, bg='#D6DEE2')
        self.preco_areia.place(relx=0.21, rely=0.12, relwidth=0.05, relheight=0.04)

        self.preco_po = Entry(self.parte_1, bg='#D6DEE2')
        self.preco_po.place(relx=0.21, rely=0.215, relwidth=0.05, relheight=0.04)

        self.preco_brita0 = Entry(self.parte_1, bg='#D6DEE2')
        self.preco_brita0.place(relx=0.21, rely=0.315, relwidth=0.05, relheight=0.04)

        self.preco_brita1 = Entry(self.parte_1, bg='#D6DEE2')
        self.preco_brita1.place(relx=0.21, rely=0.415, relwidth=0.05, relheight=0.04)

        self.preco_aditivo1 = Entry(self.parte_1, bg='#D6DEE2')
        self.preco_aditivo1.place(relx=0.21, rely=0.52, relwidth=0.05, relheight=0.04)

        self.preco_aditivo2 = Entry(self.parte_1, bg='#D6DEE2')
        self.preco_aditivo2.place(relx=0.21, rely=0.62, relwidth=0.05, relheight=0.04)

        # Entradas para as quantidades de cada item (KG/M³)
        self.quantidade_cimento = Entry(self.parte_1, bg='#D6DEE2')
        self.quantidade_cimento.place(relx=0.10, rely=0.045, relwidth=0.05, relheight=0.04)

        self.quantidade_areia = Entry(self.parte_1, bg='#D6DEE2')
        self.quantidade_areia.place(relx=0.10, rely=0.12, relwidth=0.05, relheight=0.04)

        self.quantidade_po = Entry(self.parte_1, bg='#D6DEE2')
        self.quantidade_po.place(relx=0.10, rely=0.215, relwidth=0.05, relheight=0.04)

        self.quantidade_brita0 = Entry(self.parte_1, bg='#D6DEE2')
        self.quantidade_brita0.place(relx=0.10, rely=0.315, relwidth=0.05, relheight=0.04)

        self.quantidade_brita1 = Entry(self.parte_1, bg='#D6DEE2')
        self.quantidade_brita1.place(relx=0.10, rely=0.415, relwidth=0.05, relheight=0.04)

        self.quantidade_aditivo1 = Entry(self.parte_1, bg='#D6DEE2')
        self.quantidade_aditivo1.place(relx=0.10, rely=0.52, relwidth=0.05, relheight=0.04)

        self.quantidade_aditivo2 = Entry(self.parte_1, bg='#D6DEE2')
        self.quantidade_aditivo2.place(relx=0.10, rely=0.62, relwidth=0.05, relheight=0.04)

        #Outras Entradas:

        self.nometraço = Entry(self.parte_1, bg='#D6DEE2')
        self.nometraço.place(relx=0.59, rely=0.012, relwidth=0.30, relheight=0.06)


    def resultados_tela(self):
        # Label para mostrar o total calculado
        self.resultado_total = Label(self.parte_2, text='Total: R$0.00', bg='white')
        self.resultado_total.place(relx=0.34, rely=0.27, relwidth=0.1, relheight=0.4)



Aplicativo()
