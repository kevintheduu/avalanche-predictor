# Predicting Avalanche Danger

## Slide Deck:
https://docs.google.com/presentation/d/1YZgde4rLHyOBKZ2UWvqnlnnBDEOk82rECfeQudbjq30/edit?usp=sharing

## Business Understanding

As a backcountry skier in the Pacific Northwest, I rely on the avalanche forecast provided by nwac.us to help me determine my ski route and destination for a trip. Triggering an avalanche is something I would very much like to avoid. However, outside of the North America, avalanche danger level forecasts do not exist. My goal is to create a regression model to predict avalanche danger. 

## Data Understanding

Across the state, there exists a collection of weather stations that report every hour on the hour. This is super useful for weather forecasters to measure what is happening in areas not easily accessed.
The data collected from the weather stations is handily provided through nwac.us data portal in the form of csv files, going back since 2012. Below are links to the various files necessary: 

[Precipitation Data](https://www.nwac.us/data-portal/location/stevens-pass/q?field_name=precipitation&year=2019&custom_startdate=2014-01-01&custom_enddate=2019-06-28)

[Weather Data](https://www.nwac.us/data-portal/location/stevens-pass/)
[image of where to collect weather data](data_portal.png))




The archive of avalance danger forecasts only go back until 2014, and are given daily for three elevation bands: below treeline, near treeline, and above treeline. I decide to focus only on one elevation band, near-treeline since it is the elevation band 

[Precipitation Data](https://www.nwac.us/data-portal/location/stevens-pass/q?field_name=precipitation&year=2019&custom_startdate=2014-01-01&custom_enddate=2019-06-28)

Unfortutely  within their data portal, they do not provide an archive of their predicted danger forecasts. 


This problem is easily solved by scraping their archived forecasts. To solve this, two scrapes are necessary: the first is to first collect a list of urls that point to the numerous urls of each forecast To obtain a prediction to base asses my model performance,

## Data Preparation


Modeling


Evaluation


Deployment
Once I can get a model going, I hope to deploy this via Flask so I can use it! 


