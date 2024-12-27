
*Remember for repo ssh*
- create the key with -c "your mail"
- start the ssh service
- add the the key *ssh-add*
- setup config in *.ssh* 


## Docker Flask app ##

This project consists in the python app using flask and with a fancy  css layer.

- Web Application based on Pyhton with some css
- Will be running in __GKE__


### 1. Local Testing ###

1. Define the Docker-file
2. Build the image  `docker build --tag python-css-flask . `
3. Run the local image `docker run -p local-port:container-port(5000 default-flask) image-name`
4. Acces the container webpage ``http://127.0.0.1:<local-port>``

### Tools for CI/CD: Building and Deploying Docker Images from GitHub to GCP ###
- ``GitHub`` --> Used for hosting code 
- ``GCP Cloud Build`` --> Used for bulding images and deploying it in k8's based on Github code .
- ``GCP Artifact Registry`` --> Used for storing the created images in GCP

### 2. Deploying into GKE ###

**Process**

1. Connect Github with Cloud Build using a *Cloud Build Trigger*.
2. Create/Configure the *Cloud Build Trigger*  based on  and event (could be a push to the branch) and trigger the Cloud Build Job.
3. Specify where to find the *Cloud Build Configuration file* when creating the trigger.
4.  Create a [*Cloud Build Configuration file*](https://github.com/franroad/gcp-devops/blob/main/cloud_build_config/cloudbuild.yaml) and save it in the repo. This file should be referenced in step (2)
5. Create a new branch that will contain the GKE deployment/service files that the trigger will detect when merging with the **main** branch
6. Create a ns in Kubernetes where the deployment and the service will be created


# TO-DO:
 1. **Explain** the css stuff.
 2. **Explain** cloudbuild, gke , gcp , github interaction.
 3. **Create** The diagram.

### Example image
 <img src="https://github.com/franroad/azure/blob/main/PRAC_2.drawio(2).png" alt="Alt text" title="Optional title">