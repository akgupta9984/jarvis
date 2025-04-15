import requests
import time
from fake_useragent import UserAgent

url = "https://www.flipkart.com/mobile-phones-store?fm=neo%2Fmerchandising&iid=M_25cbf4ac-8a29-43b1-b180-3609bf64593c_1_372UD5BXDFYS_MC.ZRQ4DKH28K8J&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Mobiles_ZRQ4DKH28K8J&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L0_view-all&cid=ZRQ4DKH28K8J"

r = requests.get(url)

session = requests.session()

headers = {
    'user-Agent' : UserAgent().random,
    'Accept-language' : 'en-US,en;q=0.9',
    'Accept-Encoding' : 'gzip, deflate, br',
    'connection' : 'Keep-alive',
    'Referer': 'https://www.google.com'
}

time.sleep(2)
r = session.get(url, proxies=proxies, headers=headers)
with open("file.html", "w") as f:
    f.write(r.text)
 