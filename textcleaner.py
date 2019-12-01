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
    __lemmas = {
        "auto": "car"
    }
    
    def standardize(self, text):
        text_stand = text.lower()
        text_stand = re.sub(r"\b(anti|non)[ -]([a-z])", r"\1\2", text_stand)
        text_stand = re.sub(r"[^a-z]+", " ", text_stand)
        return text_stand.strip()
    
    def tokenize(self, text):
        if text == "":
            return []
        return text.split(" ")
    
    def stem(self, token):
        return token
    
    def lemmatize(self, token):
        if token in self.__lemmas:
            return self.__lemmas[token]
        return token
    
    def clean(self, text)
        text_stand = self.standardize(text)
        tokens = self.tokenize(text_stand)
        tokens_stop = [token for token in tokens if token not in self.__stop_words]
        tokens_stem = [self.stem(token) for token in tokens_stop]
        tokens_lemma = [self.lemmatize(token) for token in tokens_stem]
        return " ".join(tokens_lemma)
    
    def get_ngrams(self, tokens, n, order=True):
        ngrams = []
        n_tokens = len(tokens)
        if n_tokens < n:
            return ngrams
        for i in range(n_tokens - n + 1):
            ngram = tokens[i:i + n]
            if not order:
                ngram = sorted(ngram)
            ngram_join = "_".join(ngram)
            if ngram_join not in ngrams:
                ngrams.append(ngram_join)
        return ngrams
    
    def get_features(self, tokens, ns, order=True):
        features = []
        for n in ns:
            features.extend([(ngram, True) for ngram in self.get_ngrams(tokens, n, order)])
        return dict(features)
