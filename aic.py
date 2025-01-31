import json
import urllib.request
import urllib.error
import random

# Constants
AIC_API_URL = "https://api.artic.edu/api/v1/artworks"
COLLECTION_SIZE = 99999

previous_works = set()
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
 
# INIT THE REQUEST
# Create a random ID
# Check if it's been shown before

def create_random_id():
    random_id = random.randrange(1, COLLECTION_SIZE)
    if random_id not in previous_works:
        previous_works.add(random_id)
        return random_id
    else:
        create_random_id()

# GET_ARTWORK
# Generates a random ID and requests it
# If 404, generates a new ID and requests it
def get_artwork():
    random_id = create_random_id()
    print(random_id)
    url = construct_request(AIC_API_URL, 1, 1, random_id)
    print(url)
    data = get_data(url)
    print(data)

get_artwork()
