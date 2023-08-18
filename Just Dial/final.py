import requests
import pandas as pd


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'requestTime': '2023-2-17%2010%3A58%3A56%20pm',
    'securityToken': '2a282a2b2a292f29282d202d2e',
    'Origin': 'https://www.justdial.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.justdial.com/Bangalore/Hotels-in-Majestic/nct-10255012',
    # 'Cookie': 'ppc=; scity=Bangalore; pincode=; alat=; alon=; sarea=Majestic; _ctok=6d4ae64aa8c721673852606506mwh4FCskjoiiFy6D8y4Cutm43hgnDF495AD4; web_visit=2023-01-16T07:03:26.506Z; jd_www_nxt=1; _abck=8ED9B570F2D19455996D36E6A8FCC19B~0~YAAQXkYDF4emPSiGAQAADMBmYAnGh2VPWXKP4fIoOs7pwzkdKyZTN6A0QzHN88i4cBrDMWfpEnkXtZy3nC9N5zft9TtOc02uXeolzDtS6uTRiHitrI1kaGoJXOf6ShCUJvOF3qqPYOBcyUt5SU/2tfGA/vfMdOWO6mOTzivUJwI6NLcauBHM8C9Te4VKWn/Tn9cuKjS/rktvoZHQ4IyLNLUCwQg/IlPA1K96acsHiaZb6ErNdk9f0OCca1Mybsd3reb8z8AWJfqMSJcthabdV3p+88irHtEVL5H1F+o51PXkhDM0HLKBx7q6NymeI7zR9u5EXyi7ifVQQTtVeCh2B+LMzUeZOYPW72EZmn3mLQj01onWpLAugVCM8mFSUFYkK+nnvJhoS3urI1gGHbn0ME2wjTbiHAxEnv+o~-1~-1~-1; _ga_5PY4KYQRFS=GS1.1.1676654055.12.1.1676654925.58.0.0; _ga=GA1.1.1796392966.1673852665; RT="z=1&dm=justdial.com&si=e4844edb-e223-45aa-ab88-b91b200b1453&ss=le8sj7or&sl=1&tt=20l&rl=1"; g_state={"i_p":1676740463443,"i_l":2}; rfr=gen; ppc=; Continent=AS; Ak_City=BANGALORE; AKA_A2=A; ak_bmsc=635695AEBABB6220158D45A941D67659~000000000000000000000000000000~YAAQckYDF5ScqTCGAQAAvhFdYBLuMYDoXiNhhGNgPJmzxvptrsiVDqZ0opdQ0sbOOIbbxgWJv+JxfW1xEzSCxu8cPVCKiAmhcWG2XROLIOSgC7ShLv6ILBy2LrU7Ytcd3lHJYV+i+3MleCLbHhVYw6dDK7S2BL8BlNybHX0qFDZYavTdJmb8rClKARR/H8Am4ycvsbcwQ4K3rz1VH8+7twg3LEzEK4eaBwjlmejBBVD1wFafbDQ3+qS1dKGrhH3+hr1VevtTanCwVSStQaV4pdF/l1csaiFRXeskZLQgIWHSZyChfIHbUAvGSy/j8f3JIQteiTpqAiJOPD+166olGVkUTJbWTK+ORuSdSGlKIN+MAFcSTc4Oq/RCFyJSFKrzhqZdi1zxQNYC/2wKSE0cwww+LhVVMMBCw82Wn4C0g1BgaKX89oQfOX7C8o/Q37isR61XpH1i2JU+IiZpwhmGYZ3B5oHvr9Al5M7HYz9nVG4VHBmXLktAwnBHDI97k84=; bm_sz=89ED1325894C49D28475E7816A7F7C16~YAAQckYDF3acqTCGAQAARQpdYBLK/ii3UlxU/+jyvNQq0mWoycipl9Lo0q+4WBWqZXbtflinr6r3lmsemOCWZfwDPILULR0tRU1SAOJKxy9uK0cZQxbUSam70F1ZHBY+vjSz+VrioYutHnkdMlZf7vYG8FNCcBa0DMqsUBORg8zLLI7Da9euuif/x+0QJX/xXxns817sf81jTEfLfqxR9CwqQvKuBncdAbZZJeusdGIw+nvKagHzdQgIvsd8UGzSeOJHjc/k0XaBndcBcuIn+hInTDzaaALFGNwyP4HdOSrnJvNnbw==~4403249~3289409; _gid=GA1.2.777436271.1676654056; bm_sv=6B8F7BCD4D2AB7BA364A9DBCFB1D8536~YAAQXkYDF+SuPSiGAQAAu4BqYBLUwdzj+xLru5wka5ZyqsdWZDEZZh9epdCUL5DSxekL0iGK1zWp4a12NP6D4OdFmnYeyJYwrNhot+dQN0NyyXYPwiDlaZb9B6zC2CBLsxgcRDvhzY3lgFAX93mkBSLqQoRob87UE2TMS1HVj1rcxppGt56XFHlO3n406u5zIANgddmfhKZDcpfAona41qKP4mfjAiXP4RS/5g/lFkm0ZrLyPt7s7QunbKEeZNd2s3NbgA==~1; web_pop_ltr={"count":2,"time":"2023-02-17T17:20:46.521Z"}; lpg=hk; TKY=5dc37780a37cf0f51dba55b00c65f9e79bff974697dc7688fc31cb8d07e382b7; main_city=Bangalore; akcty=Bangalore; PHPSESSID=f5bd15c4a349d93be18ecc278ee25a2e; inweb_city=Bangalore; bdapop=080PXX80.XX80.160711162205.Y1Q1; bd_pop_opened=1; web_prevcatidsarr=["10255012"]; _gat_gtag_UA_1220997_2=1; _gat_UA-1220997-15=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
    }

