# Predicting Avalanche Danger

## Slide Deck:
https://docs.google.com/presentation/d/1YZgde4rLHyOBKZ2UWvqnlnnBDEOk82rECfeQudbjq30/edit?usp=sharing
HELLO!


## Business Understanding

As a backcountry skier, I rely on the avalanche forecast provided by nwac.us to help me determine my ski route and destination for a trip. Triggering an avalanche is something I would very much like to avoid. However, outside of the North America, avalanche danger level forecasts do not exist. My goal is to create a regression model to predict avalanche danger. 

## Data Understanding

The data is sourced from the Northwest Avalanche Center (nwac.us). Across the state, there exists a collection of weather stations that report every hour on the hour. This is super useful for weather forecasters to measure what is happening in areas not easily accessed. During the winter season, nwac use this data, incoming  in the sky forecast information, and also human assessment of the snowpack to provide  daily avalanche danger levels at different elevation bands for the mountain areas across the Cascade and Olympic mountain ranges. This is not only important for people interested in venturing into the backcountry, but also local and state transportation agencies to asses highway and road safety. For the first iteration of modeling, I plan to use this on the ground information to help determine avalanche danger level.

talk about where to grab the csv files 

[Precipitation Data](https://www.nwac.us/data-portal/location/stevens-pass/q?field_name=precipitation&year=2019&custom_startdate=2014-01-01&custom_enddate=2019-06-28)

The data is sourced from the Northwest Avalanche Center (nwac.us). Across the state, there exists a collection of weather stations that report every hour on the hour. This is super useful for weather forecasters to measure what is happening in areas not easily accessed. During the winter season, nwac use this data, incoming  in the sky forecast information, and also human assessment of the snowpack to provide  daily avalanche danger levels at different elevation bands for the mountain areas across the Cascade and Olympic mountain ranges. This is not only important for people interested in venturing into the backcountry, but also local and state transportation agencies to asses highway and road safety. For the first iteration of modeling, I plan to use this on the ground information to help determine avalanche danger level.


## Data Preparation
The data collected from the weather stations is handily provided through nwac.us data portal in the form of csv files, going back since 2012. The archive of avalance danger forecasts only go back until 2014, and are given daily for three elevation bands: below treeline, near treeline, and above treeline. I decide to focus only on one elevation band, near-treeline, to model since that is where  Unfortutely  within their data portal, they do not provide an archive of their predicted danger forecasts. This problem is easily solved by scraping their archived forecasts. To solve this, two scrapes are necessary: the first is to first collect a list of urls that point to the numerous urls of each forecast To obtain a prediction to base asses my model performance,

Modeling


Evaluation


Deployment
Once I can get a model going, I hope to deploy this via Flask so I can use it! 


