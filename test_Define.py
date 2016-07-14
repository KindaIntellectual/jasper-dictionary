# -*- coding: utf-8 -*-
import unittest
from jasper import testutils
from . import Define


class TestMoviesPlugin(unittest.TestCase):
    def setUp(self):
        self.plugin = testutils.get_plugin_instance(Define.DefinePlugin)

    def test_is_valid_method(self):
        self.assertTrue(self.plugin.is_valid("Define"))
        self.assertFalse(self.plugin.is_valid("Jasper, you're the best!"))

def test_handle_method(self):
        '''Put your api key here to successfully run this test'''
        key = ''
        
        mic = testutils.TestMic()

        request = Request('https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key='+key+'&lang=en-en&text=cat')
        try:
            response = urlopen(request)
            data = json.load(response)
            word_type = data["def"][0]["pos"]
            defs = data["def"][0]["tr"]
            for text in defs:
                print text["text"]
        except URLError, e:
            print 'Unable to get translation', e