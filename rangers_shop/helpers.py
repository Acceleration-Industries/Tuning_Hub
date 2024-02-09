import requests
import requests_cache

# Install and configure requests-cache to cache API responses
requests_cache.install_cache('image_cache', backend='sqlite')

def get_image(search):
    url = "https://google-search72.p.rapidapi.com/imagesearch/"
    querystring = {
        "q": search,
        "gl": "us",
        "lr": "lang_en",
        "num": "10",
        "start": "0"
    }
    headers = {
         'X-RapidAPI-Key': '2e0b32e3admsh9e5edb2fe19207bp1d681djsn63057cdf50a8',
    'X-RapidAPI-Host': 'google-search72.p.rapidapi.com'
    }

    try:
        # Make the API request
        response = requests.get(url, headers=headers, params=querystring)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Check if 'items' key is present in the response data
            if 'items' in data:
                # Extract the URL of the first image from the response
                img_url = data['items'][0].get('originalImageUrl', '')
                return img_url
            else:
                # If 'items' key is not present, return None
                return None
        else:
            # If the request was not successful, print an error message and return None
            print(f"Error: {response.status_code}")
            return None
    except requests.RequestException as e:
        # If an exception occurs during the request, print the exception and return None
        print(f"Request Exception: {e}")
        return None

# Example usage:
# image_url = get_image('cats')
# if image_url:
#     print("Image URL:", image_url)
# else:
#     print("Failed to fetch image URL.")
