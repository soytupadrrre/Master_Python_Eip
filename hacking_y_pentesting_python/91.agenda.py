import sys

class Direccion:

    def __init__(self) -> None:
        self.__calle:str = 'undef'
        self.__piso:int = 0
        self.__ciudad:str = 'undef'
        self.__codigoPostal:int = 0

    def getCalle(self) -> str:
        return self.__calle

    def getPiso(self) -> int:
        return self.__piso

    def getCiudad(self) -> str:
        return self.__ciudad

    def getCodigoPostal(self) -> int:
        return self.__codigoPostal

    def setCalle(self, calle:str):
        self.__calle = calle

    def setPiso(self, piso:int):
        self.__piso = piso

    def setCiudad(self, ciudad:str):
        self.__ciudad = ciudad

    def setCodigoPostal(self, codigoPostal:int):
        self.__codigoPostal = codigoPostal

class Persona:

    def __init__(self) -> None:
        self.__nombre:str = 'undef'
        self.__apellidos:str = 'undef'
        self.__fechaNacimiento:str = 'undef'

    def getNombre(self) -> str:
        return self.__nombre

    def getApellidos(self) -> str:
        return self.__apellidos

    def getFechaNacimiento(self) -> str:
        return self.__fechaNacimiento

    def setNombre(self, nombre:str):
        self.__nombre = nombre

    def setApellidos(self, apellidos:str):
        self.__apellidos = apellidos

    def setFechaNacimiento(self, fechaNacimiento:str):
        self.__fechaNacimiento = fechaNacimiento

class Telefono:

    def __init__(self, fijo:int, movil:int, trabajo:int) -> None:
        self.__fijo:int = fijo
        self.__movil:int = movil
        self.__trabajo:int = trabajo

    def getTelefonoFijo(self) -> int:
        return self.__fijo

    def getTelefonoMovil(self) -> int:
        return self.__movil

    def getTelefonoTrabajo(self) -> int:
        return self.__trabajo

    def setTelefonoFijo(self, fijo:int):
        self.__fijo = fijo

    def setTelefonoMovil(self, movil:int):
        self.__movil = movil

    def setTelefonoTrabajo(self, trabajo:int):
        self.__trabajo = trabajo

class Contacto(Persona, Direccion, Telefono):

    def __init__(self) -> None:
        self.__email:str = 'undef'

    def __str__(self) -> str:
        return self.mostrarContacto()
    
    def getEmail(self) -> str:
        return self.__email

    def setEmail(self, email:str):
        self.__email = email

    def mostrarContacto(self) -> str:
        tmp = ''
        tmp += f"Persona\n"
        tmp += f"\tNombre: {self.getNombre()}\n"
        tmp += f"\tApellidos: {self.getApellidos()}\n"
        tmp += f"\tFecha de Nacimiento: {str(self.getFechaNacimiento())}\n"
        tmp += f"\nTeléfono:\n"
        tmp += f"\tFijo: {str(self.getTelefonoFijo())}\n"
        tmp += f"\tMóvil: {str(self.getTelefonoMovil())}\n"
        tmp += f"\tTrabajo: {str(self.getTelefonoTrabajo())}\n"
        tmp += f"\nDirección\n"
        tmp += f"\tCalle: {self.getCalle()}\n"
        tmp += f"\tPiso: {str(self.getPiso())}\n"
        tmp += f"\tCiudad: {self.getCiudad()}\n"
        tmp += f"\tCódigo Postal: {str(self.getCodigoPostal())}\n"
        
        return tmp

