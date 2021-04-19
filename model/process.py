import pandas as pd


listing = pd.read_csv("https://raw.githubusercontent.com/israelaikulola/worksample/main/Data/listings.csv")
print(listing.shape)
print(listing.head(2))
print(listing.info())
print(listing.columns)

