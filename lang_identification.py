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
