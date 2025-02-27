# Idiomata Cognitor

## Language identifier for Romance languages

Idiomata Cognitor is a multilingual highly-accurate language classifier focused on a number of Romance languages, trained with Bayesian methods. It complements general language detectors by offering finer classification within Romance languages.

## Description

The classifier is able to identify the following languages and language variants: Aragonese, Occitan, Aranese (variant of Occitan spoken in the Aran Valley), Asturian, Catalan, French, Galician, Italian, Portuguese and Spanish.

The [model](https://github.com/transducens/Romance-languages-identifier/blob/main/model.pkl.gz) was trained on fragments from the [Wikimedia](https://opus.nlpl.eu/wikimedia/ast&es/v20230407/wikimedia) and [Wikimatrix](https://opus.nlpl.eu/WikiMatrix/an&es/v1/WikiMatrix) corpora, with the exception of Aranese, for which the literary corpus from [PILAR](https://github.com/transducens/PILAR) was used.

The classification report emitted by the classifier on a multilingual joint corpus of [FLORES+](https://github.com/openlanguagedata/flores) dev sets is as follows:

```
Accuracy: 0.9763289869608827
              precision  recall  f1-score  sentences

Spanish        0.95      0.98    0.96      997
Catalan        1.00      0.99    0.99      997
Aragonese      0.96      0.99    0.97      997
Aranese        0.96      0.94    0.95      997
Occitan        0.94      0.96    0.95      997
Asturian       0.99      0.92    0.95      997
Galician       0.98      0.99    0.98      997
Italian        1.00      1.00    1.00      997
French         1.00      1.00    1.00      997
Portuguese     1.00      0.98    0.99      997

accuracy                         0.98      9970
macro avg      0.98      0.98    0.98      9970
weighted avg   0.98      0.98    0.98      9970
```
As of 08/02/2024, the FLORES+ versions of Aragonese and Aranese are not published. They will be released soon as a result of the [EMNLP 2024 Shared Task "Translation into Low-Resource Languages of Spain"](https://www2.statmt.org/wmt24/romance-task.html).

Note that the median length of sentences from the FLORES+ dev set is 22 words. It is possible that the results will vary with shorter lengths.

## Install

Clone the repository and install the dependencies:

```
git clone https://github.com/transducens/idiomata_cognitor.git
cd idiomata_cognitor
pip install -r requirements.txt
```

If you would like to use our trained model, you will need to unzip it.

## Usage

To use the [classification script](https://github.com/transducens/Romance-languages-identifier/blob/main/lang_identification.py), you would need to provide the sentences to be identified via standard input, along with the model to be used as an argument. The output will then be the input sentences along with the corresponding language identifier separated by a tab.

For example, if you have a list of sentences in the file `input.txt`, you can use the following command:

```
cat input.txt | python lang_identification.py --model model.pkl
```

The output will be in the format:

```
sentence1   language1
sentence2   language2
...
```

## Training

You can use the [training script](https://github.com/transducens/Romance-languages-identifier/blob/main/lang_identification_train.py) and monolingual corpora to train your own classifier. The script will divide the provided corpora into 70% for training and 30% for testing.

```
python lang_identification_train.py \
      --spa spanish_monolingual_corpus.txt \
      --cat catalan_monolingual_corpus.txt \
      --arg aragonese_monolingual_corpus.txt \
      --arn aranese_monolingual_corpus.txt \
      --oci occitan_monolingual_corpus.txt \
      --ast asturian_monolingual_corpus.txt \
      --ita italian_monolingual_corpus.txt \
      --glg galician_monolingual_corpus.txt \
      --fra french_monolingual_corpus.txt \
      --por portuguese_monolingual_corpus.txt \
      --output-model your_model.pkl
```

Once training is complete, the script will produce a classification report similar to the one shown in the [Description](#description) section above. This report will be generated over the 30% of the corpora that was reserved for testing.

## Citing this work

If you use this tool as part of your developments, please cite it as follows:

```
@misc{idiomatacognitor,
  author = {Galiano-Jiménez, Aarón and Sánchez-Martínez, Felipe and Pérez-Ortiz, Juan Antonio},
  title = {Idiomata Cognitor},
  url = {https://github.com/transducens/idiomata_cognitor},
  year = {2024}
}
```

A `CITATION.cff` file is also included in this repository.

## Acknowledgements

This tool has been produced as part of the research project [Lightweight neural translation technologies for low-resource languages (LiLowLa)](https://transducens.dlsi.ua.es/lilowla/) (PID2021-127999NB-I00) funded by the Spanish Ministry of Science and Innovation (MCIN), the Spanish Research Agency (AEI/10.13039/501100011033) and the European Regional Development Fund A way to make Europe.
