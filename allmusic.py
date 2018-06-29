import requests

def search_producer_on_allmusic(producer_name):
    base_url = 'http://www.allmusic.com/search/songs/'
    query = producer_name.replace(' ', '+')
    search_url = base_url + query

    response = requests.get(search_url)
    if response.status_code != 200:
        print('Error: Failed to retrieve search results.')
        return

    # Process the search results here...
    # Add your code to extract the relevant information

    # Example:
    # result = response.json()
    # for item in result['songs']:
    #     print(item['title'])

# Usage example:
search_producer_on_allmusic('Fantom')