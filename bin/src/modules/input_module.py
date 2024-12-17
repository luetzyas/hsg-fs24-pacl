# imports
import custom_classes.custome_exceptions as ex
import modules.support as sup
import inspect as ip
import modules.api_module as api
import sys

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
    
    # console input handling
    print("Hi, welcome to our co-semtiment analysing tool.") 
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


