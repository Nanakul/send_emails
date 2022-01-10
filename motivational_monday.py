import smtplib
import json
import getpass
import datetime as dt
import random

email = getpass.getpass('Email: ')
password = getpass.getpass('Password: ')
to_address = input('Email of recipient: ')
subject = 'Motivational Monday!'

now = dt.datetime.now()
weekday = now.weekday()


def weekday_check():
    if weekday == 1:
        with open('quotes.txt') as q:
            all_quotes = q.readlines()
            random_quote = random.choice(all_quotes)

    return random_quote


def send_email(_random_quote):

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(email,
                            to_addrs=to_address,
                            msg='Subject:' + subject + '\n' + random_quote)


if '__name__' == '__main__':
    random_quote = weekday_check()

    weekday_check()
    send_email(random_quote)