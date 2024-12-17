# imports
import custom_classes.custome_exceptions as ex
import modules.support as sup
import inspect as ip
import modules.api_module as api

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
    