class VowelCounter:
    def __init__(self):
        self.sentences = {}

    def add_sentence(self, sentence):
        vowel_count = sum(1 for char in sentence if char.lower() in "aeiou")
        self.sentences[sentence] = vowel_count

    def get_vowel_counts(self):
        return self.sentences

counter = VowelCounter()
sentence = input("Enter a sentence")
counter.add_sentence(sentence)
print(counter.get_vowel_counts())
