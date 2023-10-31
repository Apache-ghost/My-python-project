def are_anagrams(string1, string2):
    return sorted(string1) == sorted(string2)

word1 = "listen"
word2 = "silent"
if are_anagrams(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")