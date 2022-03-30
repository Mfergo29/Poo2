import sys
import requests


class Words:
    wordsApiEndpoint = "https://random-word-api.herokuapp.com/word"

    def __init__(self, language="en"):
        self.language = 'en'

    def get_words(self, number):
        return requests.get(self.wordsApiEndpoint + f"?number={number}" + f"&lang={self.language}")


class Definitions:
    dictionaryApiEndpoint = "https://api.dictionaryapi.dev/api/v2/entries/en/"

    def get_definition(self, word):
        return requests.get(self.dictionaryApiEndpoint + word)

    def parse_definition(self, definitionReq):
        return definitionReq.json()[0]['meanings'][0]['definitions'][0]['definition']


if __name__ == "__main__":
    wordsApi = Words()
    definitionsApi = Definitions()

    wordsRequest = wordsApi.get_words(5)
    if wordsRequest.status_code != 200:
        print("Hubo un error al contactar la API de Random Words. Por favor intentelo de nuevo.")
        sys.exit(1)

    wordList = wordsRequest.json()
    for word in wordList:
        definitionReq = definitionsApi.get_definition(word)

        print(f"===== {word} =====")
        if definitionReq.status_code != 200:
            print("No se encontro el significado de esta palabra.")
            continue

        print(definitionsApi.parse_definition(definitionReq))
