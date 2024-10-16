def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()

    wordCount = countWords(file_contents)
    charCounts = generateCharCounts(file_contents)

    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{wordCount} words found in the document\n')
    charList = []

    for key, value in charCounts.items():
        charDict = {}
        charDict['char'] = key
        charDict['count'] = value
        charList.append(charDict)

    charList.sort(reverse=True, key=sort_on)

    for item in charList:
        print(f"The '{item['char']}' character was found {item['count']} times")

    print('--- End report ---')

def sort_on(dict):
    return dict['count']


def countWords(text):
    wordList = text.split()
    return len(wordList)

def generateCharCounts(text):
    loweredText = text.lower()
    charCounts = {}

    for char in loweredText:
        if char.isalpha():
            charCounts[char] = charCounts.get(char, 0) + 1

    return charCounts

main()
