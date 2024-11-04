from twilio.rest import Client
from django.conf import settings
def send_sms(tonum, mssg):
    client=Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=mssg,
        from_= settings.TWILIO_PHONE_NUMBER,
        to= tonum
    )
    return message.sid