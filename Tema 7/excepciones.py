class ValueErrorRepeated(ValueError):
    """Señala que se ha encontrado un elemento repetido en la lista de valores
    Atributos:
        elem - elemento que se repite
        message - texto informativo para el usuario final"""
    

    def __init__(self, elem, message= "Error: Imposible añadir elementos duplicados =>"):
        self.elem = elem
        self.message = message + elem
        super().__init__(self.message)

def add_one (my_list, my_elem):
    if (my_elem in my_list):
        raise ValueErrorRepeated (my_elem, 'Este elemento está repetido')
    my_list.append(my_elem)
            


