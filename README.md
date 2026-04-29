# 😷 Face Mask Detection

A deep learning application that detects whether a person is wearing a face mask using computer vision and TensorFlow.

## 📸 Overview

This project uses a Convolutional Neural Network (CNN) with residual blocks to classify images as either "mask" or "no mask". The application includes both a training script and a web-based interface built with Streamlit for real-time inference.

## 🚀 Features

- **Deep Learning Model**: CNN with residual blocks for improved accuracy
- **Web Interface**: Interactive Streamlit app for easy image upload and prediction
- **Real-time Detection**: Fast inference with confidence scores
- **Image Preprocessing**: Handles various image formats (RGB, RGBA, Grayscale)
- **Dataset Support**: Organized dataset structure for training and validation

## 📁 Project Structure

```
Face_Mask_Detection/
├── Dataset/                 # Training dataset
│   ├── with_mask/         # Images of people wearing masks
│   └── without_mask/      # Images of people without masks
├── app.py                 # Streamlit web application
├── model.py               # CNN model architecture
├── train.py               # Model training script
├── mask_model.h5          # Pre-trained model file
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- Git

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Karun2codes/Face-Mash-Detection.git
   cd Face-Mask-Detection
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Unix/MacOS
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the pre-trained model**
   - The model file `mask_model.h5` should already be included
   - If not, train the model using the instructions below

## 🎯 Usage

### Web Application

1. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   - Navigate to `http://localhost:8501`
   - Upload an image (JPG, PNG, JPEG)
   - Get instant prediction with confidence score

### Training the Model

If you want to train the model from scratch:

1. **Prepare your dataset**
   - Place images in `Dataset/with_mask/` and `Dataset/without_mask/`
   - Ensure proper directory structure

2. **Run training**
   ```bash
   python train.py
   ```

3. **Model will be saved** as `mask_model.h5`

## 🧠 Model Architecture

The CNN model features:

- **Input Layer**: 128x128x3 images
- **Convolutional Layers**: Feature extraction with 32 and 64 filters
- **Residual Blocks**: Skip connections for better gradient flow
- **Max Pooling**: Dimensionality reduction
- **Dense Layers**: Classification with sigmoid activation
- **Output**: Binary classification (mask/no mask)

### Model Specifications
- **Input Shape**: (128, 128, 3)
- **Parameters**: ~100K+
- **Activation**: Sigmoid (binary classification)
- **Optimizer**: Adam
- **Loss Function**: Binary Crossentropy

## 📊 Performance

- **Training Accuracy**: ~95%+
- **Validation Accuracy**: ~90%+
- **Inference Time**: < 1 second per image
- **Model Size**: ~100 MB

## 🔧 Dependencies

- **TensorFlow 2.13.0**: Deep learning framework
- **NumPy 1.24.3**: Numerical computations
- **OpenCV 4.8.0.76**: Image processing
- **Matplotlib 3.7.1**: Visualization
- **Streamlit**: Web application framework

## 📈 Dataset

The model was trained on a dataset containing:
- **With Mask**: ~1000 images
- **Without Mask**: ~1000 images
- **Image Size**: Various, resized to 128x128
- **Split**: 80% training, 20% validation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Improvements

- [ ] Add real-time webcam detection
- [ ] Implement face detection before mask classification
- [ ] Add more data augmentation techniques
- [ ] Deploy as a mobile app
- [ ] Add batch image processing
- [ ] Implement model quantization for faster inference

## 🐛 Troubleshooting

### Common Issues

1. **Model not found**: Ensure `mask_model.h5` is in the root directory
2. **Import errors**: Verify all dependencies are installed
3. **Memory issues**: Reduce batch size in training if needed
4. **Streamlit not working**: Check if streamlit is installed (`pip install streamlit`)

### GPU Support

For GPU acceleration:
```bash
pip install tensorflow-gpu
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Karun2codes**
- GitHub: [@Karun2codes](https://github.com/Karun2codes)
- Project: [Face-Mash-Detection](https://github.com/Karun2codes/Face-Mash-Detection)

## 🙏 Acknowledgments

- TensorFlow team for the amazing deep learning framework
- Streamlit for the easy-to-use web app framework
- The open-source community for inspiration and support

---

⭐ If you found this project helpful, please give it a star!
