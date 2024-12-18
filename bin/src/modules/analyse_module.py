# imports
import json
from collections import Counter, defaultdict
import modules.support as sup
import inspect as ip
import sys
import pandas as pd 

# constants
FILE_PATH= 'bin/resources/json/api_response.json'


# This functions is an entry point an prepare process for the data
def prepare_data_for_statistics(trace: bool, search: str, topic: int):
    sup.traceability_handling_prints(trace, ip.currentframe().f_code.co_name)

    # load json
    data = load_json(trace)

    # entry based on topic
    match topic:
        case 1:
            title = "title"
            author = "writer"
            text = "subtitle"
        case 2:
            title = "song"
            author = "artist"
            text = "album"
        case 3:
            title = "title"
            author = "poet"
            text = "poem"

    # 1. Count poems per poet
    ctr = ctr_title_per_author(trace, topic, search, data, author)

    # 2. Search for a keyword in texts
    keywords_res = search_keyword_in_text(trace, data, search, title, author, text)

    # 3. Display analysis results
    display_analysis(trace, ctr, keywords_res, search)

    # 4. save results in dataframe
    return save_results_in_dataframe(trace, ctr, keywords_res)
    

# Load and parse JSON
def load_json(trace: bool):
    sup.traceability_handling_prints(trace, ip.currentframe().f_code.co_name)

    try:
        with open(FILE_PATH, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading file: {e}")
        sys.exit(1)


# 1. Count titles per author
# movie scripts: search per writer
# song lyrics: search per artist
# poetry: search per poet
def ctr_title_per_author (trace: bool, topic: int, search: str, data, author):
    sup.traceability_handling_prints(trace, ip.currentframe().f_code.co_name)

    # load json for analyses
    data = load_json(trace)

    # init Counter()
    ctr  = Counter()

    # count items per author
    for entry in data.get("result", []):
        author_name = entry.get(author, f"Unknown {author}")
        ctr[author_name] += 1
    return ctr


# 2. Search for a keyword in text
def search_keyword_in_text(trace: bool, data, keyword: str, title: str, author: str, text: str):
    sup.traceability_handling_prints(trace, ip.currentframe().f_code.co_name)

    search_results = defaultdict(list)

    # find keywords in text
    for entry in data.get("result", []):
        title_name = str(entry.get(title, f"Unknown {title}"))
        author_name = str(entry.get(author, f"Unknown {author}"))
        text_content = str(entry.get(text, f"Unknown {text}"))
        
        if keyword.lower() in text_content.lower():
            search_results[author_name].append(title_name)

    return search_results


# 3. Display analysis results
def display_analysis(trace: bool, ctr, search_results, search: str):
    sup.traceability_handling_prints(trace, ip.currentframe().f_code.co_name)
    
    # display results
    print(f"Total number of texts: {len(ctr)}")
    print(f"Total number of authors: {sum(ctr.values())}")
    
    print("\nTop 3 authors with the most text:")
    for author, count in ctr.most_common(3):
        print(f"- {author}: {count}")

    # reduce console, only for testing
    """print(f"\nAuthor containing the Search '{search}':")
    if search_results:
        for author, titles in search_results.items():
            print(f"\n{author}:")
            for title in titles:
                print(f"  - {title}")
    else:
        print("No authors found with the given keyword.")
    """

# 4. save results into dataframe
def save_results_in_dataframe(trace: bool, ctr: Counter, search_results: defaultdict):
    sup.traceability_handling_prints(trace, ip.currentframe().f_code.co_name)

    # Convert Counter to a DataFrame
    author_stats = pd.DataFrame(ctr.items(), columns=['Author', 'Text_Count'])
    
    # Prepare search results for DataFrame
    search_data = []
    for author, titles in search_results.items():
        for title in titles:
            search_data.append({
                'Author': author,
                'Title': title
            })
    keyword_df = pd.DataFrame(search_data)

    # Merge results
    merged_df = pd.merge(author_stats, keyword_df, on='Author', how='outer')
    print(merged_df)
    return merged_df