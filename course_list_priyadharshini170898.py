import requests
import json

url = "https://www.udemy.com/api-2.0/users/91139214/subscribed-profile-courses/?fields[course]=badges,buyable_object_type,content_info,discount,free_course_subscribe_url,has_closed_caption,headline,image_100x100,image_240x135,image_480x270,image_50x50,instructional_level,instructional_level_simple,is_in_personal_plan_collection,is_in_premium,is_in_user_subscription,is_paid,is_user_subscribed,is_wishlisted,last_update_date,learn_url,num_published_lectures,num_reviews,objectives_summary,price,price_detail,price_serve_tracking_id,published_time,rating,title,tracking_id,url,visible_instructors&page=1&page_size=12"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Cookie': '__udmy_2_v57r=366809cf2643465791b6810850030313; __udmy_1_a12z_c24t=VGhlIGFuc3dlciB0byBsaWZlLCB0aGUgdW5pdmVyc2UsIGFuZCBldmVyeXRoaW5nIGlzIDQy; _pxvid=8bd5d686-47f3-11ed-abdf-527056505a47; ext_name=ojplmecpdpgccookcobabopnaifgidhf; ud_firstvisit=2022-10-09T16:58:07.879687+00:00:1ohZct:-_qevJ82cUqG9VJYlPjVRt52DDI; __ssid=121abad9e49db23328488d183fd3473; _gcl_au=1.1.744783343.1665334699; _rdt_uuid=1665334699418.eb4a8055-3066-442d-b136-2b93a3b63810; _fbp=fb.1.1665334699715.935425772; G_ENABLED_IDPS=google; client_id=bd2565cb7b0c313f5e9bae44961e8db2; FPAU=1.1.744783343.1665334699; ud_cache_brand=INen_US; ud_cache_campaign_code=ST20MT103122; ud_cache_marketplace_country=IN; ud_cache_version=1; ud_cache_language=en; ud_cache_device=None; __cfruid=1cf1269cc1b65ef047b90fc10421f9beba0b5546-1667194792; pxcts=c50211bc-58de-11ed-b090-6373686f5a56; blisspoint_fpc=d28d01c3-a868-46a5-9f28-11b565180880; ki_s=225191:0.0.0.0.2;227428:0.0.0.0.0;228057:0.0.0.0.0; ki_r=; intercom-session-sehj53dd=RjBoaGEwdlpMK2RXMXREMTZlWThVMXA1SDE1SWJBUlBEY2xqQ0hKdmRyNy9BeFUyL3hITE9NNzFKUVVrSGZFZC0tcVdVTlJFL1BpbnVoWklSY3RwZG5xdz09--decbe3dea3db2c77856844f4d8adf71a53de445a; seen=1; ud_cache_release=2f2b6601d556491d1984; _gid=GA1.2.72540612.1667283411; ud_credit_unseen=0; ud_credit_last_seen=None; __udmy_4_a12z=c180ea87e18f1bf819b94e7d16a7b2af0a8f916b7941ed4c4fba7b1cbf664085; csrftoken=DvqfyKpQ7Z9ujeA2q3y30QpaenClmzPgGDMHnFuBztnOaw9rFCVO9jLTprM8npU1; access_token=vxp27BfFSxkU8F5WDukA3wJWnLg2mEVpySvpz5Bh; ud_last_auth_information="{\\"backend\\": \\"google\\"\\054 \\"suggested_user_email\\": \\"priyadharshini221099@gmail.com\\"\\054 \\"suggested_user_name\\": \\"Priyadharshini\\"\\054 \\"suggested_user_avatar\\": \\"https://img-c.udemycdn.com/user/50x50/anonymous_3.png\\"}:1opkaK:NasgZ6I_eQr8jfbZX3WPIuowyus"; dj_session_id=93n4v15x51adau9nomyllda642tqkn7j; ud_user_jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTcwOTYyODEwLCJlbWFpbCI6InByaXlhZGhhcnNoaW5pMjIxMDk5QGdtYWlsLmNvbSIsImlzX3N1cGVydXNlciI6ZmFsc2UsImdyb3VwX2lkcyI6W119.kS0cjhb7dCa2gSorP8oXDZyQ1Q6dr8ub3_4DgfO0xvY; ud_cache_price_country=SG; ud_cache_user=170962810; ud_cache_logged_in=1; G_AUTHUSER_H=2; ab.storage.deviceId.5cefca91-d218-4b04-8bdd-c8876ec1908d={"g":"dbbe875b-8229-b8f6-e2d5-e57665d90a0a","c":1665334698649,"l":1667283443541}; ab.storage.userId.5cefca91-d218-4b04-8bdd-c8876ec1908d={"g":"170962810","c":1667283443539,"l":1667283443542}; __cf_bm=p5Q2kRqUTMglyhgmDTkHlPexZSNbLRAn4Dbmpf2PbCk-1667283735-0-AVR9qv6WjoV9KuUqUm/oYtXGAzsujPJOPJ4tK1Wb/+UgtQvIDqUk19n4rZjwEZON9rQyaqqmMMUWpgg70WDyPBW7JKlXpwah/+PC0nbNjoPKWXDXnP7Cruu3YV9UTaOlLkC9Ee7/ewRzbSx7lNZSnmUyLr8nVnMWyGkiLyftOfvQ; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Nov+01+2022+12:00:43+GMT+0530+(India+Standard+Time)&version=202209.2.0&isIABGlobal=false&hosts=&consentId=02a46c68-f138-4950-bbd2-9ef506449b24&interactionCount=1&landingPath=NotLandingPage&groups=C0003:1,C0005:1,C0004:1,C0001:1,C0002:1&AwaitingReconsent=false; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; _px3=0209e84c0f313bd0556b4ac35ebb9c8e69cc55ed975dce5e096630ba709c9d7b:k+mlVrEfh2ABJwhZJq+H+5KOsRJRBNUfaJeosfPucIDmGKP3BVbSFP8t/AmucaO78qfoH10rSsLnl2oKJyK4Cw==:1000:wTfP788wagjHFRLaPbie8IUY5+p53gUa1uNcgKDD+3or+kv6OKW5iIWjQqmW9woah9r473JVHDPCdDNkHIMQ+E5z/KjtInM/sxpFobAI8CiHC+weGg8BJrdaZb2agL2vVdqMd1OucIT0a4fOsh3SVTu4igrSfF6ffnxdsq1/OFXDkb072ZHHxdVFqJZJPEYN31eWT1j30lgM47I/5Qf/Bw==; _px2=eyJ1IjoiYjY4YmYzMDAtNTlhZS0xMWVkLTlhNjctNmJmNzQ2NGVlYTAxIiwidiI6IjhiZDVkNjg2LTQ3ZjMtMTFlZC1hYmRmLTUyNzA1NjUwNWE0NyIsInQiOjE2NjcyODQ3NDM5MzcsImgiOiJlOTcwZTlkZDU4OTljMjdmOThkOGYyNDg0YmRmYzE3NDZkNDhhYjI4ZTk4ZDc1NDZjMmFjYjlkYWE0YmQyZWQzIn0=; ab.storage.sessionId.5cefca91-d218-4b04-8bdd-c8876ec1908d={"g":"6d5d8624-448d-f9bd-cb1d-37c5c63b4e93","e":1667286046961,"c":1667283443540,"l":1667284246961}; _ga_7YMFEFLR6Q=GS1.1.1667283392.4.1.1667284247.56.0.0; _ga=GA1.1.1760874241.1665334696; ki_t=1665334699438;1667283396293;1667284247163;3;26; evi="3@3sIYFYSzm1ZWjQtF5U-p_94RzzcZZtkf8TTMPah7B8cQ5i4umeJLS7Bww9BIxetQBWW3yF3jcOm-NHOa98ZAETkcYrjEf_oge8WJ"; ud_rule_vars=eJxljdEKwiAARX9l-FobV52mfstAnHMlBZK6vYz9e4Migl4v95yzkeryNdQw2TWWWFM2XEoF7Wcme95LcdF0lIpCCYCDU258SvcYiGnINpA55lLfrJ1cDcOxD4SBsZaihW6oNEIZ9J06JGAnwAADOR-vhzvQmhZ_szW7eY7elrRkH-zqcnTj42MrIf0AOTyXUP5rtAVtIA2HEX0nuIb41nayvwBAa0Sq:1opknW:tXVGg1P94sNR2hu_5x3cEhTT3ck; eventing_session_id=rOCfD442SUuUOoEGjjLeXg-1667286055762; __cf_bm=hhvkF06GMp2Cgf3abzjhTjf.2ifHy1VDvk2wh1gG33A-1667284577-0-AcsySEQ8Z+HMgjmjUrpzZ+kN/lOslkY3QAQOi86qousxLwJaHcGW9YKX+upDB05U6RPCmOaNUaRRX7/ILlrj9bA=; __cfruid=90ef9ca664dc1a7499552294c303709303e94f47-1667284577; evi="3@KMdDLeUCk62WyQvWb42OCIqwiw6fPZRS-vWXJKhgOhwHcc_O-R1ywkqh"; seen=1; ud_cache_brand=INen_US; ud_cache_campaign_code=ST20MT103122; ud_cache_device=None; ud_cache_language=en; ud_cache_logged_in=1; ud_cache_marketplace_country=IN; ud_cache_price_country=SG; ud_cache_release=2f2b6601d556491d1984; ud_cache_user=170962810; ud_cache_version=1; ud_rule_vars="eJxljV0LgyAYRv9KeLsVr69m5W8RxEybbEym1k303xf7gMFuH55zzkaKSbMrbtJryKHEJJkQPQzWo-CMi7Yb6Ch6Cn0LwIBRJm2M1-CIrMimiA8plzerJ1OcOnZFEBBrCjWjFQiJKIE3Qys4xxOABFDkfLxu5kBLXOxFl2S8D1bnuCTr9GpSMOPtY4tpNvdgf6DkHovL_0Vaw6vIhKRdg9gzhG9xJ_sTeL1GQA==:1opksj:163gi35Lpxn7G1X0ccbjHm2YKQQ"'
}

