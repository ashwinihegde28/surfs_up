# surfs_up 
Weather analysis using SQL Lite, SQLAlchemy, Python and Flask application.

## Overview of the surfs_up statistical analysis:
An investor  named W.Avy wants to learn more about the weather before investing money into building a Surf and Ice Cream shop in Oahu, Hawaii. In order to determine if the surf and ice cream shop business is sustainable year-round, the investor requests temperature data for the months of June and December on Oahu.The idea is that the shop will sell surf boards and ice cream throughout the year, but the investor is hesitant because he invested in a similar business that failed due to the weather conditions. In order to get this investor on board, we need to provide statistical analysis specifically on the weather conditions in Oahu that will convince him that this will be a successful business venture.This project Queries the SQLite database with the help of SQLAlchemy for the analysis with Python, Pandas functions methods and retrieve all the temperatures for the month of June and December. Then converted those temperatures to a list, than a DataFrame from the list, and generate the summary statistics.

## Results:
1. June and December Statistics for the Temperature is displayed below with the graphical representation <br>
 ![June Temperature Statistics](https://github.com/ashwinihegde28/surfs_up/blob/main/Resources/june_temp_summary.PNG) <br> <br>
 ![June Statistics graph](https://github.com/ashwinihegde28/surfs_up/blob/main/Resources/june_temp_histogram.PNG) <br> <br>
 
 ![December Temperature Statistics](https://github.com/ashwinihegde28/surfs_up/blob/main/Resources/dec_temp_summary.PNG) <br> <br>
 ![December TStatistics graph](https://github.com/ashwinihegde28/surfs_up/blob/main/Resources/dec_temp_histogram.PNG) <br> <br>
 
 
- The mean temperature of 75°F for June is higher than the mean temperature of 71°F for December.
- The maximum temperature of June is slightly higher than December. June is warmer than December.
- Even the min temperature for June is higher than December.
- This concludes that the temperature in Oahu is not more fluctuating from June to December and it's a good place suitable for the shop.


## Summary:
Additionally June and December Statistics data for the Precipitation is also calculated by querying the "hawaii.sqlite" file which indicates that December had 22 inches which is higher than 14 inches of June. This implies the chances of continuous rainfall is low.Temperature is relatively the same without any drastic difference which makes Oahu, Hawaii a good place to invest in a Surf and Ice Cream shop. <br>

![June Temperature and Precipitation](https://github.com/ashwinihegde28/surfs_up/blob/main/Resources/june_temp_precip_summary.PNG) <br> <br>
![December Temperature and Precipitation](https://github.com/ashwinihegde28/surfs_up/blob/main/Resources/dec_temp_precip_summary.PNG) <br> <br>
