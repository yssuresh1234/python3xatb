def are_angrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return
    return sorted(str1) == sorted(str2)


word1 = input("Enter First Word :\n")
word2 = input("Enter second word :\n")

if are_angrams(word1 ,word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")

