# 🤖 AI Chatbot with Neural Networks

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://tensorflow.org)
[![NLTK](https://img.shields.io/badge/NLTK-Natural%20Language-green.svg)](https://nltk.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An intelligent chatbot built with deep learning that can understand natural language, play music, and launch games. The bot uses TensorFlow/Keras with GloVe word embeddings and convolutional neural networks for intent classification.

## 🌟 Features

- **🧠 Smart Intent Recognition**: Uses CNN with GloVe embeddings for accurate intent classification
- **🎵 Music Integration**: Can play songs through integrated music player
- **🎮 Game Launcher**: Opens games based on user-specified categories
- **💬 Natural Conversation**: Lemmatized text processing for better understanding
- **🔄 Continuous Learning**: JSON-based intent system for easy updates

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Input    │───▶│   Text Processing │───▶│  Intent Prediction│
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │                        │
                       ┌────────▼────────┐    ┌─────────▼─────────┐
                       │ Word Tokenization│    │   CNN Model with  │
                       │ & Lemmatization  │    │  GloVe Embeddings │
                       └─────────────────┘    └───────────────────┘
                                                        │
                       ┌─────────────────┐    ┌─────────▼─────────┐
                       │   Action Handler│◀───│  Response Generator│
                       └─────────────────┘    └───────────────────┘
                                │
                    ┌───────────▼──────────┐
                    │  🎵 Music  🎮 Games  │
                    └──────────────────────┘
```

## 📋 Prerequisites

- Python 3.7 or higher
- TensorFlow 2.x
- NLTK
- NumPy
- Pygame (for music functionality)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-chatbot.git
   cd ai-chatbot
   ```

2. **Install required packages**
   ```bash
   pip install tensorflow nltk numpy pygame
   ```

3. **Download NLTK data**
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('wordnet')
   ```

4. **Download GloVe embeddings**
   - Download `glove.6B.300d.txt` from [Stanford NLP](https://nlp.stanford.edu/projects/glove/)
   - Place it in the project root directory

5. **Prepare your data**
   - Create `intents2.json` with your chatbot intents and responses
   - Ensure `addMinigames.py` and `music_player.py` modules are available

## 💾 Project Structure

```
ai-chatbot/
│
├── train_model.py          # Model training script
├── chatbot.py             # Main chatbot application  
├── intents2.json          # Intent definitions and responses
├── glove.6B.300d.txt      # GloVe word embeddings (download separately)
├── addMinigames.py        # Game integration module
├── music_player.py        # Music player module
├── words.pkl              # Serialized vocabulary (generated)
├── classes.pkl            # Serialized intent classes (generated)
├── chatbotmodel.h5        # Trained model (generated)
└── README.md              # This file
```

## 🎯 Usage

### Training the Model

```bash
python train_model.py
```

This will:
- Process the intents from `intents2.json`
- Create vocabulary and intent classes
- Build and train a CNN model with GloVe embeddings
- Save the trained model as `chatbotmodel.h5`

### Running the Chatbot

```bash
python chatbot.py
```

### Example Conversations

```
User: Hello there!
Bot: Hi! How can I help you today?

User: I want to play a game
Bot: What is your favourite category?
User: puzzle
Bot: [Launches puzzle games]

User: Play some music
Bot: [Starts music player]

User: Goodbye
Bot: Goodbye!
[Bot exits]
```

## 🏛️ Model Architecture

The chatbot uses a sophisticated neural network architecture:

- **Embedding Layer**: 300-dimensional GloVe word embeddings
- **Conv1D Layers**: Two convolutional layers (128 and 64 filters) with ReLU activation
- **MaxPooling1D**: Pooling layers for dimensionality reduction
- **Dense Layers**: Fully connected layers with dropout for regularization
- **Output Layer**: Softmax activation for intent classification

## 📝 Intent Configuration

Define your intents in `intents2.json`:

```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hi", "Hello", "Hey", "Good morning"],
      "responses": ["Hello!", "Hi there!", "Greetings!"]
    },
    {
      "tag": "play_song",
      "patterns": ["Play music", "Play a song", "I want to listen to music"],
      "responses": ["Playing music for you!"]
    }
  ]
}
```

## 🔧 Customization

### Adding New Intents
1. Edit `intents2.json` to add new intent patterns and responses
2. Retrain the model using `train_model.py`
3. The chatbot will automatically recognize the new intents

### Modifying Model Parameters
- Adjust `ERROR_THRESHOLD` in `chatbot.py` to change prediction sensitivity
- Modify network architecture in `train_model.py` for different performance characteristics
- Change embedding dimensions or add more layers as needed

## 🎮 Features Integration

### Music Player
- Integrated with `music_player.py` module
- Automatically triggers when music-related intents are detected

### Game Launcher  
- Connected to `addMinigames.py` module
- Supports category-based game selection
- Interactive category input system

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Stanford NLP Group](https://nlp.stanford.edu/) for GloVe word embeddings
- [TensorFlow](https://tensorflow.org) team for the deep learning framework
- [NLTK](https://nltk.org) contributors for natural language processing tools

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the documentation
- Review the example configurations

---

<div align="center">
  <p>Made with ❤️ and 🧠 by [Your Name]</p>
  <p>⭐ Star this repo if you found it helpful!</p>
</div>
