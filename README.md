# Miami-Dade Transit Sentiment Analysis

This project analyzes public sentiment toward Miami-Dade Transit service changes — particularly the Better Bus Network initiative — using Natural Language Processing (NLP) techniques applied to Twitter data.

## Overview

- **Data Collection**: Scraped recent tweets mentioning "Miami-Dade Transit", "Better Bus Network", and "MDT" using Tweepy and Twitter API.
- **Preprocessing**: Cleaned and normalized tweet text for analysis.
- **Sentiment Analysis**: Applied multiple models for comparison:
  - TextBlob (Rule-based sentiment)
  - VADER (Social media-tuned lexicon)
  - BERT (Binary classification: Positive/Negative)
  - Twitter-RoBERTa (Three-way classification: Positive/Neutral/Negative)
- **Manual Sentiment Labeling**: Human labels used for validation.
- **Visualization**: Pie charts and bar charts for each model's sentiment distribution.

