import sqlite3
from tkinter import Message
from regex import Validacion

#Torres Martinez Joaquin
#dni:35376119
#mail:joa.tm@hotmail.com
#########################################################
# Creamos una App que funciona de modelo, donde realiza todas las acciones y transacciones entre 
# la imagen de la aplicacion, y las transacciones con la Base de datos
# En este caso, el Abmc, contiene las siguientes funciones:
#    -conexion con la base de Datos ("def.conexion"), (linea --->37-41)
#    -la actualizacion del treeview ("def.actualizar_treeview") (linea --->45-77),
#    -Alta de registro ("def.alta")(linea --->77-110), 
#    -Baja de registro ("def.baja")(linea --->110-137),
#    -modificacion de registro ("def.modificacion")(linea --->137-173),
#    -consulta ("def.consulta")(linea --->173-204), 
#    -mostrar datos en Formulario ("def.actu_formu")(linea --->204-245),
#    -borrar datos del fomulario ("def.borrar_formu") (linea --->254-268)
# 
##########################################################

class A_b_m_c:
    def __init__(self,):
        ##############################################
        # DEFINO INIT CREANDO BASE DE DATOS, O EN SU DEFECTO INDICANTO ERROR DE CONEXION
        #################################################
        try:
            con=sqlite3.connect ("base_prospectos.db")
            cursor_prosp = con.cursor ()
            cursor_prosp.execute ("CREATE TABLE  Prospectos (id integer PRIMARY KEY, nombre text, apellido text, dni integer, medio_contacto text, provincia text, localidad text, telefono integer, celular integer, productos text, ahorro boolean, edad integer, fuma boolean, observacion text)"
            )
            con.commit() 
        except:
            print ("error conexion/ Base ya Creada")
        
        
    ###################################################
    ### ejecuta la conexion con la base de datos
    ###################################################
    def conexion(
        self,
    ):
        con = sqlite3.connect("base_prospectos.db")
        return con
#######################################################################################
#-------------------------------------------------------------------------------------      
    ####################################################
    #    -----------------> ACTUALIZAR TREEVIEW <------------------
    #   Definimos la funcion que se encarga de actualizar el treeview
    #   el mismo captura los datos con recors, del objeto de treeview que se encuentra
    #   en el archivo vista_prosp.py como "self.tree" para luego borrarlos, y actualizarlos
    #   con la consulta que mas abajo ejecuta de Sqlite3 para obtener los datos 
    #   y almacenarlos en "resultado".
    #   la variable resultado finalmente la pasamos por un Bucle for, para obtener 
    #   cada registro que procesa y lo envía "self.tree de vista_prosp", con
    #   "mod_arbol.insert (....)".
    ##########################################################################
    def actualizar_treeview(self, mod_arbol):
        # limpieza de tabla
        records = mod_arbol.get_children()
        for element in records:
            mod_arbol.delete(element)
        # Consiguiendo datos
        sql = "SELECT * FROM Prospectos ORDER BY id ASC"

        con = self.conexion()
        cursorObj = con.cursor()
        datos = cursorObj.execute(sql)
        con.commit()

        resultado = datos.fetchall()
        #print (resultado)
        for fila in resultado:
            #print(fila)
                     
            mod_arbol.insert("",0,text=fila[0],
                 values=( 
                    fila[1], 
                    fila[2], 
                    fila[3], 
                    fila [4], 
                    fila [5], 
                    fila [6], 
                    fila [7], 
                    fila [8], 
                    fila [9], 
                    fila [10], 
                    fila [11], 
                    fila [12], 
                    fila [13])
                    )
    

        

######################################################################################
 #-------------------------------------------------------------------------------------
 ##################################################################################
 #  #   ----------------->ALTA DE REGISTO:<----------------------
 #  #   Para el Alta de registro, ingresamos dentro de la funcion los parametros que sacamos de 
 #  #   la ejecucion de una funcion lambda en la Hoja de vista_prosp.py,
 #  #   sacamos de esta manera los valores de las entry para hacerlo pasar por la app
 #  #   que creamos en "regex.py", que tiene una funcion "regex_nombre"
 #  #   quien se encarga de revisar que el patron sea el que corresponda a texto para el nombre.
 #  #   si valida que se de esa condicion, lo que hace luego es la extraccion de los datos de
 #  #   las entrys de "vista_prosp.py" y crea el registro que luego dara de Alta con la ejecucion
 #  #   de los comandos de conexion y posterior desconexion de sqlite3.
 #  #   en este caso le agrege una funcion para que borre todo el formulario, así de esta manera
 #  #   resulta mas facil volver a cargar un nuevo formulario.
