import nltk
from nltk import (TreebankWordTokenizer,
                  word_tokenize,
                  pos_tag)
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet, stopwords
from nltk.stem.snowball import SnowballStemmer

from sklearn.feature_extraction.text import CountVectorizer

class SummaryAI:
    def __init__(self, tokenizer=TreebankWordTokenizer()):
        self.tokenizer = tokenizer
        
    def download_required_resources(self):
        nltk.download('averaged_perceptron_tagger_eng')
        nltk.download('wordnet')
        nltk.download('punkt_tab')
        nltk.download('stopwords')
        
    def get_wordnet_pos(self, tag):
        match tag[0]:
            case 'J':
                return wordnet.ADJ
            case 'V':
                return wordnet.VERB
            case 'N':
                return wordnet.NOUN
            case 'R':
                return wordnet.ADV
            case _:
                return wordnet.NOUN
            
    
    # TEXT PROCESSING FUNCTIONS
    # I decided to use greek letters
    # as named for each way to process
    # text. I also plan to have a 
    # comment that describes the 
    # corresponding function for each
            
    # ALPHA
    # Tokenizer: NLTK basic one
    # POS: N
    # Stemming/Lemmatize: Stemming
    # Remove Stop Words: Y
    # Vectorization: Bag-of-Words
    def alpha_process_text(self, text):
        cv = CountVectorizer()
        tokens = word_tokenize(text)
        stemmer = SnowballStemmer("english", True)
        
        stemmed_tokens = [stemmer.stem(token) for token in tokens]
        
        english_stopwords = stopwords.words('english')
        prevector_tokens = [t for t in stemmed_tokens if t not in english_stopwords]
        
        
        
    
    # BETA
    # Tokenizer: TreebankWordTokenizer
    # POS: Y
    # Stemming/Lemmatize: Stemming
    # Remove Stop Words: Y
    # Vectorization: Bag-of-Words
    def beta_process_text(self, text):
        pass
    
    # GAMMA
    # Tokenizer: TreebankWordTOkenizer
    # POS: Y
    # Stemming/Lemmatize: Lemmatize
    # Remove Stop Words: Y
    # Vectorization: Undecided
    def gamma_process_text(self, text):
        pass
    
    # DELTA
    # Tokenizer: NLTK Basic
    # POS: N
    # Stemming/Lemmatize: Stemming
    # Remove Stop Words: N
    # Vectorization: Bag-of-Words
    def delta_process_text(self, text):
        pass
    
    # ZETA
    # Tokenizer: TreebankWordTOkenizer
    # POS: N
    # Stemming/Lemmatize: Stemming
    # Remove Stop Words: N
    # Vectorization: Undecided
    def zeta_process_text(self, text):
        pass
    
    def process_text(self, text):
        # download required resources
        self.download_required_resources()
        
        # Tokenize and lowercase the text here
        tokenized_text = self.tokenizer.tokenize(text.lower())
        
        # Part of Speech tagging (For lemmantizing)
        pos = pos_tag(tokenized_text)
        
        # Lemmatize the text
        
        lemmatizer = WordNetLemmatizer()
        lemmatized_text = [lemmatizer.lemmatize(word, self.get_wordnet_pos(tag)) for word, tag in pos]
        
        # Remove stop words
        english_stopwords = stopwords.words('english')
        prevector_text = [t for t in lemmatized_text if t not in english_stopwords]
        
        # Vectorize the text
        
        return prevector_text