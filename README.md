# CamemBERT API

## About

A codespace to run the [French CamemBERT language model](https://camembert-model.fr/) which is a great model for text prediction based on [RoBERTa architecture](https://ai.facebook.com/blog/roberta-an-optimized-method-for-pretraining-self-supervised-nlp-systems/) through a minimalist web API.

This project use the 110M parameters [`camembert-base`](https://dl.fbaipublicfiles.com/fairseq/models/camembert-base.tar.gz) version of the model, trained with [OSCAR](https://oscar-corpus.com/) (138 Gb of text).

Under the hood, the model is run in Docker image containing a Python + PyTorch environment.

## Install

Python dependencies can be installed thanks to this command.

```
install.sh
```

Model dependency is solved during the first run.

## Run

```
run.sh
```

## API usage

```
GET /?pattern=Hello <mask>
```

The `pattern` query parameter is mandatory and must contain the `<mask>` occurence.

Result is a JSON string array containing word predictions sorted by probability.

