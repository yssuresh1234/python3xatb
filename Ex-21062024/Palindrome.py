
def is_palidrome(s):
    s = "".join(c.lower() for c in s if c.isalnum())
    # normalise the string by removing non-alphanumeric characters
    # and converting to lower case
    # isalnum() is a method to chk if a string consist
    # of alphanumeric characters
    return s == s[::-1]
    # check if string is equal to its reverse


test_string = input( "Enter a string:\n")
print( is_palidrome(test_string))