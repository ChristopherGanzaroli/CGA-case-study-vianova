# Case study


We want to know the __countries that don't host a megapolis__


The purpose of this exercice is to evaluate your skills in Python and SQL. You'll have to fork this repository and write a program that fetch the [dataset of the population of all cities in the world](https://public.opendatasoft.com/explore/dataset/geonames-all-cities-with-a-population-1000/export/?disjunctive.cou_name_en), stores it in a database, then perform a query that will compute: what are the countries that don't host a megapoliss (a city of more than 10,000,000 inhabitants)? 

The program will save the result (country code and country name) as a tabulated separated value file, ordered by country name. 

You should answer as if you were writting production code within your team. You can imagine that the program will be run automatically every week to update the resulting data.

Please send us the link to your github repository with the answer of the exercise. 



## Requirements

Dowload  Vscode

Dowload sqlite3 plugin in Vscode

Dowload python

## Schema

Directories are organised into several branches :

Class : contains scripts for connecting to the database and retrieving data from the API (10 000 rows constraint from https://public.opendatasoft.com/explore/dataset/geonames-all-cities api)

DB: contains the database and execution scripts

- ALD : contains the table feed script
- EXP : contains the script for exporting data table
- INSTALL : contains the table installation script

DATA : contains all data exported from the EXP directory and manually imported data

## Result

```bash
CreateTable_cities_pop.py
```
![db_sql](https://github.com/ChristopherGanzaroli/CGA-case-study-vianova/assets/60617045/ac5e1f71-b2f2-4f30-b629-161f2845a9fb)



```bash
AlimTable_cities_pop.py
```
![case_study_all](https://github.com/ChristopherGanzaroli/CGA-case-study-vianova/assets/60617045/a3ec7b35-342c-45de-b652-1a71270fe2d5)

```bash
main.py (export response.csv file)
```
![case_study_res](https://github.com/ChristopherGanzaroli/CGA-case-study-vianova/assets/60617045/4d69b587-8f18-4122-afb0-48c51507b285)

 
