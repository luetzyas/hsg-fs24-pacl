# Import own components
import modules.input_module as i
import modules.support as sup
import modules.api_module as api
import modules.file_module as fi

# guiding parameters
trace = True

# show tracebility status in console
sup.tracebility_handling_start(trace)

# save the user input for movie, script or peotry
topic = i.user_input(trace)

# save the searchtext from the user input
search = str(input("Please enter your search: ")) 

# save json from api in bin/resources/json
api.call_api(trace, topic, search)

# select titles for user selection
titles = fi.get_titles_from_file(trace, topic)

# user select title from list
selected_title = i.select_title_to_analyse(trace, titles)




