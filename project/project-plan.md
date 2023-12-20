# Project Plan

## Title
<!-- Give your project a short title. -->
The Great Cricket Conundrum

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
Who are statistically the best batsman and bowler in the 20-20 format of the game?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
In this data science project, I aim to determine the statistically best batsman and bowler in the 20-20 format of cricket, leveraging two comprehensive datasets: the Ball-by-ball data for International Men's Cricket Matches (2003 - 2023) and the Indian Premier League match data (2008 - 2023). As a cricket enthusiast from South Asia, particularly India, I'm passionate about resolving the age-old debate of identifying the greatest players in this format.

The project involves transforming the raw data from JSON to CSV format, followed by meticulous data cleaning and feature engineering. Through extensive exploratory data analysis (EDA), I intend to uncover significant trends and patterns related to the game. By employing advanced statistical methods and machine learning techniques, I will evaluate player performance metrics such as batting average, strike rate, economy rate, and wicket-taking ability.

By answering the fundamental question, "Who is statistically the best batsman and bowler in the 20-20 format of the game?" with rigorous statistical backing, this project not only settles a perennial debate but also provides valuable insights into player performance, contributing to the broader understanding of cricket statistics and player rankings. The findings can potentially influence team strategies, player selections, and fan perceptions, making it a vital analysis for cricket enthusiasts and professionals alike.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefix "DatasourceX" where X is the id of the datasource. -->
Following 2 datasets will be used in the project:

### Datasource1: Men's T20 internationals
<!-- * Metadata URL: https://mobilithek.info/offers/-6901989592576801458 -->
* Data URL: https://cricsheet.org/downloads/t20s_male_json.zip
* Data Type: JSON
  
Dataset contains JSON files with ball by ball data of matches, with details like, batsmen, bowler, dismissal, dismissal method etc.

### Datasource2: IPL Matches
<!-- * Metadata URL: https://mobilithek.info/offers/-6901989592576801458 -->
* Data URL: https://cricsheet.org/downloads/ipl_male_json.zip
* Data Type: JSON

Dataset contains JSON files with ball by ball data of matches, with details like, batsmen, bowler, dismissal, dismissal method etc.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Use Pandas and other visualization tools for analysis. [#3][i3]

[i3]: https://github.com/vaishnavnegi/made-Vaishnav-Negi-23114574/issues/3
