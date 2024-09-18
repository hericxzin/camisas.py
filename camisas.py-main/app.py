from modelos.camisas import Camisas

camisa_adidas = Camisas('Camisa Adidas', 'M', 'Preto', 199.90)
camisa_nike = Camisas('Camisa Nike', 'G', 'Branco', 229.90)
camisa_puma = Camisas('Camisa Puma', 'P', 'Azul', 179.90)

camisa_adidas.alterar_estado()
camisa_puma.receber_preco('Loja A', 199.90)
camisa_puma.receber_preco('Loja B', 189.90)
camisa_puma.receber_preco('Loja C', 209.90)

def main():
    Camisas.listar_camisetas()

if __name__ == '__main__':
    main()
