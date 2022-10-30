import re

# enter the word you want to convert to its main shape in the "the_sluggy_word" variable
# you need to make sure to keep the first and the last letter as the original word and reassemble the middle ones
# don't remove any letters form the word the program is not capable of handling such changes
# example "hello" > make it "hlelo" or "hlleo" and the program will return it to the orginal shape , the same goes to most of the words
# make "original" > "ognariil" and test the program

the_sluggy_word = "ognariil"
the_sluggy_word = the_sluggy_word.lower()
temp = r"(?<!\S)["+the_sluggy_word+r"]{"+str(len(the_sluggy_word))+r"}(?!\S)"
pattern = re.compile(temp)
# r"(?<!\S)[word]{wordlenthg}(?!\S)
def have_same_characters(str1, str2):
    return sorted(str1) == sorted(str2)


if len(the_sluggy_word)==1:
    print(the_sluggy_word)
elif len(the_sluggy_word) ==2 and the_sluggy_word.isalpha():
    print(the_sluggy_word)
elif len(the_sluggy_word) ==3 and the_sluggy_word.isalpha():
    for i, line in enumerate(open("D:\My Projects\Python Projects\\text_converter\words_alpha.txt")):
        for match in re.finditer(pattern, line):
            if match.group().startswith(the_sluggy_word[0]) and have_same_characters(the_sluggy_word,match.group())  :
                print('Found on line %s: %s' % (i + 1, match.group()))
elif len(the_sluggy_word) >=4 and the_sluggy_word.isalpha():
    for i, line in enumerate(open("D:\My Projects\Python Projects\\text_converter\words_alpha.txt")):
        for match in re.finditer(pattern, line):
            if match.group().startswith(the_sluggy_word[0]) and match.group().endswith(the_sluggy_word[-1]) and have_same_characters(the_sluggy_word,match.group()):
                print('Found on line %s: %s' % (i + 1, match.group()))

