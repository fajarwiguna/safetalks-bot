# 🛡️ SafeTalks Discord Bot

**SafeTalks** is a real-time Discord moderation bot powered by an LSTM-based machine learning model. It detects **hate speech**, **offensive language**, and **neutral content** in messages, taking automated actions to keep servers safe.

---

## 🚀 Features

- 🔍 Real-time detection of toxic messages
- ⚠️ Automated moderation:
  - Warns users for offensive content
  - Deletes messages with hate speech
- 📊 `!test <message>` command for testing predictions
- 🧼 Built-in text cleaning and slang normalization
- ⚙️ Modular command structure using Discord Cogs
- ☁️ Seamless deployment via [Railway](https://railway.app)

---

## 🗂️ Project Structure

```
safetalks-bot/
├── commands/
│   ├── help.py               # !help command logic
│   └── test.py               # !test command logic
├── model/
│   └── lstm/
│       ├── lstm_model.keras  # Trained LSTM model
│       └── tokenizer.pkl     # Fitted tokenizer
├── utils/
│   ├── inference.py          # Model loading and prediction
│   └── preprocessing.py      # Text cleaning utilities
├── .env                      # Environment variables (BOT_TOKEN)
├── bot.py                    # Main bot launcher
├── requirements.txt          # Python dependencies
└── README.md                 # This documentation
```

---

## 🧠 Model Overview

SafeTalks uses a custom LSTM model with:
- 🧠 **SimpleAttention** layer for enhanced token focus
- 🎯 **Focal Loss** function to handle class imbalance

**Classifications:**
- Hate Speech
- Offensive
- Neither

The model and tokenizer are stored in `model/lstm/`.

---

## ⚙️ Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/fajarwiguna/safetalks-bot.git
   cd safetalks-bot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment:**
   Create a `.env` file with:
   ```
   BOT_TOKEN=your_discord_bot_token_here
   ```

4. **Run the bot:**
   ```bash
   python bot.py
   ```

---

## ☁️ Deployment (Railway)

1. Push the project to a GitHub repository.
2. Visit [Railway](https://railway.app/).
3. Select **New Project > Deploy from GitHub Repo**.
4. Set the `BOT_TOKEN` environment variable.
5. Click **Deploy** to go live.

---

## 💬 Bot Commands

### `!help`
Displays available bot commands.

### `!test <text>`
Classifies input text and returns the prediction with confidence scores.

**Example:**
```
!test fuck you
```

---

## 🔐 Auto Moderation Rules

- **Hate Speech** (confidence ≥ 0.80): Message deleted, user warned
- **Offensive** (confidence ≥ 0.85): User warned
- **Neither**: No action taken

---

## 📜 License

Licensed under the [MIT License](LICENSE). Free to use, modify, and distribute.

---

## 🙋‍♂️ Contributing

Contributions are welcome! Submit pull requests or open issues for:
- Moderation dashboard
- Message logging with database integration
- Abuse reporting system

---

## 📬 Contact

**Developer:** Fajar Satria Wiguna  
📧 Email: [fajarsatria991@gmail.com](mailto:fajarsatria991@gmail.com)  
