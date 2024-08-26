import requests

url = "https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals"

# API Request
response = requests.get(url, headers={"accept": "text/plain"})
print(response.status_code)

if response.status_code != 200:
    print("API Request un-successful. Please try again later")
    exit()

response_json = response.json()

# function to scan bands for each festival
def list_bandname_and_recordLabel(bands_data):
    for bands in bands_data:
        if "name" in bands:
            print("Band Name:", bands["name"])
        if "recordLabel" in bands:
            print("Record Label:", bands["recordLabel"])


for cnt in response_json:
    if "name" in cnt:  # if festival name is present
        print("Festival Name:", cnt["name"])
        # list Band Name and Record Label
        list_bandname_and_recordLabel(cnt["bands"])
    else:  # if festival name is not present
        print("Festival Name does not exist")
        list_bandname_and_recordLabel(cnt["bands"])
