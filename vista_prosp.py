from tkinter import StringVar
from tkinter import IntVar
from tkinter import BooleanVar
from tkinter import Frame
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import Radiobutton
from tkinter import Tk
from tkinter import ttk
from model_prosp import A_b_m_c


#Torres Martinez Joaquin
#dni:35376119
#mail:joa.tm@hotmail.com
#########################################################
#App de Vista de la aplicacion.
#Indice  hola:
#       Variables: ----->(Line 28-47)
#       Frame: ----->(Line 49-56)
#       Etiquetas: ----->(Line 57-92)
#
#           -posicion_Etiquetas:  ----->(Line 74-92)
#
#       Entradas: ----->(Line 93-135)
#           -posicion_Entrys:  ----->(Line 120-135)
#
#       Treeview: ----->(Line 43-183)
#           -posicion y Columnas:  ----->(Line 146-163)
#           -Cabeceras Treeview:  ----->(Line 168-183)
#       Botones: ----->(Line 186-208)
#       Funciones: ------>(Line 215-300)
#           -ALTA:  ----->(Line 217-234)
#           -BAJA:  ----->(Line 237-241)
#           -MODIFICACION:  ----->(Line 242-258)
#           -CONSULTA:  ----->(Line 259-264)
#           -ACTU FORM:  ----->(Line 265-283)
#           -BORRAR FORM:  ----->(Line 283-300) 
##########################################################


class Ventana_Formulario:
    def __init__(self, ventana_prosp):
        #############################################
        ######-------->Objeto/Variables      <-------
        #############################################
        self.vraiz = ventana_prosp
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.dni = IntVar()
        self.medio_contacto = StringVar()
        self.provincia = StringVar()
        self.localidad = StringVar()
        self.telefono = IntVar()
        self.celular = IntVar()
        self.producto = StringVar()
        self.ahorro = BooleanVar()
        self.edad = IntVar()
        self.fuma = BooleanVar()
        self.observacion = StringVar()
        self.fr_pros = Frame (self.vraiz)
        self.tree = ttk.Treeview (self.fr_pros)
        self.objeto_base = A_b_m_c()
        self.objeto_base.actualizar_treeview(self.tree)   
