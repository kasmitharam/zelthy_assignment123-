import requests
import traceback


class Dictornay_search:
    def word_search(self):
        """
        input variables
        Word
        The word for which the meaning has to be found


        Purpose of the class:
        To find the meaning of the given word.

        """

        word = input("Word?")
        try:
            resp = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en_US/'+word)
            for i in resp.json():
                if i == 'title':
                    print('Word does not exist in the dictionary')
                else:
                    print(i['word']+'.'+i['meanings'][0]['partOfSpeech']+'.'+i['meanings'][0]['definitions'][0]['definition'])
            del word
            del resp
            del i
        except Exception as e:
            pass
dict = Dictornay_search()
dict.word_search()