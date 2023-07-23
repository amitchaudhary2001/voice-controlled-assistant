import requests

def search_bing(query):
    endpoint = 'https://api.bing.microsoft.com/v7.0/search'
    headers = {'Ocp-Apim-Subscription-Key': 'YOUR_SUBSCRIPTION_KEY'}

    params = {
        'q': query,
        'count': 5,  # Number of search results to retrieve
        'responseFilter': 'webpages',
        'textFormat': 'HTML'
    }

    response = requests.get(endpoint, headers=headers, params=params)
    data = response.json()
    print(data)

    # Parse the response to extract links
    links = []
    if 'webPages' in data and 'value' in data['webPages']:
        for result in data['webPages']['value']:
            links.append(result['url'])

    return data

# Example usage
search_query = 'Python programming'
results = search_bing(search_query)

for link in results:
    print(link)
