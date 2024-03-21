from transformers import pipeline
import timm

vozCliente = []
vozClienteInterno = []
with open('conversacionesAgente.txt') as cliente:
    lines = cliente.readlines()

with open('conversacionesIA.txt') as agente:
    lines2 = agente.readlines()

#Procesamiento de datos de la voz del cliente
vozCliente = lines[0].split("|")
size = len(vozCliente)
vozCliente.remove(vozCliente[size-1])
vozCliente.remove(vozCliente[0])

#Procesamiento de datos de la voz del cliente interno
vozClienteInterno = lines2[0].split("|")
size = len(vozClienteInterno)
vozClienteInterno.remove(vozClienteInterno[size-1])
vozClienteInterno.remove(vozClienteInterno[0])

sentimiento_pipeline = pipeline(task="text-classification", model="pysentimiento/robertuito-sentiment-analysis")

#textos = ["¡Me encanta poder aprender en español con Platzi y Hugging Face",
#         "Me enoja no tener más material de Hugging Face en español."]
print("Voz del cliente")
print(vozCliente)
print("Puntuaciones del chat en la voz del cliente")
print(sentimiento_pipeline(vozCliente))

print("Voz del cliente interno")
print(vozClienteInterno)
print("Puntuaciones del chat en la voz del cliente interno")
print(sentimiento_pipeline(vozClienteInterno))