import requests
import json
import time

#speak function

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(str)


if __name__ == '__main__':

    print("\n\n\t\t----->  RAVI NEWS  <------")
    speak("hello and welcome to Ravi news channel so  todays major news headlines are  ")

    url ='https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=ef3acadfce2546a0b7ac74d478f9f9f3'

    # using request module for fetching data from API

    news=requests.get(url).text


    # converting it to json file

    parse=json.loads(news)


    # fetching the required data

    articles=parse["articles"]

    for items in articles:
        a=items["title"]
        speak(a)
        time.sleep(1)
        speak("moving on to next news")

    speak("so this was all for today thanks for listening..")