cookies = {
    'ppc': '',
    # 'scity': 'Bangalore',
    'pincode': '',
    'alat': '',
    'alon': '',
    # 'sarea': 'Majestic',
    '_ctok': '6d4ae64aa8c721673852606506mwh4FCskjoiiFy6D8y4Cutm43hgnDF495AD4',
    'web_visit': '2023-01-16T07:03:26.506Z',
    'jd_www_nxt': '1',
    '_abck': '8ED9B570F2D19455996D36E6A8FCC19B~0~YAAQXkYDF4emPSiGAQAADMBmYAnGh2VPWXKP4fIoOs7pwzkdKyZTN6A0QzHN88i4cBrDMWfpEnkXtZy3nC9N5zft9TtOc02uXeolzDtS6uTRiHitrI1kaGoJXOf6ShCUJvOF3qqPYOBcyUt5SU/2tfGA/vfMdOWO6mOTzivUJwI6NLcauBHM8C9Te4VKWn/Tn9cuKjS/rktvoZHQ4IyLNLUCwQg/IlPA1K96acsHiaZb6ErNdk9f0OCca1Mybsd3reb8z8AWJfqMSJcthabdV3p+88irHtEVL5H1F+o51PXkhDM0HLKBx7q6NymeI7zR9u5EXyi7ifVQQTtVeCh2B+LMzUeZOYPW72EZmn3mLQj01onWpLAugVCM8mFSUFYkK+nnvJhoS3urI1gGHbn0ME2wjTbiHAxEnv+o~-1~-1~-1',
    '_ga_5PY4KYQRFS': 'GS1.1.1676654055.12.1.1676654925.58.0.0',
    '_ga': 'GA1.1.1796392966.1673852665',
    'RT': '"z=1&dm=justdial.com&si=e4844edb-e223-45aa-ab88-b91b200b1453&ss=le8sj7or&sl=1&tt=20l&rl=1"',
    'g_state': '{"i_p":1676740463443,"i_l":2}',
    'rfr': 'gen',
    'ppc': '',
    'Continent': 'AS',
    # 'Ak_City': 'BANGALORE',
    'AKA_A2': 'A',
    'ak_bmsc': '635695AEBABB6220158D45A941D67659~000000000000000000000000000000~YAAQckYDF5ScqTCGAQAAvhFdYBLuMYDoXiNhhGNgPJmzxvptrsiVDqZ0opdQ0sbOOIbbxgWJv+JxfW1xEzSCxu8cPVCKiAmhcWG2XROLIOSgC7ShLv6ILBy2LrU7Ytcd3lHJYV+i+3MleCLbHhVYw6dDK7S2BL8BlNybHX0qFDZYavTdJmb8rClKARR/H8Am4ycvsbcwQ4K3rz1VH8+7twg3LEzEK4eaBwjlmejBBVD1wFafbDQ3+qS1dKGrhH3+hr1VevtTanCwVSStQaV4pdF/l1csaiFRXeskZLQgIWHSZyChfIHbUAvGSy/j8f3JIQteiTpqAiJOPD+166olGVkUTJbWTK+ORuSdSGlKIN+MAFcSTc4Oq/RCFyJSFKrzhqZdi1zxQNYC/2wKSE0cwww+LhVVMMBCw82Wn4C0g1BgaKX89oQfOX7C8o/Q37isR61XpH1i2JU+IiZpwhmGYZ3B5oHvr9Al5M7HYz9nVG4VHBmXLktAwnBHDI97k84=',
    'bm_sz': '89ED1325894C49D28475E7816A7F7C16~YAAQckYDF3acqTCGAQAARQpdYBLK/ii3UlxU/+jyvNQq0mWoycipl9Lo0q+4WBWqZXbtflinr6r3lmsemOCWZfwDPILULR0tRU1SAOJKxy9uK0cZQxbUSam70F1ZHBY+vjSz+VrioYutHnkdMlZf7vYG8FNCcBa0DMqsUBORg8zLLI7Da9euuif/x+0QJX/xXxns817sf81jTEfLfqxR9CwqQvKuBncdAbZZJeusdGIw+nvKagHzdQgIvsd8UGzSeOJHjc/k0XaBndcBcuIn+hInTDzaaALFGNwyP4HdOSrnJvNnbw==~4403249~3289409',
    '_gid': 'GA1.2.777436271.1676654056',
    'bm_sv': '6B8F7BCD4D2AB7BA364A9DBCFB1D8536~YAAQXkYDF+SuPSiGAQAAu4BqYBLUwdzj+xLru5wka5ZyqsdWZDEZZh9epdCUL5DSxekL0iGK1zWp4a12NP6D4OdFmnYeyJYwrNhot+dQN0NyyXYPwiDlaZb9B6zC2CBLsxgcRDvhzY3lgFAX93mkBSLqQoRob87UE2TMS1HVj1rcxppGt56XFHlO3n406u5zIANgddmfhKZDcpfAona41qKP4mfjAiXP4RS/5g/lFkm0ZrLyPt7s7QunbKEeZNd2s3NbgA==~1',
    # 'web_pop_ltr': '{"count":2,"time":"2023-02-17T17:20:46.521Z"}',
    'lpg': 'hk',
    'TKY': '5dc37780a37cf0f51dba55b00c65f9e79bff974697dc7688fc31cb8d07e382b7',
    # 'main_city': 'Bangalore',
    # 'akcty': 'Bangalore',
    'PHPSESSID': 'f5bd15c4a349d93be18ecc278ee25a2e',
    # 'inweb_city': 'Bangalore',
    'bdapop': '080PXX80.XX80.160711162205.Y1Q1',
    'bd_pop_opened': '1',
    'web_prevcatidsarr': '["10255012"]',
    '_gat_gtag_UA_1220997_2': '1',
    '_gat_UA-1220997-15': '1',
    }

