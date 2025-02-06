#Prints the book
def print_book(text):
    print(text)

#Counts the words in the book
def word_count(text):
    return(len(text.split()))

#Return the number of times each character,symbol and space appears in the string
def character_count(text):
    lowered_text = text.lower()
    char_count = {}

    for letter in lowered_text:
        char_count[letter] = char_count.get(letter, 0) + 1

    return(char_count)
    

def sort_on(char_count):
    return char_count["num"]

#prints word and character data into a nice report
def print_report(text):
    char_count = character_count(text)
    #Printing the header
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(text)} words found in the document")
    
    #create and sort the list
    char_list = []
    for character in char_count:
        if character.isalpha():
            char_list.append({
                "char": character,
                "num": char_count[character]
                })

    char_list.sort(reverse=True, key=sort_on)


    #printing each character count
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

    #Printing end
    print("--- End report ---")


def main():
    #Reads the book for other functions to work properly
    with open("books/frankenstein.txt") as f:
        text = f.read()

    print_report(text)
    

main()

