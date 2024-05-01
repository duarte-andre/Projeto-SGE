from apscheduler.schedulers.background import BackgroundScheduler
from .models import *
from django.utils import timezone
import pandas as pd
import requests
from django.conf import settings

TOKEN = getattr(settings,'META_TOKEN')
ENDPOINT = getattr(settings,'META_ENDPOINT')

def StartChatBotScheduler():
    scheduler = BackgroundScheduler()
    scheduler.remove_all_jobs()
    scheduler.add_job(ChatBotJob, 'interval', seconds=2)
    scheduler.start()

def SendMessage(message, name, phone):
    print('Message: ', message, name, phone)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + TOKEN
    }
    body =  {
        "messaging_product": "whatsapp",
        "to": phone,
        "type": "template",
        "template": {
            "name": "senai_roberto_mange",
            "language": {
                "code": "pt_BR"
            },
            "components": [
			{
				"type": "header",
				"parameters": [
					{
						"type": "image",
						"image": {
							"link": "https://desenvolveitapevi.wordpress.com/wp-content/uploads/2016/02/logo-senai1.png"
						}
					}
				]
			},
			{
				"type": "body",
				"parameters": [
					{
						"type": "text",
						"text": name,
					},
					{
						"type": "text",
						"text": message
					}
				]
			}
		]
        }
    }
    
    response = None
    saveLog = False
    
    return requests.post(url=ENDPOINT, headers=headers, json=body)
    

def ChatBotJob():
    print('Running ChatBot Job...')
    chatBots = ChatBot.objects.filter(done=False).filter(scheduledDate__lte=timezone.now())
    for bot in chatBots:
        file = pd.read_excel(bot.file.path)
        for index,row in file.iterrows():   
            try:
                file = pd.read_excel(bot.file.path)
                for index,row in file.iterrows():
                    phone  = row['Telefone']
                    if phone is not None:
                        response = None
                        hasError = False
                        
                        try:
                           response= SendMessage(bot.message,row['Nome'],phone) 
                           print("OK --->", response.json())
                            
                        except:
                            hasError= True
                        
                        if (not response.status_code == 200):
                            print("Internal error", )
                            log = FileLogs(chatbotFK=bot,response=response.json(),type='4',row=row,phoneNumber=None)
                            log.save()
            
            except:
                log = FileLogs(chatbotFK=bot,response=None,type='4',row=None,phoneNumber=None)
                log.save()
                
        

            bot.done = True
            bot.save()
    


    