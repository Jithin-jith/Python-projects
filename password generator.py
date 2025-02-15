import streamlit as st
import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    characters = string.ascii_lowercase  # Start with lowercase letters
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    if not characters:
        return "Please select at least one character type."
    
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("🔑 Secure Password Generator")

# User input options
length = st.slider("Select Password Length", min_value=6, max_value=50, value=12)
use_uppercase = st.checkbox("Include Uppercase Letters")
use_numbers = st.checkbox("Include Numbers")
use_special_chars = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    st.success(f"Generated Password: {password}")