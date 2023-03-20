class OldDateException(Exception):
    def __init__(self):
        super().__init__(self, 'La fecha es posterior a la actual')


class FullClassInThisSport(Exception):
    def __init__(self):
        super().__init__(self, 'No hay mas hueco en el deporte y el día seleccionado')