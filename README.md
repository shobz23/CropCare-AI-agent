# Crop Doctor AI

Crop Doctor is an intelligent AI-based plant disease detection system. It helps farmers identify diseases from leaf images and provides recommendations for treatment. This project was developed as part of the Vicky Bytes Hiring Challenge.

---

## Features

- Upload or capture leaf images
- Identify plant diseases using deep learning
- Recommend treatments and best practices
- Easy-to-use interface (FastAPI or Streamlit)
- Scalable and modular codebase

---

## Dataset

- **Name**: PlantVillage Dataset  
- **Source**: [Kaggle - PlantVillage](https://www.kaggle.com/datasets/emmarex/plantdisease)  
- **Classes**: 38 crop categories with healthy and diseased labels

---

## Project Structure

```
Crop-Doctor-AI/
├── data/                       # Raw dataset
├── models/                     # Trained models (CNN, etc.)
├── src/
│   ├── preprocess.py           # Image preprocessing logic
│   ├── train_model.py          # Model training script
│   ├── predict.py              # Inference code
│   └── app.py                  # Backend interface (FastAPI/Streamlit)
├── notebooks/                  # EDA & training experiments
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Crop-Doctor-AI.git
cd Crop-Doctor-AI
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
# OR
venv\Scriptsctivate         # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Dataset

- Download the dataset from [Kaggle](https://www.kaggle.com/datasets/emmarex/plantdisease)
- Extract it and move it into the `data/` folder

### 5. Train the Model (Optional)

```bash
python src/train_model.py
```

### 6. Run the App

**For FastAPI:**

```bash
uvicorn src.app:app --reload
```

**For Streamlit:**

```bash
streamlit run src/app.py
```

---

## How to Use

1. Upload an image of a leaf.
2. Get the disease prediction and treatment suggestion.
3. Use the results to take timely action on your crops.

---

## Technologies Used

- Python
- FastAPI / Streamlit
- TensorFlow / PyTorch
- OpenCV
- Pandas & NumPy
- Scikit-learn

---

## License

This project is licensed under the MIT License.

---

## Contributors

- **Your Name**
- Contributions welcome via pull requests.
