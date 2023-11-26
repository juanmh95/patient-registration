import smtplib

sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

Patient has been registred."""

async def send_mail(sender, receiver, message = message):
    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
        server.login("a3694ca5d7e833", "29f7eb6a3fe45d")
        server.sendmail(sender, receiver, message)