response = requests.request("GET", url, headers=headers, data=payload).json()




#count number of response pages 
c = 0

#concatenate response results
data = []
data.extend(response["results"])

#iterate until last past
while(response["next"] is not None):
    response = requests.request("GET", response["next"], headers=headers, data=payload).json()
    data.extend(response["results"])
    c += 1
else:
    print("Total Pages = " , c)

print(len(data))

with open('priyadharshini170898.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
# #construction of courses list
# courses_list = []

# for item in data:
#     for item_1 in item:
#         courses_list.append(item_1)
    
# #conversion of courses list to json 

# data_json = json.dumps(courses_list)
# data_parsed = json.loads(data_json)


# #get all paid courses

# paid = 0

# #construction of hours and minutes dictionary
# dict_courses_hours = {}
# dict_courses_mins = {}

# for item in data_parsed:
#     if(item['is_paid']):
#         #getting hourses and minutes in total  
#         time = item['content_info'].split(" ")
#         if(time[len(time)-1] == 'hours' or time[len(time)-1] == 'hour' ):
#             dict_courses_hours[item['title']] = float(time[0])
#         else:
#             dict_courses_mins[item['title']] = float(time[0])
#         paid += 1
        
# #sorting dictoary based on hours and minutes value 
# hours_list = sorted(dict_courses_hours.items(), key=lambda x: x[1])    

# mins_list = sorted(dict_courses_mins.items(), key=lambda x: x[1])  

# print("/////* hours list */////")

# # for item in hours_list:
# #     print(item)
    
# print("/////* minutes list */////")

# for item in mins_list:
#     print(item)
    
# #total courses count
# print("total courses = " , len(data_parsed))

# print("All paid courses count = ",paid)

# print("Length of the courses in hours = ",len(dict_courses_hours))

# print("Length of the courses in mins = ",len(dict_courses_mins))