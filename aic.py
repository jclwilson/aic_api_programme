import json
import urllib.request
import urllib.error
import random
import os

# Constants
AIC_API_URL = "https://api.artic.edu/api/v1/artworks"
COLLECTION_SIZE = 99999
SAVE_FILE = 'already_seen.txt'
FIELDS = ['has_not_been_viewed_much', 'exhibition_history', 'description', 'api_link', 'title', 'date_display', 'date_start', 'date_end', 'is_on_view', 'gallery_title', 'artwork_type_title', 'artist_title']

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

# GET_SEEN
# This function returns the contents of saved in the file. 
def get_seen():
    with open(SAVE_FILE, 'rt') as file:
        seen_ids = set(file.readlines())
        return seen_ids

# SAVE_SEEN
# This function appends the given artwork_id to the local save file.
def save_seen(artwork_id):
    with open(SAVE_FILE, 'a') as file:
        file.write(f'{artwork_id}\n')

# INIT THE REQUEST
# Create a random ID
# Check if it's been shown before
def create_random_id(already_seen):
    random_id = random.randrange(1, COLLECTION_SIZE)
    if random_id not in already_seen:
        save_seen(random_id)
        return random_id
    else:
        create_random_id()

# GET_ARTWORK
# Generates a random ID and requests it
# If 404, generates a new ID and requests it
def get_artwork(already_seen):
    random_id = create_random_id(already_seen)
    url = construct_request(AIC_API_URL, 1, 1, random_id)
    response = get_data(url)
    return response

# PARSE_ARTWORK
# This function accepts json data representing one artwork and parses the fields.
# It prints the info to the terminal.
def parse_artwork(data):
    artwork = data['data']
    print(f"This {artwork['artwork_type_title']} titled '{artwork['title']}' is by {artwork['artist_title']}. It was made in {artwork['date_display']}.")
    if artwork['description']:
        print(f"{artwork['description']}")
    if artwork['has_not_been_viewed_much'] == True:
        if artwork['is_on_view'] == True:
            print(f"It is on view in the {artwork['gallery_title']}")
    print('### DETAILS ###')
    for key, value in artwork.items():
        if key in FIELDS:
            print(f"{key} = {value}")

# The main function runs when directly called, and not when the file is [imported as part of a module.](https://www.digitalocean.com/community/tutorials/python-main-function)

def main():
    if not os.path.exists(SAVE_FILE):
        save_seen('')
    already_seen = get_seen()
    data = get_artwork(already_seen)
    if data != 404:
        parse_artwork(data)

if __name__ == '__main__':
    main()
