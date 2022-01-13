from datetime import datetime
import pandas as pd
import smtplib
import getpass

today = (datetime.now().month, datetime.now().day)
data = pd.read_csv('birthdays.csv')
birthdays_d = {(data_row['month'], data_row['day']) : data_row for (index, data_row) in data.iterrows()}


def check_replace():
    """This function will check to see if today's date matches someone's birthday date."""
    if today in birthdays_d:
        special_person = birthdays_d[today]
        file_path = './bday_letter1.txt'
        with open(file_path) as f:
            contents = f.read()
            contents.replace('[NAME]', special_person['name'])


