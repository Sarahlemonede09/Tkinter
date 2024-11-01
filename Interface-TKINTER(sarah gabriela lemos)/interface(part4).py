import tkinter as tk


def open_window():
    window2 =  tk.Toplevel()
    window2.title('New Window')
    botao_close = tk.Button(window2, text=' Close', command = window2.destroy)
    botao_close.grid(row=1, column=0)


window = tk.Tk()
botao = tk.Button(window, text=' Go to for other window', command= open_window)
botao.grid(row=2, column=3)

window.mainloop()