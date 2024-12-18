# imports
import custom_classes.custome_exceptions as ex
import modules.support as sup
import inspect as ip
import modules.api_module as api
import sys
import pandas as pd
from tabulate import tabulate 

# input user console to select category for co-sentiment analyse 
def user_input(trace: bool) -> None:
    sup.traceability_handling_prints(trace, ip.currentframe().f_code.co_name)

    # save user options in 2-dim array 
    # [option number, display message, category name]
    options = [
        [1, "You want to analyse movie scripts?", "Movie Scripts"],  # 0: scripts
        [2, "You want to analyse lyrics?", "Song Lyrics"],           # 1: lyrics
        [3, "You want to analyse peotries?", "Poetry Texts"]         # 2: poetry
    ]

    try:
        selection = user_input_options(trace, options)
        return selection
    except ex.InvalidOption as e:
        print(e)
        sys.exit(1)


# user input handling
def user_input_options(trace: bool, options):
    sup.traceability_handling_prints(trace, ip.currentframe().f_code.co_name)
    
    try:
        # console input handling
        print("Hi, welcome to our analysing tool.") 
        print("Please enter one of the following options:")

        #print options array
        for option in options:
            print(f"{option[0]}: {option[1]}")

        #save input option
        i_int = int(input("Your selection: ")) 

        # validate the input
        valid_options = [option[0] for option in options]
        if i_int not in valid_options:
            raise ex.InvalidOption(f"Invalid option. Please choose {valid_options}.")
        
        # print user selection
        print(f"You selected: {options[i_int-1][2]}")
        return options[i_int-1][0]
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)
    

# function for the user to select the title to continue from the api response
def select_title_to_analyse(trace: bool, titles):
    sup.traceability_handling_prints(trace, ip.currentframe().f_code.co_name)

    # Display titles with numbers
    print("\nAvailable Titles:")
    for idx, title in enumerate(titles, start=1):
        print(f"{idx}: {title}")

    # Prompt user for selection
    while True:
        try:
            user_input = input("\nEnter the number of the title to analyze: ").strip()
            if not user_input.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            selected_idx = int(user_input)
            if 1 <= selected_idx <= len(titles):
                selected_title = titles[selected_idx - 1]
                print(f"You selected: {selected_title}")
                return selected_title
            else:
                raise ex.InvalidOptionf("Invalid number. Please choose a number between 1 and {len(titles)}.")
        except ex.InvalidOption as e:
            print(f"Error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(1)

# function to print more data about the selected movie
def get_more_data_about_movie(trace: bool, df: pd.DataFrame):
    sup.traceability_handling_prints(trace, ip.currentframe().f_code.co_name)

    try:
        # Validate the DataFrame is not empty
        if df.empty:
            print("No movie data available to display.")
            return

        # Safely extract the movie title
        title = df['Title'].iloc[0] if 'Title' in df.columns and not df['Title'].isnull().iloc[0] else "Unknown"

        # Ask user for more data
        user_input = input(f"Do you want to know more about your selected movie '{title}'? (yes/no): ").strip().lower()

        # Match user input
        match user_input:
            case "yes":
                # Prepare table data
                table_data = {
                    "Title": [df['Title'].iloc[0] if 'Title' in df.columns else "N/A"],
                    "Genre": [df['Genre'].iloc[0] if 'Genre' in df.columns else "N/A"],
                    "Writer": [df['Director'].iloc[0] if 'Director' in df.columns else "N/A"],  # Assuming Director as Writer
                    "Year": [df['Year'].iloc[0] if 'Year' in df.columns else "N/A"],
                    "Rating": [df['Rating'].iloc[0] if 'Rating' in df.columns else "N/A"],
                }

                # Convert to DataFrame for tabulate
                table_df = pd.DataFrame(table_data)
                
                # Print as a table
                print("\nMovie Details:")
                print(tabulate(table_df, headers="keys", tablefmt="grid", showindex=False))
            
            case "no":
                return
            case _:
                raise ex.InvalidOption("Your entry is not valid. Please enter 'yes' or 'no'.")

    except ex.InvalidOption as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)
