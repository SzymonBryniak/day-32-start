##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import re
import smtplib
import datetime as dt
import random


# print(now.isoweekday(), now)

password = 'bqep xhcu tsbb pjnx'
my_email = "szymonbryniakproject@gmail.com"

files = ['./letter_1.txt', './letter_2.txt', './letter_3.txt']
random_letter = random.choice(files)
# print(random_letter)


def check_day():
    with open('./birthdays.csv') as birthday:
        name = birthday.readline().split(',')[0]
        details = birthday.readline().split(',')[2:]
        details[-1] = details[-1].strip('\n')

    now_check = str(dt.datetime.today().date()).split('-')
    return details, now_check, name


def send_email():
    date1, date2, name = check_day()
    to_sub = r'\[NAME\]'
    if date1[2] == date2[2]:
        with open(random_letter, mode='r', encoding="utf-8") as letter:
            edited = letter.read()
            to_send = re.sub(to_sub, name, str(edited))
            print(to_send)
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs="oneplusszymonbryniak@gmail.com",
                                    msg=to_send)
                connection.close()


send_email()

