# Snapchat Filter
___
 
 ### Description
This code is a snapchat filter. You can use any image and that image will replace your face, just name the file "cartoon.png". Along with showing you a window with your face and eyes (outlined) and another that shows you with the filter on, the code records you with the filter and saves that video. The video may not work for mac, in which case you can just change the encoding type in the code

### Issues
There may be an issue when it comes to opening the video due to the encoding type. If the video does not open, change the encoding formate by changing the variable "fourcc".

### Installations
Libraries used:
- cv2
- numpy
- os

### Roadmap
So this code detects your face in a square/rectangular boundary. I want to be able to make a new version of this code that creates a boundary that perfectly outlines your face, this way it would look like a more professional face filter that you can find on Snapchat.