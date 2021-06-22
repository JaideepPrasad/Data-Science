# MNIST

#### Project Goal

The goal of this project was to create a neural network from scratch that can classify handwritten numbers.

#### Data Source

The data used in this project is the MNIST dataset, the dataset is downloaded when you run the code.<br >
The downloaded dataset has 70,000 images of handwritten numbers that are all labelled. Each image is a 28x28 grayscale image, associated with a label from 10 classes.<br >
![image](https://user-images.githubusercontent.com/32663193/120236292-ecf72680-c229-11eb-8341-53c5245e41b4.png)<br >

#### Files

There is a .ipynb jupyter notebook that has the code. Along with that when you run the code and download the MNIST dataset,
the MNIST dataset will be downloaded in the folder the code is in.

#### Overview

  - normalize data since data value is pixel intensity
  - format data so we can split data into randomized train and test data
  - display one image and label to double check
  - define loss function
  - create neural network with 1 hidden layer from scratch
  - program backwards propagation using partial derivative
  - update weights and biases
  - display loss per iteration
  - display metrics

#### Result

After 2000 epochs, the neural network had an accuracy of 93%.<br >

#### Conclusion

This project helped me learn the in depth process of how neural networks learn.
