import pandas as pd
import gzip as gz
import csv
import re
import matplotlib.pyplot as plt


def CreateSQL_csvFile():
    #this function is ran to create a csv file to import into my SQL database.
    #csv file is gotten from "Inside Airbnb" where they have many different countries-
    #and states but for this test I chose data from Austin, TX
    l_columnsToKeep = ['listing_url','bedrooms', 'beds','price',
                       'number_of_reviews','review_scores_rating','review_scores_accuracy','review_scores_value']
    df_airbnbData_csv = pd.read_csv("airbnbListings_rawData.csv.gz")
    df_airbnbData_csv = df_airbnbData_csv.set_index("id")
    df_airbnbData = df_airbnbData_csv[l_columnsToKeep]
    df_airbnbData["price"] = df_airbnbData["price"].str.replace(",","")
    df_airbnbData.to_csv("airbnbListings_SQL.csv")
    return None


def Main():

    #CreateSQL_csvFile()

    #this reads the CSV file that was created from a select query from my database-
    #only desiring the id, price, bedrooms to find average price per bedroom.
    df_airbnb = pd.read_csv("airbnb_PRICEvsBEDS.csv")
    #this turns our price string into a computable float and removes the "$"
    df_airbnb["price"] = df_airbnb["price"].str.replace("$","")
    df_airbnb["price"] = df_airbnb["price"].astype(float)
    #gets a single float for the average price per bedroom for Airbnbs in Austin TX 
    #Note this excludes any data that doesnt have price or bedroom count to not skew incomplete data
    df_airbnb["rating/price/bedroom"] = ((df_airbnb["review_scores_rating"] / (df_airbnb["price"] / df_airbnb["bedrooms"])).round(2)).clip(upper=0.5)
    
    #this plot may be a little confusing but very efficent for a consumer to visulize
    #first the Y axis is just the number of reviews being the valilidity of or x-axis or Airbnb, if the-
    #number of reviews are higher we can assume its a more accurate x axis value
    #Now the x-axis is the price of the airbnb normalized to be per bedroom and compared to the rating-
    #given to the airbnb, in short rating divided by (price per bedroom). 
    #This means bigger the number the more effective your dollar is for your airbnb
    df_airbnb.plot(x="rating/price/bedroom", y="number_of_reviews", kind="scatter")
    plt.show()    

    return
Main()