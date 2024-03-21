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


import joblib
import sys
import argparse

labels = { 
    1.: 'Spanish',
    2.: 'Catalan',
    3.: 'Aragonese',
    4.: 'Aranese',
    5.: 'Occitan',
    6.: 'Asturian',
    7.: 'Galician',
    8.: 'Italian',
    9.: 'French',
    10.: 'Portuguese'
}

def main() -> None:

    parser = argparse.ArgumentParser(description="Language classification script. Retrieves the sentences to classify from standard \
                                        input and prints each sentence with the identified language."
                                        )
    parser.add_argument("--model", type=str, required=True, help="Path of the language classifier")
    args = parser.parse_args()

    # Sentences to classify, read by standard input
    input_lines = [line.strip() for line in sys.stdin]

    # Load the model
    clf2 = joblib.load(args.model)

    # Classify
    predictions = clf2.predict(input_lines)

    for i, pred in enumerate(predictions):
        print(f"{input_lines[i]}\t{labels[pred]}")


if __name__ == "__main__":
    main()
