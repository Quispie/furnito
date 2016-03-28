from __future__ import print_function
import nltk
class Pre_Processing:
    def remove_whitespaces(self, text):
        a = ' '.join(text.split())
        return a
    def Make_Lowercase(self, text):
        b = text.lower()
        return b
    def Tokenize(self, text):
        c = nltk.word_tokenize(text)
        return c
    def Stemmer(self, text):
        d = nltk.PorterStemmer(text)
        return d


pp = Pre_Processing()
str_line = "I like tea, but  can manage with  coffee."
removed = pp.remove_whitespaces(str_line)
lowercase = pp.Make_Lowercase(removed)
tokenized_text = pp.Tokenize(lowercase)
stemmed_text = pp.Stemmer(tokenized_text)
print stemmed_text

