# Language identifier for Romance languages

This repository contains a language classifier produced as part of the R+D+i poject [Lightweight neural translation technologies for low-resource languages (LiLowLa)](https://transducens.dlsi.ua.es/lilowla/) (PID2021-127999NB-I00) funded by the Spanish Ministry
of Science and Innovation (MCIN), the Spanish Research Agency (AEI/10.13039/501100011033) and the European Regional Development Fund A way to make Europe.


## Description

The classifier is able to identify 10 languages:
```
Spanish, Catalan, Galician, Asturian, Aragonese, Aranese, Occitan, Portuguese, Italian, French
```
The published [model](https://github.com/transducens/Romance-languages-identifier/blob/main/model.pkl.gz) was trained on fragments from the [Wikimedia](https://opus.nlpl.eu/wikimedia/ast&es/v20230407/wikimedia) and [Wikimatrix](https://opus.nlpl.eu/WikiMatrix/an&es/v1/WikiMatrix) corpora, with the exception of Aranese, for which the [literary corpus from iberian_corpora](https://github.com/transducens/iberian_corpora/blob/main/aranese/literary.gz) was used.

The classification report on the Flores+ dev set is as follows:

```
Accuracy: 0.9763289869608827
              precision  recall  f1-score  support

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

## Install

## Use
```
cat file | python lang_identification.py --model model.pkl > file_identidied
```

## Training
