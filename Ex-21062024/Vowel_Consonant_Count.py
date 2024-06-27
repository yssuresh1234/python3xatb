def count_vowel_and_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count


string = input("Enter sting :\n")
vowels,consonant = count_vowel_and_consonants(string)
print(f"Vowels :{vowels} , Consonants :{consonant}")
