import smtplib
from datetime import date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import my_email, password
from subscribers import recipients

date = date.today().strftime("%m/%d")

with open("index.html", "r") as file:
    html_content = file.read()

# connection will automatically close after sending emails to all recipients
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)

    for recipient in recipients:
        email = MIMEMultipart("alternative")
        email["Subject"] = f"Good morning! {date}"
        email["From"] = my_email
        email["To"] = recipient

        html_part = MIMEText(html_content, "html")
        email.attach(html_part)

        connection.send_message(email)
