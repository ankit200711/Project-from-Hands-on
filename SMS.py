import twilio
from twilio.rest import Client
ACCOUNT_SID=""
AUTH_TOKEN=""
TWILIO_NUMBER=""
RECEIVER_NUMBER= ""
Clieant = Client(ACCOUNT_SID,AUTH_TOKEN)
message = Client.message.create(
    body = "Hello Nss",
    from_ = TWILIO_NUMBER,
to = RECEIVER 