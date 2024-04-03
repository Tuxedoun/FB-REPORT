import requests, re, json, random, os, sys, time

def h1():
    return {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Prefers-Color-Scheme':'light','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Viewport-Width':'924'}
def h2():
    return {'accept': '*/*', 'accept-encoding': 'gzip, deflate', 'accept-language': 'en-US,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'https://www.facebook.com', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '', 'sec-ch-ua-full-version-list': '', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '', 'sec-ch-ua-platform': '', 'sec-ch-ua-platform-version': '', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

def clear():
    if 'linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')

def report(c,target):
    cc = {'cookie':c}
    req = requests.get('https://www.facebook.com/',headers=h1(),cookies=cc,allow_redirects=True).text.replace('\\','')
    av = re.search(r'"actorID":"(.*?)"',str(req)).group(1)
    aa = str(random.randrange(1,6))
    hs = re.search(r'"haste_session":"(.*?)"',str(req)).group(1)
    ccg = re.search(r'"connectionClass":"(.*?)"',str(req)).group(1)
    rev = re.search(r'"__spin_r":(.*?),',str(req)).group(1)
    sb = re.search(r'"__spin_b":"(.*?)"',str(req)).group(1)
    st = re.search(r'"__spin_t":(.*?),',str(req)).group(1)
    hsi = re.search(r'"hsi":"(.*?)"',str(req)).group(1)
    dts = re.search(r'"DTSGInitialData",\[\],{"token":"(.*?)"}',str(req)).group(1)
    jaz = re.search(r'jazoest=(.*?)"',str(req)).group(1)
    lsd = re.search(r'"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1)
    dat = {
        'av':av,
        '__user':av,
        '__a':aa,
        '__hs':hs,
        'dpr':'1.5',
        '__ccg':ccg,
        '__rev':rev,
        '__spin_r':rev,
        '__spin_b':sb,
        '__spin_t':st,
        '__hsi':hsi,
        '__comet_req':'15',
        'fb_dtsg':dts,
        'jazoest':jaz,
        'lsd':lsd
    }
    ses = re.search('"sessionID":"(.*?)"',str(req)).group(1)
    gql = 'https://www.facebook.com/api/graphql/'
    v1 = {
        "input":{"content_id":target,"entry_point":"PROFILE_REPORT_BUTTON","location":"PROFILE_SOMEONE_ELSE","trigger_event_type":"REPORT_BUTTON_CLICKED","nt_context":None,"trigger_session_id":ses},
        "scale":1
    }
    dat.update({
        'fb_api_caller_class':'RelayModern',
        'fb_api_req_friendly_name':'CometIXTFacebookContentTriggerRootQuery',
        'variables':json.dumps(v1),
        'server_timestamps':True,
        'doc_id':'6769900669784116'
    })
    r1 = requests.post(gql,data=dat,headers=h2(),cookies=cc).json()
    dat.update({
        'fb_api_caller_class':'RelayModern',
        'fb_api_req_friendly_name':'CometFacebookIXTNextMutation',
        'server_timestamps':True,
        'doc_id':'6914576615289569'
    })
    ct = r1['data']['ixt_content_trigger']['screen']['view_model']['context']
    srl = r1['data']['ixt_content_trigger']['screen']['view_model']['serialized_state']
    v2 = {
        "input":{"frx_tag_selection_screen":{"context":ct,"serialized_state":srl,"show_tag_search":False,
        "tags":["PROFILE_FAKE_ACCOUNT"]},"actor_id":dat['__user'],
        "client_mutation_id":"1"},
        "scale":1
    }
    dat.update({'variables':json.dumps(v2)})
    r2 = requests.post(gql,data=dat,headers=h2(),cookies=cc).json()
    ct = r2['data']['ixt_screen_next']['view_model']['context']
    srl = r2['data']['ixt_screen_next']['view_model']['serialized_state']
    v3 = {
        "input":{"frx_report_confirmation_screen":{"context":ct,"serialized_state":srl},"actor_id":dat['__user'],"client_mutation_id":"3"},
        "scale":1
    }
    dat.update({'variables':json.dumps(v3)})
    r3 = requests.post(gql,data=dat,headers=h2(),cookies=cc).json()
    ct = r3['data']['ixt_screen_next']['view_model']['context']
    srl = r3['data']['ixt_screen_next']['view_model']['serialized_state']
    v4 = {
        "input":{"frx_post_report_process_timeline":{"context":ct,"serialized_state":srl},
        "actor_id":dat['__user'],"client_mutation_id":"4"},
        "scale":1
    }
    dat.update({'variables':json.dumps(v4)})
    r4 = requests.post(gql,data=dat,headers=h2(),cookies=cc).json()
    if 'You have submitted a report' in str(r4):
        return True
    else:
        return False

def main():
    clear()
    cookie = input('\033[93m [›] Enter cookie :\033[91m ')
    uid = input('\033[93m [›] Enter target uid :\033[91m ')
    result = report(cookie, uid)
    t = time.localtime()
    tt = "{}/{}/{} {}:{}:{}".format(t.tm_mon, t.tm_mday, t.tm_year, t.tm_hour, t.tm_min, t.tm_sec)
    if result:
        print(f'\033[92m [{tt}] reported : {uid} \033[0m')
    else:
        print(f'\033[91m [{tt}] failed : {uid} \033[0m')

main()