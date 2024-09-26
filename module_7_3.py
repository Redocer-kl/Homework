class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            with open(file, 'r', encoding='utf-8') as f:
                words = []
                for line in f:
                    for char in [',', '.', "=", '!', "?", ";", ":", " - "]:
                        line = line.replace(char, "").lower()
                    words += line.split()
                all_words[file] = words
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for file, words in self.get_all_words().items():
            ind = -1
            for i in range(len(words)):
                if word == words[i]:
                    ind = i
                    break
            result[file] = ind + 1
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        for file, words in self.get_all_words().items():
            count = 0
            for i in range(len(words)):
                if word == words[i]:
                    count += 1
            result[file] = count
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
