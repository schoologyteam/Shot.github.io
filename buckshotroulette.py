import pygame
import random
from time import sleep
pygame.init()
som_fgatilho = pygame.mixer.Sound('fgatilho.mp3')
som_tiro = pygame.mixer.Sound('Gunshot.mp3')
print("="*41)
print(" "*10, "BUCKSHOT ROULLETE")
print("="*41)
print("!!! Bem vindo a roleta russa BUCKSHOT ROULLETE !!!")
print("* Escolher a ação de atirar em si resultará no benefício de pular a vez na próxima rodada")
print("* Escolher a ação de atirar em seu oponente resultará no benefício de ganhar mais rápido kkkk")
print("* Em seguida, escolha o tambor da arma que irá disparar")
sleep(9)
print("=====================")
jogador_1=str(input("digite o nome do jogador 1: ")).strip().title()
jogador_2=str(input("digite o nome do jogador 2: ")).strip().title()
#Definindo a quantidade de tambores na arma:
quantidade_tambores=random.randint(5,11) 
#Criando uma lista com uma range que represente a numeragem de cada tambor da arma:
tambores=list(range(1,quantidade_tambores))
#Definindo a procura de um número válido de tambores carregados, sem que o numero de tambores carregados seja igual a quantidade de tambores da arma e com  no mínimo, 2 tambores vazios a mais do que carregados:
while True: 
 sleep(1)
 carregados=random.randint(1,5)
 if carregados!=len(tambores)-2 and carregados!=len(tambores)-1 and carregados < len(tambores):
  break
print("="*41)
print(f"Há {len(tambores)} tambores na escopeta e {carregados} deles estão carregados!!!")
#Escolhendo "carregados" numeros aleatórios DIFERENTES da lista "tambores" para serem "selecionados com munição":
selecionado=random.sample(tambores,k=carregados)
#a variável jogo_ativo é igual a True, a qual mantém o jogo funcionando até que jogo_ativo seja igual a False, encerrando o programa:
jogo_ativo=True
while jogo_ativo:
  for turno in (jogador_1,jogador_2):
    print("="*51)
    print(f"sua vez de jogar, {turno}")
    print("numeragem dos tambores: ",tambores)
    while True:
     acao=str(input("qual será sua ação? em si/oponente: ")).strip()
     if acao!= "em si" and acao != "oponente":
       print("Opção inválida! Por favor, digite 'em si' ou 'oponente'.")
     else:
       break 
    try:
     escolha=int(input("escolha o número do tambor: "))
    except ValueError:
       print("tu fez merda")
    if escolha in selecionado and acao.lower()=="em si":
      som_fgatilho.play()
      print("..... um barulho ecoa no corredor ....")
      sleep(4)
      som_tiro.play()
      print(f"seu oponente ri ao ver a poça de sangue no chão, você morreu {turno}")
      jogo_ativo=False
      break
    if escolha in selecionado and acao.lower()=="oponente":
      som_fgatilho.play()
      print("..... um barulho ecoa no corredor ....")
      sleep(4)
      som_tiro.play()
      print(f"a presença desagradável de seu oponente chega ao fim, você vive {turno}, enquanto seu adversário descansa eternamente")
      jogo_ativo=False
      break
    else:
      som_fgatilho.play()
      print("..... um barulho ecoa no corredor ....")
      sleep(4)
      print("Os dois continuam de pé, mas não por muito tempo...")
    tambores.remove(escolha)
pygame.quit()