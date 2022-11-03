# I have decided to create the following scenario: An advertising company wants to create targeted ads for LinkedIn
# -professionals. But since the company is unable to reach private information of persons, it has to create profiles
# for people and generate synthetic LinkedIn data to feed Machine Learning systems so the systems will have lots of data
# examples for profiles when AI wants to target certain people that fits specific profiles.

# First let's check the original dataset

import pandas as pd
from pandas import DataFrame
import numpy as np

original_data = pd.read_csv("Connections.csv", on_bad_lines='skip')
original_data.head()
# Our column names (I think this is called Data Objects) are:  First Name,Last Name,Email Address,Company,Position,
# Connected On

from faker import Faker

# First I have imported the Faker library to generate synthetic data

fake = Faker()
# I have assigned a variable to use Faker() function. Now I'll generate the data
name = []
company = []
date = []
job = []
email = []
for i in range(20):
    name.append(fake.name())
    company.append(fake.company())
    date.append(fake.date_between(start_date="-10y", end_date="now"))
    email.append(fake.email())
    job.append(fake.job())

fake_dataset = pd.DataFrame({'name': name, 'company': company, 'date': date, 'email': email, 'job': job})

# I generated the data as a list, now I'll transform it into a DataFrame and save it as a csv file

fake_dataset.to_csv('fake_dataset')

synthetic_data = pd.read_csv("fake_dataset.csv")
print(synthetic_data.head())

# It works but there are several problems: 1- CSV file is a bit messy with index and general row/column order 2-
# Faker library's date_time function gives a random date even before LinkedIn was created. While it is possible to
# give ranges to date_time function, I am not sure how to do this while generating fake data.[SOLVED]


# Also, Faker has limited
# providers aka data objects (name, company etc.) and it may take a while until it becomes a sufficient library for
# creating synthetic data for businesses. For this we can create a Dynamic Provider. And then append the aforementioned
# code to target LinkedIn legal userbase.


from faker.providers import DynamicProvider

legal_professions_provider = DynamicProvider(
    provider_name="legal_profession",
    elements=["J", "Judge", "Paralegal", "Counsel", "Solicitor"],
)

fake = Faker()

# then add new provider to faker instance
fake.add_provider(legal_professions_provider)

# now you can use:
print(fake.legal_profession())