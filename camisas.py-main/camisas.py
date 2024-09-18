

class Camisas:
    camisetas = []

    def __init__(self, nome, tamanho, cor, preco):
        self.nome = nome
        self.tamanho = tamanho
        self.cor = cor
        self.preco = preco
        self._disponivel = True
        Camisas.camisetas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.tamanho} | {self.cor} | R${self.preco:.2f} | {self.disponivel}'


    def listar_camisetas():
        print('')        
        print('''
░█████╗░░█████╗░███╗░░░███╗██╗░██████╗░█████╗░░██████╗
██╔══██╗██╔══██╗████╗░████║██║██╔════╝██╔══██╗██╔════╝
██║░░╚═╝███████║██╔████╔██║██║╚█████╗░███████║╚█████╗░
██║░░██╗██╔══██║██║╚██╔╝██║██║░╚═══██╗██╔══██║░╚═══██╗
╚█████╔╝██║░░██║██║░╚═╝░██║██║██████╔╝██║░░██║██████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░''')
        
        print(f'{"Nome da Camisa".ljust(25)} | {"Tamanho".ljust(10)} | {"Cor".ljust(10)} | {"Preço".ljust(10)} | {"Disponível"}')
        print('─'*80)
        for camiseta in Camisas.camisetas:
            print(f'{camiseta.nome.ljust(25)} | {camiseta.tamanho.ljust(10)} | {camiseta.cor.ljust(10)} | R${camiseta.preco:.2f}'.ljust(10) + ' | ' + camiseta.disponivel)
            print('─'*80)

    @property
    def disponivel(self):
        return '✅ Disponível' if self._disponivel else '❌ Indisponível'



camisa_adidas = Camisas('Camisa Adidas', 'M', 'Preto', 199.90)
camisa_nike = Camisas('Camisa Nike', 'G', 'Branco', 229.90)
camisa_puma = Camisas('Camisa Puma', 'P', 'Azul', 179.90)


Camisas.listar_camisetas()
