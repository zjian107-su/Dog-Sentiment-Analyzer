# Dog Depression Monitor

## Background
The Dog Depression Monitor is a machine learning project aimed at monitoring a dog's anxiety issue treatment. This project utilizes body posture to track the dog's progress, assuming that an anxious or depressed dog has more standing or laying time. To build and train the machine learning model, images need to be uploaded. Google AutoML Vision API is used for this purpose, which has a user-friendly drag & drop function on its web platform. However, to scale and automate tasks, one needs to connect Google AutoML Vision API to the local machine through the Terminal/Command Line tool.

## Introduction
This project cannot be run as the author does not provide Google Cloud API credentials. However, the project's code can be analyzed to understand how it could potentially work to track a dog's depression progress. 

### Prerequisite
- Python3.7.x
- Python Pipenv package 
- A trained model that can distinguish flower type
- [Google Cloud Platform AutoML Vision API Setup](https://cloud.google.com/vision/automl/docs/tutorial?authuser=0) 
    - GCloud command line tool;
    - client library;

In order to run everything in the folder, global variables need to be exported. For example:
```bash
$ export GOOGLE_APPLICATION_CREDENTIALS=key-file.json
$ export PROJECT_ID="automlname-id"
$ export REGION_NAME="us-central1" 
$ export MODEL_ID="ICN7153473003916430375" 
```

#### Resource Management ####
- **[AutoML Vision API Tutorial -- the Terminal Version](https://cloud.google.com/vision/automl/docs/tutorial?authuser=0)**   
- **[AutoML Vision Tutorial -- the UI Version](https://codelabs.developers.google.com/codelabs/cloud-automl-vision-intro/index.html?index=..%2F..index#0)**  
- **[Preparing your training data](https://cloud.google.com/vision/automl/docs/prepare?authuser=0)** 
- **[Managing data sets](https://cloud.google.com/vision/automl/docs/datasets?authuser=0#create-dataset)**
- **[Managing models](https://cloud.google.com/vision/automl/docs/models?authuser=0#get-operation)**

## Screenshots 
### Post
<img src="https://user-images.githubusercontent.com/35544956/236985376-9035958b-2cef-4890-9d38-fab9284c5137.jpg" alt="Monday_Presentation - G AutoML" width="500">

### Data
![data](https://user-images.githubusercontent.com/35544956/82737677-989c9b00-9ce7-11ea-894b-8396a33f3831.jpg)

### Graph
![graph](https://user-images.githubusercontent.com/35544956/82737943-2af16e80-9ce9-11ea-99ef-0f2c5a4194b0.jpg)

## Future Outlook
An improvement to the project could be achieved by writing Bash scripting to upload a photo every 30 minutes from a Raspberry pi to the Google Cloud Storage bucket. Eventually, the code should generate a weekly standing/sitting percentage pie chart that indicates the dog depression treatment progress. 

## Award 
This project earned the “CuseHack2019 Best Rookie” award at Syracuse University Hackathon, with some help from [Chris Chomicki](https://github.com/rahombus97).

![demo](https://user-images.githubusercontent.com/35544956/82737584-e8c72d80-9ce6-11ea-97ad-406da0aa8c4a.jpg)
