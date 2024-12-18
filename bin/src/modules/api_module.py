# imports
import inspect as ip
import modules.support as sup
import custom_classes.custome_exceptions as ex
import requests
import json
import sys
import re
from bs4 import BeautifulSoup
import pandas as pd

# constants
API_USER_ID = 12982
API_TOKEN = 'Lk05MrlNF2ijBEeZ'
API_RESULT_FORMAT = 'json'
    # https://www.scripts.com/scripts_api.php                   
SCRIPTS_API = 'https://www.stands4.com/services/v2/scripts.php' # https://www.stands4.com/services/v2/scripts.php?uid=12982&tokenid=Lk05MrlNF2ijBEeZ&term=casablanca&format=json
LYRICS_API = 'https://www.stands4.com/services/v2/lyrics.php' # https://www.stands4.com/services/v2/lyrics.php?uid=1001&tokenid=tk324324&term=forever%20young&artist=Alphaville&format=json
POETRY_API = 'https://www.stands4.com/services/v2/poetry.php' # https://www.stands4.com/services/v2/poetry.php?uid=12982&tokenid=Lk05MrlNF2ijBEeZ&term=home&format=json
    # Mimic a browser by adding headers to resolve HTTP ERROR 403
HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Connection": "keep-alive"
        }
FILE_PATH = 'bin/resources/json/api_response.json'

# Utility function to save API response to a file
def save_json_to_file(trace: bool, data):
    sup.traceability_handling_prints(trace, ip.currentframe().f_code.co_name)

    try:
        # set filename based on topic
        filename = "bin/resources/json/api_response.json"

        # open file (overwrite)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"Response saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")


# Function to set the params term together
def set_params(trace: bool, term: str):
    sup.traceability_handling_prints(trace, ip.currentframe().f_code.co_name)

    return {
        "uid": API_USER_ID,
        "tokenid": API_TOKEN,
        "term": term,
        "format": API_RESULT_FORMAT
    }


# entry funtion to determine right API process
def call_api(trace: bool, topic: int, search: str):
    sup.traceability_handling_prints(trace, ip.currentframe().f_code.co_name)

    try:
        # determine params for api call
        params = set_params(trace, search)

        # select API based on user entry
        match topic:
            case 1:
                curr_api = SCRIPTS_API # movie script json handling
            case 2:
                curr_api = LYRICS_API # song lyrics json handling
            case 3:
                curr_api = POETRY_API # poetry json handling

        # Make the GET request
        response = requests.get(curr_api, params=params, headers=HEADERS)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Print and return the JSON response
        # print("API Response:", response.json())
        data = response.json()

        # Check if the response is empty or does not contain "results"
        if not data:
            raise ex.NotFound(f"No valid results found with search: '{search}'.")

        # save response to file
        save_json_to_file(trace, data)
        return data
    except ex.NotFound as e:
        print(f"Error: {e}")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)    

# get data from url
def fetch_data_from_URL(trace:bool, title: str):
    sup.traceability_handling_prints(trace, ip.currentframe().f_code.co_name)

    # search in json file with title
    try:
        # Open and parse the JSON file
        with open(FILE_PATH, 'r') as f:
            data = json.load(f)

        # Clean the title to exclude everything after '(', if it exists
        clean_title = re.split(r'\s*\(', title)[0].strip()
        
        # Find the URL corresponding to the provided title
        url = None
        for entry in data.get("result", []):
            if entry.get("title", "").lower() == clean_title.lower():
                url = entry.get("link")
                break

        if not url:
            raise ValueError(f"Title '{clean_title}' not found in the JSON file.")
        
        print(f"Fetching data from URL: {url}")

        # Send GET request to fetch page content
        #response = requests.get(url)
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Use prettify() to format HTML
        formatted_content = soup.prettify()

        # Write the content to an XML file
        with open('bin/resources/xml/html_response.xml', 'w', encoding='utf-8') as xml_file:
            xml_file.write(formatted_content)

        # Extract and return the raw HTML content as a string
        return formatted_content

    except requests.exceptions.RequestException as e:
        print(f"ERROR: Failed to fetch URL - {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"ERROR: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)


# save url-response in a dataframe
def save_xml_soup_in_df(trace: bool):
    sup.traceability_handling_prints(trace, ip.currentframe().f_code.co_name)
    
    try:
        # get data from XML-File
        #df = pd.read_xml('bin/resources/xml/html_response.xml', parser='etree')
        # Read XML file and parse with BeautifulSoup
        with open('bin/resources/xml/html_response.xml', 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, "html.parser")

        # Extract movie details
        title = soup.find("h1", id="disp-script-title").get_text(strip=True)
        synopsis = soup.find("div", id="disp-script-subtitle").get_text(strip=True).replace("Synopsis:", "")

        # Genre
        genre_div = soup.find("div", class_="awards")
        genre = "N/A"
        if genre_div and "Genre" in genre_div.get_text():
            genre = genre_div.get_text(strip=True).replace("Genre:", "")

        # Director
        director_div = soup.find("div", class_="awards")
        director = "N/A"
        if director_div and "Director" in director_div.get_text():
            director = director_div.get_text(strip=True).replace("Director(s):", "")

        # Actors
        actors_div = soup.find("div", class_="awards")
        actors = "N/A"
        if actors_div and "Actors" in actors_div.get_text():
            actors = actors_div.get_text(strip=True).replace("Actors:", "")

        # Year
        year_dd = soup.find("dt", string=lambda x: x and "Year" in x)
        year = year_dd.find_next_sibling("dd").get_text(strip=True) if year_dd else "N/A"


        # IMDB Rating
        imdb_rating_a = soup.find("a", href=lambda x: x and "imdb.com" in x)
        rating = imdb_rating_a.get_text(strip=True) if imdb_rating_a else "N/A"

        # Extract script content
        script_body = soup.find("div", id="disp-quote-body")
        script_content = "\n".join([p.get_text(strip=True) for p in script_body.find_all("p")]) if script_body else "N/A"


        # Prepare DataFrame
        movie_data = {
            "Title": [title],
            "Synopsis": [synopsis],
            "Genre": [genre],
            "Director": [director],
            "Actors": [actors],
            "Year": [year],
            "Rating": [rating],
            "Script": [script_content]
        }
        
        df = pd.DataFrame(movie_data)

        # check if dataframe is empty
        if df.empty:
            raise ex.DataFrame_Empty("The Dataframe for Movie Data is empty.")
        
        return df
    except ex.DataFrame_Empty as e:
        print(f"ERROR: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)  # Return empty DataFrame on error