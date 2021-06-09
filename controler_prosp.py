from tkinter import Tk
from vista_prosp import Ventana_Formulario

class Controller:
    """
    Está es la clase principal
    """

    def __init__(self, root):
        self.root_controler = root
        self.visionActivada()

    def visionActivada(
        self,
    ):
        """
        Esta clase activa la vista
        """
        Ventana_Formulario(self.root_controler)
        

if __name__ == "__main__":
    root_tk = Tk()
    application = Ventana_Formulario(root_tk)
    root_tk.mainloop()
