import requests

# account credentials
username = 'rykorua'
password = 'G$.dM3Z+w2-iCqU'

# get the access token

auth_res = requests.post(
    "https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))
if auth_res.status_code == 200:
    # if response is ok, get the token
    access_token = auth_res.content.decode()
    print("[!] Got access token:", access_token)
else:
    print("[!] Cannot get access token, exiting...")
    exit()

# construct the request headers with authorization
headers = {"Authorization": f"Bearer {access_token}"}

# get the group UID associated with our account
groups_res = requests.get(
    "https://api-ssl.bitly.com/v4/groups", headers=headers)
if groups_res.status_code == 200:
    # if response is OK, get the GUID
    groups_data = groups_res.json()['groups'][0]
    guid = groups_data['guid']
else:
    print("[!] Cannot get GUID, exiting...")
    exit()

# the url you want to shorten
url = input('Paste the url that you want to shorten: ')
# make the POST request to get shortened URL for 'url'
shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten",
                            json={"group_guid": guid, "long_url": url}, headers=headers)
# if shorten_res.status_code == 200:
#if response is ok, get the shortened URL
link = shorten_res.json().get("link")
print("Shortened URL: ", link)
