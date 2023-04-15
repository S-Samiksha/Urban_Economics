### Urban Economics Project

This project was taken as part of the HE3613 Urban Economics Course. While the main aspect of this project was to focus on finding factors that affect HDB Resale Prices in Singapore, our group decided to explore further and use machine learning techniques to predic the HDB resale prices. 

##### Aim
With the introduction of new urban planning policies and the rising rate of housing ownership, it is essential to understand how housing prices in Singapore are affected by such changes. This study aims to investigate theoretical factors, such as distance of a HDB flat from the central business district (CBD) and floor area of the house, on housing resale prices. From here on, when we refer to prices, it refers to HDB resale prices. Furthermore, it aims to analyze additional factors such as distance from Mass Rapid Transit (MRT) and remaining lease period and how it affects the prices. 

#### Data Cleaning 
Most of the Data Cleaning was done using Python3 and the codes are available in this repository. 

Data used was obtained from 3 primary sources:
`Data.gov.sg` <br>
This is the government’s official website for datasets collected from various government agency. The dataset of interest is ‘Resale flat prices based on registration date from Jan-2017 onwards’, located at https://data.gov.sg/dataset/resale-flat-prices. The dataset used was a compilation of 111,027 HDB resale transactions recorded between January 2017 and September 2020.

`OpenStreetMaps API` <br>
OpenStreetMaps API is an open-source mapping software that allows users to perform routing operations given starting and ending points. This is used to generate driving distances, for HDB to CBD and for HDB to the nearest MRT. 

`LTA Bus Stop Dynamic API` <br>
The LTA official website was used to obtain the number of bus stops. The website is located at: https://datamall.lta.gov.sg/content/datamall/en/dynamic-data.html. Using latitude and longitude, a radius of 200m was calculated. The number of bus stops falling within the 200m radius was calculated. 

#### Analysis using OLS regressions 
For this analysis a mix of STATA and Python3 were used. Only Python3 Codes are avaialble in this repository. Check out the folder OLS Analysis!

#### Simple Machine Learning Using Random Forest

Out of curiosity and as an extension, our team decided to explore machine learning to help predict housing prices. For machine learning purposes, we chose to use the Executive Central Dataset. 

A supervised learning model called Random Forest. It uses an ensemble of decision trees  to help make predictions.



