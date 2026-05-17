import smtplib
from datetime import datetime
import random
import pandas

MY_EMAIL = "USE YOUR EMAIL"
PASSWORD = "USE YOUR PASS3"

today = (datetime.now().month, datetime.now().day)

# CREATED DICT USING PANDAS
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row
                  for (index, data_row) in data.iterrows()}

# REPLACING BIRTHDAY PERSON NAME AND PICKING RANDOM LATTER FROM LETTER_TEMPLATES
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthday_person["name"] )

    # FOR SEND MAIL
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # starttls make our connection secure
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
            )