###################################################################################################
    def alta(self, nombre, apellido, dni, medio, provincia, localidad, telefono, celular, producto, ahorro, edad, fuma, observacion, mod_arbol):
        print("alta")
        vali = Validacion()
        validacion = vali.regex_nombre(nombre.get (), apellido.get(),dni.get())

        if validacion is None:
            print ("Usted ingreso mal Algún Campo")  
        else:
            print ("Los Datos Son Correctos")
            #datos = (nombre, apellido, dni, medio, provincia, localidad, telefono, celular, producto, ahorro, edad, fuma, observacion)
            reg_alta = (nombre.get(), apellido.get(), dni.get(), medio.get(), provincia.get(), localidad.get(), telefono.get(), celular.get(), producto.get(), ahorro.get(), edad.get(), fuma.get(), observacion.get()) 
            con = self.conexion()
            sql = "INSERT INTO Prospectos( nombre , apellido, dni, medio_contacto, provincia, localidad, telefono, celular, productos, ahorro, edad, fuma, observacion) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) "
            cur = con.cursor()
            cur.execute(sql, reg_alta)
            con.commit()               
            self.borrar_formu(nombre, 
                apellido, 
                dni, 
                medio, 
                provincia, 
                localidad, 
                telefono, 
                celular, 
                producto, 
                ahorro, 
                edad, 
                fuma, 
                observacion, 
                mod_arbol)
            
######################################################################################
#-------------------------------------------------------------------------------------
 ##################################################################################
 #  #   ----------------->BAJA DE REGISTO:<--------------------------------
 #  #   para la baja del registro, por medio de una funcion lambda sacamos los datos 
 #  #   del "Self.tree" (treeview) de "vista_prosp.py", para luego obtener el id del Objeto.
 #  #   este id lo vamos a almacenar en una variable, para luego pasarla por 
 #  #   las funciones de Sqlite3 dentro del script correspondiente de "DELETE"
 #  #   donde luego le ponemos como dimension a tener en cuenta como id,
 #  #   la variable que anteriormente habiamos obtenido del Treeview.
 #  #   Ejecutamos la conexion / desconexion, y luego le agregamos una conexion a la 
 #  #    Actualizacion del Treeview (funcion anteriormente creada. Lineas (55-75))
 #  ####################################################################################
    
    def baja (self,  mod_arbol):
        #print ("baja")
        tree_select = mod_arbol.focus()
        reg_baja = mod_arbol.item (tree_select)["text"]
        print(reg_baja)
        
        con = self.conexion()
        sql = "DELETE FROM Prospectos WHERE id = ? "
        cur = con.cursor()
        cur.execute(sql, (reg_baja,))
        con.commit()
        
        self.actualizar_treeview(mod_arbol)
######################################################################################
#-------------------------------------------------------------------------------------
##################################################################################
#  #   ----------------->MODIFICACION DE REGISTO:<--------------------------------  
#  #    Para la modificacion como el caso del alta, extraemos los datos de las entrys
#  #    con los que luego vamos a almacenar cada uno en una variable distinta, ya que
#  #    cuando queremos pasar los parametros a sqlite, lo hacemos por cada variable.
#  #    tambien sacamos el id de la seleccion del treeview, para indicarle a sqlite3
#  #    el "WHERE id = x", y de esta manera no borrar un dato erroneo.
#  #    este script, se conectaría con la base de datos, y realizaría el UPDATE, con los 
#  #    Parametros que le pasamos.
#  #    A esto se le agrega la ejecucion de la actualizacion del treeview, y la de borrar formurlario.
#  ######################################################################################### 
    def modificacion (self,
        nombre, 
        apellido, 
        dni, 
        medio, 
        provincia, 
        localidad, 
        telefono, 
        celular, 
        producto,
        ahorro, 
        edad, 
        fuma, 
        observacion, 
        mod_arbol
        ):

        tree_select = mod_arbol.focus()
        num_id = mod_arbol.item (tree_select)["text"]
        v1 = nombre.get()
        v2 = apellido.get()
        v3 = dni.get()
        v4 = medio.get()
        v5 = provincia.get()
        v6 = localidad.get()
        v7 = telefono.get()
        v8 = celular.get()
        v9 = producto.get()
        v10 = ahorro.get()
        v11 = edad.get()
        v12 = fuma.get()
        v13 = observacion.get()                    
        con = self.conexion()
        sql = "UPDATE Prospectos SET nombre = ? , apellido = ? , dni = ? , medio_contacto = ? , provincia = ? , localidad = ? , telefono = ? , celular = ? , productos = ? , ahorro = ? , edad = ? , fuma = ? , observacion = ? WHERE id = ? "
        cur = con.cursor()
        cur.execute(sql, (v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, num_id))
        con.commit()
        self.actualizar_treeview(mod_arbol)
        self.borrar_formu(nombre, 
                apellido, 
                dni, 
                medio, 
                provincia, 
                localidad, 
                telefono, 
                celular, 
                producto, 
                ahorro, 
                edad, 
                fuma, 
                observacion, 
                mod_arbol)
