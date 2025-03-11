from flask import Flask, render_template, request
import numpy as np
import joblib
from Bio.Seq import Seq

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and the list of all 3-mers

model = joblib.load('kinase_model.pkl')
all_kmers = joblib.load('all_kmers.pkl')

# Function to compute 3-mer frequencies
def compute_kmer_frequencies(sequence, k=3):
    seq = Seq(sequence.upper())
    kmers = [str(seq[i:i+k]) for i in range(len(seq) - k + 1)]
    unique_kmers = set(kmers)
    frequencies = {kmer: kmers.count(kmer) / len(kmers) for kmer in unique_kmers}
    return frequencies

# Define the route for the homepage
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    probability = None
    message = None
    error = None
    if request.method == 'POST':
        try:
            # Retrieve and preprocess the sequence
            sequence = request.form.get('sequence').upper()
            if len(sequence) < 3:
                raise ValueError("Sequence must be at least 3 amino acids long.")
            
            # Compute 3-mer frequencies
            freq_dict = compute_kmer_frequencies(sequence)
            
            # Create feature vector in the same order as training
            feature_vector = np.zeros(len(all_kmers))
            for i, kmer in enumerate(all_kmers):
                feature_vector[i] = freq_dict.get(kmer, 0)
            feature_vector = feature_vector.reshape(1, -1)
            
            # Make prediction
            pred = model.predict(feature_vector)[0]
            prob = model.predict_proba(feature_vector)[0][1]
            prediction = "Kinase" if pred == 1 else "Not Kinase"
            probability = f"{prob:.2f}"
            message = "This sequence is likely a kinase." if pred == 1 else "This sequence is unlikely to be a kinase."
        except Exception as e:
            error = f"An error occurred: {str(e)}"
    return render_template('index.html', prediction=prediction, probability=probability, message=message, error=error)

if __name__ == '__main__':
    app.run(debug=True)