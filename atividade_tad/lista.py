class _No():
    def __init__(self, valor):
        self.__valor = valor
        self.__proximo = None
    
    def get_valor(self):
        return self.__valor
    
    

class lista():
    def __init__(self):
        self.__inicio = None

    def inserir(self, valor):
        novo_no = _No(valor)
        novo_no.__proximo = self.__inicio 
        self.__inicio = novo_no
        #eu tive que criar uma variável "novo_no" e conctar ela a classe "no". 
        #depois instanciei a variável "novo_no" e conectei ela a variavel "__inicio" que é o inicio da lista.

    def  remover (self, valor):
        atual = self.__inicio
        anterior = None

        while atual is not None:
            if atual.get_valor() == valor:
                if anterior is None:
                    self.__inicio = atual.get_proximo()
                else:
                    anterior.set_proximo(atual.get_proximo())
                atual.set_proximo(None)
                return True
        anterior = atual
        atual = atual.get_proximo()
        return False

    def buscar(self, valor:int) ->bool:
        atual = self.__inicio
        while atual is not None:
            if atual.get_valor() == valor:
                return True
            atual = atual.get_proximo()
        return False

    def destruir(self) -> None:
        atual = self.__inicio
        while atual is not None:
            proximo = atual.get_proximo()
            atual.set_proximo(None)
            atual = proximo
            self.__inicio = None

    def __str__(self) -> str:
        elementos = []
        atual = self.__inicio
        while atual is not None:
            elementos.append(str(atual.get_valor()))
            atual = atual.get_proximo()
        if not elementos: 
            return "Lista Vazia"
        return "->".join(elementos) + "->None"
        
    