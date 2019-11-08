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
        "nvc_val" : r"%7B%22a%22%3A%22FFFF0N0N00000000807F%22%2C%22c%22%3A%221573226483337%3A0.4382613529072723%22%2C%22d%22%3A%22nvc_login%22%2C%22j%22%3A%7B%22test%22%3A1%7D%2C%22h%22%3A%7B%22umidToken%22%3A%22T07735F83CBE7EC701175833AAE357DA18B429A212FDC4C4A45BF379A01%22%7D%2C%22b%22%3A%22121%23j6jlkRKXjsMlVlh0%2BVXFllXYechfKujVAG6bxYu5oOZGTj1N5OD5lwLYAcFfKujVllgm%2BaP5KMllK9rJEGi5LgO9N7FfK5DWlmgY%2Bz95DM9lOQrJEmD5lwLYAcfMKujVlwgY%2BaP5KMlVAQ5zEmDIlaeUuPo5AQ9PD0g6bqRVpSCvxBu3bZ3546ocFtFbMXrDnj29p2D0C6e783BhbZsbkeAaF9QVVnV76q29pXseC60T8uV2CbibCeIaFtFbbZsbnjxVp2D0CZ0T83BhbZs0CehiFtK0gZBonnx9ByY7kez8v5ORlIWsneaXQd60C6eEVw13hQFRDq%2B25DAdP35biIZGZaiMCjLPbvnx9CtnbvkZEfpdDBCTXrpR%2BnYIfjnQAh8IMeiIsIFdqFQSTViIPl8qoL9yEIg49MDOqRsb0A0OeAr57R%2FlEwAneysPsV2NUZJAC9p4%2F88k7mRyNU%2FxyavZ3huZ4dpNqWmUCRKpNInV5m8uD9bFepCBfo1GXGGekSjx5edwAX9LLoc0VP6O5d%2BRP6%2FUwRCjaOtWBdlv0lrQWFviE9u7YJBJW8msIh4YL4hDZH8nqHzBm8L2kxZ%2FPKBJsNYS4jpzBiGRMtV1XuaEqQvnEJs%2F%2FFPNnyC84aQi%2Bi4S%2FB0f1zyNpSO3Hvr9nCZXQlEBPYn9MoY8BFgmnqJyb7ksNTTFwnglbJh4AYluhb93m5JR%2BBy0ldjfuEf%2B86pUoUPHTWrbto5o09BOW0ftBt%2Fq86D59Hv%2F83ooxKeGpt1JWpq9Dd5cXwD%2B5fo7wDWJty93YV6Khik69qFOwEScgrpunjZT0Rzr8iU8ItRXJ6wLfHd%2FDmeo4hpSq56ataDDw8kBHVohPBVMTV81VjrDYmfzP7jmO0SLGSqWQa19RoekW3NEkzWHCiCJwb1r4s5OJr7aTuCRGxwFqZgycYmmCmDJoZAQiECEeU79VLQYRH9ZmFAGSj2PxZnl8%2FYyp%2B%2BzlbQuHT4mzAMd7aICVUb9J7bsV1Es4qa1vO3J%2BMXufJ0qNguFenQ%2FkxsfRNEbMxlpVkFZ%2BXzPMA0idCuAepm0mIAztH5dTvAh%2Byzm4yhoVQbhEn52KXhBZwnolh2Pu1Yo8i1ofjCtY%2BgDtYpbonT7uHIFOrgFiap8soe7Wji0JwWwK9CAbd5zA8Og0ELqw8bG%2BwD25ofVi24ThPfoUHAtWj5Ot79Uh28H%22%2C%22e%22%3A%226V9RSQfZ0kC32qhgY6QDEzDzyQHGJZnbDUsfkCo4mAeOu02fmTbbQ8TJwo5S8wQyxFTeobcgqh4RB6SlJnz3dfhP9_15dpnrtSqJnvya92AqwVDaHNZgpMg_4xpYvsTMEAm48ZHXJRNfarQNwp4bK4it641nSxZjobHOJY1ziQGxNhHyyzjqjekUPz83kk7nuj_r0ZDUxx5o14nClKpcnA%22%7D"
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
    
    


    

        