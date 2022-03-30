# FairytaleQA: A Dataset for Question and Answer Generation

This repository contains the FairytaleQA dataset. It contains CSV files of children's stories from [Project Gutenberg](https://www.gutenberg.org/) and a set of questions and answers developed by highly trained coders for each story. 

Thus far, three papers have been published that include this dataset. Check back here for updates on any further papers using this dataset.

- Xu, Y., Wang, D., Yu, M., Ritchie, D., Yao, B., Wu, T., Zhang, Z., Li, T., Bradford, N., Sun, B., Hoang, T., Sang, Y., Hou, Y., Ma, X., Yang, D., Peng, N., Yu, Z., & Warschauer, M. (2022). Fantastic questions and where to find them: FairytaleQA- An authentic dataset for narrative comprehension. *Association for Computational Linguistics*.
- Yao, B., Wang, D., Wu, T., Zhang, Z., Li, T., Yu, M., & Xu, Y. (2022). It is AI's Turn to Ask Humans a Question: Question and Answer Pair Generation for Children's Storybooks with FairytaleQA Dataset. *Association for Computational Linguistics*. [https://doi.org/10.48550/arXiv.2109.03423](https://doi.org/10.48550/arXiv.2109.03423)
- Zhang, Z., Xu, Y., Wang Y., Yao, B., Ritchie, D., Wu, T., Yu, M., Wang, D., & Li, T. (2022). Storybuddy: A human-AI collaborative agent for parent-child interactive storytelling. *In Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems*. [https://doi.org/10.1145/3491102.3517479](https://doi.org/10.1145/3491102.3517479)

## Descriptive Statistics

### Database Size

Total Stories: 278

Total Sections: 4095

Avg Sections per Story: 14.73021582733813

Avg Words per Section: 146.18144078144078

Avg Words per Story: 2153.2841726618703

Total Questions: 10580

Avg Questions per Section: 2.583638583638584

Avg Questions per Story: 38.05755395683453

### Breakdown of Question Types

#### Explicit/Implicit

Explicit:             7880 questions - 74.48% of dataset

Implicit:             2700 questions - 25.52% of dataset

#### Question Attributes

Character:            1204 questions - 11.38% of dataset

Feeling:              1167 questions - 11.03% of dataset

Setting:               636 questions -  6.01% of dataset

Causal Relationship:  2949 questions - 27.87% of dataset

Prediction:            708 questions -  6.69% of dataset

Action:               3564 questions - 33.69% of dataset

Outcome Resolution:   1116 questions - 10.54% of dataset

*Note: Sum of attributes does not add up to 100% because some questions have more than 1 attribute*

## File Structure

`FairytaleQAData`
- `README.md`
- `LICENSE`
- `story_meta.csv`
- `data-by-origin/`
  - `questions/`
    - `andersen-fairybook/`
      - `brave-tin-soldier-questions.csv`
      - ...
    - ...
  - `section-stories/`
    - `andersen-fairybook/`
      - `brave-tin-soldier-story.csv`
      - ...
    - ...
  - `sentence-stories/`
    - `andersen-fairybook/`
      - `brave-tin-soldier-story.csv`
      - ...
    - ...
- `data-by-train-split/`
  - `questions/`
    - `test/`
      - `alleleiraugh-or-the-many-furred-creature-questions.csv`
      - ...
    - `train/`
      - `adventures-of-kintaro-golden-boy-questions.csv`
      - ...
    - `val/`
      - `assipattle-and-the-mester-stoorworm-questions.csv`
      - ...
  - `section-stories/`
    - `test/`
      - `alleleiraugh-or-the-many-furred-creature-story.csv`
      - ...
    - `train/`
      - `adventures-of-kintaro-golden-boy-story.csv`
      - ...
    - `val/`
      - `assipattle-and-the-mester-stoorworm-story.csv`
      - ...
  - `sentence-stories/`
    - `test/`
      - `alleleiraugh-or-the-many-furred-creature-story.csv`
      - ...
    - `train/`
      - `adventures-of-kintaro-golden-boy-story.csv`
      - ...
    - `val/`
      - `assipattle-and-the-mester-stoorworm-story.csv`
      - ...

The files in both `data-by-origin` and `data-by-train-split` are split into `question`, `section-stories`, and `sentence-stories`. The `question` files contain the QA pairs, the `section-stories` files contain the corresponding stories split into sections determined by human coders, and the `sentence-stories` contain the stories split by sentence. All files are in CSV format, and corresponding QA pair/story files should have the same name, except for the suffix `-question` for QA pair files and the suffix `-story` for the story files (both section-level and sentence-level). 

The files in `data-by-origin` are also split by the book of fairytales that the stories were found in. The files in `data-by-train-split` are instead split into training, validation, and test sets for the machine learning models trained in Xu et al. (2022), Yao et al. (2022), and Zhang et al. (2022).

## Using this Dataset

To start using this dataset, either clone the repo or download it as a zip file.

You can find some Jupyter Notebooks to train and run a BART-based QAG model [here](https://github.com/WorkInTheDark/FairytaleQA_QAG_System).

`story_meta.csv` also contains a list of stories and their corresponding metadata. This can be useful for traversing or filtering the dataset.

## Future Work

We are currently writing some starter code to help people who wish to use this dataset. Also, we are working on annotating the data for bias found in the stories within the dataset.