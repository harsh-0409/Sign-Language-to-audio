# Sign-Language-to-audio
Real-time sign language detection system using computer vision and machine learning. Translates hand signs to text and audio output with OpenCV and MediaPipe.




[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

A real-time sign language detection system that translates hand signs into text and audio. Using computer vision and machine learning, this program processes webcam input to detect hand signs and provides instant translations, making communication more accessible for the deaf and hard-of-hearing community.


## 🌟 Features

- Real-time hand sign detection via webcam
- Text and audio translation of detected signs
- Support for 10 common signs
- Optional LCD display integration
- High accuracy using MediaPipe hand tracking
- User-friendly interface

## 🛠️ Prerequisites

- Python 3.7+
- Webcam
- Required Python packages (see requirements.txt)

## 📦 Installation

1. Clone the repository:

git clone https://github.com/harsh-0409/Sign-Language-to-audio
cd Handy-Sign-Language-Detection


2. Install dependencies:

pip install -r requirements.txt


## 🚀 Usage

### 1. Data Collection

python img_collect.py

- Press '1' to start collecting images
- Collects 100 images for each sign

### 2. Process Landmarks

python landmarks.py

### 3. Train Model

python train.py

### 4. Run Detection

# For text output only
python classifier.py

# For text and audio output

python classifier_w_audio_output.py

## 🔧 Technical Details

### Core Components
- **Hand Detection**: MediaPipe for accurate hand landmark tracking
- **Machine Learning**: Random Forest Classifier for sign prediction
- **Image Processing**: OpenCV for real-time video processing
- **Audio Output**: pyttsx3 for text-to-speech conversion

### Supported Signs
1. Hello
2. I love you
3. Yes
4. Good
5. Bad
6. Okay
7. You
8. I/I'm
9. Why
10. No

### Project Structure
- `classifier.py`: Main detection script
- `classifier_w_audio_output.py`: Detection with audio
- `landmarks.py`: Data processing
- `train.py`: Model training
- `img_collect.py`: Data collection
- `LCD_I2C.py`: LCD display integration

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request


## 📝 License

Licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- MediaPipe team for hand tracking
- OpenCV community
- scikit-learn developers
- Contributors and testers

---

<p align="center">
  Made with ❤️ for accessibility
</p>
