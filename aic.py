import json
import urllib.request
import urllib.error

# Constants
AIC_API_URL = "https://api.artic.edu/api/v1/artworks"

page = 1
limit = 10 # MUST be lower than 100

# GET_DATA
# Function to get data from a given URL, it expects a JSON response.
def get_data(url):
    try:
        response = urllib.request.urlopen(url)
        raw_data = response.read()
        json_data = json.loads(raw_data)
        return json_data
    except urllib.error.HTTPError as error:
        print(f"ERROR {error.code}\n{error.reason} -> {error.url}\n")
        return error.code

# CONSTRUCT_REQUEST
# Function to build the request URL
def construct_request(api, page='', limit='', artwork_id=''):
    if artwork_id:
        artwork_id = f"/{artwork_id}"
    if page:
        page = f"page={page}"
    if limit:
        limit = f"limit={limit}"
    if page or limit:
        params = f"?{page}&{limit}"
    request = f"{api}{artwork_id or ''}{params or ''}"
    return request

url = construct_request(AIC_API_URL, 1, 1, 12345)
print(url)
data = get_data(url)
print(data)
