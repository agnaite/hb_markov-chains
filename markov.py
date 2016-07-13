from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path)
    contents_read = contents.read()
    text = contents_read.split()
    contents.close()

    return text

def make_chains(text_string, num_words):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
 
    chains = {}

    #loops through the text string until it reaches the "num" to last word
    for index in range(0, len(text_string) - num_words): 
        #defines a variable for the first word. makes a list of next words and puts first_word in it
        first_word = text_string[index]
        next_words = [first_word]
        
        #goes through the text string from right after your first word, above, to the number of words you need.
        #for each loop til you get to the number of words needed, appends the next word to your next_words list
        for i in range (1, num_words):
            next_words.append(text_string[index + i])
        # converts the next_words list into a tuple and gets the word that follows the tuple
        next_words_tuple = tuple(next_words)
        following_word = text_string[num_words + index]

        #if a key with a next_word_tuple is already in the dict,
        #appends the following word to the list already in place as the value.
        #else, creates the key with the following word in a list.
        if next_words_tuple in chains:
            chains[next_words_tuple].append(following_word)
        else:
            chains[next_words_tuple] = [following_word]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    #sets a variable text equal to an empty string
    text = ""

    #sets variable current_key equal to a random choice in the keys in dict chains
    current_key = choice(chains.keys())
    
    #while the current_key is in the chains dict, loops through the below:
    while current_key in chains:
        current_value = choice(chains[current_key])
        #concatenates the current value to text
        text += current_value + " "
        #sets the new current key equal old key from index one onwards plus the current value       
        current_key = current_key[1:] + (current_value,)

    return text


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
# print input_text
# Get a Markov chain and pass in number of words for the n-gram
chains = make_chains(input_text, 2)
# Produce random text
random_text = make_text(chains)

print random_text
