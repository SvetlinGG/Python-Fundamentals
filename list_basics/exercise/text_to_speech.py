import pyttsx3

def text_to_speech_function(text, lang='bulgarian'):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 40)
    engine.setProperty('voice', lang)
    engine.say(text)
    engine.runAndWait()


text_to_speech_function('Oбичам те бе, Тони')