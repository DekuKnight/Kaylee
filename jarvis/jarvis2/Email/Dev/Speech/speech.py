import urllib.parse,urllib.request

def getGoogleSpeechURL(phrase):
    googleTranslateURL = "http://translate.google.com/translate_tts?tl=en&"
    parameters = {'q':phrase}
    data = urllib.parse.urlencode(parameters)
    test = urllib.request.urlopen( googleTranslateURL + '?' + data)
    print(test.read())
    googleTranslateURL = "%s%s" % (googleTranslateURL, data)
    return googleTranslateURL

def speakSpeechFromText(phrase):
    googleSpeechURL=getGoogleSpeechURL(phrase)
    response = urllib.request.urlopen(googleSpeechURL)
    html = response.read()

def test(phrase):
    site= "http://translate.google.com/translate_tts?tl=en&"
    param = {'q':phrase}
    hdr = {'User-Agent': 'Mozilla/5.0'}
    data = urllib.parse.urlencode(param)
    req = urllib.request.Request(site + data,headers=hdr)
    page = urllib.request.urlopen(req)
    html = page.read()

test("test")
