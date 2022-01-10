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

