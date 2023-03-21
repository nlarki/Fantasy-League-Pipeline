# Course Project - FPL ingestion and analysis ⚽

## Overview
The core premise of this project is to showcase what i have learned whilst partaking in the [Data Talks Club Data Engineering course](https://github.com/DataTalksClub/data-engineering-zoomcamp). I will be utilising multiple tools in order to create an effective pipeline that can ingest and manipulate the sourced [FPL](https://github.com/vaastav/Fantasy-Premier-League) data into a finalised visual dashboard. 

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

## Demo of visualisations

gif of visualisation created SAS Visual Analytics:

![alt text](https://github.com/nlarki/FPL_DE_Zoomcamp/blob/main/images/demo.gif)

Home page for visualisation:

![alt text](https://github.com/nlarki/FPL_DE_Zoomcamp/blob/main/images/Capture.PNG)

Overview analysis of all seasons:

![alt text](https://github.com/nlarki/FPL_DE_Zoomcamp/blob/main/images/second.PNG)

Individual team analysis:

![alt text](https://github.com/nlarki/FPL_DE_Zoomcamp/blob/main/images/third.PNG)





