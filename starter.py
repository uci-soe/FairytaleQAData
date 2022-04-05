# STARTER CODE FOR FAIRYTALE QA
# Author: Daniel Ritchie

import pandas as pd
import os

# Loading metadata: used to loop over the file system
meta_df = pd.read_csv('story_meta.csv')

# Get Aggregated DataFrame of Questions
# Params:
# - origins (list of strings): story origins to filter by
# - split (string): filter by train, test, or validation splits
# Returns:
# A single pd.DataFrame with the aggregate questions

def get_question_df(origins=[], split=""):
  if split not in ["", "train", "test", "val"]:
    print('Incorrect split argument: expected "train", "test", "val", or default empty string.')
    return

  if split == "":
    filtered_meta = meta_df
  else:
    filtered_meta = meta_df[meta_df['split'] == split]

  if len(origins) != 0:
    filtered_meta = meta_df[meta_df['origin'].isin(origins)]

  def get_q_file(row):
    df = pd.read_csv('data-by-train-split/questions/' + row[1] + '/' + row[0] + '-questions.csv')
    df['filename'] = row[0] + '-questions.csv'
    df['split'] = row[1]
    df['origin'] = row[2]
    return df

  qdfs = [ get_q_file(row)
    for row in zip(filtered_meta['filename'].to_list(), filtered_meta['split'].to_list(), filtered_meta['origin'].to_list())
  ]

  return pd.concat(qdfs, ignore_index=True)
  
# Get Aggregated DataFrame of Questions
# Params:
# - origins (list of strings): story origins to filter by
# - split (string): filter by train, test, or validation splits
# - sent_level (boolean): if true, return sentence-level stories, and else return section-level stories
# Returns:
# A single pd.DataFrame with the aggregate story sections or sentences

def get_story_df(origins=[], split="", sent_level=False):
  if split not in ["", "train", "test", "val"]:
    print('Incorrect split argument: expected "train", "test", "val", or default empty string.')
    return

  if split == "":
    filtered_meta = meta_df
  else:
    filtered_meta = meta_df[meta_df['split'] == split]

  if len(origins) != 0:
    filtered_meta = meta_df[meta_df['origin'].isin(origins)]

  def get_s_file(row):
    file_str = 'data-by-train-split/'
    if sent_level:
      file_str += 'sentence-stories/'
    else:
      file_str += 'section-stories/'
    
    file_str += row[1] + '/' + row[0] + '-story.csv'

    df = pd.read_csv(file_str)
    df['filename'] = row[0] + '-questions.csv'
    df['split'] = row[1]
    df['origin'] = row[2]
    return df

  sdfs = [ get_s_file(row)
    for row in zip(filtered_meta['filename'].to_list(), filtered_meta['split'].to_list(), filtered_meta['origin'].to_list())
  ]

  return pd.concat(sdfs, ignore_index=True)