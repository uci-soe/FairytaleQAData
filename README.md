# FairytaleQA: A Dataset for Question and Answer Generation

This repository contains the FairytaleQA dataset. It contains CSV files of children's stories from [Project Gutenberg](https://www.gutenberg.org/) and a set of questions and answers developed by highly trained coders for each story. 

Thus far, three papers have been published that include this dataset. Check back here for updates on any further papers using this dataset.

- Xu, Y., Wang, D., Yu, M., Ritchie, D., Yao, B., Wu, T., Zhang, Z., Li, T., Bradford, N., Sun, B., Hoang, T., Sang, Y., Hou, Y., Ma, X., Yang, D., Peng, N., Yu, Z., & Warschauer, M. (2022). Fantastic questions and where to find them: FairytaleQA- An authentic dataset for narrative comprehension. *Association for Computational Linguistics*.
- Yao, B., Wang, D., Wu, T., Zhang, Z., Li, T., Yu, M., & Xu, Y. (2022). It is AI's Turn to Ask Humans a Question: Question and Answer Pair Generation for Children's Storybooks with FairytaleQA Dataset. *Association for Computational Linguistics*. [https://doi.org/10.48550/arXiv.2109.03423](https://doi.org/10.48550/arXiv.2109.03423)
- Zhang, Z., Xu, Y., Wang Y., Yao, B., Ritchie, D., Wu, T., Yu, M., Wang, D., & Li, T. (2022). Storybuddy: A human-AI collaborative agent for parent-child interactive storytelling. *In Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems*. [https://doi.org/10.1145/3491102.3517479](https://doi.org/10.1145/3491102.3517479)

## File Structure

`FairytaleQAData`
- `README.md`
- `LICENSE`
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

### Files in Progress
- `meta-db.csv` - contains metadata about the database as a whole
- `meta-story.csv` - contains metadata about each individual story (also used to loop over the stories and questions in the dataset)
- `starter.py` - some basic starter code to either get the whole dataset as one pandas DataFrame or apply a function to each file in the dataset
- `starter.r` - equivalent starter code as `starter.py` but in R