##################################################################### 
###############--------FRAME/MARCO<-----------//////<------------
#####################################################################
        self.vraiz.title ("Ingreso de Prospectos")
        self.fr_pros.config (width= 2020, height = 2020)
        self.fr_pros.grid (row = 20, column = 0, columnspan = 8)
        #########################################################
        ######--------> Etiquetas      <---------
        #########################################################
        self.titulo = Label (self.vraiz, text = "Ingrese sus datos", bg= "green", fg ="white", width = 40)
        self.eti_nombre = Label(self.vraiz, text = "Nombre")
        self.eti_apellido = Label(self.vraiz, text = "Apellido")
        self.eti_dni = Label (self.vraiz, text = "DNI (busqueda)")
        self.eti_medio = Label (self.vraiz, text = "Medio Fisico")
        self.eti_provin = Label (self.vraiz, text = "Provincia")
        self.eti_locali = Label (self.vraiz, text = "Localidad")
        self.eti_telefono = Label (self.vraiz, text = "Telefono")
        self.eti_celu = Label (self.vraiz, text = "Celular")
        self.eti_product = Label (self.vraiz, text = "Producto de Interes")
        self.eti_ahorro = Label (self.vraiz, text = "Ahorro?")
        self.eti_edad = Label (self.vraiz, text = "Edad")
        self.eti_fuma = Label (self.vraiz, text = "Fuma?")
        self.eti_observ = Label (self.vraiz, text = "Observacion")
        ################################################################
        ###--->Posicion Etiquetas<----
        ################################################################
        self.titulo.grid (row=0, column =0, columnspan=14, pady=1, sticky = "w"+"e")
        self.eti_nombre.grid (row=1, column =0, sticky = "w")
        self.eti_apellido.grid (row=2, column =0, sticky = "w")
        self.eti_dni.grid (row=3, column =0, sticky = "w")
        self.eti_medio.grid (row=4, column =0, sticky = "w")
        self.eti_provin.grid (row=5, column =0, sticky = "w")
        self.eti_locali.grid (row=6, column =0, sticky = "w")
        self.eti_telefono.grid (row=7, column =0, sticky = "w")
        self.eti_celu.grid (row=7, column =3, sticky = "w")
        self.eti_product.grid (row=2, column = 3, sticky = "w")
        self.eti_ahorro.grid (row=3, column =3, sticky = "w")
        self.eti_edad.grid (row=4, column =3, sticky = "w")
        self.eti_fuma.grid (row=5, column =3, sticky = "w")
        self.eti_observ.grid (row=6, column =3, sticky = "w")
        ####################################################
        ######--------> Entradas      <---------
        ####################################################
        self.ent_nomb = Entry(self.vraiz, width=25, textvariable=self.nombre)
        self.ent_apell = Entry(self.vraiz, width=25, textvariable=self.apellido)
        self.ent_dni = Entry(self.vraiz, width=25, textvariable=self.dni)
        #_________________________________________________________
        # selector especial para Medios de contacto
        #---------------------------------------------------------
        self.tab_medios = ["Telefono", "Mail", "WhatsApp", "Otro"]
        self.medio_contacto.set(self.tab_medios[0])
        self.ent_medio = ttk.OptionMenu(self.vraiz, self.medio_contacto, *self.tab_medios)
        #-----------------------------------------------------------
        self.ent_prov = Entry(self.vraiz, width=25, textvariable=self.provincia)
        self.ent_local = Entry(self.vraiz, width=25, textvariable=self.localidad)
        self.ent_tel = Entry(self.vraiz, width=25, textvariable=self.telefono)
        self.ent_cel = Entry(self.vraiz, width=25, textvariable=self.celular)
        #_____________________________________________________________
        # selector especial para Productos
        #-------------------------------------------------------------
        self.tab_productos = ["Vida", "Accidentes", "Tecnología", "Mascotas", "Bolso", "Cajero", "Hogar"]
        self.producto.set(self.tab_productos[0])
        self.ent_produ = ttk.OptionMenu(self.vraiz, self.producto, *self.tab_productos)
        self.ent_ahor = ttk.Checkbutton(self.vraiz, variable=self.ahorro, onvalue=True, offvalue=False)
        self.ent_edad = Entry(self.vraiz, width=25, textvariable=self.edad)
        self.ent_fuma = ttk.Checkbutton(self.vraiz, variable=self.fuma, onvalue=True, offvalue=False)
        self.ent_observ = Entry(self.vraiz, width=25, textvariable=self.observacion)
        #########################################################
        ###--->Posicion Entradas<----
        #########################################################
        self.ent_nomb.grid(column=2, row=1)
        self.ent_apell.grid(column=2, row=2)
        self.ent_dni.grid(column=2, row=3)
        self.ent_medio.grid(column=2, row=4)
        self.ent_prov.grid(column=2, row=5)
        self.ent_local.grid(column=2, row=6)
        self.ent_tel.grid(column=2, row=7)
        self.ent_cel.grid(column=4, row=7)
        self.ent_produ.grid(column=4, row=2)
        self.ent_ahor.grid(column=4, row=3)
        self.ent_edad.grid(column=4, row=4)
        self.ent_fuma.grid(column=4, row=5)
        self.ent_observ.grid(column=4, row=6)
        ######################################################################################
        #######################------->Etiqueta Separadora<-----------########################
        ######################################################################################
        self.titulo_medio = Label (self.vraiz, text = "Datos", bg= "darkblue", fg ="white", width = 40)
        self.titulo_medio.grid (row=9, column =0, columnspan=14, pady=1, sticky = "w"+"e")
        ######################################################################################
        #############------------>____TREVIEW_____<--------------################
        #posicion, y columnas
        #   posicion, y columnas: ------>(Lineas 146-163)
        #########
        self.tree.grid(row=10, column=0)
        self.tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10", "col11", "col12","col13" )
        self.tree.column("#0", width=50,  anchor="e")
        self.tree.column("col1", width=50)
        self.tree.column("col2", width=50)
        self.tree.column("col3", width=50)
        self.tree.column("col4", width=50)
        self.tree.column("col5", width=50)
        self.tree.column("col6", width=50)
        self.tree.column("col7", width=50)
        self.tree.column("col8", width=50)
        self.tree.column("col9", width=50)
        self.tree.column("col10", width=50)
        self.tree.column("col11", width=50)
        self.tree.column("col12", width=50)
        self.tree.column("col13", width=50)
        #------->Cabeceras de Treview<-------
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Nombre")
        self.tree.heading("col2", text="Apellido")
        self.tree.heading("col3", text="dni")
        self.tree.heading("col4", text="Medio Ingr")
        self.tree.heading("col5", text="Provincia")
        self.tree.heading("col6", text="Localidad")
        self.tree.heading("col7", text="Telefono")
        self.tree.heading("col8", text="Celular")
        self.tree.heading("col9", text="Producto")
        self.tree.heading("col10", text="Ahorro")
        self.tree.heading("col11", text="Edad")
        self.tree.heading("col12", text="Fuma")
        self.tree.heading("col13", text="Observacion")
