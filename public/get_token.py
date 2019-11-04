import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import requests
from conf import BASE_URL,APP_VERSION,APP_ID

def get_token(username, password, **kwargs):

    api = "/login/account"
    url = BASE_URL + api

    payload = {
        "name":username,
        "password":password,
        "nvc_val" : r"%7B%22a%22%3A%22FFFF0N0N00000000807F%22%2C%22c%22%3A%221572876441337%3A0.47320057975657237%22%2C%22d%22%3A%22nvc_login%22%2C%22j%22%3A%7B%22test%22%3A1%7D%2C%22h%22%3A%7B%22umidToken%22%3A%22TF3E21C2AFB9EFC5F395542D8B979C2C3B22002316B9798AFB5AA7B8063%22%7D%2C%22b%22%3A%22121%23VoQlkCteAdMlVl2b%2BVyZllXYechfKujVAG6bxyq5oOZ8T3hN8TD5lwLYAcFfKujVllgm%2BaP5KMllK9rJEGi5LgO9N7FfK5DWlmgY%2Bz95DM9lOQrJEmD5lwLYAcfMKujVlwgY%2BaP5KMlVAQ5zEmDIlaiqIv%2FyAQ9PD0g6bqRVpSCvxBuGbZ3546ocFtFbMXrDnj29p2D0C6e783BhbZsbkeAaF9QVVnV76q29pXseC60T8uV2CbibCeIaFtFbbZsbnjxVp2D0CZ0T83BhbZs0CehiFtK0gZBonnx9ByY7kiT8v5OglXVsZNaXQd60C6e%2BVMhldFBRDEilhfw9nX9j6oq61aEHhtO0SKHbgF8jysr2DpAIRdv4R%2BDeNU4l6mOmxou6%2FEVGKIXyvQYsqnPisPDalmgfZMfXRhWhmdAKPgONu132KrEW2uuXiAeen3vOp8f0wYpA%2FNL93Gmu1tfSDOOedXhMMd0d7fSleZY292VCHWIHIsHyakDYn1kDrCFSpIZo%2FIXvFU8fRQijdzdSbEy63q5pco3efbw2SNrT1aIhcCTPniVFl2bjgHAlQWgnxJxq4gIsr5y87hG8%2Ff1DS9r9uhgDjDapwx3rcNuS0sLepvMKMVqaIfr6gt5zGJYLP1EG%2FPklR72BRtDcrzFK40LqDqJ2A5Uy3FfLXgUuAyr7j%2BFeiyFkEsQ30zUt3BxxTBp9qHjuvt%2BYZVNvnz0HkD6XCpvTEQirrbBNVo9yHZqM5EH3oVyUQv9RM7l%2B4wwSFFVUt2pQ%2FOVd9u%2FBLnzO4%2BCkVdhS6rAXPx82HyJdBZ04I5jXRVd7MwUP28RdcoC19HmcBQr2%2BwEbTcQ47sdDw3h7euFV69GSjR8pFv3ilW2VL1Kd5X%2FvBoza0CDSc6068shgMlqY7FLSevI3Jll5ijVbTi%2B4XsKV%2FWHJy4mQNHyMA4ug4ovOmKFYJPxn6lMraEI6Mee9iHejcu23KM%2BGs4KeY%2BTxu%2FAZTnt97INvGWFw8bhJ8CLSiOXrwGyBgpUX461TMFPtzCWc48yizchFAZTLF5dh7eTaO9kfGab%2BZXlofeyAtOprpBl4S0T41yx78ytcg9SRIfV%2FrPUES02qi0CFXX3QNCp%2F69B2uAqwc7C6%2Fl8rr0brsjsYHrHjZNPulblV1q46L0bqrxZuh6q%2B66xuDwdAPKLVQJJLf0Enqx66%2B%2BgGhAeuoxD3AYD4nzaDu%2BGSp9Kb%2FJIY%2BNiuAWOnD2hihZmOpksnJir5mxxUsDWdNI4wugjNcqR7AdD00PP4ndfo2xbn1tjapNLwAouIbVg8vXe1ItjlHva0KttlROuRrev1TGmKP35zvZDXl7ptnCu1nCisNUNqvcxmkkfTLHimFl%2F6KFI9zMS6%22%2C%22e%22%3A%226V9RSQfZ0kC32qhgY6QDEzDzyQHGJZnbDUsfkCo4mAeOu02fmTbbQ8TJwo5S8wQyxFTeobcgqh4RB6SlJnz3dfhP9_15dpnrtSqJnvya92AqwVDaHNZgpMg_4xpYvsTMEAm48ZHXJRNfarQNwp4bK4bRov9Pyj3BLVtazwhyowyxNhHyyzjqjekUPz83kk7nuj_r0ZDUxx5o14nClKpcnA%22%7D"
    }
    header = {
        "app-id" : APP_ID,
        "app-version" : APP_VERSION,
    }
    resp = requests.post(url,data=payload,headers=header)
    # return resp.json()["token"]
    # print(resp.json())
    return resp.json()["data"]["token"]

if __name__ == "__main__":
    abc = get_token("tsj123","abc123")
    print(abc)
    
    


    

        