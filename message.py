from twilio.rest import Client 
 
account_sid = 'ACbd8c650239ced11c40f3adcaba19813a' 
auth_token = '3f006ddb3c66b711844c7826654fde1f' 
client = Client(account_sid, auth_token) 

def sendMessage():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Good Morning',      
                                to='whatsapp:+916366268430' 
                            ) 
 

