CREATE TABLE AirbnbListings(
    id VARCHAR(255),
    listing_url VARCHAR(255),
    bedrooms VARCHAR(255), 
    beds VARCHAR(255),
    price VARCHAR(255),
    number_of_reviews VARCHAR(255),
    review_scores_rating VARCHAR(255),
    review_scores_accuracy VARCHAR(255),
    review_scores_value VARCHAR(255),
);

BULK INSERT AirbnbListings
FROM 'C:\Air BnB vs Hotel Market\airbnbListings_SQL.csv'
WITH (FIRSTROW = 2,
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n',
BATCHSIZE = 25000,
MAXERRORS = 2);


SELECT [id],
[price],
[bedrooms],
[review_scores_rating],
[number_of_reviews]
FROM [Hotel_Airbnb].[dbo].[AirbnbListings]

