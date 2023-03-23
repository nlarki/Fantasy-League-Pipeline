
<p align="center">
  <img width="1000" height="400" src="![image](https://user-images.githubusercontent.com/25886776/227315236-88e4730d-7e84-40e0-aada-cf7636f0c217.png)
">
</p>

<h1 style="text-align: center;">Fantasy Premier League data ingestion and analysis ⚽</h1>

## Overview
The core premise of this project is to showcase what i have learned whilst partaking in the [Data Talks Club Data Engineering course](https://github.com/DataTalksClub/data-engineering-zoomcamp). I will be utilising multiple tools in order to create an effective pipeline that can ingest and manipulate the sourced [FPL](https://github.com/vaastav/Fantasy-Premier-League) data into a finalised visual dashboard which you can view [here!](https://viyawaves.sas.com/SASVisualAnalytics/?reportUri=%2Freports%2Freports%2F7b62f8d0-3df5-45d2-ad4d-451bff9aac39&sectionIndex=0&sso_guest=true&reportViewOnly=true&reportContextBar=false&pageNavigation=false&sas-welcome=false) 

## What is Fantasy Premier League
Fantasy Premier league is an [online game](https://fantasy.premierleague.com/#:~:text=With%20over%209%20million%20players,you%20can%20win%20great%20prizes!https://fantasy.premierleague.com/#:~:text=With%20over%209%20million%20players,you%20can%20win%20great%20prizes!) that casts you in the role of a Fantasy manager of Premier League players. You must pick a squad of 15 players from the current Premier League season, who score points for your team based on their performances for their clubs in PL matches.

## Problem description
The project will aim to extract multiple years of FPL data for analysis so that we can take a deeper look into individual stats of players and teams across the 2016 to 2023 seasons. 

Key insights to be extracted:
* Who are the most inform goal scorers
* Who are the most inform assisters
* What players influence their teams the most
* What players have the highest points
* Who are the most expensive players
* How many goals are scored per season

## Technologies
I will use the technolgies below to help with the creation of the project:
* Cloud: GCP
    * Data Lake: GCS
    * Data warehouse: Big Query
* Terraform: Infrastructure as code (IaC) - creates project configuration for GCP to bypass cloud GUI.
* Workflow orchestration: Prefect (docker)
* Transforming data: DBT
* Data Visualisation: SAS Visual Analytics

## Architecture visualised:

<p align="center">
  <img width="400" height="400" src="https://github.com/nlarki/FPL_DE_Zoomcamp/blob/main/images/fpl_arch.png">
</p>


## Dashboard examples

The dashboard allows the user to ingest a highlevel analysis of both players and teams across several seasons in the Barclays Premier League. You can view the dashboard [here](https://viyawaves.sas.com/SASVisualAnalytics/?reportUri=%2Freports%2Freports%2F7b62f8d0-3df5-45d2-ad4d-451bff9aac39&sectionIndex=0&sso_guest=true&reportViewOnly=true&reportContextBar=false&pageNavigation=false&sas-welcome=false)

## Home page for visualisation:

![alt text](https://github.com/nlarki/FPL_DE_Zoomcamp/blob/main/images/Capture.PNG)

## Overview analysis of all seasons:

![alt text](https://github.com/nlarki/FPL_DE_Zoomcamp/blob/main/images/overview.PNG)

## Individual team analysis:

![alt text](https://github.com/nlarki/FPL_DE_Zoomcamp/blob/main/images/player_team.PNG)

## How to run the project

## How to make it work?

1. Clone the repo and install the neccesary packages

```bash
pip install -r requirements.txt
```
2. Next you will want to setup your Google Cloud environment
- Create a [Google Cloud Platform project] if you do not already have one(https://console.cloud.google.com/cloud-resource-manager)
- Configure Identity and Access Management (IAM) for the service account, giving it the following privileges: BigQuery Admin, Storage Admin and Storage Object Admin
- Download the JSON credentials and save it somehwere you'll remember....
- Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install-sdk)
- Let the [environment variable point to your GCP key](https://cloud.google.com/docs/authentication/application-default-credentials#GAC), authenticate it and refresh the session token
```bash
export GOOGLE_APPLICATION_CREDENTIALS=<path_to_your_credentials>.json
gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
gcloud auth application-default login
```
3. Set up the infrastructure of the project using Teeraform
- If you do not have Terraform installed you can install it [here](https://developer.hashicorp.com/terraform/downloads) and then add it to your PATH
- Once donwloaded run the following commands:
```bash
cd terraform/
terraform init
terraform plan -var="project=<your-gcp-project-id>"
terraform apply -var="project=<your-gcp-project-id>"
```
4. Run python code in Prefect folder
- After installing the required python packages, prefect should be installed
- You can setup the prefect server so that you can access the UI using the command below:
```bash
prefect orion start
```
- access the UI at: http://127.0.0.1:4200/
- You will then want to change out the blocks so that they are registered to your credentials for GCS and Big Query. This can be done in the Blocks options
- You can keep the blocks under the same names as in the code or change them. If you do change them make sure to change the code to reference the new block name
- Go back to the terminal and run:
```bash
cd flows/
python etl_gcs_player.py
```
- The data will then be stored both in your GCS bucket and in Big Query
- If you want to run the process in Docker you can run the commands below:
```bash
cd Prefect/
docker image build -t <docker-username>/fantasy:fpl .
docker image push <docker-username>/fantasy:fpl
```
- the docker_deploy.py will load the flows into deployment area of prefect so that they can then be run directly from your container.
```bash
cd flows/
python docker_deploy.py
```
- will start the agent to listen for job flows to run
```bash
prefect agent start
```
- run the containerized flow from CLI:
```bash
prefect deployment run etl-parent-flow/docker_player_flow --param yr=[16,17,18,19,20,21,22] --param yrs=[17,18,19,20,21,22,23]"
```
5. Running the dbt flow
- Create a dbt account and log in using dbt cloud [here](https://cloud.getdbt.com/)
- Once logged in clone the repo for use 
- in the cli at the bottom run the following command:
```bash
dbt run
```
- this will run all the models and create our final dataset "final_players"
- final_players will then be placed within the schema chosen when setting up the project in dbt.

6. How the lineage should look once run:
![alt text](https://github.com/nlarki/FPL_DE_Zoomcamp/blob/main/images/lineage.PNG)

7. Visualisation choices
- You can now take the final_players dataset and use it within Looker or another data visualisation tool like SAS VA which i used.