params = {
    'searchReferer': 'gen|hk',
    }


just_dial_data = []


def crawl_contact_no_popup(allocateid,params,cookies,headers):
    json_data = {
        'allocateid': allocateid,
        'ask_mob': 0,
        'is_verified': 0,
        'ncatid': '10255012',
        'page': 'results',
        }
    response = requests.post(
        'https://www.justdial.com/api/callallocate',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
        )

    js = response.json()
    try:
        contact = js['result']['vn'] , js['result']['an'].get('l' and 'm')
    except:
        contact = None
    # print('contact', contact)

    return contact
    


def crawl_list_page_detail(results):
    for details in results:
        name = details[1]
        address = details[12]
        city = details[18]
        rating = details[7]
        votes = details[16]
        if details[8] == '1':
            verification = 'JD Verified'
        else :
            verification = 'Not Verified '
        allocateid = details[49]
        detail_url = 'https://www.justdial.com/' + details[59]
        print('allocate id', allocateid)

        contact = crawl_contact_no_popup(allocateid,params,cookies,headers)

        data = {
            "NAME" : name,
            "CITY" : city,
            "ADDRESS" : address,
            "CONTACT NO." : contact,
            "VERIFICATION" : verification,
            "RATING" : rating,
            "VOTES" : votes,
        }
        print(data)
        just_dial_data.append(data)

        

def crawl_list_page_ajax(cookies,params,headers,url):
    page_no = 0
    while True:
        page_no += 1
        json_data = {
            'median_latitude': '',
            'median_longitude': '',
            'city': url.split('/')[3],
            #  'search': 'Hotels',
            # 'area': 'Majestic',
            'lat': '',
            'long': '',
            'national_catid': url.split('-')[-1],
            # 'nextdocid': '080PXX80.XX80.170921200851.J5C6,080PXX80.XX80.191104193953.X1J7,080PXX80.XX80.200929235436.V6P2,080PXX80.XX80.170921194324.V2U4,080PXX80.XX80.200701220630.E5Y9,080PXX80.XX80.190926173301.K3C5,080PXX80.XX80.170113002322.R6F8,080PXX80.XX80.170928165220.Y7R3,080PXX80.XX80.170913130512.P5R7,080PXX80.XX80.101221150112.I5B7',
            'stype': 'category_list',
            'opt': '',
            'pg_no': page_no,
            'nearme': 0,
            'checkin': 1676764800,
            'checkout': 1676851200,
            'attribute_values': '',
            # 'mncatname': 'Hotels',
            'darea_flg': 0,
        }

        response = requests.post(
            'https://www.justdial.com/api/resultsPageListing',
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data,
        )

        print(page_no,response)
        js = response.json()
        if js['results']['data']:
            results = js['results']['data']
        else:
            break

        crawl_list_page_detail(results)
        
#  Enter just dial category url to scrap the data
url = 'https://www.justdial.com/Bangalore/Second-Hand-Car-Buyers/nct-10425711'
crawl_list_page_ajax(cookies,params,headers,url)

df = pd.DataFrame(just_dial_data)
df.to_excel('just_dial_data.xlsx', index=False)

print('!!!!!!!!!!!!completed!!!!!!!!!!!!!!')