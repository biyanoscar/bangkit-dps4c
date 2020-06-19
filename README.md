# Aksara Jawa Classification Application
Final Project Bangkit Denpasar

### DPS4-C Group
1. Biyan Oscar
2. Ni Luh Ayu Sonia Ginasari

#### Improved Model
The process of making the Tensorflow model can be seen in [Model CNN Aksara Jawa Improved](aksara_DPS4C_CNN_Improved.ipynb)

### Duplicate the web app source code
- The web application source code is on [deploy_aksara](deploy_aksara/) folder
- To using this app on local machine, run app using this command to start Flask API
```
python main.py
```
The application will run on port 5000.

- Navigate to URL http:/127.0.0.1:5000


### Deploying web app to Google App Engine
1. Create a Google Cloud account

2. On local computer, install the gcloud SDK/CLI

3. Install the App Engine extension
```
gcloud components install app-engine-python
```

4. Set the project as your gcloud default with this command:
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

