from django.http import JsonResponse
import requests
import json

def view(request):

    # 모델에서 받아오는건지
    pass

def translate(language, text):
    #언어코드(ko), 텍스트(변환될 대상) 을 받아 변환된 문자로 리턴.
    # parameter : ko, Hi
    # return : 안녕

    URL = "https://microsoft-azure-microsoft-text-translation-3-0-v1.p.rapidapi.com/translate?to="+str(language)+"&api-version=3.0"
    header = {"X-RapidAPI-Host": "microsoft-azure-microsoft-text-translation-3-0-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "dd3add1c5emsh2be6cdb031c24cep13c2d4jsnbc187ba7e275",
        "Content-Type": "application/json"
        }

    data = [{"Text": text,
        }]
    res = requests.post(URL, headers=header,data=json.dumps(data))
    res = json.loads(res.text)

    result = res[0]['translations'][0]['text']
    #print(return_value)
    return str(result)
    #Korean
    #ko
    #English
    #en
    #Japanese
    #ja

    #한중일독프스영아랍


if __name__=="__main__":
    translate("ko", "hi")