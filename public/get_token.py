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
        "nvc_val" : r"%7B%22a%22%3A%22FFFF0N0N00000000807F%22%2C%22c%22%3A%221574085752136%3A0.39703074271749883%22%2C%22d%22%3A%22nvc_login%22%2C%22j%22%3A%7B%22test%22%3A1%7D%2C%22h%22%3A%7B%22umidToken%22%3A%22TB0CC02710E4C10A67C4F7AAC3809465261F12465342CCD678B34B45977%22%7D%2C%22b%22%3A%22121%23gPMlkxsemWQlVlRFxVmKllXYechfKujVAG6bxh%2FIoO7KK2UrWtD5lwLYAcFfKujVllgm%2BaAZLPhHA3rnE9jIlwXYLa%2BxNvo9lGuYZ7pIKM9STQrJEmD5lwLYAcfdK5jVVmgY%2BzP5KMlVA3rnEkD5bwLYOcMYZR860luVS0bvsbc9MtFPe69x32ibYnsshu%2FmCjVDkeILF9K0bZs0JnCVMZujhLzT83%2Fybbi0CNk1INn0lPi0n6XSp2D0kZ748u%2FmCbibCeIaFtFbbZrDnnx9pCibCZ0T83BhC6ibCeyaKdK0bZicNfxVbyAR%2F5%2B7huL3MXsjk%2BHXFmwXl0%2BpaSYr8vgek1dRseEb86AFaY0zMdBAmcklrfHu7CJ6q4RPuhzZWwO3S0gN0yzCUHfEBfFMoID8CuB2NKyKSJOUNkNkjizfK3NnaidkZ3HmqOBK6s8hkaj1sHClC1yX88glZ01nTxViUTOZFUmhSc3A%2F9pjO4Ny3VPWdx%2Ffmub1eyRCWR0vRGysqZ7qFc%2FdJEZmd83D6jBeVVznA%2Bu5MpD%2BzpV1PmfK8HJbJ2kXUikEOuWZSVWM%2FrGYWx%2B8o0HOcgZ%2BBevQjlhLH50ZInBhRkbQoPxwQo2izrcEPqcDy1vHJtHHUETNl4lOg55%2BtIelpOjAb%2B6hIWDkNbcRDIBwFq3J4MbUXUhpsathXh2MkzOnX%2B%2FChPk0xXfd%2FBbbNTXw%2BY4%2BkZ6Z2NN0qvn6ELcc676N92BTilroFx94svF40NNaOUW2FPn1Ps6qniRLavhiRyGUUVrZ2VE5ArAREMbWcSvtugpZ9ZT9j8sbstXhENii6IBKxYXrX8FoUeDrYAbwS3N6y%2Bge3Z024TO4MmVxo8gTlUCmkq9O5w2UFUj2f7Pm4UZ3ZcAVxDEy3MVnB15WOtbB2CrAyKt%2BumVvnjephPvB2R%2FLvY7oqfVUYdkY4xK1bxzxyv4CkKYrhYpHIa5D%2BfwPXUu9lxLYdDMmENpEHXib%2FJYiKT%2F5EVjoYlO7SIvqeFU8ihu6XPpN6uq8U2ZBfzumetPgFyBKvZx24miASk8s7w63yvFfEk6qCKsHNkwcUcMartuvxoj8yQVbn8IRU09gSCVKvDKfKyGI0Rb9YjQ85SXCPgIO73CfcojX6OqVGinr20rJTCNwI8rpaFsV%2BOr1d7sEwRqqsU6z9hTL2wFNpaDnOAejpJsx%2BOGbkGwoMVB0LZQGnwWa9NbaOkDYgphVbjdMsAq5F4N5xZ63v9spUTRhjh60r8fDpN7AEVUwIqGWW%2FjP3ZenxgsGoPWrqwq5%2F%2F8k%2FXpM154m%2BRu8Uv9WtrlqlaHDONHZzmhDxWtqKgdfzf5l3JRMcpIFP7PnpNotXGfsOuqcx61%2FXh2sB%2BiIsx%2BWA6sn0nsc9z0ssOO6YSg0eRejygQZq0yRArClwPFqfPNE0lNCkB%2B%2B2ZLVjVhHpFtLkFKvATKmCPJNqFcCJQ%2BB%2F4YAcmqwsoFVzcnOV3pbcf9Ly8aREgxJsK%2F0bn5ToURSGNXKbJMVNvECGsp8Xc3t%2FtIfWbJOiUYwiZNdzWwfn3VM8KK8nRe79NIboVLC3Vq6e9mR2NKwKF2As0Ja4loh3flK2lghMrsQoe5765dyCQ%3D%3D%22%2C%22e%22%3A%226V9RSQfZ0kC32qhgY6QDEzDzyQHGJZnbDUsfkCo4mAeOu02fmTbbQ8TJwo5S8wQyxFTeobcgqh4RB6SlJnz3dfhP9_15dpnrtSqJnvya92AqwVDaHNZgpMg_4xpYvsTMEAm48ZHXJRNfarQNwp4bK1mKNiUQ6BaxVjGwhVLj0ByxNhHyyzjqjekUPz83kk7nuj_r0ZDUxx5o14nClKpcnA%22%7D"
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
    
    


    

        