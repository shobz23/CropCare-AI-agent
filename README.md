# CropCare-AI-agent

An AI-powered agent that detects plant diseases from leaf images and recommends treatments.

## 🚀 Features
- Upload a leaf image 📸
- Get instant disease diagnosis 🌱
- Suggests pesticide/organic treatments 💊
- Built with Python + Streamlit + Deep Learning

## 🧠 How It Works
1. Trained on PlantVillage dataset with CNN (ResNet/MobileNet)
2. Classifies plant disease from leaf image
3. Returns disease name + treatment suggestions

## 🖥 Demo
![Sample Output](sample_leaf.jpg)

## 🔧 Tech Stack
- Python
- TensorFlow/Keras or PyTorch
- Streamlit or Flask
- OpenCV, PIL

## 📦 Installation

```bash
git clone https://github.com/shobz23/CropCare-AI-agent
cd crop-doctor-ai
pip install -r requirements.txt
streamlit run app.py
