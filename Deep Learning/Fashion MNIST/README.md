# Fashion MNIST

#### Project Goal

The goal of this project was to create a neural network that can classify articals of clothing and learn how to use a GPU for neural networks.

#### Data Source

The data used in this project is the FashionMNIST dataset. I personally used [zalandoresearch](https://github.com/zalandoresearch/fashion-mnist) for the dataset and information about the data.
Basically the Fashion MNIST dataset is a set of pictures of various clothing articals that has been labelled.<br >
![image](https://user-images.githubusercontent.com/32663193/120233136-1f515580-c223-11eb-8ffe-c6850f69ce0e.png)


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
