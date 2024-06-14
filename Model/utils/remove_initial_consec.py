def remove_initial_consec(word):
    if isinstance(word,str):
        word = word.strip()
        if len(word)>1:
            if ((word[0] == word[1]) & (word[0] not in ['l', 'a'])):
                firstLetter = word[0]
                stripped = word.lstrip(word[0])
                if len(stripped)<len(word):
                    return firstLetter + stripped
                else:
                    return word
            else:
                return word
        else:
            return word