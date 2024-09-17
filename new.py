import requests

cookies = {
    '_ga': 'GA1.3.426743895.1725413195',
    '_gid': 'GA1.3.514855093.1726385692',
    'locale': 'zhtw',
    'session': 'eyJsb2NhbGUiOiJ6aHR3IiwicmVkaXJlY3RfdG8iOiJodHRwczovL2pnaXJsLmRkbnMubmV0LyIsInVpZCI6MTQwMjAsImxnbiI6IkIxMDQwMTAwNiIsImNsYXNzIjoiMSIsInBlcmlvZCI6IkNTSUUxMjEwXzExMzEiLCJzdWJtaXRfbG5nIjoiMSJ9',
    'session.sig': 'qH2y8TsvYU0-TXJdn3J2-8yP3G4',
    'io': 'vHu4Ky8POncukpvJADPg',
    '_gat': '1',
    '_ga_Z7XFV74L6Q': 'GS1.3.1726452300.4.1.1726452925.0.0.0',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': '_ga=GA1.3.426743895.1725413195; _gid=GA1.3.514855093.1726385692; locale=zhtw; session=eyJsb2NhbGUiOiJ6aHR3IiwicmVkaXJlY3RfdG8iOiJodHRwczovL2pnaXJsLmRkbnMubmV0LyIsInVpZCI6MTQwMjAsImxnbiI6IkIxMDQwMTAwNiIsImNsYXNzIjoiMSIsInBlcmlvZCI6IkNTSUUxMjEwXzExMzEiLCJzdWJtaXRfbG5nIjoiMSJ9; session.sig=qH2y8TsvYU0-TXJdn3J2-8yP3G4; io=vHu4Ky8POncukpvJADPg; _gat=1; _ga_Z7XFV74L6Q=GS1.3.1726452300.4.1.1726452925.0.0.0',
    'Pragma': 'no-cache',
    'Referer': 'https://jgirl.ddns.net/problems/domain/0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://jgirl.ddns.net/problem/0/1004', cookies=cookies, headers=headers)
print(response.text[ response.text.find('1004') : response.text.find('1004') + 100 ])
