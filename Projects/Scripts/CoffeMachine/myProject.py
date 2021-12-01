from menu import MENU, resources

#Campo das funcoes


def contar_moedas(q = 0, d = 0, n = 0, p = 0):
    q = quarters*0.25
    d = dimes*0.10
    n = nickles*0.05
    p = pennies*0.01

    return q+d+n+p


def mostrar_recursos():
    print(f'Água = {resources["water"]}\n Leite = {resources["milk"]}\n Café = {resources["coffee"]}')


def consumir_recursos(water, milk, coffee):
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee

# ---- FIM ----


# Programa Principal
while True:
    # TODO 1 - Perguntar ao usuario qual opçao de café deseja escolher (espresso, latte, cappuccino)
    escolher_cafe = input("Qual bebida gostaria? (espresso/latte/cappuccino): ").lower()

    if escolher_cafe == "off":
        break

    if escolher_cafe == "status":
        mostrar_recursos()
        continue
    else:
        bebida = MENU[escolher_cafe]
        preco = MENU[escolher_cafe]["cost"]
        water = MENU[escolher_cafe]["ingredients"]["water"]
        milk = MENU[escolher_cafe]["ingredients"]["milk"]
        coffee = MENU[escolher_cafe]["ingredients"]["coffee"]
        consumir_recursos(water, milk, coffee)
        print(f"Valor: R$ {preco}")

    # TODO 2 - Depois de escolher a opcao mostrar na tela Inserir as moedas
    # TODO 2.1 - Quantos quarters=0,25 dimes=0,10 nickles=0,05 pennies=0,01
    print("Por favor inserir as moedas")
    quarters = int(input("Quantos quarters?: "))
    dimes = int(input("Quantos dimes?: "))
    nickles = int(input("Quantos nickles?: "))
    pennies = int(input("Quantos pennies?: "))
    status_moedas = contar_moedas(quarters, dimes, nickles, pennies)
    print(f"Total R$ {round(status_moedas, 3)}")
    # TODO 2.2 - Condicao para verificar se a quantidade de moedas é suficinte para comprar o cafe
    # Caso a condicao seja satisfeita mostrar a mensagem = Aqui está seu troco R$ __ . Aqui é seu (opcao escolhida)
    # Subtrair dos recursos as quantidades para fazer a bebida
    # Caso a condicao não seja satisfeita mostrar a mensagem = Descupe vc não tem dinheiro suficiente. Dinheiro devolvido
    if status_moedas >= preco:
        troco = status_moedas - preco
        print(f"Aqui está seu troco R$ {round(troco,3)} Aproveite seu {escolher_cafe}")
    else:
        print("Desculpe você não tem fundos suficientes. Dinheiro devolvido")
    # TODO 3 - Criar um laco repicao
    # ---- FIM DO PROGRAMA PRINCIPAL ----



