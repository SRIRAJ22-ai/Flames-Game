# 🔥 FLAMES Relationship Predictor

This is a fun Python project that implements the classic **FLAMES** game logic to predict the relationship between two names. Whether it's friendship, love, or sibling vibes—this script gives you a playful result based on character elimination and modular arithmetic.

## 💡 What is FLAMES?

FLAMES stands for:
- **F** – Friends
- **L** – Love
- **A** – Affection
- **M** – Marriage
- **E** – Enemies
- **S** – Siblings

The game compares two names, eliminates common characters, and uses the remaining count to determine the relationship.

## 🧠 How It Works

1. Takes two names as input.
2. Removes matching characters.
3. Counts remaining characters.
4. Uses modular arithmetic to eliminate letters from the word "FLAMES".
5. Returns the final relationship result.

## 🚀 How to Run

```bash
python flames.py
