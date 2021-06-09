import re

#######################################################################################
#-------------------------------------------------------------------------------------      
    ####################################################
    #    -----------------> VALIDACIÓN <------------------
    #   Este archivo lo creamos para volcar en el las distintas expresiones regulares 
    #   aqui traemos los datos de "nombre, apellido, dni" con los que luego 
    #   cruzamos con el patro, para identificar si coincide con el patrón o no.
    #   con la consulta que mas abajo ejecuta de Sqlite3 para obtener los datos 
    ##########################################################################

class Validacion:
    def __init__(self,):
        print ("Valida Celda")

    def regex_nombre(self, nombre, apellido, dni):
        #Patron de Validacion Nombre Y Apellido
        v1 = "[a-zA-Z ]+"

        #Convertimos al dni en STR
        str_dni = str (dni)
        #Damos Patron a la validacion de numeros 
        v_num ="[0-9]{8}"
        print ("--------------PRUEBA")
        print (str_dni)

        ####---Utilizamos re.search para validar el campo, y traerlo como Boleano
        validacion_nombre = bool (re.search (v1, nombre))
        validacion_apellido = bool (re.search (v1, apellido))
        validacion_dni = bool(re.search (v_num, str_dni))
        print (validacion_dni)
        #Luego Aplicamos la logica para retornar TRUE o False
        if validacion_nombre is False or validacion_apellido is False:
            print("Algo paso con el Nombre, o el Apellido")
        else:
            if validacion_dni is False:
                print ("Error en el DNI")

            else:
                return True
       