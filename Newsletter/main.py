import smtplib
from datetime import date
from config import my_email, password
from subscribers import recipients

date = date.today().strftime("%m/%d")

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)

for recipient in recipients:
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient,
        msg=f"Subject:Weekly Recipes {date}\n\nThis is the body of my newsletter"
        )

connection.close()