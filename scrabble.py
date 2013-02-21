import re

def makeRoughRegex(inputchars):
    expression = "^[" + inputchars + "]*$"
    return re.compile(expression)
 
# Takes a string and returns a regex that tests for any
# combination of any number of letters in the string.
# So, if inputchars = "ABCDE",
# it will return a regex of ^[ABCDE]*$

def makeFineRegex(inputchars):
    expression = ""
    charlist = list(inputchars)

    chardict = {}

    for char in charlist:
        chardict[char] = chardict.get(char, 0) + 1

    for char in chardict:
        expression += char + ".*" + char
        
        number = chardict[char] - 1
        for i in range(number):
            expression += ".*" + char

        expression += "|"

    expression = expression[:-1]
    print "Using expression ", expression

    return re.compile(expression)

# Takes a string and returns a regex that tests for any repeats
# of letters in the string. If there's repeats in the input string,
# then it allows for that many repeats in the regex.
# So, if inputchars = "AACEEED",
# it will return a regex of A.*A.*A|C.*C|E.*E.*E.*E|D.*D


dictionary = open('/home/mike/Desktop/dictionary.txt', 'r')

wordlist = []

for line in dictionary:
    wordlist.append(line.strip())

dictionary.close()

print "Enter a list of characters."
inputchars = raw_input()
inputchars = inputchars.upper()

roughregex = makeRoughRegex(inputchars)
fineregex = makeFineRegex(inputchars)

matches = []

for word in wordlist:
    if roughregex.match(word):
        matches.append(word)

wordlist = matches
matches = []

for word in wordlist:
    if fineregex.findall(word):
        "Discarding {0}.".format(word)

    else:
        matches.append(word)

for word in matches:
    print word
