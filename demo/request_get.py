# _*_ coding : utf-8 _*_
# @Time : 2024/4/30 0:19
# @Author : aiqinghua
# @File : request_get
# @Project : prs_v5
import requests

url = "https://10.0.81.124/nta/asset/ck/security_overview/riskAsset"
data = {
    "ts": [1713801600000,1714405895776]
}
# data["ts"] = "1714405895776"
headers = {"Token": "15f5e828a3ee4274c6066be4eeeae0ec"}

res = requests.get(url=url, params=data, headers=headers, verify=False)
print(res.url)
print(res.json())