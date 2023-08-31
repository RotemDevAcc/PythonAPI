import requests


url = "https://google-translate1.p.rapidapi.com/language/translate/v2"


def TranslateWord(word,language):
    if(not language or not word):
        print("ERROR, NO Language or word detected")
        return


    reverse = False if language != "he" else True

    payload = {
        "q": word,
        "target": language,
        "source": "en"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "YOUR-API-KEY", # Please Add Your Own https://rapidapi.com/googlecloud/api/google-translate1/
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    translateresult = response.json()['data']['translations'][0]['translatedText']

    if(not translateresult):
        print(f"ERROR: Word {word} could not be translated to {language}")
        return
    

    print(f"Translated: {word} To: {translateresult[::-1] if reverse else translateresult} From {payload['source']} to {payload['target']}")