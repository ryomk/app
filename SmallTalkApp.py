import requests    #1

def talk_api(message):
    apikey = "DZZGcIZsOcGKUlziwSQDk0j7s7PEMwgf"
    talk_url = "https://api.a3rt.recruit.co.jp/talk/v1/smalltalk"    #4

    payload = {"apikey": apikey, "query": message}    #5
    response = requests.post(talk_url, data=payload)

    try:
        return response.json()["results"][0]["reply"]    #6
    except:
        return "ごめん！もう一回言って！"

def main():
     while(True):
         print("あなた：", end="")    #2
         message = input()

         print("BOT：" + talk_api(message))    #3  #7

if __name__ == "__main__":
     main()
