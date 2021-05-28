# Surveillance Camera
___
 
### Description
This code is a surveillance camera. It will detect motion and place an outlined box around the area with motion. On top of this, it will record everything including the time and date.

### Issues
There may be an issue when it comes to opening the video due to the encoding type. If the video does not open, change the encoding formate by changing the variable "fourcc".

### Installations
Libraries used:
- argparse
- datetime
- imutils
- time
- cv2

### Roadmap
I want to fix the background noise, probably can use blur filter for that. On top of that I want to make the first part of the code more "fool proof". There are certian bugs that arise when you start the code as there is no time to position yourself, could use time.sleep to add a delay. Ideally I would like to put this on a raspberry pi with the pi cam, test it out and have a video of my dog entering my room or something like that. This project was more of a "proof of concept" rather than a fully completed project as there are many other options I'd like to change later on when using this code for a specific application.