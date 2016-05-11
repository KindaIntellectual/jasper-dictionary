#Written by Jake Schultz, updated by James Harding
#TODO Add more lang support, limit number of results returned
import re
from urllib2 import Request, urlopen, URLError
import json
from jasper import app_utils
from jasper import plugin
from imdb import IMDb

def format_names(people):
    del people[5:] # Max of 5 people listed
    ret = ''
    for person in people:
        ret += '%s.  ' %person.get('name')
    return ret.strip('. ')

class DefinePlugin(plugin.SpeechHandlerPlugin):
    def get_phrases(self):
        return ["DEFINE"]

    def is_valid(self, text):
        """
            Returns True if the text is related to Jasper's status.

            Arguments:
            text -- user-input, typically transcribed speech
        """
        return bool(re.search(r'\Define\b',text, re.IGNORECASE))

    def handle(self, text, mic):
        #Yandex Dictionary API Key
        dict_key = self.profile['keys']['YANDEX_DICT']
        #method to get the def
        self.get_def(text,mic,dict_key)

    def get_def(self, text, mic, key):
        mic.say("What word would you like to define?")
        theWord = mic.active_listen()
        #make a call to the API
        print "The Word To Define: " + theWord[0]
        request = Request('https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key='+key+'&lang=en-en&text=' +theWord[0])
        try:
            response = urlopen(request)
            data = json.load(response)
            #get the word type (noun, verb, ect)
            if(len(data["def"]) <= 0):
                mic.say("There does not appear to be a definition for the word " + theWord[0])
            else:
                word_type = data["def"][0]["pos"]
                mic.say("The word is a " + word_type)
                defs = data["def"][0]["tr"]
                #loop through the definitions
                for text in defs:
                    mic.say(text["text"])
        except URLError, e:
            mic.say("Unable to reach dictionary API.")