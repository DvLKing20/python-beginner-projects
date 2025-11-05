import requests
from time import sleep

class NewsApp:
    def __init__(self):
        self.url = ""
        self.apiKey = ""
        self.query = ""
        self.language = ""
        self.country = ""
        self.source = ""

    def ask_user(self):
        print("What you are looking for?!")
        print("1: Top Headlines")
        print("2: Everything")

    def get_input(self):
        self.ask_user()
        while True:
          choice = ["https://newsapi.org/v2/top-headlines?","https://newsapi.org/v2/everything"]
          try:
           self.url = choice[int(input("Enter your choice: "))-1]
          except ValueError:
              print("Please enter a valid choice.")
              continue
          self.apiKey = input("Enter your api key: ")
          self.query = input("Enter your query(tesla,ai,sports): ").lower()
          self.language = input("Enter your language eg(en,de,fr)You can skip: ").lower()
          self.country = input("Enter your country eg(us,in,eu)You can skip: ").lower()
          self.source = input("Enter your source eg(bbc,abp,etc) You can skip: ").lower()
          break

    def get_news(self):
        try:
         params = {"q": self.query, "language": self.language, "country": self.country, "apiKey": self.apiKey, "source": self.source}
         response = requests.get(self.url,params=params)
         news = response.json()
         response.raise_for_status()
        except requests.exceptions.HTTPError:
            print("Unknow Error Occurred!")
        if news["status"] == "ok":
          for new in news["articles"]:
              print()
              source = new["source"]
              print("source : ",source["name"] or "unknown channel")
              print("author : ",new["author"] or "unknown author")
              print("title : ",new["title"])
              print("url : ",new["url"])
              print("publishedAt : ",new["publishedAt"])
              print()
        else:
          print("Your API key is invalid or incorrect. Check your key, or go to https://newsapi.org to create a free API key.")
    def save_news(self):
        print("\nsaving news...")
        sleep(2)
        try:
         params = {"q": self.query, "language": self.language, "country": self.country, "apiKey": self.apiKey, "source": self.source}
         response = requests.get(self.url,params=params)
         news = response.json()
         response.raise_for_status()
        except requests.exceptions.HTTPError:
            print("No Internet Connection!")
        if news["status"] == "ok":
          for new in news["articles"]:
              with open("news.txt", "a") as file:
                  file.write(f"author : {new["author"]}"+"\n")
                  file.write(f"title : {new["title"]}"+"\n")
                  file.write(f"url : {new["url"]}"+"\n")
                  file.write(f"publishedAt : {new["publishedAt"]}"+"\n")
                  file.write(f"\n")
if __name__ == "__main__":
   reference = NewsApp()
   print("\nWelcome to the News App\n")
   print("IF YOU HAVEN'T GOTTEN YOURSELF AN API KEY PLEASE TRY VISITING AND SINGH UP ON (NEWSAPI) FOR FREE\n")
   user_input = input("Do you want to save this news(yes/no): ")
   if user_input.lower() == "yes":
       reference.get_input()
       reference.save_news()
   elif user_input.lower() == "no":
       reference.get_input()
       reference.get_news()
   else:
       print("Please enter a valid choice.")