from Navegable import navegable
from Volador import volador

class Hidroavion(navegable, volador):
    def navegar(self):
        return "El hidroavión está navegando."

    def volar(self):
        return "El hidroavión está volando."