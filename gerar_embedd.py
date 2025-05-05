import requests

def gerar_embeddings_ollama(texto, modelo="nomic-embed-text"):
    url = "http://localhost:11434/api/embeddings"
    payload = {
        "model": modelo,
        "prompt": texto
    }

    try:
        resposta = requests.post(url, json=payload)
        resposta.raise_for_status()
        dados = resposta.json()

        vetor = dados.get("embedding", [])
        print(f"Texto fornecido: {texto}")
        print(f"Tamanho do vetor de embeddings: {len(vetor)}")
        print(f"Início do vetor (10 primeiros valores): {vetor[:10]}")

    except requests.exceptions.RequestException as erro:
        print(f"Erro ao conectar ao Ollama: {erro}")
    except ValueError:
        print("Erro ao processar resposta JSON.")

texto_exemplo = "Ola amigos como estão tranquilos"
gerar_embeddings_ollama(texto_exemplo)

texto_exemplo2 = "mankind knew that they cannot change society, so instead of reflecting upon themselves, they blamed the beasts"
gerar_embeddings_ollama(texto_exemplo2)