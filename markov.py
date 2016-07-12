from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path)
    contents_read = contents.read()
    text = contents_read.split()
    contents.close()


    return text

def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """


    chains = {}

    # your code goes here
    for index in range(0, len(text_string) - 2):
        first_word = text_string[index]
        second_word = text_string[index + 1] 
        third_word = text_string[index + 2]
        
        if (first_word, second_word) in chains.keys():
            chains[(first_word, second_word)].append(third_word)
        else:
            chains[(first_word, second_word)] = [third_word]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
# print input_text
# Get a Markov chain
chains = make_chains(input_text)
for keys, values in chains.items():
    print keys, values

# Produce random text
random_text = make_text(chains)

print random_text
