import smtplib
import json
import getpass
import datetime as dt
import random

email = getpass.getpass('Email: ')
password = getpass.getpass('Password: ')

now = dt.datetime.now()
weekday = now.weekday()


def weekday_check():
    if weekday == 1:
        with open('quotes.txt') as q:
            all_quotes = q.readlines()
            random_quote = random.choice(all_quotes)

    return random_quote


def send_email(random_quote):

    to_address = input('Email of recipient: ')
    subject = 'Motivational Monday!'

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(email,
                            to_addrs=to_address,
                            msg='Subject:' + subject + '\n' + random_quote)


if '__name__' == '__main__':
    weekday_check()
