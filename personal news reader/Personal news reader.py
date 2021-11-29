import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
def category_list():
    print("1.Entertainment\n2.Technology\n3.Health\n4.Science\n5.Sports\n6.Business")
    speak("Select your category")
    n = int(input("select your category: "))
    set_category = ''
    if n == 1:
        set_category = "entertainment"
    elif n == 2:
        set_category = "technology"
    elif n == 3:
        set_category = "health"
    elif n == 4:
        set_category = "science"
    elif n == 5:
        set_category = "sports"
    elif n == 6:
        set_category = "business"
    else:
        speak("you have entered invalid value")
        speak("Please enter values between 1-6")
        category_list()   #recurs the function if entered invalid category
    return set_category

if __name__ == '__main__':
    speak("Welcome to Varma news channel")

    category = category_list()
    r = requests.get(f"https://newsapi.org/v2/top-headlines?"
                     f"country=in&category={category}&apiKey=9ba66e790a27478ba86e713163bda8e2")
    data = r.text   #info from api into text form and stores in variable
    data = json.loads(data)   #converts the info into json format

    speak(f"starting your top news on {category}........lets start...")
    article = data["articles"]   #access the key/value pairs
    count = 0
    for i in article:
        speak("moving to the next news....listen carefully")
        count += 1
        print(count)
        print(i['title'])
        print("for more information click here", i['url'])
        print()
        speak(i['title'])
        if count == 10:
            break
    speak(f"This was your top {count} daily dose of news, by Varma python code")
    speak("Thank you bro, for listening till end")
