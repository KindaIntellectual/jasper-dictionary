#Written by Jake Schultz
import re
from urllib2 import Request, urlopen, URLError
import json

WORDS = ["DEFINE"]

PRIORITY = 1


def handle(text, mic, profile):

    dict_key = profile['keys']['YANDEX_DICT']

    get_def(text,mic,dict_key)


def get_def(text,mic,key):
    mic.say("What word would you like to define?")
    theWord = mic.activeListen()

    request = Request('https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key='+key+'&lang=en-en&text='+theWord)
    try:
        response = urlopen(request)
        data = json.load(response)
        word_type = data["def"][0]["pos"]
        mic.say("The word is a " + word_type)
        defs = data["def"][0]["tr"]
        for text in defs:
            mic.say(text["text"])
    except URLError, e:
        mic.say("Unable to reach dictionary API.")


def isValid(text):
    return bool(re.search(r'\Define\b',text, re.IGNORECASE))
