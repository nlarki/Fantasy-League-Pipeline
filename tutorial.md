# Tutorial 

## Introduction  
Within this tutorial I plan on explaining how to replicate my envioronment settings, aswell as how to execute the code within the repository. The technologies that have been used for this project are, Prefect, Python, GCP, Terraform, Docker and DBT cloud. It would be advised that you have some basic level understanding of python in order to replicate most of these tasks, however, if youre struggling please reach out. This will be an ever adapting project, with further additional changes in the future to help performance.

## Setting up GCP - 1
To begin with, its advised that you create a GCP account so that you can load the files to both Google Cloud Storage and Big Query later using Python. You can create an account [here](https://cloud.google.com/).
- **Create a new project**
  - Steps:
    1. Go to the [Google Cloud Console](https://console.cloud.google.com/) and sign into your account.
    2. In the top navigation bar, select the project drop-down list and click on the "New Project" button.
     3. Enter a unique name for your project and select the billing account that you want to associate with the project.
    4. Select a location for your project. This location determines the default region for your resources. You can change this later if needed.
    5. Click on the "Create" button to create your project.
  - Notes:
    -  Make sure to keep track of your **projectID** and the **location** for your project
    - You can use an existing project but we strongly recommend for  everyone to create a new project. If you decide to use an existing project make sure your project has the same exact setup/authorization as us.
    - Once you have created your project, you can access it from the Google Cloud Console by clicking navigational bar and selecting your project. From now on, we are assuming your project is selected.
 - **Create a service account**
    - Steps:
      1. Go to GCP main page
      2. In the left-hand menu, click on "IAM & Admin" and then select "Service accounts".
      3. Click on the "Create Service Account" button at the top of the page.
      4. Enter a name for the service account and an optional description.
      5. Select the Viewer role and click continue and done. 
   - Notes:
      - A service account is a special type of account that is used to authenticate applications and services to access GCP resources programmatically. 
      - In GCP A Viewer role grants read-only access to specific GCP resources.
- **Authenticate local environment to cloud**
  - steps:
    1. Go to GCP main page
    2.  In the left navigation menu, click on "IAM & Admin" and then "Service accounts".
    3. Click on the three verticals dots under the action section for the service name you just created. 
    4. Then click Manage keys, Add key, Create new key. Select JSON option and click Create.
    5. Go to your download folder and find the json file. 
    6. Rename the json file to google_credentials.json
        ```bash
          mv ~/Downloads/<xxxxxx.json> ~/Downloads/google_credentials.json
        ```
    7. Create the following path .google/credentials/ in your HOME directory. You can use the command below in a terminal.
          ```bash
         mkdir -p $HOME/.google/credentials/ 
          ```
    8. Move the google_credentials.json file to the directory above
        ```bash
        mv ~/Downloads/google_credentials.json ~/.google/credentials/ 
        ```
    9. Follow the instruction on [here](https://cloud.google.com/sdk/docs/install-sdk) to Download and install GCP SDK on your OS. GCP SDK is a CLI tool that can communicate to GCP services from local environment.
    10. After installation, run the following command to see if you installed GCP SDK correctly:
        ```bash
        gcloud -v
        ``` 
    11. Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of the json file. Use the command bellow:
        ``` bash
        export GOOGLE_APPLICATION_CREDENTIALS="~/.google/credentials/google_credentials.json"
        ```

    12.  Run the command bellow - it will make you sign into your google account and verify the authentication. If all goes well your a google browser will open with the following message displayed: **You are now authenticated with the gcloud CLI!**
            ```bash
            gcloud auth application-default login
            ```

- **Add additional Roles and permission (i.e services)**
  - steps:
    1. Go to GCP main page
    2. In the left-hand menu, click on "IAM & Admin" and then select "IAM". You should see the service account we created in the previous steps and our Viewer role.
    3. On the same row we see our Service account name, click 'edit principal' button which is located in the last column.
    4. Then add the BigQuery Admin, Storage Admin, Storage Object Admin as roles for our service account and click the save button. 
    5. Enable IAM APIs by clicking the following links:
        - [IAM-API](https://console.cloud.google.com/apis/library/iam.googleapis.com)
        - [IAM-credential-API](https://console.cloud.google.com/apis/library/iamcredentials.googleapis.com)
