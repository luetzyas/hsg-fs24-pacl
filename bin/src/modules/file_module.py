# imports
import inspect as ip
import modules.support as sup
import json
import os
import custom_classes.custome_exceptions as ex
import sys
import pandas as pd

# constants
FILE_PATH= 'bin/resources/json/api_response.json'


# get titles when the json request was a movie 
def get_titles_from_file(trace: bool, topic: int):
    sup.traceability_handling_prints(trace, ip.currentframe().f_code.co_name)

    try:
        # Ensure file exists
        if not os.path.exists(FILE_PATH):
            print(f"File not found: {FILE_PATH}")
            return "No title found"

        # Open and parse JSON file
        with open(FILE_PATH, 'r') as f:
            data = json.load(f)

        # Extract titles from the 'result' list
        match topic:
            case 1:
                titles = [
                    f"{entry.get('title', 'No Movie')} ({entry.get('writer', 'Unknown Writer')})"
                    #f"{entry.get('title', 'No Movie')} ({entry.get('subtitle', 'Unknown Writer')})"
                    for entry in data.get("result", [])
                    if isinstance(entry, dict)
                ]
            case 2:
                titles = [
                    f"{entry.get('song', 'No Song')} ({entry.get('artist', 'Unknown Artist')}, {entry.get('album', 'Unkown Album')})"
                    for entry in data.get("result", [])
                    if isinstance(entry, dict)
                ]
            case 3:
                titles = [
                    f"{entry.get('title', 'No Peotry')} ({entry.get('poet', 'Unknown Poet')})"
                    for entry in data.get("result", [])
                    if isinstance(entry, dict)
                ]
        
        # check if titles are empty
        if not titles:
            raise ex.NotFound(f"No results found.")
        else: return titles
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return "No title found"
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
    except ex.NotFound as e:
        print(f"Error: {e}")
        sys.exit(1)

# save dataframe in csv file
def save_df_to_csv_file(trace:bool, df: pd.DataFrame):
    sup.traceability_handling_prints(trace, ip.currentframe().f_code.co_name)

    try:    
        # check if dataframe is empty
        if df.empty:
            raise ex.NotFound("No data to save.")
        print(df)
        # Save DataFrame to CSV
        output_dir = "bin/resources/csv/"
        os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists
        csv_filename = os.path.join(output_dir, "movie_result.csv")
        df.to_csv(csv_filename, index=False)
        print(f"Movie details saved to {csv_filename}")
    except ex.NotFound as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)