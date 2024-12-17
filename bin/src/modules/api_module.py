# imports
import inspect as ip
import modules.support as sup
import custom_classes.custome_exceptions as ex
import requests
import json
import sys

# constants
API_USER_ID = 12982
API_TOKEN = 'Lk05MrlNF2ijBEeZ'
API_RESULT_FORMAT = 'json'
    # https://www.scripts.com/scripts_api.php                   
SCRIPTS_API = 'https://www.stands4.com/services/v2/scripts.php' # https://www.stands4.com/services/v2/scripts.php?uid=12982&tokenid=Lk05MrlNF2ijBEeZ&term=casablanca&format=json
LYRICS_API = 'https://www.stands4.com/services/v2/lyrics.php' # https://www.stands4.com/services/v2/lyrics.php?uid=1001&tokenid=tk324324&term=forever%20young&artist=Alphaville&format=json
POETRY_API = 'https://www.stands4.com/services/v2/poetry.php' # https://www.stands4.com/services/v2/poetry.php?uid=1001&tokenid=tk324324&term=grass&format=json
    # Mimic a browser by adding headers to resolve HTTP ERROR 403
HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Connection": "keep-alive"
        }
        

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