from TubeLoader import *

escolha = input("Digite 1 para Video ou 2 para Playlist -> ")
print()

if escolha == "1":
    url = input("Digite uma url: ")
    baixarVideo(url)

elif escolha == "2":
    url = input("Digite uma url: ")
    baixarPlaylist(url)
