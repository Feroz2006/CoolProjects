import smtplib

from email.message import EmailMessage

print("Hello ! I'm going to send an email for you! ")
username = input("Enter your email ID: ")
password = input("Enter your password: ")
name = input("Enter the name you want to appear on your email: ")
send_to_address = input("Enter the email ID you want to send your email to: ")

email = EmailMessage()

email["from"] = name

email["to"] = send_to_address

email["subject"] = "I sent this with Python !"

email.set_content("Bet u didn't see this coming")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(username, password)
    smtp.send()







