#Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".

out=input()
word=input()
def make_out_word(out, word):
    if len(out)==4:
        return out[:2]+word+out[1:]
    return False
print(make_out_word(out, word))