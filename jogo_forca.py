import os

def sortear_palavra():
    from random import choices

    if not os.path.exists("Palavras.txt"):
        raise FileNotFoundError("Arquivo não encontrado para sortear as palavras")

    with open("Palavras.txt","r",encoding="utf-8") as arquivo:

        ler=arquivo.read().split()
        palavra_sorteada=choices(ler)

    return palavra_sorteada     
 
class JogoForca:
    def __init__(self):
        self.__palavra=sortear_palavra()[0]
        self._erros=0
        self.FORCA_ESTAGIOS = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""
]
        self._letras_chutadas=[]


    def desenhar(self):
        desenho=[j if j in self._letras_chutadas else "_" for j in self.__palavra]
        silabas=""
        for i in desenho:
            silabas+=f"{i} "
        if self._erros <len(self.FORCA_ESTAGIOS):
            print(self.FORCA_ESTAGIOS[self._erros])

        else:
            print(self.FORCA_ESTAGIOS[self._erros-1])

        print(silabas)
        

    def chutar(self,silaba:str):
        if len(silaba)>1 or len(silaba) == 1:
            silaba=silaba[0].upper()

        if silaba in self.__palavra:
            self._letras_chutadas.append(silaba)
            self.desenhar()

        else:
            self._erros+=1

    def verificar_vitoria(self):
        venceu=True
        for i in self.__palavra:
            if not i in self._letras_chutadas:
                venceu=False
                break
        if venceu:
            return True

        if self._erros>=7:
            return False

        return "Continua"
