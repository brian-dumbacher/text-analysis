
import re

class TextCleaner():

    __stop_words = [
        a,
        an,
        and,
        by,
        for,
        from,
        if,
        in,
        is,
        or,
        so,
        that,
        the,
        what
    ]

    def standardize(self, text):
        text = text.lower()
        text = re.sub(r"[^a-z]+", r" ", text)
        text = text.strip()
        return text
    
    def tokenize(self, text):
        if text == "":
            return []
        return text.split(" ")
    
    def remove_stop_words(self, tokens):
        return [token for token in tokens if token not in self.__stop_words]
    
    def get_ngrams(self, tokens, n):
        ngrams = []
        n_tokens = len(tokens)
        if n_tokens < n:
            return ngrams
        return ngrams
