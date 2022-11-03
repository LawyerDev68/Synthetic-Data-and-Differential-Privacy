from typing import List, Any
from faker import Faker
from faker.providers import DynamicProvider
import numpy as np
import pandas as pd
from diffprivlib import tools
import matplotlib.pyplot as plt

# The previous scenario was this: An advertising company wants to create targeted ads for LinkedIn professionals. But
# since the company is unable to reach private information of persons, it has to create profiles for people and
# generate synthetic LinkedIn data to feed Machine Learning systems so the systems will have lots of data examples
# for profiles when AI wants to target certain people that fits specific profiles. LinkedIn dataset did not have
# salaries, also the Faker library of Python does not have a salary provider, so we need to create a dynamic provider
# for salaries first, and then generate synthetic data.

# But let us assume that the synthetic data we generated is actually a private dataset and company has to apply
# differential privacy and visualize the data. How would that happen?

original_data = pd.read_csv("Connections.csv", on_bad_lines='skip')
original_data.head()

# Our column names are:  First Name,Last Name,Email Address,Company,Position,
# Connected On

fake = Faker()
# I have assigned a variable to use Faker() function. Now I'll generate the data. But before that, I will create a
# new dynamic provider for salary

salary_provider: DynamicProvider = DynamicProvider(
    provider_name="salary",
    elements=["30.000", "50.000", "70.000", "90.000", "110.000"],
)
# then add new provider to faker instance
fake.add_provider(salary_provider)

# now you can use:
print(fake.salary())

# Now to proceed with generating fake data:

name = []
company = []
date = []
job = []
email = []
salary = []
for i in range(100):
    name.append(fake.name())
    company.append(fake.company())
    date.append(fake.date_between(start_date="-10y", end_date="now"))
    email.append(fake.email())
    job.append(fake.job())
    salary.append(fake.salary())

fake_dataset2 = pd.DataFrame(
    {'name': name, 'company': company, 'date': date, 'email': email, 'job': job, 'salary': salary})

# I generated the data as a list, now I'll transform it into a DataFrame and save it as a csv file

fake_dataset2.to_csv('fake_dataset2')

synthetic_data = pd.read_csv("fake_dataset2.csv")
print(synthetic_data.head())

# I will proceed with applying differential privacy and visualizing the data assuming that it's not synthetic but
# actually a private dataset.

data = pd.read_csv("fake_dataset2.csv")

# Get counts and bars for non-private histogram of salaries
counts, bins = np.histogram(data["salary"])

# Normalize counts to get proportions of the height
proportions = counts / counts.sum()

# Draw the histogram of proportions
plt.bar(bins[:-1], proportions, width=(bins[1] - bins[0]))
plt.show()

# Get counts and bars for private histogram of salaries with epsilon of 0.1
dp_counts, dp_bins = tools.histogram(data["salary"], epsilon=0.1)

# Normalize counts to get proportions
dp_proportions = dp_counts / dp_counts.sum()

# Draw the histogram of proportions and see the differences
plt.bar(dp_bins[:-1], dp_proportions, width=(dp_bins[1] - dp_bins[0]))
plt.show()

# Since our epsilon value is small, our private data is not exactly close to the original data,
# but it is perfectly private.