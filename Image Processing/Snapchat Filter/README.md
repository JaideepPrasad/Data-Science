# Snapchat Filter
___
 
### Project Goal
The goal of this project is to make a snapchat filter. This filter will find your face and replace it with any image you choose, if you decide to use a different image than the one provided to you either change the file name to 'cartoon.jpg'(like you see in this github folder) or go into the code and add your file name there. When you run the .ipynb a new .avi file will be created in the folder containing the ipynb called "output.avi", this avi file is just a recording of the filter and starts as soon as you run the code. If you run the code you should know pressing the 'q' key on your keyboard will end the code. Upon running the ipynb file, you will see 2 windows pop up. One of them will be a small window that will only show you your face along with blue circles to show you the location of your eyes. The other window will have 2 live feeds from your camera, the one on the left will show your face with a green bounding box and blue circles for your eyes. The one on the right will show you with the cartoon filter applied to it.  

### Process
  
  - get and initialize Opencv's face and eyes classifier
  - import cartoon image: `cartoon = cv2.imread("cartoon.jpg")`
     - if you plan to import your own image 
         - please make sure the image is in the same folder as the ipynb file
         - change "catroon.jpg" with then name of your image file in quotes    
  - Turn your camera on
  - Set parameters for recording filter
  - capture each frame of the video and grayscale them
  - find faces and eyes for each face
  - reshape the image to fit over face
  - keep image on face
  - display all windows/frames
  - check for waitkey to break forloop
  - deactivate camera and close all windows

### Result
The results were very good as the tracking was better than I expected. I plan to learn how to make a bounding box that covers exactly the face rather than a rectanngular bounding box. This way the filters will look more professional. However for now, you will see a bit of what the code outputs and what output.avi displays.

What the code displays:

![ezgif com-gif-maker](https://user-images.githubusercontent.com/32663193/121992934-92ed7980-cd70-11eb-82ba-33b23a9dfd86.gif)

What output.avi displays:

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/32663193/121993540-a220f700-cd71-11eb-839d-9142c3fc97ae.gif)

### Issues
1) If the camera does not find a face when you start the code, the code will crash. However after starting up, the code won't crash if it doesn't detect a face
2) Due to the encoding type, somoetimes output.avi cannot be opened and viewd.
3) While the code can pick up multiple faces and sets of eyes, the display window that shows your face specifically stays on the last frame when 2 faces are detected.
