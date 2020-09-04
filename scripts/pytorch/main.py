from . import rnn
import numpy as np
import pandas as pd
from string import punctuation
import torch
import nltk
from nltk.corpus import movie_reviews


review_data = ""