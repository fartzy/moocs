"""
We are using the common data store when we have a reference from the inner class Token to the outer 
class Sentence. I didnt use a range to demonstrate the flyweight pattern but instead I am using a 
dict and there is an assumption that if ever the token is not specified to be capitalized then it 
is not capitalized.  

"""


class Sentence:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.indexer = dict()

    class Token:
        def __init__(self, index, sentence):
            self.index = index
            self.capitalize = False
            self.sentence = sentence
            if not sentence.indexer.get(index):
                self.sentence.indexer[index] = self

    def __getitem__(self, index):
        if self.indexer.get(index):
            return self.indexer[index]
        else:
            return self.Token(index, self)

    def __str__(self):
        tokens = self.plain_text.split(" ")

        result = []
        for i in range(len(tokens)):
            word = tokens[i]
            token = self.indexer.get(i)
            # TODO - make sure if it is specifically not capitalized that it turns a not capitalized token
            # TODO   into a lowercase token
            if token:
                if token.capitalize:
                    word = word.upper()

            result.append(word)

        return " ".join(result)


if __name__ == "__main__":
    sentence = Sentence("hello world")
    sentence[1].capitalize = True
    print(sentence)