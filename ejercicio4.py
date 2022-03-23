import os #limpia pantalla
class Persona():
    def __init__(self): #Es una funcion que se inicializa cuando se estancia la clase
        self.__perso = {} #Es un objeto
        self.__listaPersonas = [] #Es un arreglo

    def agregarPersona(self, cedula,nombre,apellidos, direccion,telefono):
        self.__perso = { #Aquí recibo los datos, los pongo en el mismo orden en que los envío
            'cedula': cedula,
            'nombres': nombre,
            'apellidos': apellidos,
            'direccion': direccion,
            'telefono': telefono,
        }
        self.__listaPersonas.append(self.__perso)

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.__devengado = {}
        self.__deducciones = {}
        self.__listaEmpleados = []

    def agregarEmpleado(self):
        cedula = input("Digite la cédula: ")
        nombre = input("Digite su nombre: ")
        apellidos = input("Digite sus apellidos: ")
        direccion = input("Digite su dirección: ")
        telefono = input("Digite su teléfono: ")
        salario = float(input("Digite su salario: "))

        per = { 
            'cedula': cedula,
            'nombres': nombre,
            'apellidos': apellidos,
            'direccion': direccion,
            'telefono': telefono,
        }
        self.__devengado = {
            'salario': salario,
            'alimentacion': 0,
            'transporte': 0,
        }

        self.__deducciones ={
            'salud': 0,
            'pension':0
        }
            
        super().agregarPersona(cedula,nombre,apellidos,direccion,telefono)#aquí mando los datos 
        self.__listaEmpleados.append([{"persona":per}, {"devengado": self.__devengado},{"deducciones": self.__deducciones}])

    def calcularDevengado(self):
        if self.__devengado ['salario'] < 2000000:
            self.__devengado ['alimentacion']= 80000
            self.__devengado ['transporte']= 60000


    def calcularDeducciones(self):
        self.__deducciones['salud'] = self.__devengado['salario']*4/100
        self.__deducciones['pension'] = self.__devengado['salario']*3,375/100
    

    def menu (self, opciones):
        while(True):
            os.system("clear")
            for item in range (len(opciones)):
                print (opciones[item])

            opcion = input("Digite una opcion correcta: ")

            if opcion == "1":
                os.system("clear")
                self.agregarEmpleado()
                self.calcularDevengado()
                self.calcularDeducciones()

            elif opcion == "2":
                os.system("clear")
                print (self.__listaEmpleados)
                input("Digite enter para continuar")

            elif opcion == "4":
                break
            

def menuPrincipal():
    os.system("clear")
    opciones = ( #menu en forma de tupla
        "MENU PRINCIPAL",
        "1. Adicionar Empleado",
        "2. Mostrar Empleado",
        "3. Eliminar Empleado",
        "4. Salir"
    )
    emp = Empleado ()
    emp.menu(opciones)

def main():
    menuPrincipal()






if __name__ == "__main__":
    main()