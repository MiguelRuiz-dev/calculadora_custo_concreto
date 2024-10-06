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
        self.root.configure(background='#4682B4')
        self.root.geometry('600x600')
        self.root.resizable(False, False)

    def parte_tela(self):
        # Parte 1 - Frame principal
        self.parte_1 = Frame(self.root, bd=4, bg='#00FFFF',
                             highlightthickness=1, highlightbackground='#000000')
        self.parte_1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.8)

        # Parte 2 - Frame inferior (onde ficam os botões e o total)
        self.parte_2 = Frame(self.root, bd=4, bg='#00FFFF',
                             highlightthickness=1, highlightbackground='#000000')
        self.parte_2.place(relx=0.01, rely=0.85, relwidth=0.98, relheight=0.14)

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
            messagebox.showerror("Erro", "Por favor, insira números válidos.")

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

        self.aviso_virgula = Label(self.parte_1, text = ' ⚠️ AVISO IMPORTANTE:   USE . (ponto) NO LUGAR DA , (vírgula) EM CASAS DECIMAIS!',
                                   bg= '#00FFFF', fg = '#FF0000' )
        self.aviso_virgula.place(relx=0.0001, rely=0.7, relwidth=0.8, relheight=0.2)

        self.quantidade = Label(self.parte_1, text='KG/M³:', bg='#00FFFF')
        self.quantidade.place(relx=0.075, rely=0.001, relwidth=0.3, relheight=0.03)

        self.preco_coluna = Label(self.parte_1, text='Preço KG/M³:', bg='#00FFFF')
        self.preco_coluna.place(relx=0.4, rely=0.00001, relwidth=0.3, relheight=0.03)

        # Labels de materiais
        self.cimento = Label(self.parte_1, text='Cimento:', bg='#00FFFF')
        self.cimento.place(relx=0.01, rely=0.050, relwidth=0.1, relheight=0.03)

        self.areia = Label(self.parte_1, text='Areia:', bg='#00FFFF')
        self.areia.place(relx=0.01, rely=0.1, relwidth=0.1, relheight=0.08)

        self.po = Label(self.parte_1, text='Pó:', bg='#00FFFF')
        self.po.place(relx=0.01, rely=0.22, relwidth=0.1, relheight=0.03)

        self.brita0 = Label(self.parte_1, text='Brita 0:', bg='#00FFFF')
        self.brita0.place(relx=0.01, rely=0.3, relwidth=0.1, relheight=0.08)

        self.brita1 = Label(self.parte_1, text='Brita 1:', bg='#00FFFF')
        self.brita1.place(relx=0.01, rely=0.4, relwidth=0.1, relheight=0.08)

        self.aditivo1 = Label(self.parte_1, text='Aditivo 1:', bg='#00FFFF')
        self.aditivo1.place(relx=0.01, rely=0.5, relwidth=0.14, relheight=0.08)

        self.aditivo2 = Label(self.parte_1, text='Aditivo 2:', bg='#00FFFF')
        self.aditivo2.place(relx=0.01, rely=0.6, relwidth=0.14, relheight=0.08)

    def entrada_tela(self):
        # Entradas para os campos de preço de cada item (KG/M³)
        self.preco_cimento = Entry(self.parte_1)
        self.preco_cimento.place(relx=0.48, rely=0.045, relwidth=0.15, relheight=0.04)

        self.preco_areia = Entry(self.parte_1)
        self.preco_areia.place(relx=0.48, rely=0.12, relwidth=0.15, relheight=0.04)

        self.preco_po = Entry(self.parte_1)
        self.preco_po.place(relx=0.48, rely=0.215, relwidth=0.15, relheight=0.04)

        self.preco_brita0 = Entry(self.parte_1)
        self.preco_brita0.place(relx=0.48, rely=0.315, relwidth=0.15, relheight=0.04)

        self.preco_brita1 = Entry(self.parte_1)
        self.preco_brita1.place(relx=0.48, rely=0.415, relwidth=0.15, relheight=0.04)

        self.preco_aditivo1 = Entry(self.parte_1)
        self.preco_aditivo1.place(relx=0.48, rely=0.52, relwidth=0.15, relheight=0.04)

        self.preco_aditivo2 = Entry(self.parte_1)
        self.preco_aditivo2.place(relx=0.48, rely=0.62, relwidth=0.15, relheight=0.04)

        # Entradas para as quantidades de cada item (KG/M³)
        self.quantidade_cimento = Entry(self.parte_1)
        self.quantidade_cimento.place(relx=0.17, rely=0.045, relwidth=0.15, relheight=0.04)

        self.quantidade_areia = Entry(self.parte_1)
        self.quantidade_areia.place(relx=0.17, rely=0.12, relwidth=0.15, relheight=0.04)

        self.quantidade_po = Entry(self.parte_1)
        self.quantidade_po.place(relx=0.17, rely=0.215, relwidth=0.15, relheight=0.04)

        self.quantidade_brita0 = Entry(self.parte_1)
        self.quantidade_brita0.place(relx=0.17, rely=0.315, relwidth=0.15, relheight=0.04)

        self.quantidade_brita1 = Entry(self.parte_1)
        self.quantidade_brita1.place(relx=0.17, rely=0.415, relwidth=0.15, relheight=0.04)

        self.quantidade_aditivo1 = Entry(self.parte_1)
        self.quantidade_aditivo1.place(relx=0.17, rely=0.52, relwidth=0.15, relheight=0.04)

        self.quantidade_aditivo2 = Entry(self.parte_1)
        self.quantidade_aditivo2.place(relx=0.17, rely=0.62, relwidth=0.15, relheight=0.04)

    def resultados_tela(self):
        # Label para mostrar o total calculado
        self.resultado_total = Label(self.parte_2, text='Total: R$0.00', bg='#00FFFF')
        self.resultado_total.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=0.8)



Aplicativo()
