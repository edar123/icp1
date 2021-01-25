#2.1.##–Input the string “Python” as a list of characters
# from console, delete at least 2 characters, reverse the resultant string and print it.
def reverse(result):       ### function declaration
    str = ""               ### str as stirng declaration
    for i in result:       ### reversing string
        str = i + str
    return str             ### returning value of reverse string
input = "Python"

# Printing original string
print("Original string: " + input)

result = ""               ##declaring as string
#### removing two character from given string
for i in range(0, len(input)):
    if i != 0 and i!=3:   ### removing 1st and 4th characters
        result = result + input[i]

    # Printing final string
print("final reverse string after removing two characters : " + reverse(result))   ###calling reverse function