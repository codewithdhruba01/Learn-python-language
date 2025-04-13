import unittest
import string
import sys

def find_longest_word(sentence):
    # Remove punctuation
    cleaned_sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    words = cleaned_sentence.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

class TestFindLongestWord(unittest.TestCase):

    def test_regular_sentence(self):
        self.assertEqual(find_longest_word("Random sentences can also spur creativity"), "creativity")

    def test_with_punctuation(self):
        self.assertEqual(find_longest_word("The quick, brown fox jumped over the lazy dog."), "jumped")

    def test_tie_same_length(self):
        self.assertEqual(find_longest_word("Cat bat rat mat"), "Cat")

    def test_single_word(self):
        self.assertEqual(find_longest_word("Supercalifragilisticexpialidocious!"), "Supercalifragilisticexpialidocious")

    def test_with_numbers_and_punctuation(self):
        self.assertEqual(find_longest_word("Python 3.10 is awesome, right?"), "awesome")

    def test_empty_input(self):
        self.assertEqual(find_longest_word(""), "")

    def test_only_punctuation(self):
        self.assertEqual(find_longest_word("!!! ,,, ???"), "")

def interactive_mode():
    """Provides interactive input for the user to test the function."""
    print("Enter sentences to find the longest word, or type 'q' to quit.")
    while True:
        sentence = input("Enter a sentence: ")
        if sentence.lower() == 'q':
            break
        print("Longest word:", find_longest_word(sentence))
    print("Goodbye!")


if __name__ == '__main__':
    # If "test" is provided as an argument, run unit tests.
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Remove the "test" argument so unittest doesn't process it.
        sys.argv.pop(1)
        unittest.main()
    else:
        interactive_mode()