import re

class TextCleaner():
    __stop_words = (
        "a",
        "an",
        "and",
        "b",
        "by",
        "c",
        "d",
        "e",
        "f",
        "for",
        "from",
        "g",
        "h",
        "i",
        "if",
        "in",
        "is",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "or",
        "p",
        "q",
        "r",
        "s",
        "so",
        "t",
        "that",
        "the",
        "u",
        "v",
        "w",
        "what",
        "x",
        "y",
        "z",
    )
    __vowels = "aeiouy"
    __double_consonants = ("bb", "dd", "ff", "gg", "mm", "nn", "pp", "rr", "tt")
    __li_ending = "cdeghkmnrt"
    __step1a_suffixes = ("sses", "ied", "ies", "us", "ss", "s")
    __step1b_suffixes = ("eedly", "ingly", "edly", "eed", "ing", "ed")
    __step2_suffixes = (
        "ization",
        "ational",
        "fulness",
        "ousness",
        "iveness",
        "tional",
        "biliti",
        "lessli",
        "entli",
        "ation",
        "alism",
        "aliti",
        "ousli",
        "iviti",
        "fulli",
        "enci",
        "anci",
        "abli",
        "izer",
        "ator",
        "alli",
        "bli",
        "ogi",
        "li",
    )
    __step3_suffixes = (
        "ational",
        "tional",
        "alize",
        "icate",
        "iciti",
        "ative",
        "ical",
        "ness",
        "ful",
    )
    __step4_suffixes = (
        "ement",
        "ance",
        "ence",
        "able",
        "ible",
        "ment",
        "ant",
        "ent",
        "ism",
        "ate",
        "iti",
        "ous",
        "ive",
        "ize",
        "ion",
        "al",
        "er",
        "ic",
    )
    __step5_suffixes = ("e", "l")
    __step6_suffixes = (
        "curist",
        "graphi",
        "logi",
        "logist",
        "nomi",
        "nomist",
        "pathi",
        "pathet",
        "physicist",
        "scopi",
        "therapeut",
        "therapi",
        "therapist",
        "tri",
        "trist",
        "trician",
        "turist",
    )
    __special_stems = {
        "skis": "ski",
        "skies": "sky",
        "dying": "die",
        "lying": "lie",
        "tying": "tie",
        "idly": "idl",
        "gently": "gentl",
        "ugly": "ugli",
        "early": "earli",
        "only": "onli",
        "singly": "singl",
        "sky": "sky",
        "news": "news",
        "howe": "howe",
        "atlas": "atlas",
        "cosmos": "cosmos",
        "bias": "bias",
        "andes": "andes",
        "inning": "inning",
        "innings": "inning",
        "outing": "outing",
        "outings": "outing",
        "canning": "canning",
        "cannings": "canning",
        "herring": "herring",
        "herrings": "herring",
        "earring": "earring",
        "earrings": "earring",
        "proceed": "proceed",
        "proceeds": "proceed",
        "proceeded": "proceed",
        "proceeding": "proceed",
        "exceed": "exceed",
        "exceeds": "exceed",
        "exceeded": "exceed",
        "exceeding": "exceed",
        "succeed": "succeed",
        "succeeds": "succeed",
        "succeeded": "succeed",
        "succeeding": "succeed",
        
        #Brian's additions
        
        "bearing": "bearing",
        "bearings": "bearing",
        "boarding": "boarding",
        "boardings": "boarding",
        "bowling": "bowling",
        "bowlings": "bowling",
        "coating": "coating",
        "coatings": "coating",
        "dressing": "dressing",
        "dressings": "dressing",
        "heading": "heading",
        "headings": "heading",
        "holding": "holding",
        "holdings": "holding",
        "marketing": "marketing",
        "marketings": "marketing",
        "parking": "parking",
        "parkings": "parking",
        "seasoning": "seasoning",
        "seasonings": "seasoning",
        "stocking": "stocking",
        "stockings": "stocking",
        "warehousing": "warehous",
        "warehousings": "warehous",
        "watching": "watching",
        "watchings": "watching",
        "authority": "authoriti",
        "authorities": "authoriti",
        "hospitality": "hospitaliti",
        "university": "universiti",
        "universities": "universiti",
        "fitness": "fitness",
        "alumna": "alumn",
        "alumnae": "alumn",
        "alumnus": "alumn",
        "alumni": "alumn",
        "analyses": "analyz",
        "analysis": "analyz",
        "animal": "animal",
        "animals": "animal",
        "bureaus": "bureau",
        "buses": "bus",
        "busy": "busy",
        "engineer": "engineer",
        "engineered": "engineer",
        "engineering": "engineer",
        "engineers": "engineer",
        "financial": "financ",
        "financier": "financ",
        "financiers": "financ",
        "gases": "gas",
        "organization": "organiz",
        "organizations": "organiz",
        "organize": "organiz",
        "organized": "organiz",
        "organizes": "organiz",
        "organizing": "organiz",
        "paste": "paste",
        "pasted": "paste",
        "pastes": "paste",
        "pasting": "paste",
        "wholesaled": "wholesal",
    }
    __lemmas = {
        "auto": "car"
    }
    
    def standardize(self, text):
        text_stand = text.lower()
        text_stand = re.sub(r"\b(anti|non)[ -]([a-z])", r"\1\2", text_stand)
        text_stand = re.sub(r"[^a-z]+", " ", text_stand)
        return text_stand.strip()
    
    def tokenize(self, text):
        return [] if text == "" else text.split(" ")
    
    def r1r2(self, token, vowels):
        r1 = ""
        r2 = ""
        for i in range(1, len(token)):
            if token[i] not in vowels and token[i - 1] in vowels:
                r1 = token[i + 1 :]
                break
        for i in range(1, len(r1)):
            if r1[i] not in vowels and r1[i - 1] in vowels:
                r2 = r1[i + 1 :]
                break
        return (r1, r2)
    
    def replace_suffix(self, original, old, new):
        return original[: -len(old)] + new
    
    def stem(self, token):
        if token in self.__special_stems:
            return self.__special_stems[token]
        elif len(token) <= 3:
            return token
        
        if token.startswith("y"):
            token = "Y" + token[1:]
        for i in range(1, len(token)):
            if token[i - 1] in self.__vowels and token[i] == "y":
                token = token[:i] + "Y" + token[i + 1:]

        step1a_vowel_found = False
        step1b_vowel_found = False

        r1 = ""
        r2 = ""
        if token.startswith(("gener", "commun", "arsen")):
            r1 = token[5:] if token.startswith(("gener", "arsen")) else token[6:]
            for i in range(1, len(r1)):
                if r1[i] not in self.__vowels and r1[i - 1] in self.__vowels:
                    r2 = r1[i + 1 :]
                    break
        else:
            r1, r2 = self.r1r2(token, self.__vowels)

        # STEP 1a
        for suffix in self.__step1a_suffixes:
            if token.endswith(suffix):
                if suffix == "sses":
                    token = token[:-2]
                    r1 = r1[:-2]
                    r2 = r2[:-2]
                elif suffix in ("ied", "ies"):
                    if len(token[: -len(suffix)]) > 1:
                        token = token[:-2]
                        r1 = r1[:-2]
                        r2 = r2[:-2]
                    else:
                        token = token[:-1]
                        r1 = r1[:-1]
                        r2 = r2[:-1]
                elif suffix == "s":
                    for letter in token[:-2]:
                        if letter in self.__vowels:
                            step1a_vowel_found = True
                            break
                    if step1a_vowel_found:
                        token = token[:-1]
                        r1 = r1[:-1]
                        r2 = r2[:-1]
                break

        # STEP 1b
        for suffix in self.__step1b_suffixes:
            if token.endswith(suffix):
                if suffix in ("eed", "eedly"):
                    if r1.endswith(suffix):
                        token = self.replace_suffix(token, suffix, "ee")                            
                        r1 = self.replace_suffix(r1, suffix, "ee") if len(r1) >= len(suffix) else ""
                        r2 = self.replace_suffix(r2, suffix, "ee") if len(r2) >= len(suffix) else ""
                else:
                    for letter in token[: -len(suffix)]:
                        if letter in self.__vowels:
                            step1b_vowel_found = True
                            break
                    if step1b_vowel_found:
                        token = token[: -len(suffix)]
                        r1 = r1[: -len(suffix)]
                        r2 = r2[: -len(suffix)]
                        if token.endswith(("at", "bl", "iz")):
                            token = token + "e"
                            r1 = r1 + "e"
                            if len(token) > 5 or len(r1) >= 3:
                                r2 = r2 + "e"
                        elif token.endswith(self.__double_consonants):
                            token = token[:-1]
                            r1 = r1[:-1]
                            r2 = r2[:-1]
                        elif (
                            r1 == ""
                            and len(token) >= 3
                            and token[-1] not in self.__vowels
                            and token[-1] not in "wxY"
                            and token[-2] in self.__vowels
                            and token[-3] not in self.__vowels
                        ) or (
                            r1 == ""
                            and len(token) == 2
                            and token[0] in self.__vowels
                            and token[1] not in self.__vowels
                        ):
                            token = token + "e"
                            if len(r1) > 0:
                                r1 = r1 + "e"
                            if len(r2) > 0:
                                r2 = r2 + "e"
                break

        # STEP 1c
        if len(token) > 2 and token[-1] in "yY" and token[-2] not in self.__vowels:
            token = token[:-1] + "i"
            r1 = r1[:-1] + "i" if len(r1) >= 1 else ""
            r2 = r2[:-1] + "i" if len(r2) >= 1 else ""

        # STEP 2
        for suffix in self.__step2_suffixes:
            if token.endswith(suffix):
                if r1.endswith(suffix):
                    if suffix == "tional":
                        token = token[:-2]
                        r1 = r1[:-2]
                        r2 = r2[:-2]
                    elif suffix in ("enci", "anci", "abli"):
                        token = token[:-1] + "e"                            
                        r1 = r1[:-1] + "e" if len(r1) >= 1 else ""
                        r2 = r2[:-1] + "e" if len(r2) >= 1 else ""
                    elif suffix == "entli":
                        token = token[:-2]
                        r1 = r1[:-2]
                        r2 = r2[:-2]
                    elif suffix in ("izer", "ization"):
                        token = self.replace_suffix(token, suffix, "ize")
                        r1 = self.replace_suffix(r1, suffix, "ize") if len(r1) >= len(suffix) else ""
                        r2 = self.replace_suffix(r2, suffix, "ize") if len(r2) >= len(suffix) else ""
                    elif suffix in ("ational", "ation", "ator"):
                        token = self.replace_suffix(token, suffix, "ate")
                        r1 = self.replace_suffix(r1, suffix, "ate") if len(r1) >= len(suffix) else ""
                        r2 = self.replace_suffix(r2, suffix, "ate") if len(r2) >= len(suffix) else ""
                    elif suffix in ("alism", "aliti", "alli"):
                        token = self.replace_suffix(token, suffix, "al")
                        r1 = self.replace_suffix(r1, suffix, "al") if len(r1) >= len(suffix) else ""
                        r2 = self.replace_suffix(r2, suffix, "al") if len(r2) >= len(suffix) else ""
                    elif suffix == "fulness":
                        token = token[:-4]
                        r1 = r1[:-4]
                        r2 = r2[:-4]
                    elif suffix in ("ousli", "ousness"):
                        token = self.replace_suffix(token, suffix, "ous")
                        r1 = self.replace_suffix(r1, suffix, "ous") if len(r1) >= len(suffix) else ""
                        r2 = self.replace_suffix(r2, suffix, "ous") if len(r2) >= len(suffix) else ""
                    elif suffix in ("iveness", "iviti"):
                        token = self.replace_suffix(wortokend, suffix, "ive")
                        r1 = self.replace_suffix(r1, suffix, "ive") if len(r1) >= len(suffix) else ""
                        r2 = self.replace_suffix(r2, suffix, "ive") if len(r2) >= len(suffix) else "e"
                    elif suffix in ("biliti", "bli"):
                        token = self.replace_suffix(token, suffix, "ble")
                        r1 = self.replace_suffix(r1, suffix, "ble") if len(r1) >= len(suffix) else ""
                        r2 = self.replace_suffix(r2, suffix, "ble") if len(r2) >= len(suffix) else ""
                    elif suffix == "ogi" and token[-4] == "l":
                        token = token[:-1]
                        r1 = r1[:-1]
                        r2 = r2[:-1]
                    elif suffix in ("fulli", "lessli"):
                        token = token[:-2]
                        r1 = r1[:-2]
                        r2 = r2[:-2]
                    elif suffix == "li" and token[-3] in self.__li_ending:
                        token = token[:-2]
                        r1 = r1[:-2]
                        r2 = r2[:-2]
                break

        # STEP 3
        for suffix in self.__step3_suffixes:
            if token.endswith(suffix):
                if r1.endswith(suffix):
                    if suffix == "tional":
                        token = token[:-2]
                        r1 = r1[:-2]
                        r2 = r2[:-2]
                    elif suffix == "ational":
                        token = self.replace_suffix(token, suffix, "ate")                            
                        r1 = self.replace_suffix(r1, suffix, "ate") if len(r1) >= len(suffix) else ""
                        r2 = self.replace_suffix(r2, suffix, "ate") if len(r2) >= len(suffix) else ""
                    elif suffix == "alize":
                        token = token[:-3]
                        r1 = r1[:-3]
                        r2 = r2[:-3]
                    elif suffix in ("icate", "iciti", "ical"):
                        token = self.replace_suffix(token, suffix, "ic")                            
                        r1 = self.replace_suffix(r1, suffix, "ic") if len(r1) >= len(suffix) else ""
                        r2 = self.replace_suffix(r2, suffix, "ic") if len(r2) >= len(suffix) else ""
                    elif suffix in ("ful", "ness"):
                        token = token[: -len(suffix)]
                        r1 = r1[: -len(suffix)]
                        r2 = r2[: -len(suffix)]
                    elif suffix == "ative" and r2.endswith(suffix):
                        token = token[:-5]
                        r1 = r1[:-5]
                        r2 = r2[:-5]
                break

        # STEP 4
        for suffix in self.__step4_suffixes:
            if token.endswith(suffix):
                if r2.endswith(suffix):
                    if suffix == "ion":
                        if token[-4] in "st":
                            token = token[:-3]
                            r1 = r1[:-3]
                            r2 = r2[:-3]
                    else:
                        token = token[: -len(suffix)]
                        r1 = r1[: -len(suffix)]
                        r2 = r2[: -len(suffix)]
                break

        # STEP 5
        if r2.endswith("l") and token[-2] == "l":
            token = token[:-1]
        elif r2.endswith("e"):
            token = token[:-1]
        elif r1.endswith("e"):
            if len(token) >= 4 and (
                token[-2] in self.__vowels
                or token[-2] in "wxY"
                or token[-3] not in self.__vowels
                or token[-4] in self.__vowels
            ):
                token = token[:-1]
        token = token.replace("Y", "y")

        # STEP 6
        for suffix in self.__step6_suffixes:
            if token.endswith(suffix):
                if suffix == "curist" and len(token) >= 8:
                    token = token[:-3]
                elif suffix == "graphi" and len(token) >= 9:
                    token = token[:-1]
                elif suffix == "logi" and len(token) >= 7:
                    token = token[:-1]
                elif suffix == "logist" and len(token) >= 9:
                    token = token[:-3]
                elif suffix == "nomi" and len(token) >= 7:
                    token = token[:-1]
                elif suffix == "nomist" and len(token) >= 9:
                    token = token[:-3]
                elif suffix == "pathi" and len(token) >= 6:
                    token = token[:-1]
                elif suffix == "pathet" and len(token) >= 7:
                    token = token[:-2]
                elif suffix == "physicist":
                    token = token[:-5]
                elif suffix == "scopi" and len(token) >= 8:
                    token = token[:-1]
                elif suffix == "therapeut" and len(token) >= 7:
                    token = token[:-3]
                elif suffix == "therapi":
                    token = token[:-1]
                elif suffix == "therapist":
                    token = token[:-3]
                elif suffix == "tri" and len(token) >= 8 and token[-4] in "ae":
                    token = token[:-1]
                elif suffix == "trist" and len(token) >= 10 and token[-6] in "ae":
                    token = token[:-3]
                elif suffix == "trician" and len(token) >= 10 and token[-8] in "ae":
                    token = token[:-5]
                elif suffix == "turist" and len(token) >= 8:
                    token = token[:-3]
                break
        
        return token
    
    def lemmatize(self, token):
        return self.__lemmas[token] if token in self.__lemmas else token
    
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
        return {ngram:True for n in ns for ngram in self.get_ngrams(tokens, n, order)}
