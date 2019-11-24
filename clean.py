
import re

class TextCleaner():

    __stop_words = [
        "a",
        "an",
        "and",
        "by",
        "for",
        "from",
        "if",
        "in",
        "is",
        "or",
        "so",
        "that",
        "the",
        "what"
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
    
    def get_ngrams(self, tokens, n, order):
        ngrams = []
        n_tokens = len(tokens)
        if n_tokens < n:
            return ngrams
        for i in range(n_tokens - n + 1):
            ngram = tokens[i, i + n]
            if not order:
                ngram = sorted(ngram)
            ngrams.append("_".join(ngram))
        return ngrams
    
    def get_features(self, tokens, ns, order):
        features = []
        for n in ns:
            features.extend(self.get_ngrams(tokens, n, order))
        return features
    
    def clean(self, text)
        text_stand = self.standardize(text)
        tokens = self.tokenize(text_stand)
        tokens_no_stop = self.remove_stop_words(tokens)
        return tokens_no_stop
    
