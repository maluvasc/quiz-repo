print("Hello, world!")

def print_name():
    name = input("Insira aqui seu nome: ")
    birth_day = input("Insira aqui seu dia de nascimento: ")
    print("Olá, {}. Seu aniversário é no dia {}".format(name.capitalize(),birth_day))

print_name()