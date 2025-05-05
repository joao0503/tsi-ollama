Bonjour.
Para gerar o vetor de embeddings, além de ja ter o ollama instalado e executando na sua máquina,
precisa instalar algumas dependências no seu diretório com o script.

Caso não tenha o Ollama instalado, vá para o site deles e instale com base no seu sistema operacional:
https://ollama.com/download

Após instalar (ou caso ja o tenha instalado), instale as seguintes dependências, como pelo terminal do VSCode:

pip install requests

ollama pull nomic-embed-text

Em seguida, rodar o script Python no mesmo terminal com:

python gerar_embedd.py

Caso queira mudar o texto de exemplo, só abrir o script e mudar a variável na penúltima linha.
