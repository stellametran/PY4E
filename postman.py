import requests

url = "https://c1978781149.ipg.web.cddbp.net/webapi/xml/1.0/"

payload = "<QUERIES>\r\n<LANG>eng</LANG>\r\n<COUNTRY>usa</COUNTRY>\r\n<AUTH>\r\n<CLIENT>1978781149-E94F77BF485E48BA6D360350D2F46021</CLIENT>\r\n<USER>27120364013420445-F6C3E6DB7ACA06E0E9700C89FAC70037</USER>\r\n</AUTH>\r\n<COUNTRY>NLD</COUNTRY>\r\n<QUERY CMD=\"TVCHANNEL_FETCH\"><GN_ID>251535482-645094EB842B6873A0860AE9DFDB2C6B</GN_ID>\r\n<OPTION><PARAMETER>SELECT_EXTENDED</PARAMETER>\r\n<VALUE>IMAGE</VALUE></OPTION>\r\n<OPTION><PARAMETER>IMAGE_SIZE</PARAMETER><VALUE>220</VALUE></OPTION></QUERY></QUERIES>\r\n"
headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "8bbd9400-47e9-1e1d-1e33-ff77a4dadf4b"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)