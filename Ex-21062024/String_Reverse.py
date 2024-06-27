# Using String slicing
def string_reverse(s):
    return s[::-1]


input_text_method1 = input("Enter string :\n")
print(string_reverse(input_text_method1))


# combining join(0 and reversed()

def reversed_string_reversed(s):
    return "".join(reversed(s))


input_text_method2 = input("Enter string :\n")
print(reversed_string_reversed(input_text_method2))

# use for Loop

def reverse_string_loop(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str

    input_text_method3 = input("Enter string :\n")
    print(reverse_string_loop(input_text_method3))