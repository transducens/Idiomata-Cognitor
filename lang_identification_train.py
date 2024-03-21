#  This file is part of Idiomata Cognitor.
#
#  Idiomata Cognitor is free software: you can redistribute it and/or modify
#  it under the terms of the Apache-2.0 License as published by
#  the Apache Software Foundation.
#
#  Idiomata Cognitor is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  Apache-2.0 License for more details.
#
#  You should have received a copy of the Apache-2.0 License
#  along with Idiomata Cognitor.  If not, see <http://www.apache.org/licenses/>.

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import numpy as np
import pandas as pd
import joblib
import argparse


labels = { 
    'spa': 'Spanish',
    'cat': 'Catalan',
    'arg': 'Aragonese',
    'arn': 'Aranese',
    'oci': 'Occitan',
    'ast': 'Asturian',
    'glg': 'Galician',
    'ita': 'Italian',
    'fra': 'French',
    'por': 'Portuguese'
}

"""
Max length of training corpus per language
Ensure each language has similar amount of representation (Balanced Dataset)
"""
MAX_LENGTH = 10000

def read_languages_data(path):

    with open(path) as f:
        language_transcription = f.readlines()
        language_transcription = language_transcription[:MAX_LENGTH]
    return language_transcription

def combine_language_data(sentences, language_index):
    
    sentences = np.array(sentences)
    sentences = sentences.reshape(sentences.shape[0],1)
    target = np.zeros((sentences.shape[0],1))
    target += language_index
    language_data = np.hstack((sentences, target))
    return language_data

def shuffle_rows(languages):
    index = np.arange(0, len(languages))
    np.random.shuffle(index)
    shuffled_languages = languages[index,:]

    return shuffled_languages

"""
Run all data preprocessing helper functions
"""
def preproccess_raw_data(file_paths):

    # Read all raw text data from file paths
    language_transcriptions = [ read_languages_data(path) for path in file_paths ]

    # Combine each language with its language_index
    languages = [ combine_language_data(sentences,i+1) for i,sentences in enumerate(language_transcriptions) ]
    
    # Vertically stack all data into one 2D np.array
    languages =  np.vstack((languages))
    
    # Shuffle languages by row
    languages = shuffle_rows(languages)
    
    return languages



def main() -> None:

    parser = argparse.ArgumentParser(description="Train Romance language identifier from monolingual corpora")
    parser.add_argument("--spa", type=str, required=True, help="Spanish training corpus")
    parser.add_argument("--cat", type=str, required=True, help="Catalan training corpus")
    parser.add_argument("--arg", type=str, required=True, help="Aragonese training corpus")
    parser.add_argument("--arn", type=str, required=True, help="Aranese training corpus")
    parser.add_argument("--oci", type=str, required=True, help="Occitan training corpus")
    parser.add_argument("--ast", type=str, required=True, help="Asturian training corpus")
    parser.add_argument("--ita", type=str, required=True, help="Galician training corpus")
    parser.add_argument("--glg", type=str, required=True, help="Italian training corpus")
    parser.add_argument("--fra", type=str, required=True, help="French training corpus")
    parser.add_argument("--por", type=str, required=True, help="Portuguese training corpus")
    parser.add_argument("--output-model", type=str, required=True, help="The trained model path")
    args = parser.parse_args()


    # Get all file paths
    file_paths = [getattr(args, language) for language in labels]

    # Preprocess all raw text into a form suitable for TfidfVectorizer
    languages = preproccess_raw_data(file_paths)

    df_languages = pd.DataFrame(languages)
    df_languages.columns = ['natural language', 'language index']
    df_languages['language index'] = df_languages['language index'].apply(float)
    df_languages['language'] = df_languages['language index'].map(labels)
    df_languages.shape

    # Split data into raw features and labels
    language_features = df_languages['natural language']
    language_targets = df_languages['language index']

    unique, counts = np.unique(language_targets, return_counts=True)
    print(dict(zip(unique, counts)))

    # Split data into training and test set
    # Train on 70% of data, Test on remaining 30%
    X_train, X_test, y_train, y_test = train_test_split(language_features, 
                                                        language_targets,
                                                        test_size = 0.3,
                                                        random_state = 42)

    # Make Pipeline with TfidfVectorizer and MultinomialNB
    tfidf_vect = TfidfVectorizer(analyzer='char', ngram_range=(1,5))
    model = MultinomialNB()
    text_clf = Pipeline([('tfidf', tfidf_vect), ('clf', model)])

    # Train model with pipeline classifier
    text_clf.fit(X_train, y_train)

    # save
    joblib.dump(text_clf, args.output_model) 

    # Measure accuracy
    predictions = text_clf.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test,predictions)}")
    print(classification_report(y_test, predictions, target_names=labels.values()))

if __name__ == "__main__":
    main()




