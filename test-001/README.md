# Test 001

## About

This expiernement is going to test text processing to make it easier for the ai model to understand what is going on.

## Data

The data will consist of a large amount of text such as an article and guidance text and then have notes based on that text.
Currently I want to get to about 100 entries of this to start testing with actual training.
However, for this test I do not have to have a large amount of data since I am just testing with some text processing and not training an AI model yet.

## Steps For Text Processing

I plan to stick with these few steps for right now but may expand on them in the future to include Part-of-Speech Tagging, Named Entity Recognition, Topic Modeling, and Removal of puncuation.

1. Lowercase: I am going to lowercase eveything in the text.
2. Tokenize the text: I am going to split the text into an array of words and also test with splitting it into sentences.
3. Remove Stop Words: Remove common words like "the", "is", and "and" that don't serve a purpose or don't have important meaning.
4. Stemming/Lemmatization: This will use a dictionary to reduce the words to there base form such as "better" --> "good". I might test Stemming but that has some flaws which I want to avoid.
5. Vectorization: Converts text to numerical format. Will test out Bag-of-words and TF-IDF.
