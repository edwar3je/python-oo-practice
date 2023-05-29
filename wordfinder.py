"""Word Finder: finds random words from a dictionary."""

from random import randint

class WordFinder:
    """Creates a list of words based on path of file provided
    and can return a random word"""
    
    def __init__(self, path):
        """initializes the path to the file along with a final_word_list"""
        self.path = path
        self.word_list = self.get_words_list()
        self.final_word_list = [word.strip() for word in self.word_list]
    
    def get_words_list(self):
        lst1 = open(self.path, 'r')
        read = lst1.readlines()
        return read
    
    def __str__(self):
        return f'{len(self.final_word_list)} words read'
    
    def random(self):
        random_number = randint(0, len(self.final_word_list) - 1)
        return self.final_word_list[random_number]


class SpecialWordFinder(WordFinder):

    def __init__(self, path):
        super().__init__(path)
        self.actual_word_list = [word.strip() for word in self.word_list if '#' not in word and word.strip()]
    
    def __str__(self):
        return f'{len(self.actual_word_list)} words read'
    
    def random(self):
        random_number = randint(0, len(self.actual_word_list) - 1)
        return self.actual_word_list[random_number]