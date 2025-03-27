import random
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

CANAIS = {
    "Programador de Sucesso": "UCHgQAOkK8EPR01C6VgN6Kzg",
    "Codigo Fonte TV": "UCFuIUoyHB12qpYa8Jpxoxow"
}

def sortear_video_do_canal(channel_id):
    youtube = build("youtube", "v3", developerKey=API_KEY)

    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=50,
        order="date"
    )

    videos = []
    while request:
        response = request.execute()
        for item in response.get("items", []):
            if item["id"].get("kind") == "youtube#video":
                videos.append(item["id"]["videoId"])
        request = youtube.search().list_next(request, response)

    print(f"Quantidade de vídeos encontrados: {len(videos)}")
    if videos:
        escolhido = random.choice(videos)
        print(f"Vídeo sorteado: https://www.youtube.com/watch?v={escolhido}")

if __name__ == "__main__":
    print("Escolha um canal:")
    for i, nome in enumerate(CANAIS.keys(), 1):
        print(f"{i}. {nome}")
    
    escolha = int(input("Digite o número do canal desejado: "))
    
    if 1 <= escolha <= len(CANAIS):
        canal_selecionado = list(CANAIS.keys())[escolha - 1]
        print(f"Você escolheu: {canal_selecionado}")
        sortear_video_do_canal(CANAIS[canal_selecionado])
    else:
        print("Opção inválida.")