################################################################################
#-------------------------------------------------------------------------------      
#   ############################################################################
#   #----------------->   BOTONES      <-----------------------------------
#   #
        self.boton_alta = Button(self.vraiz, text="Alta", comman=lambda: self.alta())
        self.boton_alta.grid(row=2, column=5)

        self.boton_alta = Button(self.vraiz, text="Baja", comman=lambda: self.baja())
        self.boton_alta.grid(row=2, column=6)

        self.boton_alta = Button(self.vraiz, text="Modificacion", comman=lambda: self.modificacion())
        self.boton_alta.grid(row=4, column=5)

        self.boton_alta = Button(self.vraiz, text="Buscar", comman=lambda: self.consulta())
        self.boton_alta.grid(row=4, column=6)
        
        self.boton_alta = Button(self.vraiz, text="Ver Formu", comman=lambda: self.actu_form())
        self.boton_alta.grid(row=6, column=6)
        
        self.boton_alta = Button(self.vraiz, text="Borrar Form", comman=lambda: self.borra_formu())
        self.boton_alta.grid(row=8, column=6)
################################################################################
#-------------------------------------------------------------------------------      
#   ############################################################################
#   #----------------->   FUNCIONES Para LAMBDA      <-----------------------------------      
# ##############################################################################
#   #----------------->   FUNCIONES ALTA      <-----------------------------------       
    def alta(self,):
        print ("Alta")
        self.objeto_base.alta(
            self.nombre, 
            self.apellido, 
            self.dni,
            self.medio_contacto, 
            self.provincia,
            self.localidad, 
            self.telefono, 
            self.celular, 
            self.producto, 
            self.ahorro, 
            self.edad, 
            self.fuma,
            self.observacion, 
            self.tree)

# ##############################################################################
#   #----------------->   FUNCIONES BAJA      <-----------------------------------                       
    def baja(self,):
        print ("Baja")
        self.objeto_base.baja(self.tree)
# ##############################################################################
#   #----------------->   FUNCIONES MODIFICACION      <-----------------------------------           
    def modificacion(self,):
        print ("modificacion")
        self.objeto_base.modificacion(self.nombre, 
            self.apellido, 
            self.dni,
            self.medio_contacto, 
            self.provincia, 
            self.localidad, 
            self.telefono, 
            self.celular, 
            self.producto, 
            self.ahorro, 
            self.edad, 
            self.fuma, 
            self.observacion, 
            self.tree)       
# ##############################################################################
#   #----------------->   FUNCIONES CONSULTA      <-----------------------------         
    def consulta(self,):
        print ("modificacion")
        self.objeto_base.consulta(self.dni, self.tree)

# ##############################################################################
#   #----------------->   ACTUALIZACION DE FORMULARIO      <-------------------    
    def actu_form(self,):
        print ("actu formu")
        self.objeto_base.actu_form(self.nombre, 
            self.apellido,
            self.dni,
            self.medio_contacto, 
            self.provincia, 
            self.localidad, 
            self.telefono, 
            self.celular, 
            self.producto, 
            self.ahorro, 
            self.edad, 
            self.fuma,
            self.observacion, 
            self.tree)
# ##############################################################################
#   #----------------->    BORRADO DE FORMULARIO     <-------------------    
    def borra_formu(self,):
        print ("actu formu")
        self.objeto_base.borrar_formu (self.nombre, 
            self.apellido, 
            self.dni,
            self.medio_contacto, 
            self.provincia, 
            self.localidad, 
            self.telefono, 
            self.celular, 
            self.producto, 
            self.ahorro, 
            self.edad, 
            self.fuma,
            self.observacion, 
            self.tree)
          


