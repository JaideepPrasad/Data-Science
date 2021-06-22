# Loan Eligibility
___
 
## Project Goal

A bank has approached us and asked us if we could automate the screening process for loan applications. Our goal here is to create a classifier to accurately determine who should get a loan or not.

## Dataset

The dataset can be found here: https://raw.githubusercontent.com/subashgandyer/datasets/main/loan_train.csv <br>
We are given general information about the applicant as well as the loan they applied for.

## Process

#### Data Preprocessing:
   - Missing Data:
      - there is missing data in this dataset, we can test different imputers to see which one is the best in this case
   - Data Encoding:
      - encode categorical data
   - Feature Scaling:
      - normalize columns such as loan amount and applicant income to prevent discrimination 
   - Feature Selections:
      - Use a few statistical models (pearson, chi-square, rfe, and others) along with a voting system to determine what is the most important features as I don't have the best financial knowledge. Can also use PCA if you like.

#### Model:
   - split data into train and test data
   - test a few classifiers (Decision Tree, KNN, Logistic Regression, SVM, and others) with base hyper parameters 
   - choose best models
   - finetune best models using gridsearch

#### Ensemble:
   - use a voting system that includes all the finetuned best models

## Results

As mentioned before there were a few features with missing data for both numerical and categorical data.

![Capture](https://user-images.githubusercontent.com/32663193/122125050-1d2fef00-cdfe-11eb-8edf-3b93d6455d1e.PNG)

For the categorical data, we used the mode to fill in any nulls as they were categories such as "married' and 'gender'. For the numerical categories, I tested a few imputers and used the best imputer for this dataset.

![Capture1](https://user-images.githubusercontent.com/32663193/122125491-8adc1b00-cdfe-11eb-96cb-20d0ce2ced7d.PNG)

For the feature selection as mentioned before, I don't have a strong understanding in finance so I used a voting system. I decided to use all the features however if I was to reduce the feature, I would only keep the top 3-5 features.

![Capture2](https://user-images.githubusercontent.com/32663193/122126033-2b323f80-cdff-11eb-989e-f18e26d7976d.PNG)

We look at all the models we chose and noticed that log reg (lr), SVC, random forest (rf) and naive bayes (nb) were the top 4 models.

![Capture3](https://user-images.githubusercontent.com/32663193/122126395-a8f64b00-cdff-11eb-8df0-e3cee02bf81e.PNG)

We pass the top 4 models through a gridsearch to see how much performance we can squeeze out of the models.

![Capture4](https://user-images.githubusercontent.com/32663193/122126506-da6f1680-cdff-11eb-843d-7c1e00e54505.PNG)

Now we use a voting system but notice that the voting model have a lower accuracy.

![Capture5](https://user-images.githubusercontent.com/32663193/122126660-11ddc300-ce00-11eb-8dc1-b3cdc070bf09.PNG)

## Conclusion
First off I should add recall, precision and F1 as metrics. We want to look at how many positive assumptions were true, this way we don't give loans to people that cannot pay the loan back. <br>
 
It seems that the voting ensemble didn't do as good as the individual models. I think it's important to note that when I didn't enforce random state, the voting model did better than the individual models. All the models had an accuracy of about 82% and the voting model had an accuracy of about 78%. I think this is due to potentially forcing bad splits however the K-Folds should have dealt with that. I'm not too sure what caused the inconsistency.

After getting rid of all the random states, you can see that the voting model is back to a 78% accuracy. For the future I would like to try other boosting techniques such as XG boosting as I heard that's the best boosting method so far.
