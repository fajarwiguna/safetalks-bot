import csv
import os
from datetime import datetime

LOG_FILE = "logs/violations.csv"
os.makedirs("logs", exist_ok=True)

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        # Tambahkan kolom GuildID
        writer.writerow(["Timestamp", "GuildID", "Username", "UserID", "Message", "PredictedClass", "Confidence", "Action"])

def log_violation(user, message, result, action):
    with open(LOG_FILE, mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        guild_id = message.guild.id if message.guild else "DM"  # atau None jika DM
        writer.writerow([
            datetime.now().isoformat(),
            guild_id if guild_id else "Unknown",  # HARUS di posisi kedua
            user.name,
            user.id,
            message.content,
            result["predicted_class"],
            f"{result['confidence']:.4f}",
            action
        ])

