LOAD DATA LOCAL INFILE './ecommerce_clickstream_transactions.csv'
INTO TABLE clickstream
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(UserID, SessionID, Timestamp, EventType, ProductID, Amount, Outcome);
