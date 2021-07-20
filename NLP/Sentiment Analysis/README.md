# Sentiment Analysis of Financial News Headlines

#### Project Goal

The goal of this project was to create a classifier that tells us if a news headline has a positive, neutral or negative sentiment.

#### Dataset

The data is from the following url:<br>
https://raw.githubusercontent.com/subashgandyer/datasets/main/financial_news_headlines_sentiment.csv

It is a table with 2 columns for sentiment and the headline with 4846 samples.

![Capture](https://user-images.githubusercontent.com/32663193/126402479-68b7c459-ae14-496b-bd75-a06c79b4890c.PNG)

The dataset is unbalanced,

| Sentiment | Samples |
|---|---|
| neutral | 2879 |
| positive | 1363 |
| negative | 604 |

however you can use SMOTE or another data balancing method to deal with this.

### Process

- Check for nulls in the csv
- Parse the data to clean the text
   - I used RegEx to make a list of all the words I didn't want and then replaced them with a space
- Embedding
   - You can use BoW or TF-IDF however I used TF-IDF in this example as it considers the importance of words, one of BoW's weak points
- Balance dataset
   - I use SMOTE in this example so that every class (positive, neutral, negative) has the same amount of samples 
- Encode labels
   - One hot Encoder or label encoder works however because there aren't a lot of classes, I decided to manually encode the labels  
- Create training and test dataset
- Train your model
   - I used SGD and Random Forest to compare which would be better however, you can use an classifier here. 

### Result

SGD had an accuracy of 91% while random forest had an accuracy of 90%.

When we look at the confusion matrix for both:

| SGD | Random Forest |
|---|---|
| ![SGD](https://user-images.githubusercontent.com/32663193/126405006-25c42c17-cd83-4edc-94ce-7c41ef7345f6.PNG) | ![rf](https://user-images.githubusercontent.com/32663193/126405013-bdb6129e-651f-4888-b3d2-f59979b378f6.PNG) |

We can see that SGD had a hard time differentiating positive and neutral headlines. Random Forest on the other predicted some headlines to be neutral when they were actually positive headlines. 
These issues could stem from how expressive the dataset was when it comes to emmotions however, both models did achive an accuracy of 90 or above which is great.
