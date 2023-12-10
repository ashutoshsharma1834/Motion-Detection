account_sid='Enter_Your_Sid'

auth_token='Enter_Token'

twilio_number='Enter_Number'

my_phone_number='+91 Your_no'

from twilio.rest import Client


client = Client(account_sid,auth_token)

message=client.messages.create(
    body="  Motion is detected  ",
    from_=twilio_number,
    to=my_phone_number
)

print(message.body)
