# Fall Semester 2024
## Programming with Advanced Computer Languages

[ ] TODO: finish readme.md after enhancement

### Overview
This project focuses on analyzing sentiment trends and variations in topics using natural language processing techniques. The main goal is to process, analyze, and visualize sentiment data to uncover meaningful patterns.

---
The project comprises three main components:
1. **Variations in Topics:** Exploration of sentiment variation across topics.
2. **Reusable Functions:** Utility functions for data preprocessing, sentiment analysis, and visualization.
3. **Main Process:** Integration of the above components to execute the complete sentiment analysis workflow.

---
**Members**
- Yasmin Lützelschwab → [e-Mail](mailto:yasminesmeralda.luetzelschwab@student.unisg.ch)
- Stefan Meier → [e-Mail](mailto:stefan.meier@student.unisg.ch)
- Lars Nehr → [e-Mail](mailto:lars.nehr@student.unisg.ch)


### Main Process (Pseudo Code)

```plaintext
1. Load necessary libraries and datasets.
2. Preprocess the data:
   - Clean and tokenize text data.
   - Remove stopwords and apply stemming or lemmatization.
3. Perform sentiment analysis:
   - Use a pre-trained sentiment analysis model or library.
   - Assign sentiment scores or labels to text.
4. Analyze topic variations:
   - Group data by topics.
   - Calculate sentiment statistics for each topic.
5. Visualize the results:
   - Generate graphs and charts to represent sentiment trends.
6. Save outputs:
   - Store processed data and visualizations in the output directory.
7. Document insights and observations.
```


### Usage

1. **Run the main process:**
   Execute the Jupyter Notebook `Co-Sentiment_Analysis_Process.ipynb` to run the complete workflow.
2. **Explore Variations in Topics:**
   Use the `Co-Sentiment_Analysis_Variations_In_Topics.ipynb` notebook to analyze topic-based sentiment variations.
3. **Use Utility Functions:**
   Refer to `Co_Sentiment_Analysis_Functions.ipynb` for reusable functions to preprocess data and perform analysis.


### Files and Structure

- `Co-Sentiment_Analysis_Variations_In_Topics.ipynb`: Notebook for topic variation analysis.
- `Co_Sentiment_Analysis_Functions.ipynb`: Collection of utility functions.
- `Co-Sentiment_Analysis_Process.ipynb`: Main notebook for integrating the workflow.
- `data/`: Directory to store input datasets.
- `outputs/`: Directory to save analysis results and visualizations.
- `README.md`: Documentation for the project.


### License

This project is licensed under the MIT License. See the `LICENSE` file for details.


### Python3 Version 3.13.1