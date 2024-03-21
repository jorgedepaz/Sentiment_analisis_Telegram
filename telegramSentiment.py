import requests
from transformers import pipeline
import timm
#from dotenv import load_dotenv
lines = ""
lines2 = ""

token = "6605265409:AAGTEBUcdbMXJXwXZ5gHXIaz1oXhlQxTf7I"

sentimiento_pipeline = pipeline(task="text-classification", model="pysentimiento/robertuito-sentiment-analysis")

def get_updates(offset):
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    params = {"timeout":100,"offset":offset} #if offset else{}
    response = requests.get(url,params=params)
    return response.json() 

def send_message(chat_id,text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {"chat_id":chat_id,"text":text} #if offset else{}
    response = requests.post(url,params=params)
    return response.json()

def get_human_response():
    human_res = input("Type your response: ")
    return human_res

def main():
    global lines
    global lines2
    print("Starting bot..")
    offset = 0
    
    while True:
        updates = get_updates(offset)
        if "result" in updates:
            for update in updates["result"]:
                offset = (int(update["update_id"])+1)
                chat_id = update["message"]["chat"]["id"]
                user_message = update["message"]["text"]
                #user_message_score = sentimiento_pipeline(user_message)
                user_message_score = ",".join(str(element) for element in sentimiento_pipeline(user_message))

                #lines.append(user_message)
                lines=lines+"User: "+user_message+" Score: "+user_message_score+'|'+'\n'
                #with open('conversacionesAgente.txt') as cliente:
                    #lines = cliente.readlines()
                with open('conversacionesAgente.txt','w') as cliente:  
                    #cliente.write(str(lines))
                    cliente.write(lines)
                
                print(f"Received Message: {user_message}")
                print(sentimiento_pipeline(user_message))
                GPT = get_human_response()
                #GPT_score = sentimiento_pipeline(GPT)
                GPT_score = ",".join(str(element) for element in sentimiento_pipeline(GPT))
                send_message(chat_id,GPT)
                #lines2.append(GPT)
                lines2=lines2+"BAC Center: "+GPT+" Score: "+GPT_score+'|'+'\n'
               
                with open('conversacionesIA.txt','w') as agente:
                    agente.write(lines2)
        else:
            time.sleep(1)
if __name__ == '__main__': 
    main()