# Course Project - FPL ingestion and analysis ⚽

## Overview
The core premise of this project is to showcase what i have learned whilst partaking in the [Data Talks Club Data Engineering course](https://github.com/DataTalksClub/data-engineering-zoomcamp). I will be utilising multiple tools in order to create an effective pipeline that can ingest and manipulate the sourced [FPL](https://github.com/vaastav/Fantasy-Premier-League) data into a finalised visual dashboard which you can view [here!](https://viyawaves.sas.com/SASVisualAnalytics/?reportUri=%2Freports%2Freports%2F92b11cd0-8cc9-4392-9023-d0d0bdaf5341&sectionIndex=0&sso_guest=true&reportViewOnly=true&reportContextBar=false&pageNavigation=false&sas-welcome=false) 

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

![alt text](https://github.com/nlarki/FPL_DE_Zoomcamp/blob/main/images/fpl_arch.png)

## Dashboard of visualisations

The dashboard allows the user to ingest a highlevel analysis of both players and teams across several seasons in the Barclays Premier League. You can view the dashboard [here](https://viyawaves.sas.com/SASVisualAnalytics/?reportUri=%2Freports%2Freports%2F92b11cd0-8cc9-4392-9023-d0d0bdaf5341&sectionIndex=0&sso_guest=true&reportViewOnly=true&reportContextBar=false&pageNavigation=false&sas-welcome=false)

Home page for visualisation:

![alt text](https://github.com/nlarki/FPL_DE_Zoomcamp/blob/main/images/Capture.PNG)

Overview analysis of all seasons:

![alt text](https://github.com/nlarki/FPL_DE_Zoomcamp/blob/main/images/overview.PNG)

Individual team analysis:

![alt text](https://github.com/nlarki/FPL_DE_Zoomcamp/blob/main/images/player_team.PNG)








