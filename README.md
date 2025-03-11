# Kinase Prediction App

A web application to predict whether a protein sequence is a kinase or not using a random forest model trained on 3-mer features.

## Project Structure

```plain text
├── README.md
├── app
│   ├── app.py
│   └── templates
│       └── index.html
├── bin
│   └── model.ipynb
├── data
│   ├── Protein_Data.tsv
│   └── all_kmers.pkl
├── docs
│   ├── INSTALL.pdf
│   ├── MODEL_INFO.pdf
│   └── USAGE.pdf
├── model
│   └── kinase_model.pkl
├── requirements.txt
└── static
    └── protein-icon.jpg
```

## Features

- **Protein Sequence Prediction:** Enter a protein sequence to predict whether it is a kinase.
- **3-mer Feature Extraction:** Converts sequences into overlapping 3-mers.
- **Random Forest Classifier:** Uses a trained random forest model for classification.
- **Flask Web Interface:** Provides an easy-to-use web interface.

## Setup and Installation

Follow the instructions in the **docs/INSTALL.md** file to install the required dependencies and set up the project environment.

## Usage

For details on running the application and using the interface, please refer to the **docs/USAGE.pdf** file.

## Model and Theory

This project leverages a random forest model trained on 3-mer features derived from protein sequences. For more detailed information on how the model works, including feature extraction techniques and the biological rationale behind classifying kinases versus non-kinases, please see the **docs/MODEL_INFO.pdf** file.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any bugs or feature requests.
