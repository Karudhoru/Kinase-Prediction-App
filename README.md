# 🧬 Kinase Prediction App

<div align="center">

![Kinase Predictor](https://img.shields.io/badge/BioML-Kinase_Predictor-6366F1?style=for-the-badge)
![Flask](https://img.shields.io/badge/framework-Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-active-success?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)

</div>

## 📋 Overview

A sophisticated web application for predicting kinase functionality in protein sequences using advanced machine learning techniques. The application employs a highly accurate random forest classifier trained on 3-mer frequency features extracted from protein sequences.

<div align="center">
  <img src="static/protein-icon.jpg" alt="Kinase Prediction" width="300px">
</div>

## ✨ Key Features

- **🔍 Protein Sequence Analysis**: Submit any amino acid sequence for instant kinase functionality prediction
- **🧩 Advanced Feature Extraction**: Sophisticated 3-mer frequency analysis for comprehensive sequence representation
- **🤖 High-Performance ML Model**: Random forest classifier with exceptional predictive accuracy
- **📊 Detailed Results**: Clear prediction outcomes with probability scores and interpretations
- **💻 Intuitive Web Interface**: User-friendly design with responsive layout for all devices

## 📈 Model Performance

Our random forest model demonstrates exceptional performance in predicting kinase functionality:

| Metric | Score |
|--------|-------|
| Accuracy | 0.95 |
| Precision | 1.00 |
| Recall | 0.84 |
| F1-score | 0.91 |
| AUC Score | 1.00 |

<div align="center">
  
*The model achieves perfect precision (1.00), indicating zero false positives, and excellent overall accuracy (0.95).*

</div>

## 🔧 Technology Stack

- **Backend**: Python 3.8+, Flask, Scikit-learn, Biopython
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Machine Learning**: Random Forest Classifier
- **Data Processing**: NumPy, Pandas

## 📁 Project Structure

```
kinase-predictor/
├── README.md                # Project documentation
├── app/                     # Web application
│   ├── app.py               # Flask application main file
│   └── templates/           # HTML templates
│       └── index.html       # Main application interface
├── bin/                     # Development scripts
│   └── model.ipynb          # Jupyter notebook for model development
├── data/                    # Data resources
│   ├── Protein_Data.tsv     # Training and testing dataset
│   └── all_kmers.pkl        # Precomputed k-mer features
├── docs/                    # Documentation
│   ├── INSTALL.pdf          # Installation instructions
│   ├── MODEL_INFO.pdf       # Detailed model information and theory
│   └── USAGE.pdf            # Application usage guide
├── model/                   # Trained models
│   └── kinase_model.pkl     # Serialized random forest model
├── requirements.txt         # Project dependencies
└── static/                  # Static assets
    └── protein-icon.jpg     # Application logo/icon
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/kinase-predictor.git
cd kinase-predictor
```

2. **Set up a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Start the application**

```bash
cd app
python app.py
```

5. **Access the application**

Open your browser and navigate to `http://127.0.0.1:5000/`

For more detailed installation instructions, please refer to the **docs/INSTALL.pdf** file.

## 💡 How It Works

### Feature Extraction

The application utilizes 3-mer frequency analysis to convert protein sequences into feature vectors:

1. Each amino acid sequence is broken down into overlapping triplets (3-mers)
2. Frequencies of each unique 3-mer are calculated
3. A standardized feature vector is created for model input

### Classification

The random forest classifier analyzes the 3-mer frequency patterns to identify kinase functionality:

1. Multiple decision trees evaluate the feature vector
2. The ensemble produces a probability score
3. Results are interpreted and presented to the user

For a deeper understanding of the biological and technical principles, see **docs/MODEL_INFO.pdf**.

## 📖 Usage Guide

1. **Enter a protein sequence** in single-letter amino acid code (e.g., "MAVKLERTAGVFDLSAFDEV...")
2. **Click "Analyze Sequence"** to process the input
3. **Review the prediction results**, including:
   - Classification outcome (Kinase/Not Kinase)
   - Probability score
   - Interpretation of results

For a comprehensive usage tutorial, please refer to **docs/USAGE.pdf**.

## 🔬 Scientific Background

Kinases are enzymes that catalyze the transfer of phosphate groups from ATP to specific substrates, playing crucial roles in cellular signaling pathways. Identifying potential kinases from sequence data can provide valuable insights for:

- Drug discovery and development
- Understanding cellular regulation
- Exploring disease mechanisms
- Protein function annotation

Our 3-mer frequency approach captures important sequence patterns that correlate with kinase functionality, enabling accurate prediction without requiring structural information.

## 🤝 Contributing

Contributions are welcome and appreciated! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code follows project conventions and includes appropriate tests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

For questions, suggestions, or issues, please open an issue on GitHub or contact the repository maintainer.

---

<div align="center">
  
**Developed with ❤️ for the bioinformatics community**

</div>
