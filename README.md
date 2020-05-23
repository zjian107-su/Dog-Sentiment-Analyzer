# **Dog Depression Monitor**

## **Backgrond**

This [Presentation](https://www.youtube.com/watch?v=cR2Uhl·jnNu0&t=500s) explains more details about this project. There is more information on my [LinkedIn](https://www.linkedin.com/in/zezhengjiang/).

We all love pets. Some dogs suffer from separation anxiety/depression. Some dogs suffer from medical issues that cause unstoppable stress. Daniel wants to build a device that implements machine learning programs and keeps track of a dog's anxiety issue treatment. 

Assuming an anxious or depressed dog has more standing or laying time, we may see the treatment progress by identifying body posture and calculate time.

### Problem to be solved
Uploading images to build and train a machine learning model is necessary.

Google AutoML Vision API is easy to use with its drag & drop function on its web. However, if you want to scale and automate tasks, you will need the Terminal/Command Line tool to connect Google AutoML Vision API to your local machine. 

Instead of using my dog pictures taken from a Raspberry Pi, I followed the [full google instruction](https://cloud.google.com/vision/automl/docs/before-you-begin) to test with flower data. 

***I am using flower type recognition model to simulate how it could potentially work in dog depression progress track**

## Introduction

You can not run this project because I do not provide my Google Cloud API credentials. 

### Prerequisite
- [full google instruction](https://cloud.google.com/vision/automl/docs/before-you-begin)
- A traind model that can distinguish flower type
- Python3.7.x
- Python [Pipenv](https://pipenv.pypa.io/en/latest/) package 
- [Google Cloud Platform AutoML Vision API Setup](https://cloud.google.com/vision/automl/docs/tutorial?authuser=0) 
    - GCloud command line tool;
    - client library;

#### In order to run everything in the folder, you need to export global variables. For example, Daniel did: ####
```bash
$ export GOOGLE_APPLICATION_CREDENTIALS=key-file.json
$ export PROJECT_ID="automlname-id"
$ export REGION_NAME="us-central1" 
$ export MODEL_ID="ICN7153473003916430375" 
```

**In AutoML Vision API Tutorial, "your-userid@your-domain" is your google account.**

#### Resource Management ####
- **[AutoML Vision API Tutorial -- the Terminal Version](https://cloud.google.com/vision/automl/docs/tutorial?authuser=0)**   

- **[AutoML Vision Tutorial -- the UI Version](https://codelabs.developers.google.com/codelabs/cloud-automl-vision-intro/index.html?index=..%2F..index#0)**  

- **[Preparing your training data](https://cloud.google.com/vision/automl/docs/prepare?authuser=0)** 

- **[Managing data sets](https://cloud.google.com/vision/automl/docs/datasets?authuser=0#create-dataset)**

- **[Managing models](https://cloud.google.com/vision/automl/docs/models?authuser=0#get-operation)**

## Screenshots 
**Data**

![data](https://user-images.githubusercontent.com/35544956/82737677-989c9b00-9ce7-11ea-894b-8396a33f3831.jpg)

**Graph**

![graph](https://user-images.githubusercontent.com/35544956/82737943-2af16e80-9ce9-11ea-99ef-0f2c5a4194b0.jpg)

## Future Outlook
Potentional improvement:    
- Writing Bash scripting to upload a photo every 30 minutes from a Raspberry pi to the Google Cloud Storage bucket. 

Eventually, the code should generate a weekly standing/sitting percentage pie chart, which indicates the dog depression treatment progress. 

## Award 
Earned “CuseHack2019 Best Rookie” award at Syracuse University Hackathon

![demo](https://user-images.githubusercontent.com/35544956/82737584-e8c72d80-9ce6-11ea-97ad-406da0aa8c4a.jpg)

