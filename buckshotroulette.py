import pygame
import random
from time import sleep
pygame.init()
som_fgatilho = pygame.mixer.Sound('fgatilho.mp3')
som_tiro = pygame.mixer.Sound('Gunshot.mp3')
print("="*41)
print(" "*10, "\033[4;31;40mBUCKSHOT ROULLETE\033[m")
print("="*41)
print("\033[1;33;40m!!! Bem vindo a roleta russa BUCKSHOT ROULLETE !!!")
print("* Escolher a ação de atirar em si resultará no benefício de pular a vez na próxima rodada")
print("* Escolher a ação de atirar em seu oponente resultará no benefício de ganhar mais rápido kkkk")
print("* Em seguida, escolha o tambor da arma que irá disparar\033[m")
sleep(9)
print("=====================")
jogador_1=str(input("digite o nome do jogador 1: ")).strip().title()
jogador_2=str(input("digite o nome do jogador 2: ")).strip().title()
#Definindo a quantidade de tambores na arma:
quantidade_tambores=random.randint(6,57) 
#Criando uma lista com uma range que represente a numeragem de cada tambor da arma:
tambores=list(range(1,quantidade_tambores))
#Definindo a procura de um número válido de tambores carregados, sem que o numero de tambores carregados seja igual a quantidade de tambores da arma e com  no mínimo, 2 tambores vazios a mais do que carregados:
carregados=random.randint(1,5)
while carregados >= len(tambores) - 2: 
 carregados = random.randint(1,5)
#informações sobre os tambores
print("="*41)
print(f"Há \033[0;36m{len(tambores)} tambores\033[m na escopeta e\033[0;31m {carregados} deles estão carregados!!!\033[m")
#Escolhendo "carregados" numeros aleatórios DIFERENTES da lista "tambores" para serem "selecionados com munição":
selecionado = random.sample(tambores,k=carregados)
#a variável jogo_ativo é igual a True, a qual mantém o jogo funcionando até que jogo_ativo seja igual a False, encerrando o programa:
jogo_ativo = True
atirar_duas_vezes = False
while jogo_ativo:
  for turno in (jogador_1,jogador_2):
    print("="*51)
    print(f"sua vez de jogar, \033[0;32m{turno}\033[m")
    print("numeragem dos tambores: ",tambores)
    # se o atirar duas vezes for acionado ( o adversario escolher atirar em si e sobreviver)
    if atirar_duas_vezes:
      print(f"\033[1;31m{turno} deve atirar em si mesmo duas vezes, porque o jogador anterior sobreviveu!\033[m")
      for i in range(2):
        som_fgatilho.play()
        print("..... um barulho ecoa no corredor ....")
        sleep(4)
        escolha = random.choice(tambores)
        tambores.remove(escolha)
        if escolha in selecionado:
          som_tiro.play()
          print(f"\033[0;31mVocê morreu, {turno}.\033[m")
          jogo_ativo = False 
          break
        else:
          print("Você sobreviveu, mas ainda precisa atirar novamente!")
      atirar_duas_vezes = False  # Resetar a condição após os dois tiros
      if not jogo_ativo:# Interrompe o loop 'for' se o jogo acabou
        break
      print(f"Há \033[0;36m{len(tambores)} tambores\033[m na escopeta e\033[0;31m {carregados} deles estão carregados!!!\033[m")
      print("numeragem dos tambores: ",tambores)
    # escolha de ação do jogador
    while True:
     acao=str(input("qual será sua ação? em si/oponente: ")).strip().lower()
     if acao not in ("em si", "oponente"):
       print("Opção inválida! Por favor, digite 'em si' ou 'oponente'.")
     else:
       break
    # escolha de tambor do jogador
    while True:
     escolha=int(input("escolha o número do tambor: "))
     if escolha not in tambores:
        print("Número de tambor inválido! Escolha um número disponível.")
     else:
        tambores.remove(escolha)
        break
    som_fgatilho.play()
    print("..... um barulho ecoa no corredor ....")
    if escolha in selecionado:
      # tocar som de tiro
      som_tiro.play()
      # mensagem de acordo com a ação escolhida
      mensagem = {"em si": f"seu oponente ri ao ver a poça de sangue no chão, \033[0;31m você morreu {turno}\033[m",
                  "oponente": f"a presença desagradável de seu oponente chega ao fim, \033[0;32m você vive {turno}\033[m, enquanto seu adversário descansa eternamente"}
      print(mensagem[acao])
      jogo_ativo=False
      break
    else:
      sleep(4)
      print("Os dois continuam de pé, mas não por muito tempo...")
      if acao in ("em si"):
        atirar_duas_vezes = True
pygame.quit()
