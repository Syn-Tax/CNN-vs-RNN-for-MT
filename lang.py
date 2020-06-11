SOS_token = 0
EOS_token = 1

class Lang:
    def __init__(self):
        self.word2index = {}
        self.index2word = {SOS_token: "SOS", EOS_token: "EOS"}
        self.num_words = 2 # counting SOS and EOS

    def add_sentence(self, sentence):
        for word in sentence.split(" "):
            self.add_word(word)

    def add_word(self, word):
        if word not in word2index:
            self.word2index[word] = self.num_words
            self.index2word[num_words] = word
            self.num_words += 1

