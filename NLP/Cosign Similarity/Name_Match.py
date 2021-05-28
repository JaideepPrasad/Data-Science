import pandas as pd
from collections import Counter
import math

def preprocessing(file):
    
    df_a = pd.read_excel(file)                                         # import data
    col = df_a.columns[0]                                              # get name of colum in df
    df_a.drop_duplicates(subset = col, keep = "first", inplace = True) # get rid of duplicates
    df_a = df_a.reset_index(drop=True)                                 # reset index
    df_a = df_a.iloc[:,0].str.lower().str.replace(" ", "")             # .lower makes input lowercase, .replace gets rid of space
    return df_a

def word2vec(df):
    
    token = list(df.values) # tokenize names
    
    for names in token:
        #print(names)
        count_char = Counter(names)                               # creates set containing char & number of char occurancs 
        char = set(count_char)                                    # creates set of char in name
        lenght = math.sqrt(sum(x*x for x in count_char.values())) # magnitude of word vec(for cosine eq), each dim is a letter in name
        yield count_char, char, lenght, names

def cosine_similarity(vector1, vector2):
    
    common_char = vector1[1].intersection(vector2[1])                 # common letters between both names/vectors
    dot_product = sum(vector1[0][char] * vector2[0][char] for char in common_char) # dot product (for cosin eq)
    total_length = vector1[2] * vector2[2]                            # total lenght of vectors
    if total_length == 0:                                             # condition so we don't divide by zero in cosign eq 
        similarity = 0
    else:
        similarity = round(dot_product/total_length, 3)               # similar letters/all letters to 3 decimal places
    return similarity

a = "File_A.xlsx"                                               # Name of the first file in quotes
b = "File_B.xlsx"                                               # Name of the second file in quotes
similarity_threshold = 0.9                                      # Similarity threshold is a decimal that represents a percentage (0.9 = 90%)

df1 = preprocessing(a)                                          # preprocess data from files 1 and 2
df2 = preprocessing(b)

vectorization = word2vec(df1)                                   # vectorize data form df 1 and 2
w2v1 = [v for v in vectorization]
vectorization = word2vec(df2)
w2v2 = [v for v in vectorization]

results = []                                                     # list that holds results

for x in w2v1:                                                   # compare every name from df1 with every name from df 2
    for y in w2v2:
        score = cosine_similarity(x, y)                          # get similarity score
        if similarity_threshold <= score <= 1:                   # if score is within threshold, add it to our results
            results.append([x[3], y[3], score])                  # (name 1, name 2, similarity score of name 1 and 2)
    
results_df = pd.DataFrame(results)                                           # turn into a dataframe (output looks nice)
if len(results_df) != 0:                                                                     # safety condition
    results_df.columns = ['First Name', 'Second Name', 'Cosine Similarity Score']            # name colums
results_df = results_df.sort_values(by = 'Cosine Similarity Score', ascending=False)         # sort names based on score
results_df = results_df.reset_index(drop=True)                                               # reset the index

print(results_df)