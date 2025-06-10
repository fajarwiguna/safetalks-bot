# 🛡️ SafeTalks Discord Bot

SafeTalks is a real-time Discord moderation bot powered by an LSTM-based machine learning model to detect **hate speech**, **offensive language**, and **neutral content**. It automatically warns users or removes messages based on model predictions.

---

## 🚀 Features

- 🔎 Real-time detection of hate speech and offensive messages
- ⚠️ Automatic warnings or message deletion based on confidence thresholds
- 📊 `!test <message>` command to test classification results
- 🧼 Automatic text cleaning and slang normalization
- ☁️ Seamless deployment to [Railway](https://railway.app)

---

## 🗂️ Project Structure

```
safetalks-bot/
├── model/
│   └── lstm/
│       ├── lstm_model.keras    # Trained LSTM model
│       └── tokenizer.pkl       # Fitted tokenizer
├── .env                        # Environment variables (BOT_TOKEN)
├── bot.py                      # Main bot script
├── requirements.txt            # Python dependencies
└── README.md                   # This documentation
```

---

## 🧠 Model

SafeTalks uses a custom LSTM model featuring:
- A `SimpleAttention` layer for improved context understanding
- A custom `focal_loss_fn` to handle imbalanced classes effectively

The model classifies messages into:
- Hate Speech
- Offensive
- Neither

Model and tokenizer are stored in the `model/lstm/` directory.

---

## ⚙️ Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/fajarwiguna/safetalks-bot.git
   cd safetalks-bot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file:**
   ```
   BOT_TOKEN=your_discord_bot_token_here
   ```

4. **Run the bot:**
   ```bash
   python bot.py
   ```

---

## ☁️ Deploying on Railway

1. Push the project to a GitHub repository.
2. Visit [Railway](https://railway.app/).
3. Select **New Project > Deploy from GitHub Repo**.
4. Add `BOT_TOKEN` to Environment Variables.
5. Click **Deploy**.

---

## 💡 Bot Commands

### `!test <text>`

Test a message and view its classification result.

**Example:**
```
!test I hate you all
```

---

## 🔐 Message Moderation Logic

- **Hate Speech** (confidence ≥ 0.80): Message deleted, user warned
- **Offensive** (confidence ≥ 0.85): User warned
- **Neither**: No action taken

---

## 📜 License

Licensed under the [MIT License](LICENSE). Free to use, modify, and distribute.

---

## 🙋‍♀️ Contributing

Contributions are welcome! Submit pull requests or open issues for:
- Moderation dashboard
- Abuse reporting features
- Violation logging with database integration

---

## 📬 Contact

Developed by: Fajar Satria Wiguna  
Email: fajarsatria991@gmail.com