# StoryQA: A Dataset for Question and Answer Generation

This repository contains the StoryQA dataset. It contains CSV files of children's stories from [Project Gutenberg](https://www.gutenberg.org/) and a set of questions and answers developed by highly trained coders for each story. 

Papers about this dataset and Machine Learning models trained on this dataset have been submitted for publication. Progress on those papers will be updated here.

## Files

- `data/` - contains the data for the stories and the questions and answers.
  - `test` - contains the data to test a model
  - `val` - contains the data to validate a model
  - `train` - contains the data to train a model
	- `[title]-story.csv` - the story files contain the text of the story, broken down into sections.
	- `[title]-questions.csv` - the question files contain question, answers, and category data about each question

### Files in Progress
- `meta-db.csv` - contains metadata about the database as a whole
- `meta-story.csv` - contains metadata about each individual story (also used to loop over the stories and questions in the dataset)
- `starter.py` - some basic starter code to either get the whole dataset as one pandas DataFrame or apply a function to each file in the dataset