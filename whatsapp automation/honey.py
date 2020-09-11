from twilio.rest import Client 
 
account_sid = 'AC4c40202e627943604b70613568630006' 
auth_token = '5d1ce5a4bafd28782ed863e9f1ba4893' 
client = Client(account_sid, auth_token) 
def my_mes(): 
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='hi, i am arnav , this is my sample code',      
                              to='whatsapp:+919622955576' 
                          ) 
 
    print(message.sid)