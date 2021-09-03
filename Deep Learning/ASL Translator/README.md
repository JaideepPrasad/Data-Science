# ASL Translator

The following is built on top of my [ASL Object Detection](https://github.com/JaideepPrasad/Data-Science/tree/main/Deep%20Learning/ASL%20Object%20Detection) project. If you would like to know more about the object detection model, check out that project.

### Overview

So we now have an odject detection model that detects American Sign Language (ASL). Let's take this to the next level. We will make a Flask application that allows you to access the ASL object detection model

### Wants and Haves

So originally I wanted this Flask app to be sort of a full product however due to time constricts, this is still a working progress.
<br>
<br>
I wanted the Flask app to:
- have a landing page and associated web pages
- make my model run on the webpage
- convert the detected signs to text
- parse the text to make sentences
- display all of letters/sentences
- convert the sentences to text to speech
- create a docker image of my Flask app and post it on Github and Docker Hub
- run the docker image on a server (cloud or Heroku) so anyone can call the Flask web page via internet

However I have:
- the web pages
- model running on my webpage
- convert the detected sign to text
- display the letters

Here is a demo of what I have so far:

https://user-images.githubusercontent.com/32663193/132054323-7309be5c-4279-4712-9e4e-5516c0630d25.mp4


### Files

- App.py is the main file you want to run as it contains the Flask code. <br>
- Helper.py is mainly responsible for the object detection code. If you know about the [ASL Object Detection](https://github.com/JaideepPrasad/Data-Science/tree/main/Deep%20Learning/ASL%20Object%20Detection) project, we are using the CenterNet model. <br>
- The templates folder contains the custom html pages. The base html template was found by clicking [here](https://startbootstrap.com/theme/grayscale). <br>
- The static folder has all the other stuff from the model and it's label map to the images, js and css code. <br>
- The tfod.yml is the environment I used to run the code, in case anyone wants to run the code locally. To install and activate the environment, click [here](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) for the requires steps.

### Process

The process was stright forward. While I had to learn new skills such as Flask, html, css and AJAX, google helped me out quite a bit. On a high level Flask was used to build the webpage and I used bootstrap to edit a website template as I am not a frontend developer. AJAX was used to display the detected text under the camera. To parse the letters into a sentence, I plan on using [wordninja](https://github.com/keredson/wordninja). For the text to speeck I remember using a gogole api library however I need to dog though previous projects or do a bit more research.

### Issues

There are a few that I am stuck on right now. So the easiest one is the make the text under the camera look nice. For the text to speech section, I'm goning to have to research how to play audio files using html, as I plan on making the user click on a button and then the text gets processed into audio and then displayed to the user via speakers. But I think the biggest problem right now is Docker. I am using a conda environment right now and am struggling to make the Dockerfile for the docker image. I tried making a normal environment but ran into depenacy hell so I either need to research a bit more or spend time making a regualr environment.

These are the things I have currently done and am facing. This project is not done and I simply am posting this so I can pick up where I left off and have some sort of documentation.
