import requests

LOGIN_URL = "https://www.wechall.net/login"
YOUR_NAME = "luk6xff"
YOUR_PASS = "11071990"

# Store session
session = requests.Session()

# Login first to get cookies
r = session.post(LOGIN_URL,  data={'username':YOUR_NAME, 
                                   'password':YOUR_PASS,
                                   'bind_ip':'on',
                                   'login':'Login'}, 
                             headers={'Host': 'www.wechall.net',
                                      'Connection': 'keep-alive',
                                      'Content-Length': '57',
                                      'Origin': 'https://www.wechall.net',
                                      'Cache-Control': 'max-age=0',
                                      'Upgrade-Insecure-Requests': '1',
                                      'Content-Type': 'application/x-www-form-urlencoded',
                                      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
                                      'Sec-Fetch-Mode': 'navigate',
                                      'Sec-Fetch-User': '?1',
                                      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                                      'Sec-Fetch-Site': 'same-origin',
                                      'Referer': 'https://www.wechall.net/logout',
                                      'Accept-Encoding': 'gzip, deflate, br',
                                      'Accept-Language': 'en-US,en;q=0.9,pl;q=0.8',
                                      'Cookie': 'WC=12054242-0-uoYF3Bszzc0nOYEGW'})

# Get a message
r = session.get("https://www.wechall.net/challenge/training/programming1/index.php?action=request")
message = r.text
print("MESSAGE: " + message)

# Send message back to WeChall
r = session.post("https://www.wechall.net/challenge/training/programming1/index.php?answer={}".format(message))
print(r.text)