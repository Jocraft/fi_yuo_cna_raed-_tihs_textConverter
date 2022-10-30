import re

# enter the text you want to convert to its main shape in the "weird_text.txt" file
# you need to make sure to keep the first and the last letter as the original word and reassemble the middle ones for every word in the file
# don't remove any letters form the words the program is not capable of handling such changes
# example "hello" > make it "hlelo" or "hlleo" and the program will return it to the orginal shape , the same goes words in the file

def have_same_characters(str1, str2):
    return sorted(str1) == sorted(str2)
with open("D:\My Projects\Python Projects\\text_converter\weird_text.txt") as file:
    for line in file:
        for word in line.split():
            if word.isalpha():
                word = word.lower()
            temp = r"(?<!\S)[" + word + r"]{" + str(len(word)) + r"}(?!\S)"
            pattern = re.compile(temp)
            if len(word) == 1:
                print(word, end=" ")
            elif len(word) == 2 and word.isalpha():
                print(word, end=" ")
            elif word.isnumeric():
                print(word, end=" ")
            elif len(word) == 3 and word.isalpha():
                for i, line in enumerate(open("D:\My Projects\Python Projects\\text_converter\words_alpha.txt")):
                    for match in re.finditer(pattern, line):
                        if match.group().startswith(word[0]) and have_same_characters(word,match.group()):
                            print(match.group(), end=" ")
            elif len(word) >= 4 and word.isalpha():
                for i, line in enumerate(open("D:\My Projects\Python Projects\\text_converter\words_alpha.txt")):
                    for match in re.finditer(pattern, line):
                        if match.group().startswith(word[0]) and match.group().endswith(
                                word[-1]) and have_same_characters(word, match.group()):
                            print(match.group(), end=" ")





