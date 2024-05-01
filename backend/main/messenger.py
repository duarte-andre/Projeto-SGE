# class TempleteMetaMessage():
#     messaging_product = "whatsapp"
#       to = ""



jsonMessage = {"messaging_product": "whatsapp",
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
        }}