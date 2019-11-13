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
        "nvc_val" : r"%7B%22a%22%3A%22FFFF0N0N00000000807F%22%2C%22c%22%3A%221573657437318%3A0.11207479956521205%22%2C%22d%22%3A%22nvc_login%22%2C%22j%22%3A%7B%22test%22%3A1%7D%2C%22h%22%3A%7B%22umidToken%22%3A%22T1943A7D9B5C422B3B1187AF90FD20B441C86D3CA37916655F82FBD97C0%22%7D%2C%22b%22%3A%22121%23s09lkCC8gCwlVlmy%2BVXqllXYechfKujVAG6bxmq5oO7MTDhNFTD5lwLYAcFfKujVllgm%2BaP5KMllK9rJEGi5LgO9N7FfK5DWlmgY%2Bz95DM9lOQrJEmD5lwLYAcfMKujVlwgY%2BaP5KMlVAQ5zEmDIlajdPqa%2FAQ9PD0g6bqRVpSCvxB53bZ3546ocFtFbMXrDnj29p2D0C6e783BhbZsbkeAaF9QVVnV76q29pXseC60T8uV2CbibCeIaFtFbbZsbnjxVp2D0CZ0T83BhbZs0CehiFtK0gZBonnx9ByY7ksT8v5KglSVs6NaXQd60C6e4VlywsM8RDPx2Tpozi8msGWFVjyMVvpeVmQ5%2F4TwNs5Mo4j%2FXDFgG%2FwmI6YfmVqiBctVkStcIA0iXAOe3%2F58FrNWVGzgmEs%2B9CaASGVCCADhC6nNDSXPbezjIXHGkBLOEJlJdg4cl3Jmljv%2BWRn%2FhwjbEVNkaF0IUMBq8Op90spL40A%2BO%2B3l1CZj%2FIOmAfQRtQwCL2d8%2Fc0CEreqa9%2B0SI7wfRIdFPhxYekqEsGyWE58Z4sBspl9ValcD6lm0%2Fcm0zwiehDlnRRpDuuQAFyx7%2BxqD%2BKyi%2BIt2kuLRBy%2B2M4xUtXm9d2jzagUNzR3YH8gN4oPwE1Qns%2BC6ZP9L6Y%2FDk%2BAq7eSwCcBAubPW4MjCOaicI4vB1mcXj4gW%2BoLUEwkbmRro8W37mWguIAMbMy6lPkvHaX1isttDyP51LDbvWzso5p0qc2fkUsMPZVAJR%2B51gGvY2nMn4xa9I0l1N3iPRDruEuiItu1Z20Ir9%2BDUjZTT%2B8CWT9pi4NMjJHFKvMXmykKfyE%2BqDhRfPHdTCq44nPgkuAiXREl%2FPLTvEOD5G4l1yeGw%2FOvVbBZuGGOnH4AZeRaidozWKKmTyVsL77vIP52EtXrS1m5oaIBf1qdxfqDNLFx%2F0YIw3Iqyvt5J8pWD%2FVI%2Fyo2Yg9SXwyQBZHzE%2FuXwNbiEMKmcB84b%2BEUtoqv2LfcBS43d36wa6zT9n79mhw9Jd9LMSVELCdYGBOHyNAIAbgw%3D%22%2C%22e%22%3A%226V9RSQfZ0kC32qhgY6QDEzDzyQHGJZnbDUsfkCo4mAeOu02fmTbbQ8TJwo5S8wQyxFTeobcgqh4RB6SlJnz3dfhP9_15dpnrtSqJnvya92AqwVDaHNZgpMg_4xpYvsTMEAm48ZHXJRNfarQNwp4bK1mKNiUQ6BaxVjGwhVLj0ByxNhHyyzjqjekUPz83kk7nuj_r0ZDUxx5o14nClKpcnA%22%7D"
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
    
    


    

        