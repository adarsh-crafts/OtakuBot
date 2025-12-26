# OtakuBot 🎌 | A Modular Discord Anime Interaction Bot

**OtakuBot** is a modular, command-based Discord bot designed to provide fun anime-style interactions like hugging, slapping, and more — perfect for anime communities. Built using Python and `discord.py`, it also includes classic fun commands like 8-ball, dice rolls, and avatars.

---

## ✨ Features

- 💫 Anime-style interaction commands: `hug`, `blush`, `slap`, `bonk`, `kick`, etc.
- 🎲 Fun commands: `roll`, `8ball`, `avatar`, `flip`
- 🧩 Modular folder structure: easy to expand and maintain
- 🎨 Embed customization and color schemes
- ⚙️ Environment config support with `.env` for token management

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- `discord.py` (v1.7 or compatible fork)
- A Discord bot token

### Installation

1. **Clone this repo**:
    ```bash
    git clone https://github.com/your-username/OtakuBot.git
    cd OtakuBot
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up `.env`**:
    Create a `.env` file in the root directory and add your token:
    ```env
    DISCORD_TOKEN=your_token_here
    ```

4. **Run the bot**:
    ```bash
    python main.py
    ```

---

## 🧠 Folder Structure

Anime-bot/  
├── main.py # Entry point of the bot  
├── .env # Environment variables (add your token here)  
├── Actions/ # Anime interaction commands  
├── Fun/ # Fun commands like 8ball, flip, roll  
├── Config/ # Help and information command files  
├── DataFiles/ # Static data like replies, colors, and embeds  

yaml
Copy
Edit

---

## 📷 Example Commands

- `/hug @user`
- `/slap @user`
- `/8ball <your question>`
- `/roll`
- `/avatar @user`

---

## 🛡️ License

This project is open-source under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- Built for fun and learning — inspired by anime Discord communities.
- Uses the [discord.py](https://github.com/Rapptz/discord.py) library.

---

## 📬 Contact

If you have suggestions or improvements, feel free to fork and PR!
