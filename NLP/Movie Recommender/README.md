# Movie 
___
 
## Project Goal

The goal of this project is to create a movie recommender using multiple types of recommender filtering such as content filtering, collaborative filtering and hybrid filtering. We should be able to both recommend similar movies based on an input movie and recommend movies based on what a user has already watched.

## Dataset

The csv files used in this code can be found here: https://grouplens.org/datasets/movielens/20m/ <br>
The ml-20m.zip will contain the csv files.

## Process

#### Data Preprocessing:
   - import relevant files and parse text
   - make a pivot table that shows the "rating" of "movies" from every "user", call it movie ratings

#### Content Filtering Prep
   - vectorize data in the movies dataframe, we use TF-IDF here
   - make new pivot table based on relevance of movies with genres, call it tfidf_df
   - truncate tfidf_df so we don't have sparse matrix, call this latent_matrix_1_df

#### Collaborative Filtering Prep
   - create a truncated version of movie ratings, call it latent_matrix_2_df

#### Recommender
   - define hybrid equation, lets say 50% content, 50% collaborative
   - depending on what movie we choose, find the corresponding table for it, compare the characteristics of that movie with all the other movies via cosine similarity
   - sort by descending
   
## Results

To start of lets quickly review content, collaborative, and hybrid filtering: <br><br>
Content Filtering:
   - A user is recommended item A because the characteristics of items the user like is similar to item A
      - User like book A which is a horror story? Recommend book B which is also a horror story by the same author
        - Useful when we have data on user 

Collaborative Filtering:
   - A user is recommended item A because other users with similar taste likes item A
      - User like book A which is a horror story? Recommend book B which is a top seller horror story even though it's by a different author
        - Useful when we don't have data on user 

Hybrid Filtering:
   - Filtering based on a mixture of both content and collaborative filtering
      - Useful so we get the best of both worlds
        - If we only use content filtering, we will run out of very similar items
        - If we only use collaborative filtering, we will never offer a more curated item/experience
 
![image](https://user-images.githubusercontent.com/32663193/122165577-64da6900-ce46-11eb-8245-df678235cbea.png)


Now back to the code. First of we want to trim the 20M ratings file down to say 1M, this will cases us problems later on but it's ok. We move on to making a pivot table that shows us the rating of every movie by every user.

Movie Rating Pivot table:

![Capture](https://user-images.githubusercontent.com/32663193/122165915-e5996500-ce46-11eb-9669-f907a376c2ba.PNG)

For content filtering, we will make a new pivot table that will show us how relevant a genres is in a movie. The idea is if a user like a Dave Chappelle movie, we can check this table and find out the movie is 90% comedy. Now we can recommend another movie that is predominantly a comedy.

Latent_matrix_1_df (image below is a small snippet of the table):

![Capture1](https://user-images.githubusercontent.com/32663193/122166969-4e351180-ce48-11eb-8447-f9c6534cfcba.PNG)

For collaboration filtering, we will use the movie rating pivot table but truncate it (so it's no longer a sparse matrix). Remember how I said we will have issues for using 1 million ratings rather than 20 million? Yea, it's time to deal with that. Because we used a subset of the ratings data, we need to make user we ate using the movies that are related to the subset of the ratings data.

Latent_matrix_2_df (image below is a small snippet of the table):

![Capture2](https://user-images.githubusercontent.com/32663193/122168020-bf28f900-ce49-11eb-8e0d-c2e32cd5595a.PNG)

When truncating our tables, we chose to reduce the dimension of our tables to 20 (no real reason to choose 20). This can hurt the performance of our recommender model because we do not use all the data available to us. when looking at our cumulative sum of variance, we notice we are only using around 37% of our original data. This is ok for now as this project is supposed to teach us the concepts of recommender systems rather than focus on optimizing the system.

![Capture3](https://user-images.githubusercontent.com/32663193/122168954-dd432900-ce4a-11eb-82bb-937aafa5224a.PNG)

We now understand why we use Latent_matrix_1_df for content filtering. We use Latent_matrix_2_df for collaborative filtering as this shows what the user base thinks is good due to showing us the ratings of each movie. Now it's time for use to talk about hybrid filtering. We  can't just use both Latent_matrix_1_df and Latent_matrix_2_df as they are of different size. So we make a new table called latent_matrix_1_trimmed takes latent_matrix_1_df and only used the movies from latent_matrix_2_df.

We then compare the column of the movie in question with the specific table related to the filtering type and output the results. 

The last bit of the code shows you how you can use a python library called Surprise to do most of the above steps for you. Feel free to check the code and their documentation for more information if interested.

http://surpriselib.com/

## Conclusion

The results of this code were great. <br>

When looking at the hybrid filter, we see that recommended movies for Toy Story are other popular Disney adventure movies.

![Capture4](https://user-images.githubusercontent.com/32663193/122169967-09ab7500-ce4c-11eb-822d-463d26f3a08b.PNG)

When looking at the content filter, we see that recommended movies for Toy Story are other animated adventure movies that aren't as popular such as the first 2 recommended movies.

![Capture5](https://user-images.githubusercontent.com/32663193/122170286-64dd6780-ce4c-11eb-86da-51bcbf603afc.PNG)

And finally, when looking at the collaborative filter, we see that recommended movies for Toy Story are other popular adventure movies.

![image](https://user-images.githubusercontent.com/32663193/122170530-a3732200-ce4c-11eb-86e9-202aefe6efad.png)


