"""
    Código desenvolvido como solução da Questão 1: Loja do seu Manoel.

Para o desenvolvimento do código eu me baseei na altura das caixas e dos produtos.
E assumi que o seu Manoel não gira as caixas dos produtos em nenhum sentido, sempre
empilhando-as para pôr nas caixas.

"""


# Classe usada para criar os objetos que representam as caixas do seu Manoel e também os produtos.
# Todos os objetos possuem altura, largura e comprimento.

class PhysicalObject:
    def __init__(self, height, width, length):
        self.height = height
        self.width = width
        self.length = length


#Função principal do código. É passada uma lista com os produtos como argumento.
#A função possui 3 possíveis retornos:
#-A caixa selecionada, caso encontre uma caixa onde os produtos caibam.
#-Nenhuma caixa, caso os produtos não caibam em nenhuma caixa.
#-Nenhum produto checar, caso a entrada de dados seja 0.

def get_box(products):
    if len(products) == 0:
        return '0items'  # caso retorne '0items', significa que a entrada de dados foi 0, não há produtos, logo não precisa selecionar caixas

    height_total = 0
    for product in products:
        height_total += product.height  # como eu me baseei somente na idéia de empilhar as caixas, eu somo todas as alturas dos produtos

    if height_total <= BOX1.height:  # checa se os produtos empilhados cabem na caixa 1
        all_fit = True
        for product in products:
            if product.width > BOX1.width or product.length > BOX1.length:  # checa se a largura e comprimento dos os produtos empilhados cabem na caixa 1
                all_fit = False
        if all_fit:
            return '1'
    if height_total <= BOX2.height:  # checa se os produtos empilhados cabem na caixa 2
        all_fit = True
        for product in products:
            if product.width > BOX2.width or product.length > BOX2.length:  # checa se a largura e comprimento dos os produtos empilhados cabem na caixa 2
                all_fit = False
        if all_fit:
            return '2'
    if height_total <= BOX3.height:  # checa se os produtos empilhados cabem na caixa 3
        all_fit = True
        for product in products:
            if product.width > BOX3.width or product.length > BOX3.length:  # checa se a largura e comprimento dos os produtos empilhados cabem na caixa 3
                all_fit = False
        if all_fit:
            return '3'
    return 'noBox'  # retorno de nenhuma caixa selecionada


# Função de leitura do arquivo .txt. Funciona como a entrada de dados.
# A função retorna uma lista de listas, essas listas são as medidas dos produtos.
def get_products_from_txt():
    products_list = []
    items = []
    with open('produtos.txt', 'r') as file:
        content = file.readlines()
        truck = []
        for line in content:
            products = line.strip().split("x")
            for a in products:
                truck.append(int(a))
            products_list.append(truck)
            truck = []
    for product in products_list:
        items.append(PhysicalObject(product[0], product[1], product[2]))
    return items


BOX1 = PhysicalObject(30, 40, 80)
BOX2 = PhysicalObject(80, 50, 40)
BOX3 = PhysicalObject(50, 80, 60)


def main():
    products = get_products_from_txt()  # entrada de dados dos produtos
    chosen_box = get_box(products)  # chamando a função get_box

    # checagem do retorno da função get_box.
    if chosen_box == '0items':
        print('0 itens. Nenhuma caixa selecionada.')
    elif chosen_box == 'noBox':
        print('Não coube em nenhuma caixa.')
    else:
        print(f'A caixa selecionada foi a CAIXA {chosen_box}.')


if __name__ == "__main__":
    main()

# entrada de dados teste
# products = [PhysicalObject(40, 10, 25), PhysicalObject(40, 30, 30), PhysicalObject(15, 20, 10), PhysicalObject(10, 30, 10), PhysicalObject(30, 15, 10), PhysicalObject(50, 20, 20)]
# products = [PhysicalObject(10, 15, 30), PhysicalObject(20, 10, 20)]
# products = [PhysicalObject(10, 10, 10), PhysicalObject(20, 20, 20), PhysicalObject(30, 10, 10)]
