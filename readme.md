



*Remember for repo ssh*
- create the key with -c "your mail"
- start the ssh service
- add the the key *ssh-add*
- setup config in *.ssh* 


## Table of Contents
1. [Project Description](#project-description)
2. [Diagram](#diagram)
3. [Docker Flask App](#docker-flask-app)
4. [Tools for CI/CD: Building and Deploying Docker Images from GitHub to GCP](#tools-for-cicd-building-and-deploying-docker-images-from-github-to-gcp)
5. [Setup Process](#set-up-process)
6. [Conclusions](#conclusions)


## Project Description

This project leverages Cloud Build and Github to create a CI/CD setup.

The setup consist in configuring a trigger in Cloud Build that is configured to detect any push to the main of the repo.

**Technologies used**
- Docker
- CI/CD
- GCP (GKE, Cloud Build)
- Python (Flask)
- CSS
- Containerization

#### Ideally multiple triggers should be configured for various environments, including main, staging, and production branches. 
This ensures that different branches corresponding to development, staging, and production environments can be handled separately
### In the repo we have the following directories:

- *Cloud_Build_config* contains the cloud build [file](https://github.com/franroad/gcp-devops/blob/main/cloud_build_config/cloudbuild.yaml) (used by cloud build for performing the steps)
- *docker_image* contains the [configuration](https://github.com/franroad/gcp-devops/tree/main/docker_image) for building the image.
- *k8s_crd* contains the [file](https://github.com/franroad/gcp-devops/tree/main/k8s_crd) for the deployment using the image and a LB service for exposing the app.

With the current files and configurations the results obtained are the following:

 - Web application using flask deployed in K8's using a Deployment
 - k8's LB service for accessing the web-app
 - CI/CD set up using Cloud Build and GitHub

 ### **Note:** Aservice account is required when creating the trigger. This SA required the following permisisons:
 - ``Cloud Build Service Account``
 - ``Kubernetes Engine Developer``


## Diagram


<img src="https://github.com/franroad/gcp-devops/blob/main/images/cloudbuild_github.drawio%20(1).png" alt="Alt text" title="Optional title">


## Docker Flask app ##

The image used for CI/CD testing  consists a python app using flask and with some  css layer.

- Web Application based on Pyhton with some css
- Will be running in __GKE__


### 1. Local Testing ###

1. Define the Docker-file
2. Build the image  `docker build --tag python-css-flask . `
3. Run the local image `docker run -p local-port:container-port(5000 default-flask) image-name`
4. Acces the container webpage ``http://127.0.0.1:<local-port>``

## Tools for CI/CD: Building and Deploying Docker Images from GitHub to GCP
- ``GitHub`` --> Used for hosting code 
- ``GCP Cloud Build`` --> Used for bulding images and deploying it in k8's based on Github code .
- ``GCP Artifact Registry`` --> Used for storing the created images in GCP

## Set-up Process ##

The following steps describe in a summarized wayh how to link Cloud Build with Github and the files required for deploying and exposing the app in GKE.

**Process**

1. Connect Github with Cloud Build using a *Cloud Build Trigger*. (Installing the Cloud Build Plugin in the GitHub repo)
2. Create/Configure the *Cloud Build Trigger*  based on  and event (in this case based on a push) that trigger the Cloud Build Job.
<img src="https://github.com/franroad/gcp-devops/blob/gke-cloudbuild/images/any_push.png" alt="Alt text" title="Optional title">

3. Create a [*Cloud Build Configuration file*](https://github.com/franroad/gcp-devops/blob/main/cloud_build_config/cloudbuild.yaml) and save it in the repo. This file build the image and push it to the artifact registry, additionally deploy the GKE infra. 
4. Specify where to find the[*Cloud Build Configuration file*](https://github.com/franroad/gcp-devops/blob/main/cloud_build_config/cloudbuild.yaml) when creating the trigger.
<img src="https://github.com/franroad/gcp-devops/blob/gke-cloudbuild/images/path_cloud_build_file.png">

5. Create a ns in Kubernetes where the deployment and the service will be deployed.
6. Create a new branch that will contain the GKE deployment/service files that the trigger will detect when merging with the **main** branch or commit directly to the main branch.
7. Create [*CRD*](https://github.com/franroad/gcp-devops/blob/gke-cloudbuild/k8s_crd/deployment-service.yaml) to deploy the  application and  service in K8's along with building the image via cloud build Job.


## Conclusions

- Cloud build Works seamesly with github and in a quick and responsive way.
- Great Serverless solution.
- Great interface for debugging the Job.
