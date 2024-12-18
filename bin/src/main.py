# Import own components
import modules.input_module as i
import modules.support as sup
import modules.api_module as api
import modules.file_module as fi
import modules.analyse_module as am
import modules.visualisation_module as vm

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

# analyse keyword per author and save results in df
res_df = am.prepare_data_for_statistics(trace, search, topic)

# work on visualisation of the gathered data
vm.generate_visualisations(trace, search, res_df)

# link processing only possible for movies
if topic == 1: 
    # additional movie path for users
    api.fetch_data_from_URL(trace, selected_title)

    # save XML in dataframe
    df = api.save_xml_soup_in_df(trace)

    # print movie data
    i.get_more_data_about_movie(trace, df)


print("Thank you for using our Tool.")