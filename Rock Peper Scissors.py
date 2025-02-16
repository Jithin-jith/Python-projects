import streamlit as st
import random

# Game choices and images
choices = ["Rock", "Paper", "Scissors"]
images = {
    "Rock": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Rock-paper-scissors_%28rock%29.png",
    "Paper": "https://upload.wikimedia.org/wikipedia/commons/4/43/Rock-paper-scissors_%28paper%29.png",
    "Scissors": "https://upload.wikimedia.org/wikipedia/commons/6/67/Rock-paper-scissors_%28scissors%29.png"
}

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You Win! 🎉"
    else:
        return "Computer Wins! 😢"

# Streamlit UI
st.title("✊ Rock, 📄 Paper, ✂️ Scissors Game")
st.write("Choose an option below to play against the computer.")

# Display choices as images with buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Rock ✊"):
        user_choice = "Rock"
with col2:
    if st.button("Paper 📄"):
        user_choice = "Paper"
with col3:
    if st.button("Scissors ✂️"):
        user_choice = "Scissors"

# Game logic
if 'user_choice' in locals():
    computer_choice = random.choice(choices)
    st.image(images[user_choice], caption=f"You chose: {user_choice}")
    st.image(images[computer_choice], caption=f"Computer chose: {computer_choice}")
    result = get_winner(user_choice, computer_choice)
    st.subheader(result)