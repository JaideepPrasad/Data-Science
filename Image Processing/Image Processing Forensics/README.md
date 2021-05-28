# Speed Camera Licence Plate Identifier
___
 
 ### Description
In this project we are told that someone was caught on a speeding camera but was going too fast, so the image is distorted. Our job is to fix/clean the image. This file has the code used to clean the image as well as the distorted image called "car.png". 

### Installations
Libraries used:
- cv2
- numpy
- matplotlib.pyplot
`import imshow` 
- numpy.fft
`import fft2, fftshift, ifft2`
- skimage.feature
`import peak_local_max`
- skimage
`import exposure`
- skimage.filters.rank
`import mean`
- skimage.morphology
`import disk`
- skimage
`import img_as_ubyte`

### Extra
For an electrical engineer like me, this project was a fun way to refresh my fourier skills but also understand different types of filters along with the differnet ways the affect an image. For anyone who is interested in filters or even photography, this is a great project as it gives you a lot of insight into the how and why we do what we do, rather that what we should do. If you plan on picking this project up, we prepared to do some research on how to numerically represent the effects of different filters. 