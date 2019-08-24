# Dog_Depression_Monitor

Google AutoML Vision API is very easy to use with it's drag & drop function on its web. 

However, if you want to scale & automate tasks, you will need to use Terminal/Command Line tool to connect Google AutoML Vision API to your local machine. 

Instead of using my dog pictures taken from Raspberry Pi, I followed full google [instruction](https://cloud.google.com/vision/automl/docs/before-you-begin) to test flower data. 

In the future, Bash scripting in Raspberry Pi to upload a photo every 30 minutes to the Google Cloud Storage bucket. 

Eventually, generating a weekly standing/sitting percentage pie chart, it could indicates the dog depression treatment progress. 

### Introduction - [Presentation](https://www.youtube.com/watch?v=cR2UhljnNu0&t=500s). There is more information on my [LinkedIn](https://www.linkedin.com/in/zezhengjiang/).

You can not run this project because I do not provide my Google Cloud API redentials. 

However, if you create your own API credentials, that's how you would run it.

#### In order to run everything in the folder, you need to have packages listed below. (Python VirtualEnv(such as [PipEnv](https://docs.pipenv.org)) setup is strongly recommended.) #####
    - Python3.7
    - Google Cloud Platform AutoML Vision API Set up: 
        https://cloud.google.com/vision/automl/docs/tutorial?authuser=0
        - GCloud command line tool;
        - client library;

#### In order to run everything in the folder, you need to have extra file named "key-file.json" to identify you as a gcloud administrator. #### 
    - You may download it after setting up in the gCloud "IAM" or "Service Account" section in the Google Cloud Console.  
    - Put it into your working directory

#### In order to run everything in the folder, you need to export global variables. For example, I did: ####
    - export GOOGLE_APPLICATION_CREDENTIALS=key-file.json
    - export PROJECT_ID="automlname-id"
    - export REGION_NAME="us-central1" 
    - export MODEL_ID="ICN7153473003916430375" 

#### In AutoML Vision API Tutorial, "your-userid@your-domain" is your google accoun. ####

#### Resource Management ####
    -"AutoML Vision API Tutorial" -- Terminal Version  https://cloud.google.com/vision/automl/docs/tutorial?authuser=0 
    -AutoML Vision Tutorial -- UI Version https://codelabs.developers.google.com/codelabs/cloud-automl-vision-intro/index.html?index=..%2F..index#0
    -"Preparing your training data" https://cloud.google.com/vision/automl/docs/prepare?authuser=0
    -"Managing data sets" https://cloud.google.com/vision/automl/docs/datasets?authuser=0#create-dataset
    -"Managing models" https://cloud.google.com/vision/automl/docs/models?authuser=0#get-operation

