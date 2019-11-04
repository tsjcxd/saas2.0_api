import execjs
import requests
import os
# password = execjs.compile(open(r"https://g.alicdn.com/sd/nvc/1.1.151/nvc.js")

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

resp = requests.get("https://g.alicdn.com/sd/nvc/1.1.151/nvc.js")
# print(resp.text)
# js_path =  os.path.dirname(os.path.abspath(__file__))
# js_path = os.path.join(js_path, 'abc.js')

# with open(js_path, 'r+') as f:
#     f.write(resp.text)



# with open(js_path, 'r') as f:
#     content = f.read()
#     print(content)
content = resp.text
ctx = execjs.compile("var window = {}; {}")
val = ctx.call('window.getNVCVal')
print(ctx)


# Passwd = execjs.compile(open(r"https://g.alicdn.com/sd/nvc/1.1.151/nvc.js").read().decode("utf-8")).call('getNVCVal')
# print(Passwd)