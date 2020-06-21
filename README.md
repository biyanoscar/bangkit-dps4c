<h1 align="center">Welcome to Aksara Jawa Classification Application!</h1>
![Aksara Jawa apps](https://user-images.githubusercontent.com/42605366/85228458-b572de00-b40d-11ea-8fda-47369983bcab.jpg)


Final Project Bangkit Denpasar

### DPS4-C Group
1. Biyan Oscar
2. Ni Luh Ayu Sonia Ginasari


### Overview
This application is a classification of Aksara Jawa based on the results of Javanese script pattern of users that have been provided on the application and will be searched for the pronunciation of the script.
You can access application on https://bangkit-dps4-c-0001.uc.r.appspot.com/

### Improved Model
Our dataset are taken from kaggle https://www.kaggle.com/phiard/aksara-jawa

The process of making the Tensorflow model can be seen in [Model CNN Aksara Jawa Improved](aksara_DPS4C_CNN_Improved.ipynb). After make model, we export it so we create app that use that model.

**Improved result:**
- The model is small in size
- Accuracy is high, it is 96.9%


### Web App source code
- First you can clone the source code. The web application source code is on [deploy_aksara](deploy_aksara/) folder
- Export models from notebooks are placed in the folder [deploy_aksara/model/](deploy_aksara/model/)
- To using this app on local machine, run app using this command to start Flask API
```
python main.py
```
The application will run on port 5000.

- Navigate to URL http:/127.0.0.1:5000


### Deploying web app to Google App Engine
For this project we use Google App Engine. Following are the steps taken to deploy our source code.
1. Create a Google Cloud account

2. On local computer, install the gcloud SDK/CLI

3. Install the App Engine extension
    ```
    gcloud components install app-engine-python
    ```

4. Set the project as your gcloud default with this command. Change MY-PROJECT-ID according to your respective PROJECT-ID
    ```
    gcloud config set project MY-PROJECT-ID
    ```

5. Enable the Cloud Build API
    ```
    gcloud services enable cloudbuild.googleapis.com
    ```

6. Initialize App Engine for our project
    ```
    gcloud app create --project=MY-PROJECT-ID
    ```

7. Deploy to App Engine
    ```
    gcloud app deploy
    ```

