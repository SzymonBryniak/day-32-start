import smtplib
import datetime as dt
import random

now = dt.datetime.today()

print(now.isoweekday(), now)
password = 'bqep xhcu tsbb pjnx'
my_email = "szymonbryniakproject@gmail.com"

if now.isoweekday() == 6:
    with open('../Birthday Wisher (Day 32) start/quotes.txt') as quotes:
        all_quotes = quotes.readlines()
        random_phrase = random.choice(all_quotes)
        print(random_phrase)
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="oneplusszymonbryniak@gmail.com",
                                msg=random_phrase)
            connection.close()

