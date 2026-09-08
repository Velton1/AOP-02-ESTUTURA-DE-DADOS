from lista import lista

def main():
    minha_lista = lista()
    print("----teste do TAD----")
    print(f"Estado inicial: {minha_lista}\n")

    print("inserindo valores 1, 2, 3, 4")
    minha_lista.inserir(1)
    minha_lista.inserir(2)
    minha_lista.inserir(3)
    minha_lista.inserir(4)
    print(f"conteúdo atual da lista:{minha_lista}\n")

    print("buscando o elemento 2")
    if minha_lista.buscar(2):
        print("Elemento 2 encontrado")
    else:
        print("Elemento 2 não encontrado")

    print("buscando o elemento 5")
    if minha_lista.buscar(5):
        print("Elemento 5 encontrado")
    else:
        print("Elemento 5 não encontrado")

    print("removendo o elemento 3")
    if minha_lista.remover(3):
        print("Elemento 3 removido com sucesso")
    else:
        print("Elemento 3 não encontrado para remoção")
    print(f"conteúdo atual da lista:{minha_lista}\n")

    print("removendo um elemento inexistente (5)")
    if minha_lista.remover(5):
        print("Elemento 5 removido com sucesso")
    else:
        print("Elemento 5 não encontrado para remoção")
    print(f"conteúdo atual da lista:{minha_lista}\n")

    print("destruindo a lista")
    minha_lista.destruir()
    print(f"conteúdo atual da lista:{minha_lista}\n")

    
    print("buscando algum elemento da lista")
    if minha_lista.buscar(1):
        print("Elemento 1 encontrado")
    else:
        print("Elemento 1 não encontrado")

if __name__ == "__main__":
    main()    