import os
from twilio.rest import Client
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def send_whatsapp_message():
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = 'whatsapp:' + os.getenv("TWILIO_WHATSAPP_FROM")
    to_number = 'whatsapp:' + os.getenv("TWILIO_WHATSAPP_TO")

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=from_number,
        body=f"⏰ Drink Water Reminder - {datetime.now().strftime('%I:%M %p')}",
        to=to_number
    )
    print(f"Sent at {datetime.now()}: {message.sid}")

# Scheduler runs every hour
scheduler = BlockingScheduler()
scheduler.add_job(send_whatsapp_message, 'interval', hours=1)
scheduler.start()
