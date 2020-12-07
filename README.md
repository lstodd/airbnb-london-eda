# Airbnb London EDA

## Motivation
We know that the Coronavirus-19 virus has affected the travel industry a lot. In this 
piece of analysis we try to understand the impact on volume, availability and sentiment of 
airbnb guests. 

The github link for this project is: https://github.com/lstodd/airbnb-london-eda

In 2020, many industries have taken a hit due to coronavirus, particularly the travel industry. 
Let's take a look at how London airbnb rentals have changed by comparing 2020 to 2019.


### Requirements & Installation

The requirements for this repository can be found in a separate requirements.txt file. 

```pip install -r requirements.txt```

Libraries used:
* pandas
* matplotlib
* seaborn

### Datasets

The datasets we analyse are too big to store in github. The files were originally downloaded using the 
following link, selecting data from London in August 2019 and 2020: [Inside Airbnb](http://insideairbnb.com/get-the-data.html).

We compare 2020 and 2019 data, to see the difference before and after coronavirus. 

* **calendar.csv** contains the listings, availability and price per date.
* **listings.csv** contains detailed information on each listing including name, description and cancellation_policy.
* **reviews** contains a columns containing the written review, along with information about the reviewer and listing id.


## Summary

We see that the volume of stays has changed dramatically between 2019 and 2020. 

![Enter message](/images/before_after_reviews.PNG)

The sentiment of the reviews has generally remained the same, which we can see from the 
corresponding wordclouds from the 2019 and 2020 reviews respectively having the same top words.

![Enter message](/images/2019_wordcloud.PNG) ![Enter message](/images/2020_wordcloud.PNG)
 
 The volume of propoerties available was slightly higher in 2019 vs 2020, but not 
 dramatically different.
 
![Enter message](/images/available_rentals.PNG)