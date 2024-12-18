# Fall Semester 2024
## Programming with Advanced Computer Languages

### Overview
This project focuses on processing, analyzing, and visualizing user-selected topics such as movies, scripts, or poetry. The main goal is to retrieve data from APIs, analyze keywords and statistics, and generate meaningful visualizations while providing additional details for movies.

---
The project comprises three main components:
1. **Reusable Functions:** Utility functions for data preprocessing, sentiment analysis, and visualization.
2. **Main Process:** Integration of the above components to execute the some analysis workflow.
3. **Interactive Interface:** A user-friendly interface for users to input their queries and receive results.

---
**Members**
- Yasmin Lützelschwab → [e-Mail](mailto:yasminesmeralda.luetzelschwab@student.unisg.ch)
- Stefan Meier → [e-Mail](mailto:stefan.meier@student.unisg.ch)
- Lars Nehr → [e-Mail](mailto:lars.nehr@student.unisg.ch)


### Main Process (Pseudo Code)

```plaintext
1. Load necessary libraries and modules:
   - Import support, input, API, file, analysis, and visualization modules.

2. Initialize traceability:
   - Enable traceability to track the execution flow.

3. Gather user input:
   - Prompt the user to select a topic (1: Movie, 2: Script, 3: Poetry).
   - Ask the user to enter a search query.

4. Fetch data from API:
   - Call the API to retrieve data based on the selected topic and search query.
   - Save the JSON response to 'bin/resources/json'.

5. Present titles to the user:
   - Extract available titles from the JSON file.
   - Display a list of titles for user selection.

6. Analyze the selected data:
   - Prepare statistics or keyword analysis for the selected title.
   - Save the results in a DataFrame.

7. Generate visualizations:
   - Create visual graphs and charts for the analyzed data.

8. Movie-specific workflow (if the selected topic is a movie):
   - Fetch additional movie details from a URL.
   - Save the fetched XML content to a DataFrame.
   - Display movie details (e.g., title, director, genre, year, rating) in table format.

9. Save outputs:
   - Store movie data in a CSV file in 'bin/resources/csv'.
   - Save visualizations in the output directory.

10. End the process:
    - Display a closing message thanking the user.

```


### Usage

project-root/
│
├── bin/
│   ├── resources/
│   │   ├── json/             # JSON data saved from API
│   │   ├── xml/              # XML responses saved locally
│   │   └── csv/              # Final movie or script data in CSV
│
├── modules/
│   ├── input_module.py       # User input handling
│   ├── support.py            # Traceability functions
│   ├── api_module.py         # API calls and XML/JSON processing
│   ├── file_module.py        # File handling (titles, saving/loading)
│   ├── analyse_module.py     # Data analysis (keywords, statistics)
│   └── visualisation_module.py  # Graph and chart generation
│
└── main.py                   # Entry point for the script


### Files and Structure

- `resources`: Save working files
- `src`: Pythong code
   - `cutom_classes`: To create custom Excpetions
   - `modules`: To structure functions by purpose
- `README.md`: Documentation for the project.


### License

This project is licensed under the MIT License. See the `LICENSE` file for details.


### Python3 Version 3.13.1