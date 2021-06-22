# Cosine Similarity
___
 
## Project Goal

The goal of this project is to understand cosine similarity as it is a powerful tool for recommender and other applications. This project should be able to take 2 different files of names and show us similar names between both the files. There is both a jupyter notebook and a python file for the code. 

## Dataset

There are 2 files here that has a list of names.

## Process

#### Preprocessing:
   - we are going to take a file, capture the column of names, drop duplicated names if any, lowercase the text and get rid of space between names if any

#### Word2vec:
   - store characters in each name
   - store character occurences for each name
   - calculate magnitude of name

#### Cosine_similarity:
   - calculate the cosine equation
   
#### Name_matching:
   - preprocess both files
   - vectorize all the names in both files
   - compare every name from one file to every name in the second file
      - apply cosine similarity and check if it meets a specified cosine similarity score
   - display the results

## Results

Lets have a quick reminder of what the cosine similarity equation looks like:

![image](https://user-images.githubusercontent.com/32663193/122131868-d6df8d80-ce07-11eb-8baf-60b86fac353a.png)

The hardest part of this project was creating and understanding the word2vec method. If we look at the right most expression in the equation above, we start to see that the length variable mimics the denominator. We use the characters and character occurences for the dot product, only using common characters for the dot product and using the character occurences to carry out the dot product calculation. Overall this was a new way to view math for me and was an interesting project.

## Conclusion

Below you will see a small part of the output as the chart is rather long.
![Capture](https://user-images.githubusercontent.com/32663193/122132450-ddbad000-ce08-11eb-8e26-e704437f3fb9.PNG)

