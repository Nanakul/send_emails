from datetime import datetime
import pandas as pd
import smtplib
import getpass

today = (datetime.now().month, datetime.now().day)
data = pd.read_csv('birthdays.csv')
birthdays_d = {(data_row['month'], data_row['day']) : data_row for (index, data_row) in data.iterrows()}

# Check to see if today's date matches a birthday.
if today in birthdays_d:
    special_person = birthdays_d[today]
    file_path = './bday_letter1.txt'
    with open(file_path) as f:
        contents = f.read()
        contents = contents.replace('[NAME]', special_person['name'])


def send_email():
    my_email = getpass.getpass('Email: ')
    my_password = getpass.getpass('Password: ')

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(my_email, special_person['email'],
                            msg=f'Subject:Happy Birthday!! \n\n{contents}')


if __name__ == '__main__':
    send_email()
