import smtplib
import datetime as dt
import pandas
import random

MY_EMAIL = "rounakmishra1508@gmail.com"
APP_PASSWORD = "ipjx pxdx qunb tvrm"

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        content = letter.read()
        new_content = content.replace("[NAME]", person["name"])

    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=APP_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person["email"],
                msg=f"Subject:!! Happy Birthday !!\n\n{new_content}")
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")