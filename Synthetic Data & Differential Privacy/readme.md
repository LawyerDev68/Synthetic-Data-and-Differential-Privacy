# Histograms-with-Differential-Privacy
 The previous scenario was this: An advertising company wants to create targeted ads for LinkedIn professionals. But
 since the company is unable to reach private information of persons, it has to create profiles for people and
 generate synthetic LinkedIn data to feed Machine Learning systems so the systems will have lots of data examples
 for profiles when AI wants to target certain people that fits specific profiles. LinkedIn dataset did not have
 salaries, also the Faker library of Python does not have a salary provider, so we need to create a dynamic provider
 for salaries first, and then generate synthetic data.

 But let us assume that the synthetic data we generated is actually a private dataset and company has to apply
 differential privacy and visualize the data. How would that happen? You can check the code for that.
 
 Resulting histograms:
 
## Non-Private: 
 
 ![image](https://user-images.githubusercontent.com/95018675/189114748-b9871793-0787-4d7c-82da-aad00be4695c.png)

 
## Private:
 
 ![image](https://user-images.githubusercontent.com/95018675/189114781-76e317a7-ea59-4705-becb-5736ada462d6.png)

They are not so similiar with each other because our epsilon value is small. If epsilon value would be bigger, it would be much more accurate
but this time, privacy of the dataset would be lowered. It is a trade-off to consider.
 

