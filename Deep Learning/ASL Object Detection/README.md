# ASL Object Detection

### Problem Statement:

The goal for this project is to make an object detection model that can recognize American Sign Language (ASL) alphabets.  We plan on creating a mobile android app that will be 
able to detect ASL, understand the alphabets we want to say and convert them into sentences. From here we would like to incorporate text to speech so we have a sort of google 
translate app from ASL to any language. In the future there will be a few issues we face such as potentially incorporating the object detection model into an android app due to 
hardware limitations, [accurately representing ASL as it is common for one hand action/sign to represent a word rather than an alphabet](https://www.handspeak.com/word/search/index.php?id=1017), and converting alphabets to 
grammatically correct sentences with spaces and punctuation. All of this however is for the future, as mentioned above the goal of this project is to detect ASL alphabets, and 
a proof of concept to see what can be possible for the future.    

### Dataset:

The dataset we are using is called [American Sign Language Letters Dataset V1 from Roboflow](https://public.roboflow.com/object-detection/american-sign-language-letters/1). 
This dataset comes with a training, validation, and test dataset. Along with this every object in all the images are annotated in various formats such as csv and tfrecords. 
The images are all 416x416 with augmentations such as horizontal flips, crops, rotation, shear, grayscale, brightness, and blur. The training dataset has 1512 images, validation
has 144 images, and the test dataset has 72 images however for the purpose of this project we only used the train and test dataset. There are 26 classes (one for each alphabet 
in the English language) with diverse characteristics per images as seen below:

|   | H | O | W |	 	 	 
|---|---|---|---|
| Train | ![image](https://user-images.githubusercontent.com/32663193/128615225-3fd64201-8300-428b-90e4-0e3f33e29d6a.png) | ![image](https://user-images.githubusercontent.com/32663193/128615230-960d1cd4-aecb-4f0f-8245-659ec3a34893.png) | ![image](https://user-images.githubusercontent.com/32663193/128615234-f8d7847e-9bbc-47cf-9c8b-fc7873b3a39c.png) |
| Test | ![image](https://user-images.githubusercontent.com/32663193/128615239-5c7d61d0-7daa-48bb-8048-b7bc6ae42b8b.png) | ![image](https://user-images.githubusercontent.com/32663193/128615242-14687b0c-b9bc-4bd8-9cd4-4b48546239ab.png) | ![image](https://user-images.githubusercontent.com/32663193/128615241-426f7255-208b-4fc0-902e-8a71571022a7.png) | 
			
Originally, we thought it would be a good idea to grayscale every image to reduce potential bias from skin tones and designate a region of interest (ROI) on the screen 
(such as a box in the bottom left of the screen) where we would allow signs to show up. However, we wanted to benchmark the data as it is in order to see how effective 
the changes above and some other would be. Due to time constraints, we did not get a chance to test these out however, we do plan on exploring these topics in the future 
based on the evaluations of our models.

### Models:

The 3 models used in this project were imported from the [TensorFlow 2 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md).
These are prebuilt neural network architectures that have been optimized for general cases and benchmarked based on speed and mean average precision (mAP) on the COCO 2017 
dataset. The models we used are the following:

| Model |	COCO Speed (ms) |	COCO mAP	Reason |
|-------|-----------------|------------------|
| Faster R-CNN ResNet152 V1 1024x1024 |	72 |	37.1 |	Try something semi fast, semi accurate |
| SSD MobileNet V2 FPNLite 640x640 |	39 |	28.2 |	Try a MobileNet as they are meant for mobile devices |
| CenterNet MobileNetV2 FPN 512x512 |	6 |	23.4 |	Try something very fast |

### Results:

##### Faster R-CNN ResNet152 v1 1024x1024:

The first model we trained was the Faster R-CNN model however this model proved to be the most troublesome. Due to hardware limitations, we had to train our model using a batch 
size of 1 which made the training process long. Originally, we planned on training the model over night for 22680 steps however after looking at the results, we ended up getting
null for our loss.

![image](https://user-images.githubusercontent.com/32663193/128615384-bc82120d-5db9-4bd6-a06b-f4afef3240c6.png)

We thought this could be due to exploding or vanishing gradient as we believe there is no gradient clipping in the Faster R-CNN model. This could also be due to the Faster R-CNN
not using regularization in its default architecture. Due to the long time it takes to train the Faster R-CNN, we wanted to train the model for 5000 steps as it seems somewhat 
stable till then, the idea being we will see how good the model was before getting nulls and then troubleshoot the model after trying all the other models. While we trained the
model with 5000 steps, we unfortunately did not have enough time to troubleshoot the model. Below are the results for the faster R-CNN model that trained on 5000 steps:

Faster RCNN Results
|  |
|---|
| ![image](https://user-images.githubusercontent.com/32663193/128615391-11af3aae-e19b-43d9-8161-3c48dcfa3a92.png) |
| ![image](https://user-images.githubusercontent.com/32663193/128615392-ae3513ff-c2be-4b6b-a6a9-a6e0362fb6f3.png) | 
| ![image](https://user-images.githubusercontent.com/32663193/128615399-6de7914c-80eb-489a-ae1b-9fbf5ef954d5.png) |

Faster RCNN Predictions

| | |
|---|---|
| ![image](https://user-images.githubusercontent.com/32663193/128615432-d0a4af20-131f-4bfa-9e56-0586922da591.png) | ![image](https://user-images.githubusercontent.com/32663193/128615435-1ea1fc77-57a1-4a27-a60e-da1d658ca9d3.png) |
| ![image](https://user-images.githubusercontent.com/32663193/128615455-68b306b0-27d0-418e-bf1c-4d81d6bfe287.png) | ![image](https://user-images.githubusercontent.com/32663193/128615451-63a4788f-ec66-4dba-bc1e-b88126920d07.png) |

When we look at the loss for this model, it seems erratic and unstable. It is clear that the train process needs to continue for a munch longer time. 
Both the mean average precision (mAP) and mean average recall (mAR) are both at zero meaning the model does not have any true positives. 
This claim is also backed up when looking at the predictions the model made. Though we show a very small subset of predictions, the model did not make any predictions on any 
of the test data images. It is clear that the results of this project does not accurately represent Faster R-CNN and needs more attention during the future of this project.

##### SSD MobileNet V2 FPNLite 640x640:

The second model we trained was a MobileNet SSD model which ran smoothly and as expected. Below are the results for the MobileNet SSD model that trained on 50,000 steps:

SSD Results
|  |
|---|
| ![image](https://user-images.githubusercontent.com/32663193/128615517-502f8b33-a3ce-4375-b8b5-fb503abbb688.png) |
| ![image](https://user-images.githubusercontent.com/32663193/128615521-98ee0458-5026-4af4-8ef5-caeb39128c91.png) | 
| ![image](https://user-images.githubusercontent.com/32663193/128615523-87ddb5f5-6f7f-43e3-a5fa-41094ba7fae8.png) |

SSD Predictions

| | |
|---|---|
| ![image](https://user-images.githubusercontent.com/32663193/128615527-288255fe-704d-4094-8ccb-a940a81cab4f.png) | ![image](https://user-images.githubusercontent.com/32663193/128615531-79f98614-b158-4707-ba48-77d5d94f1f9d.png) |
| ![image](https://user-images.githubusercontent.com/32663193/128615535-36e7de18-5e7a-4930-96c1-9054f93bcdba.png) | ![image](https://user-images.githubusercontent.com/32663193/128615537-d9e3e3cf-f607-42a4-ad1e-3256aaaaa500.png) |

We notice that the loss seems to have stabilized as it seems to plateau, informing us that 50,000 steps was the way to go. While this model is light and quick to train, 
we can train it for 10,00 more steps to be sure the model learned whatever it could though it seems unnecessary at this point. While the training loss seems to be low 
(the orange curve) sitting at approximately 0.12, it’s important to note that the evaluation loss (the blue dot) seems to be higher than we like sitting at approximately 0.37. 
It also looks like the mAP and mAR are pretty high approximately sitting at 0.75 and 0.8 respectively. This means that 75% of the model’s predictions are true positives rather 
than false positives and 80% of the model’s predictions are true positives rather than false negatives, all great signs. When we take a look at the predictions the model made,
pretty much every image has a prediction and most of them are the correct prediction. In the subset above we see that all the images have a prediction and only one of the images
is misclassified.

##### CenterNet MobileNet V2 FPN 512x512:

The last model we trained was a MobileNet CenterNet model which ran smoothly and as expected. Below are the results for the MobileNet CenterNet model that trained on 53,000 
steps:

CenterNet Results
|  |
|---|
| ![image](https://user-images.githubusercontent.com/32663193/128615564-76189aeb-0922-4405-8b5b-be9095387272.png) |
| ![image](https://user-images.githubusercontent.com/32663193/128615568-37ee5b03-f2ab-4066-9b27-1eec1540b12a.png) | 
| ![image](https://user-images.githubusercontent.com/32663193/128615574-220a19ef-3e65-4fed-b2d8-c93a431ce510.png) |

CenterNet Predictions

| | |
|---|---|
| ![image](https://user-images.githubusercontent.com/32663193/128615580-c775a538-e60b-43e0-8c54-42b9a4cf8998.png) | ![image](https://user-images.githubusercontent.com/32663193/128615592-d357ae74-c352-464c-a631-ef8bbc4463fa.png) |
| ![image](https://user-images.githubusercontent.com/32663193/128615585-b3fb258c-e392-4f8c-9608-50389d6ae80a.png) | ![image](https://user-images.githubusercontent.com/32663193/128615597-26aa2dad-2ebc-4e10-a729-655b8d54feb1.png) |

Looking at the loss graph, it seems like training the model for a bit longer would be advised but it is important to note that the train and evaluation loss are close to each 
other. Unfortunately, we cannot use total loss to compare training and evaluation loss. The training loss seems to be slightly below 1, which is good when we take into 
consideration that the model can still learn. We have a mAP and a mAR of approximately 0.7 and 0.8 respectively which is very similar to our SSD model. When we look at the 
CenterNet’s predictions however we notice that there are quite a few images that do not have a label or are misclassified. All in all, this model looks promising, and can 
could potentially be better than the previous SSD model.

### Conclusion:

Both the SSD and CenterNet models looks great however it is important to consider the use case of this project. This project was a steppingstone to build an ASL to English 
translator app, that said the speed and accuracy of the model is equally important when it comes to live stream test environments. Both models are MobileNet models which were
made to be light weight models that can run on weaker devices. While CenterNet has a detection speed of approximately 94 milliseconds and SSD has a detection speed of 
approximately 1253.5 milliseconds, making CenterNet considerably faster than SSD. As if right now the SSD model is the best as the time delay for the SSD is justified by its
accuracy when compared to CenterNet however, with more training CenterNet could be a better model than SSD.	

| SSD | CenterNet |
|-----|-----------|
| ![image](https://user-images.githubusercontent.com/32663193/128615730-52de3917-1393-4329-b7e1-3f1df26fd2d6.png) | ![image](https://user-images.githubusercontent.com/32663193/128615725-0afc5466-fab7-4c02-885e-a62efc3309b8.png) |
| gif | gif |

As far as our initial worries on the dataset goes, the models seem 
to have a harder time detecting when the hand has a darker pigmentation. The models to pick up the gestures on darker hands however it is very finicky. More data not only on
the ASL alphabets but also introducing different skin tones and shades of grayscale should solve this problem.


