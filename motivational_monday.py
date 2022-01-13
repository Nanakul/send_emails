import smtplib
import getpass
import datetime as dt
import random
import sqlite3 as db

# NOTE: To use this script, you must set up Two-Factor Authentication and
# create an app password on Gmail.

# Log in with Gmail
my_email = getpass.getpass('Email: ')
my_password = getpass.getpass('Password: ')
to_address = input('Email of recipient: ')
subject = 'Motivational Monday!'

now = dt.datetime.now()
weekday = now.weekday()

# Connect the database
db_conn = db.connect('Emails.db')
cursor = db_conn.cursor()
cursor.execute("""CREATE TABLE if NOT EXISTS Emails (email VARCHAR UNIQUE)""")
db_conn.commit()


def weekday_check() -> str:
    if weekday == 0:
        with open('quotes.txt') as q:
            all_quotes = q.readlines()
            rand_quote = random.choice(all_quotes)

        return rand_quote
    else:
        pass


def send_email(_random_quote):

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(my_email,
                            to_addrs=to_address,
                            msg=('Subject:' + subject + '\n' + _random_quote).encode('ascii', 'ignore'))


def db_add_email(_to_address):
    cursor.execute('INSERT or IGNORE INTO Emails (email) VALUES (?)', (_to_address,))
    db_conn.commit()


if __name__ == '__main__':
    random_quote = weekday_check()

    weekday_check()
    send_email(random_quote)
    db_add_email(to_address)
