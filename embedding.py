import ollama

texto_exemplo = "Ola amigos como estão tranquilos"

res = ollama.embeddings(model='llama3.2', prompt=texto_exemplo) 

print(texto_exemplo)
print(len(res.embedding))
print(res.embedding[:10])

texto_exemplo2 = "mankind knew that they cannot change society, so instead of reflecting upon themselves, they blamed the beasts"

res2 = ollama.embeddings(model='llama3.2', prompt=texto_exemplo2) 

print(texto_exemplo2)
print(len(res2.embedding))
print(res2.embedding[:10])
