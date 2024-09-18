from modelos.valor import Valor

class Camisas:
    camisetas = []

    def __init__(self, nome, tamanho, cor):
        self._nome = nome.upper()
        self._tamanho = tamanho
        self._cor = cor.title()
        self._disponivel = True
        self._valor = []
        Camisas.camisetas.append(self)

    def __str__(self):
        return f'{self._nome} | {self._tamanho} | {self._cor} | {self._disponivel}'

    @classmethod
    def listar_camisetas(cls):
        print('''
░█████╗░░█████╗░███╗░░░███╗██╗░██████╗░█████╗░░██████╗
██╔══██╗██╔══██╗████╗░████║██║██╔════╝██╔══██╗██╔════╝
██║░░╚═╝███████║██╔████╔██║██║╚█████╗░███████║╚█████╗░
██║░░██╗██╔══██║██║╚██╔╝██║██║░╚═══██╗██╔══██║░╚═══██╗
╚█████╔╝██║░░██║██║░╚═╝░██║██║██████╔╝██║░░██║██████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚════╝░╚═╝░░╚═╝╚═════╝░''')
        
        print(f'{"Nome da Camisa".ljust(25)} | {"Tamanho".ljust(10)} | {"Cor".ljust(10)} | {"Disponível".ljust(15)} | {"Média Preço".ljust(10)}')
        print('─'*80)
        for camiseta in cls.camisetas:
            print(f'{camiseta._nome.ljust(25)} | {camiseta._tamanho.ljust(10)} | {camiseta._cor.ljust(10)} | {camiseta.disponivel.ljust(15)} | R${camiseta.media_preço:.2f}')
            print('─'*80)

    @property
    def disponivel(self):
        return '✅ Disponível' if self._disponivel else '❌ Indisponível'

    def alterar_estado(self):
        self._disponivel = not self._disponivel        

    def receber_preço(self, loja, preço):
        preço = Valor(loja, preço)
        self._valor.append(preço)

    @property
    def media_preço(self):
        if not self._valor:
            return 0 
        somas_dos_preços = sum(valor._preço for valor in self._valor)
        quantidade_lojas = len(self._valor)
        media = round(somas_dos_preços / quantidade_lojas, 1)
        return media