######################################################################################
#-------------------------------------------------------------------------------------
##################################################################################
#  #   ----------------->CONSULTA DE REGISTO:<-------------------------------- 
#  #    En la ejecucion de esta funcion, tenemos como entrada el "Self.tree", 
#  #    como siempre, la utilizaremos para actualizar el tree.
#  #    Luego tenemos el dni, que lo sacamos de"vista_prosp.py", 
#  #    la cual sacamos con una funcion lambda, y el cual usaremos para validar
#  #    y Ejecutar la busqueda de los archivos con las funciones de Sqlite3
#  #    cuando se ejecuta la conexion y busqueda en la base de datos, los resultados se almacenan 
#  #    en una variable que luego levantaremo con un bucle For, y luego los insertaremos
#  #    Nuevamente en el "self.tree" que sería "mod_arbol"
   ######################################################################################### 
    def consulta(self, dni, mod_arbol):
        reg_buscar = dni.get()
        records = mod_arbol.get_children()

        for element in records:
            mod_arbol.delete(element)

        con = self.conexion()
        sql = " SELECT * FROM Prospectos WHERE dni = ?"
        cur = con.cursor()
        datos = cur.execute(sql, (reg_buscar,))
        con.commit()
        resultado = datos.fetchall()
        #print (resultado)
        for fila in resultado:
            #print(fila)
                     
            mod_arbol.insert("",0,text=fila[0], 
                    values=( fila[1], 
                        fila[2], 
                        fila[3], 
                        fila [4], 
                        fila [5], 
                        fila [6], 
                        fila [7], 
                        fila [8], 
                        fila [9], 
                        fila [10], 
                        fila [11], 
                        fila [12], 
                        fila [13]))
######################################################################################
#-------------------------------------------------------------------------------------
##################################################################################
#   #   ----------------->ACTUALIZA FORMULARIO:<--------------------------------
#   # esta funcion lo que hace es llevar la informacion del treeview, al formulario,
#   # de esta manera se puede modificar de una manera mas sencilla el formulario
#   # utilizado antes de modificar un registro, sería el correcto Uso. (me gustaría mejorarlo pero hasta aca pude llegar)
#   # #############################################################################      
    def actu_form(self, nombre, apellido, dni, medio, provincia, localidad, telefono, celular, producto, ahorro, edad, fuma, observacion, mod_arbol):
        #----->Obtengo los datos del treeview y los almaceno en distintas variables
        option = mod_arbol.focus()
        nombre_tree = mod_arbol.item (option)["values"][0]
        apellido_tree = mod_arbol.item(option)["values"][1]
        dni_tree = mod_arbol.item(option)["values"][2]
        medio_tree = mod_arbol.item(option)["values"][3]
        prov_tree = mod_arbol.item (option)["values"][4]
        local_tree = mod_arbol.item(option)["values"][5]
        tel_tree = mod_arbol.item (option) ["values"][6]
        cel_tree = mod_arbol.item ( option) ["values"][7]
        produ_tree = mod_arbol.item (option) ["values"][8]
        ahorro_tree = mod_arbol.item (option) ["values"][9]
        edad_tree = mod_arbol.item (option) ["values"][10]
        fuma_tree = mod_arbol.item (option)["values"][11]
        obs_tree = mod_arbol.item (option)["values"][12]
        ##########
        #Luego seteo las variables que me traje de "vista_prosp.py" con las variables del TREEVIEW
        ##########
        print (nombre_tree +" "+ apellido_tree)
        nombre.set (nombre_tree)
        apellido.set(apellido_tree)
        dni.set(dni_tree)
        medio.set(medio_tree)
        provincia.set (prov_tree)
        localidad.set (local_tree)
        telefono.set (tel_tree)
        celular.set (cel_tree)
        producto.set (produ_tree)
        ahorro.set (ahorro_tree)
        edad.set (edad_tree)
        fuma.set(fuma_tree)
        observacion.set(obs_tree)
##################################################################################
# #-------------------------------------------------------------------------------------
##################################################################################
#   #   ----------------->BORRAR FORMULARIO:<--------------------------------  
#   # Esta Funcion, lo que hace es con los datos de "Vista_prosp.py" que estan 
#   # en las variables de nombre,apellido, etc. Es setearlas en vacíos, o en algunos
#   # casos a valores por defecto, para que luego de modificar un formulario, o de haber
#   # visto un formulario, si no era la intencion modificarlo se pueda eliminar.
#   # y volver de esta manera a empezar de cero.
#   ##############################################################################
    def borrar_formu (self, nombre, apellido, dni, medio, provincia, localidad, telefono, celular, producto, ahorro, edad, fuma, observacion, mod_arbol):
        nombre.set ("")
        apellido.set("")
        dni.set("0")
        medio.set("Telefono")
        provincia.set ("")
        localidad.set ("")
        telefono.set ("011")
        celular.set ("011")
        producto.set ("Vida")
        ahorro.set ("0")
        edad.set ("0")
        fuma.set("0")
        observacion.set("")
        self.actualizar_treeview(mod_arbol)
    
