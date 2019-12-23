import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import requests
from conf import BASE_URL,APP_VERSION,APP_ID

def get_token(usename,password,is_store=True,**kawrgs):
    brand_token = get_brand_token(usename,password)
    if not is_store:
        return brand_token
    else:
        store_token = get_store_token(brand_token,**kawrgs)
        return store_token



def get_brand_token(username, password):
    api = "/login/account"
    url = BASE_URL + api

    payload = {
        "name":username,
        "password":password,
        "nvc_val" : r"%7B%22a%22%3A%22FFFF0N0N00000000807F%22%2C%22c%22%3A%221576931793836%3A0.7395385499616136%22%2C%22d%22%3A%22nvc_login%22%2C%22j%22%3A%7B%22test%22%3A1%7D%2C%22h%22%3A%7B%22umidToken%22%3A%22T5FB73B83C94B3BF73A37C5D4D7A9938ECF7FF660E9D7EA96EA1E6BAB7B%22%7D%2C%22b%22%3A%22121%239Rqlk%2F8rW2MlVlGvxVyzllXYechfKujVAG6bx2l5oO7zTKVN3AD5lwLYAcFfKujVllgm%2BaAZLPhHA3rnE9jIlwXYLa%2BxNvo9lGuYZ7pIKM9STQrJEmD5lwLYAcfdK5jVVmgY%2BzP5KMlVA3rnEkD5bwLYOcMHo6O4HluVS0bvsbc9MtFPe69xq2ibYnsshu%2FmCjVDkeILF9K0bZs0JnCVMZujhLzT83%2Fybbi0CNk1INn0lPi0n6XSp2D0kZ748u%2FmCbibCeIaFtFbbZrDnnx9pCibCZ0T83BhC6ibCeyaKdK0bZicNfxVcwAR%2FuI893CElXsjk%2BHXFYjmVdxNwSYrvZ0A%2BlLsPWQkYACtte%2B4DIMlGcZxBRIIIlgqBZ7M7G%2FJsOkBYxzqYjc%2FaBHLpjMkF4%2BYQEnTKRAYKtuxvmX%2FjKdz55v1%2B9UpqNugU%2FliVkEnIjf2VyLRADcLYPIqeqaJpA2lPWc1t3Moi%2F1ru%2BxTRQInE81TGShV2ic7H7%2Fry4aqZ8Sc7A85BZaHiGzRxUixy4qMGISQIKg26vDeRTjOblQORplV4XRCYKjgOobCaucvR3c0EngHONgusP%2Fv%2FF%2BYMZbBWCSJ8qLDRhfSvvXUvIn66g62FkO8SmiSPe%2FAL8toZ5LpQKBMPmT2ac9pbsW61B86Q5arZVDOdbsjh0W1D7itaih5q7yy1c9VqFtbRMciFNFSS4l2lY7uYFNBKiTp3SY4vHnX%2FV8%2F%2BFtJ7UUwQELvE%2Bdc2yk8ea%2F5GN%2BcljYmDzKEp3SmRl5IH5u%2BKKVlZ6cUaFtro6tFjpTot2NJI6%2B5nDrlrX%2FYjD%2FFOrU8qwb6rsZ8z75Nc9ASKT22m88ZNj%2FQn82ddCh4s%2F6X3Yo%2BJ9eHW35ZK2cw%2BPNEfQKuahwDgNm52z6QkR%2Fa4K5FCgrQCrlxNuxE%2FfZCt%2BB8km8vwyxC8UybQVqnU2S54ULSqObF5rJFWMUQWc9R%2BzJy3iqJ92dc36e1HUSimFFZ%2BQj6N%2Fp9Vf4yu%2FA3tqauR1RVI5vnxg7diSTyt0vM3MU7p2ajmZSK6Y8iSuBDwZfpjDPVHvvMAvcaJSd%2F8Sk2o28LZNvmg3G%2B%2BXnbYJDmCnrDmDbDnsIiiUfx8IiWzpzuPWk8%2F4b4F7u5ra131LXbSHw8EHDy0EjMkiwDzgdNphiNLIUC15SYx6A3CaocP51KGlvARO3alW1AmE6vn9uDilqgoy65ipDOa8pJ%2BZnqog%2B83hjiQ1B8D2iwpker63vFMDntNxyL3wG3QwpgYjsdMEg%2BSWG02L0VQz0G6QIH5cfaofWZkYFhwP9OMnBN7M4I%2FYGEkeo0JhhChPh%2Blkhe0%2BPljFbiUuY4SPs3j5LY5UPJHS7bwp1xVNiHTV98O59oN6nuB0T0LSF79qc5gEILvjs6NHt6FtHGQoXaEU6kIp%2BFh%2FD2az3jv7Mjibp2ZjDk2UNV9IYbnGGfQDYppTS25VRRHHV3qYwEJv%2BFoE65fjIekUVfZ2Fgd%2FXjpuGBpPyYrCfK%2FnlyyuwiZoSQYIkL4uWIUj6eMNtZkGHM4cK2lmy073vMEmFhqU%2Bu7EZeOYpnja%2BJk2vl1DBnKo0LYtSpd27p2Z%2B4KxlzMLhKQ1pFAQ9uF1D8PDU3IGdoYvKhN4lxaIwAhGyEoFEjzWoQN6gDxi8rn6BDggnsMg%2Byxm2In4vSlQv7sovJWMnvWrWeNnzu6m%2Fq6o0f7sgEfCxJsJPtH9Njo8c3jl7U8wLCF%2FLagsOAYdX5ZMwYATqky6D1vbnEQ16yMA08sfxgYYSGMTlAuNu8aoYR4ED%2BFPTIdwC06K%2F7E%2FUuGDpIlY4zL30dmL9ZVsL8%2FwkwHKBpNpl2OsSDlUNr28rWaMVVtsqeyHtsI3gNAh9lPtZyZPPIRGkyh00tYNoZwaLl%2BDKbx%2Fq%2Bg6wdB9cvTrRAFszIN%2Bxeda9DCNV4ilIfaKV6%2BNKTn1c0R2advuN%2FJ5%2FKJMdmHpNzDGvTHcctOoQtGnEvPAAFhB3KWTwyOGQS68%2BHVqpoTKg7abS4Z8fWgE7U7OhUbDUIQ%2BUQbkNy1O104cZVosWPUPmu8Au%2FD50NqMYd4ZALnDIbaz%2Bj75DYlmS15Qlr5fDcDOPEKcD0LhRsgpRlcQOMFYIDK5qn0caLCrXfNE47JnEJjyZ886nigI8JkI3CUyGq445gJ4sfkL10QjclfYE5VjJ4AioNzKtSfQvNJKRfLNmdFDqwaWPfzwewmxG96T6ZVg3xIgsf25x1kBZKPSUQPNrXtTsqFlFJCOw%2F%2BSfCXQKFb2V5IRPcIuMF2TCbTp95REAIYWnRXLTc27H2QqiQcYRDJ6MN0yMjF7XutGu1Ed1bUsidbu9Z5chEem1qbKGr%2B7UjIUsrsTlAue%2F%2B%2B1uJQG7QHwZWiA0ARaP9qW1o4bp9vNCJ560fvsCG5diWMv9Hd9bNw9cIkr0TjH91mQnHt9U84EHGarQcOaOnl6%2FIhXt%3D%22%2C%22e%22%3A%226V9RSQfZ0kC32qhgY6QDE4jqIxty32xLB24ef9MvXpaOu02fmTbbQ8TJwo5S8wQyxFTeobcgqh4RB6SlJnz3dfhP9_15dpnrtSqJnvya92AqwVDaHNZgpMg_4xpYvsTMEAm48ZHXJRNfarQNwp4bK_Cuvt7-8yqwTN_DvPea1V6xNhHyyzjqjekUPz83kk7nuj_r0ZDUxx5o14nClKpcnA%22%2C%22f%22%3A%2201jDVvKjEkiEfpZAc_kXFvfzyyoqUIN-S9fGRkGT2WGuMIUTplQnrsWolt36IpjvOPN8HPWMx6QlMWV-Nw9LKhFln6-0AXmw2z9nEi93BnEERx_xYL7sszuQSIyvH-2yOcw1XszU46hKT00Hc0c5yIY_-ZVyuTYzHc3sDcak1i1WXlEuS4KpMaiewYBhYAfHk5%22%2C%22g%22%3A%2205XBa8EtGVqtX0rzvVYJMIN_tFJf3y-YY5T4fMcGpYd8IvGkd4fDNSfe3xeFJmeAsWq4x7RRwLncT5qxgQOKjI8w6Ulbs8N-oEsERIfS6Iij-tMQRfW8SqIsV-fOPZOUQwC0vYvUm401qA-VDxII3g9WwdVrzO7deDnCIosmA6z1-2ATVZ53XNpKbZSxnHiTkxOrcvuHf-YvsOIwOLBBapAOBsEYay5TA9I1G8Gho5-7twojFADLzEUCN2CojU26IptQHVfjsyhdrrIp0-3WvFmQ4LWj16svCwfiEQqm8UOTdeSQarURBw6BEpbM6qGVpEIWtxaQpdwL1_v9HPKUfzPWg6AbdHZ49ZLoDFzjVSwhUlIbowwBSq9mMCmkUfW2fVLJqVi8cwshhnCc8T-aY_iF3zoSlaIZ7xne7XHdr3noQ%22%7D"
    }
    header = {
        "app-id" : APP_ID,
        "app-version" : APP_VERSION,
    }
    resp = requests.post(url,data=payload,headers=header)
    # print(resp.json())
    # print(resp.json()["data"]["token"]+"123")
    return resp.json()["data"]["token"]
    

def get_store_token(token,shop_id=None):
    if not shop_id:
        shop_id = 179734466593137
    api="/v1/account/switch/shop"
    url=BASE_URL+api
    header={
        "app-id": APP_ID,
            "app-version" : APP_VERSION,
            "token" : token
    }
    payload={
        "shop_id": shop_id
    }
    resp = requests.put(url,data=payload,headers=header)
    return resp.json()["data"]["token"]


if __name__ == "__main__":
    abc = get_token("tsj123","abc123")
    print(abc)
    
    


    

        