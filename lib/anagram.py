class Anagram:
    def __init__(self, word):
        # Store the sorted version of the word for easy comparison
        self.letters_in_word = sorted(word)

    def match(self, word_list):
        # Return a list of words from word_list that are anagrams of the initialized word
        return [word for word in word_list if sorted(word) == self.letters_in_word]
