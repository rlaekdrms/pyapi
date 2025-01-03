import os
import requests 
from dotenv import load_dotenv


load_dotenv()


appkey = os.getenv("APPKEY")
appsecret = os.getenv("APPSECRET")


url = "https://openapi.koreainvestment.com:9443/oauth2/tokenP"

headers = {
    "Content-Type":"application/json"
    }

data = {
  "grant_type": "client_credentials",
  "appkey": appkey,
  "appsecret":appsecret
}
res = requests.post(url,headers=headers,json=data)
print(res.status_code)

access_token = f"{res.json()['token_type']} {res.json()['access_token']}"


url = "https://openapi.koreainvestment.com:9443/uapi/domestic-stock/v1/quotations/inquire-price"

params = {
    "fid_cond_mrkt_div_code": "J",
    "fid_input_iscd": "000660"
}

headers = {
    "authorization":access_token,
    "appkey":appkey,
    "appsecret":appsecret,
    "tr_id":"FHKST01010100"
}
res = requests.get(url,params=params,headers=headers)
print(res.status_code)
print(res.json())




url = "https://openapi.koreainvestment.com:9443/uapi/domestic-stock/v1/quotations/search-stock-info"

params = {
    "PRDT_TYPE_CD": "300",
    "PDNO": "Q500001"
}

headers = {
    "authorization":access_token,
    "appkey":appkey,
    "appsecret":appsecret,
    "tr_id":"CTPF1002R",
    "custtype":"P",
    "content-type":"application/json; charset=utf-8"

}
res = requests.get(url,params=params,headers=headers)
print(res.status_code)
print(res.json())




url = "https://openapi.koreainvestment.com:9443/uapi/domestic-stock/v1/quotations/inquire-price-2"

params = {
    "fid_cond_mrkt_div_code": "J",
    "fid_input_iscd": "000660"
}

headers = {
    "authorization":access_token,
    "appkey":appkey,
    "appsecret":appsecret,
    "tr_id":"FHKST01010100",
    "content-type":"content-type",
    "custtype":"P"
}
res = requests.get(url,params=params,headers=headers)
print(res.status_code)
print(res.json())




url = "https://openapi.koreainvestment.com:9443/uapi/domestic-stock/v1/quotations/inquire-ccnl"

params = {
    "fid_cond_mrkt_div_code": "J",
    "fid_input_iscd": "000660"
}

headers = {
    "authorization":access_token,
    "appkey":appkey,
    "appsecret":appsecret,
    "tr_id":"FHKST01010100"
}
res = requests.get(url,params=params,headers=headers)
print(res.status_code)
print(res.json())