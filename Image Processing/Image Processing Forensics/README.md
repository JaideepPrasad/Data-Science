# Speed Camera Licence Plate Identifier

#### Project Goal

The goal of this project was to clean up an image of a speeding car, so we can read the licence plate on the car.

#### Data Source

The data png file is in this github folder. It's a grayscale image of a car with a sort of dotty filter, in essence with a lot of noise.<br >
![image](https://github.com/JaideepPrasad/Data-Science/blob/main/Image%20Processing/Image%20Processing%20Forensics/car.png?raw=true)<br >

#### Files

There are 2 files here, a .ipynb jupyter notebook that has the code and a .pth file that contains the model parameters.

#### Overview

  - use data loader to load data
  - define what device the computer will be using
     - using cuda we can test if the computer has a GPU
     - if so we will use GPU, if not we will use CPU
  - define our neural network
  - optimize our neural network
  - create a train and test loop to identify training loss per batch, testing accuracy and avg loss per epoch
  - save model parameters
  - test a prediction

#### Result

After 25 epochs, the neural network had an accuracy of 76.7% and a avg loss of 0.009995.<br >
When testing a random prediction, the model predicted correctly

#### Conclusion

This being the first neural network I made using a GPU, the model came out well. 
An accuracy of 76.7% is pretty good although I'm sure I can bump that number up if I play around with the neural network architecture.
2 valuable skills where learnt in this project:
 - using GPU and how to move the model and data to the GPU
 - how to save and loag model parameter files


### Extra
For an electrical engineer like me, this project was a fun way to refresh my fourier skills but also understand different types of filters along with the differnet ways the affect an image. For anyone who is interested in filters or even photography, this is a great project as it gives you a lot of insight into the how and why we do what we do, rather that what we should do. If you plan on picking this project up, be prepared to do some research on how to numerically represent the effects of different filters. 
