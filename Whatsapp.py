from twilio.rest import Client

account_sid = "your_account_sid_here"
auth_token = "your_auth_token_here"

client = Client(account_sid, auth_token)

from_whatsapp_number = "whatsapp:+9179079*****"
to_whatsapp_number = "whatsapp:+91xxxxxxxxxx"
message_body = "Hello This is Ankit."

message = client.messages.create(
    body=message_body,
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)

print("Message Status:", message.status)
print("Message SID:", message.sid)