class Agenda:

    def __init__(self, path:str) -> None:
        self.__listaContactos:list[Contacto] = []
        self.__path:str = path

    def cargarContactos(self):
        with open(self.__path, "r") as f:
            for linea in f:
                lista = linea.split(",")
                contacto = Contacto()
                contacto.setNombre(lista[0])
                contacto.setApellidos(lista[1])
                contacto.setFechaNacimiento(lista[2])
                contacto.setTelefonoFijo(int(lista[3]))
                contacto.setTelefonoMovil(int(lista[4]))
                contacto.setTelefonoTrabajo(int(lista[5]))
                contacto.setCalle(lista[6])
                contacto.setPiso(int(lista[7]))
                contacto.setCodigoPostal(lista[8])
                contacto.setCiudad(lista[9])
                contacto.setEmail(lista[10])
                self.__listaContactos.append(contacto)

    def crearNuevoContacto(self, contacto:Contacto):
        self.__listaContactos.append(contacto)

    def guardarContactos(self):
        with open(self.__path, "w") as f:
            for contacto in self.__listaContactos:
                f.write(str(contacto.getNombre())+",")
                f.write(str(contacto.getApellidos())+",")
                f.write(str(contacto.getFechaNacimiento())+",")
                f.write(str(contacto.getTelefonoFijo())+",")
                f.write(str(contacto.getTelefonoMovil())+",")
                f.write(str(contacto.getTelefonoTrabajo())+",")
                f.write(str(contacto.getCalle())+",")
                f.write(str(contacto.getPiso())+",")
                f.write(str(contacto.getCodigoPostal())+",")
                f.write(str(contacto.getCiudad())+",")
                f.write(str(contacto.getEmail())+",\n")
        f.close()

    def mostrarAgenda(self):
        print(self.__listaContactos)

    def buscarContactoPorNombre(self, nombre:str) -> Contacto:
        for item in self.__listaContactos:
            if item.getNombre() == nombre:
                return item.mostrarContacto()

    def buscarContactoPorTelefono(self, telefono:int) -> Contacto:
        for item in self.__listaContactos:
            if item.getTelefonoFijo() == telefono:
                return item.mostrarContacto()

            elif item.getTelefonoMovil() == telefono:
                return item.mostrarContacto()

            elif item.getTelefonoTrabajo() == telefono:
                return item.mostrarContacto()

    def borrarContactoPorNombre(self, nombre:str):
        try:
            for obj in self.__listaContactos:
                if obj.getNombre() == nombre:
                    self.__listaContactos.remove(obj)
                    print("Contacto eliminado correctamente")

        except:
            print(f"{nombre} no existe, no se puede eliminar")

    def borrarContactoPorTelefono(self, telefono:int):
        try:
            for obj in self.__listaContactos:
                if obj.getTelefonoFijo() == telefono:
                    self.__listaContactos.remove(obj)
                    print("Contacto eliminado correctamente")

                elif obj.getTelefonoMovil() == telefono:
                    self.__listaContactos.remove(obj)
                    print("Contacto eliminado correctamente")

                elif obj.getTelefonoTrabajo() == telefono:
                    self.__listaContactos.remove(obj)
                    print("Contacto eliminado correctamente")
        except:
            print(f"{telefono} no existe, no se puede eliminar")


def obtenerOpcion(choice:str, path:str):
    if choice == "1":
        buscarContacto(path)
    elif choice == "2":
        crearContacto(path)
    elif choice == "3":
        borrarContacto(path)
    elif choice == "0":
        sys.exit(2)
    else:
        main()

def mostrarMenu():
    print("=======================")
    print("    AGENDA - PYTHON    ")
    print("-----------------------")
    print("Bienvenido a su agenda\n")
    print("1. Buscar Contacto")
    print("2. Crear Contacto")
    print("3. Borrar Contacto")
    print("0. Salir")
    print("=======================\n")
    
def buscarContacto(path:str):
    busqueda = input("¿Qué contacto desea búscar? (nombre o telefono)\n")
    agenda = Agenda(path)
    agenda.cargarContactos()
    try:
        busqueda:int = int(busqueda)
    except:
        busqueda:str = str(busqueda)
    
    if isinstance(busqueda, int):
        print(agenda.buscarContactoPorTelefono(busqueda))
    else:
        print(agenda.buscarContactoPorNombre(busqueda))
    
    main()

def crearContacto(path:str):
    contacto:Contacto = Contacto()
    agenda:Agenda = Agenda(path)
    agenda.cargarContactos()

    contacto.setNombre(input("Indique el nombre\n"))
    contacto.setApellidos(input("\nIndique los apellidos\n"))
    contacto.setFechaNacimiento(input("\nIndique la fecha de nacimiento\n"))
    contacto.setCiudad(input("\nIndique la ciudad\n"))
    contacto.setCodigoPostal(input("\nIndique el codigo postal\n"))
    contacto.setCalle(input("\nIndique la calle\n"))
    contacto.setPiso(input("\nIndique el piso\n"))
    contacto.setTelefonoMovil(int(input("\nIndique el telefono móvil\n")))
    contacto.setTelefonoFijo(int(input("\nIndique el telefono fijo\n")))
    contacto.setTelefonoTrabajo(int(input("\nIndique el telefono de trabajo\n")))
    contacto.setEmail(input("\nIndique el correo electrónico\n"))

    agenda.crearNuevoContacto(contacto)
    agenda.guardarContactos()

    print("Contacto guardado correctamente")

    main()

def borrarContacto(path:str):
    busqueda:int or str = input("¿Qué contacto desea eliminar? (nombre o telefono)\n")
    agenda:Agenda = Agenda(path)
    agenda.cargarContactos()

    try:
        busqueda:int = int(busqueda)
    except:
        busqueda:str = str(busqueda)

    if isinstance(busqueda, int):
        agenda.borrarContactoPorTelefono(busqueda)
    else:
        agenda.borrarContactoPorNombre(busqueda)

    agenda.guardarContactos()

    main()

def main(path:str="./agenda.txt"):
    mostrarMenu()
    obtenerOpcion(input(), path)

if __name__ == "__main__":
    main()