from TubeLoader import *

url = input("Digite uma url: ")

try:
    if "list" in url:
        baixarPlaylist(url)
    else:
        baixarVideo(url)

except Exception as ex:
    print(type(ex))
