from abc import ABC, abstractclassmethod

class Observer(ABC):
    @abstractclassmethod
    def update(self,data):
        pass

#Observado
class PalavrasCont:
    def __init__(self):
        self.observes = []
        self.words = []

    def adicionaObservador(self, observer):
        self.observes.append(observer) 

    def notificaObservador(self):
        for obsover in self.observes:
            obsover.update(self.words)

    def frase(self, frase):
        self.words = frase.split()
        self.notificaObservador()


# Observador
class TotalPalavras(Observer):
    def update(self, data):
        print("Total de palavras: {}".format(len(data)))

class PalavrasPar(Observer):
    def update(self, data):
        pares = [word for word in data if len(word) % 2 == 0]
        print("Palavras com comprimento par: {}".format(len(pares)))

class CapsLockOn(Observer):
    def update(self, data):
        capslock = [word for word in data if word[0].isupper()]
        print("Palavras começadas com maiúsculas: {}".format(len(capslock)))
       


if __name__ == "__main__":
    contador = PalavrasCont()

    allWords = TotalPalavras()
    palavrasPares = PalavrasPar()
    capsWords = CapsLockOn()

    contador.adicionaObservador(allWords)
    contador.adicionaObservador(palavrasPares)
    contador.adicionaObservador(capsWords)

    phrase = input("Digite uma frase: ")
    contador.frase(phrase)       