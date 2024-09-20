# Gmail: smtp.gmail.com
#
# Hotmail: smtp.live.com
#
# Outlook: outlook.office365.com
#
# Yahoo: smtp.mail.yahoo.com

# hpad lqsh ssqo qstd


# dpbn brps nhly wlwc
import smtplib
smtplib.SMTP("smtp.gmail.com", port=587)


my_email = "szymonbryniakproject@gmail.com"
password = "hpad lqsh ssqo qstd"


# connection = smtplib.SMTP("smtp.gmail.com")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="oneplusszymonbryniak@gmail.com",
                        msg="Subject:Hello\n\n Hello, This is the body of my email.")
    connection.close()
