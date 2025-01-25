# Imports the requests library, which allows us to make HTTP requests (like GET or POST) to web pages.
import requests
# Imports the BeautifulSoup class from the bs4 library, which helps with parsing HTML and XML documents.
from bs4 import BeautifulSoup
# Imports urllib.parse, which provides functions for working with URLs 
import urllib.parse

# Defines a function called google_search that accepts a query (the search term) and num_results (defaulting to 10), which specifies the number of results to retrieve.
def google_search(query, num_results=10):
    # Sets the base URL for Google’s search page.
    #headers = {...}: Sets the User-Agent header to mimic a browser request, helping to avoid blocks or captchas from Google.
    base_url = "https://www.google.com/search"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }

    # Defines the parameters for the search request, with q for the query term and num for the number of results
    params = {
        "q": query,
        "num": num_results
    }

    # Sends a GET request to Google’s search URL with the specified headers and params. The response (HTML content) is stored in the response variable.
    response = requests.get(base_url, headers=headers, params=params)

    # Checks if the request was successful by verifying the HTTP status code. A code of 200 means the request was successful.
    if response.status_code != 200:
        print("Failed to retrieve results")
        return []

    # Initializes a BeautifulSoup object called soup to parse the HTML content from response.text using the "html.parser" parser.
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Debugging: Uncomment the following line to print the HTML content if results are not appearing
    # print(soup.prettify())
    
    # Initializes an empty list named results that will store each search result’s title, link, and description.
    results = []

    # Try alternative selectors if the default class-based selection fails
    for result in soup.select('.tF2Cxc'):
        #title_element = result.select_one('h3'): Attempts to find the first <h3> tag within each result block, which generally contains the title.
        #link_element = result.select_one('a'): Attempts to find the first <a> tag within each result block, which typically contains the link (URL).
        #description_element = result.select_one('.VwiC3b'): Attempts to find the description text within each result block using the .VwiC3b class.
        title_element = result.select_one('h3')
        link_element = result.select_one('a')
        description_element = result.select_one('.VwiC3b')

        # Check if all elements are present
        if title_element and link_element and description_element:
            results.append({
                "title": title_element.get_text(),
                "link": link_element['href'],
                "description": description_element.get_text()
            })

    # Check if results are empty
    if not results:
        print("No results found. The HTML structure might have changed.")
    
    return results


# Usage
query = "HTML tutorial"
results = google_search(query, num_results=10)

# Print results
#for idx, result in enumerate(results, start=1):: Loops over each result in results, with idx as the 1-based index.
#print(f"{idx}. {result['title']}"): Prints the index and title of each result.
#print(f" Link: {result['link']}"): Prints the link (URL) of each result.
#print(f" Description: {result['description']}\n"): Prints the description, followed by a newline for spacing.
for idx, result in enumerate(results, start=1):
    print(f"{idx}. {result['title']}")
    print(f"   Link: {result['link']}")
    print(f"   Description: {result['description']}\n")
