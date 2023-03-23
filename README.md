# Course Project - FPL ingestion and analysis ⚽

## Overview
The core premise of this project is to showcase what i have learned whilst partaking in the [Data Talks Club Data Engineering course](https://github.com/DataTalksClub/data-engineering-zoomcamp). I will be utilising multiple tools in order to create an effective pipeline that can ingest and manipulate the sourced [FPL](https://github.com/vaastav/Fantasy-Premier-League) data into a finalised visual dashboard which you can view [here!](https://viyawaves.sas.com/SASVisualAnalytics/?reportUri=%2Freports%2Freports%2F7b62f8d0-3df5-45d2-ad4d-451bff9aac39&sectionIndex=0&sso_guest=true&reportViewOnly=true&reportContextBar=false&pageNavigation=false&sas-welcome=false) 

## What is Fantasy Premier League
Fantasy Premier league is an [online game](https://fantasy.premierleague.com/#:~:text=With%20over%209%20million%20players,you%20can%20win%20great%20prizes!https://fantasy.premierleague.com/#:~:text=With%20over%209%20million%20players,you%20can%20win%20great%20prizes!) that casts you in the role of a Fantasy manager of Premier League players. You must pick a squad of 15 players from the current Premier League season, who score points for your team based on their performances for their clubs in PL matches.

## Problem description
The project will aim to extract multiple years of FPL data for analysis so that we can take a deeper look into individual  stats of players and teams across the 2016 to 2023 seasons. 

Key goals of the project are:
* Develop a data pipeline that will help to organize data processing in a batch manner (on a yearly basis);
* Build analytical dashboard that will make it easy to discern the trends and digest the insights.

## Technologies
I will use the technolgies below to help with the creation of the project:
* Cloud: GCP
    * Data Lake: GCS
    * Data warehouse: Big Query
* Terraform: Infrastructure as code (IaC) - creates project configuration for GCP to bypass cloud GUI.
* Workflow orchestration: Prefect (docker)
* Transforming data: DBT
* Data Viz: SAS Visual Analytics

## Design architecture
<img src="https://github.com/nlarki/FPL_DE_Zoomcamp/blob/main/images/fpl_arch.png" width="600" height="400">

## Dashboard of visualisations

The dashboard allows the user to ingest a highlevel analysis of both players and teams across several seasons in the Barclays Premier League. You can view the dashboard [here](https://viyawaves.sas.com/SASVisualAnalytics/?reportUri=%2Freports%2Freports%2F7b62f8d0-3df5-45d2-ad4d-451bff9aac39&sectionIndex=0&sso_guest=true&reportViewOnly=true&reportContextBar=false&pageNavigation=false&sas-welcome=false)

Home page for visualisation:

![alt text](https://github.com/nlarki/FPL_DE_Zoomcamp/blob/main/images/Capture.PNG)

Overview analysis of all seasons:

![alt text](https://github.com/nlarki/FPL_DE_Zoomcamp/blob/main/images/overview.PNG)

Individual team analysis:

![alt text](https://github.com/nlarki/FPL_DE_Zoomcamp/blob/main/images/player_team.PNG)








