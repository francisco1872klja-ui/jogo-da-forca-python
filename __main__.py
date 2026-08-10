from jogo_forca import JogoForca
from os import system
from time import sleep

def Jogo_Forca():
    jogo=JogoForca()
    print("Começou o jogo..")
    sleep(0.9)
    while True:
        try:
            system("cls") 
            jogo.desenhar()
            escolha=str(input("Chute uma silaba: "))
            jogo.chutar(escolha)


            vitoria=jogo.verificar_vitoria()

            if vitoria == "Continua":
                continue

            elif vitoria:
                print("VOCÊ VENCEU!!")
                break

            else:
                print("VOCÊ PERDEU!!")
                break

        except KeyboardInterrupt:
            print("Fechando...")
            break

if __name__ == "__main__":
    Jogo_Forca()
