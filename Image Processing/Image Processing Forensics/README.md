# Speed Camera Licence Plate Identifier

#### Project Goal

The goal of this project was to clean up an image of a speeding car, so we can read the licence plate on the car.

#### Data Source

The data png file is in this github folder. It's a grayscale image of a car with a sort of dotty filter, in essence with a lot of noise.<br >
<br >
![image](https://github.com/JaideepPrasad/Data-Science/blob/main/Image%20Processing/Image%20Processing%20Forensics/car.png?raw=true)<br >

#### Files

There are 2 files here, a .ipynb jupyter notebook that has the code and a .png image file.

#### Overview

  - use fourier transform to get magnitude spectrum
  - block out the noise from magnitude spectrum
  - inverse fourier transform to compare current image with input image
  - change contrast 
  - sharpen image

#### Result

After all the image processing steps, we get an image clear enough to learn a few things:
  - The licence plate looks like "BHT 01Z". Its fair to say the licence plate looks pretty legible.
  - We can also say the make of the car is mazda and the model is a miata.

#### Conclusion

Using the fourier transform on the input image, we can tell the image has a lot of noise. 
The white light/star thing in the magnitude graph shows us which frequency component contributes to the noise.<br >

![image](https://github.com/JaideepPrasad/Data-Science/blob/main/Image%20Processing/Image%20Processing%20Forensics/Capture.PNG?raw=true)<br >

We want to get rid of all the white stars other than the center one. You can image the magnitude graph as a graph with 2 perpendicular axis going though the middle of the graph.
We want to save the center star as that is the DC component of our image. Filtering out the stars results in our new magnitude graph.<br >

![image](https://github.com/JaideepPrasad/Data-Science/blob/main/Image%20Processing/Image%20Processing%20Forensics/Capture1.PNG?raw=true)<br >

At this point we dealt with the noise in the image so we do an inverse fourier transform to get back to the real domain. Our current image looks faded so we will play with the contrast. We try gamma and log exposure functions to darken the image and find out that log was not helpful but gamma was.
  - left image: current image
  - middle image: gamma correction
  - right image: log correction
<br >

![image](https://github.com/JaideepPrasad/Data-Science/blob/main/Image%20Processing/Image%20Processing%20Forensics/Capture2.PNG?raw=true)<br >

We normalize the image and try to apply a smoothing filter but the quality of the image doesn't get better. From all the above steps (minus the smoothing filter), we cleaned the image well enough to read the licence plate. 
### Extra
For an electrical engineer like me, this project was a fun way to refresh my fourier skills but also understand different types of filters along with the differnet ways the affect an image. For anyone who is interested in filters or even photography, this is a great project as it gives you a lot of insight into the how and why we do what we do, rather that what we should do. If you plan on picking this project up, be prepared to do some research on how to numerically represent the effects of different filters. 
