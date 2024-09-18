
class Preços:
    preços =  {}
    def __init__(self):
        self.preco_base = 0

    def calcular_preco(self, valor):
        return valor * 1.2  # Exemplo de cálculo de preço com markup
